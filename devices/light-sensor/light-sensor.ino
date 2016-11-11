#include <Adafruit_CC3000.h>
#include <ccspi.h>
#include <SPI.h>
#include <Arduino.h>
#include <errno.h>
#include <string.h>

#include "Adafruit_CC3000.h"
#include "utility/socket.h"


// These are the interrupt and control pins
#define ADAFRUIT_CC3000_IRQ   3  // MUST be an interrupt pin!
// These can be any two pins
#define ADAFRUIT_CC3000_VBAT  5
#define ADAFRUIT_CC3000_CS    10
// Use hardware SPI for the remaining pins
// On an UNO, SCK = 13, MISO = 12, and MOSI = 11
Adafruit_CC3000 cc3000 = Adafruit_CC3000(ADAFRUIT_CC3000_CS, ADAFRUIT_CC3000_IRQ, ADAFRUIT_CC3000_VBAT,
                                         SPI_CLOCK_DIVIDER); // you can change this clock speed but DI

#define WLAN_SSID       "The LAN b4 time"        // cannot be longer than 32 characters!
#define WLAN_PASS       "360noscope420blazeit"
// Security can be WLAN_SEC_UNSEC, WLAN_SEC_WEP, WLAN_SEC_WPA or WLAN_SEC_WPA2
#define WLAN_SECURITY   WLAN_SEC_WPA2

#define UDP_READ_BUFFER_SIZE 20

Adafruit_CC3000_Client client;

const unsigned long
  connectTimeout  = 15L * 1000L, // Max time to wait for server connection
  responseTimeout = 15L * 1000L; // Max time to wait for data from server
int
  countdown       = 0;  // loop() iterations until next time server query
unsigned long
  lastPolledTime  = 0L, // Last value retrieved from time server
  sketchTime      = 0L; // CPU milliseconds since last server query

// Sensor range constants
const int sensorMin = 0;
const int sensorMax = 800;
int photocellPin = A0;
int interval = 250; // 4 Hz



uint16_t port = 8080;
int soc = -1;

void setup(void)
{
  Serial.begin(115200);
  Serial.println(F("Hello, CC3000!\n")); 

  displayDriverMode();
  
  Serial.println(F("\nInitialising the CC3000 ..."));
  if (!cc3000.begin()) {
    Serial.println(F("Unable to initialise the CC3000! Check your wiring?"));
    for(;;);
  }

  uint16_t firmware = checkFirmwareVersion();
  if (firmware < 0x113) {
    Serial.println(F("Wrong firmware version!"));
    for(;;);
  }
  
    displayMACAddress();
  
  Serial.println(F("\nDeleting old connection profiles"));
  if (!cc3000.deleteProfiles()) {
    Serial.println(F("Failed!"));
    while(1);
  }

  /* Attempt to connect to an access point */
  char *ssid = WLAN_SSID;             /* Max 32 chars */
  Serial.print(F("\nAttempting to connect to ")); Serial.println(ssid);
  
  /* NOTE: Secure connections are not available in 'Tiny' mode! */
  if (!cc3000.connectToAP(WLAN_SSID, WLAN_PASS, WLAN_SECURITY)) {
    Serial.println(F("Failed!"));
    while(1);
  }
   
  Serial.println(F("Connected!"));
  
  /* Wait for DHCP to complete */
  Serial.println(F("Request DHCP"));
  while (!cc3000.checkDHCP()) {
    delay(100); // ToDo: Insert a DHCP timeout!
  }

  /* Display the IP address DNS, Gateway, etc. */  
  while (!displayConnectionDetails()) {
    delay(1000);
  }
  initUDP();
}


void displayDriverMode(void)
{
  #ifdef CC3000_TINY_DRIVER
    Serial.println(F("CC3000 is configure in 'Tiny' mode"));
  #else
    Serial.print(F("RX Buffer : "));
    Serial.print(CC3000_RX_BUFFER_SIZE);
    Serial.println(F(" bytes"));
    Serial.print(F("TX Buffer : "));
    Serial.print(CC3000_TX_BUFFER_SIZE);
    Serial.println(F(" bytes"));
  #endif
}


void displayMACAddress(void)
{
  uint8_t macAddress[6];
  
  if(!cc3000.getMacAddress(macAddress))
  {
    Serial.println(F("Unable to retrieve MAC Address!\r\n"));
  }
  else
  {
    Serial.print(F("MAC Address : "));
    cc3000.printHex((byte*)&macAddress, 6);
  }
}

uint16_t checkFirmwareVersion(void)
{
  uint8_t major, minor;
  uint16_t version;
  
#ifndef CC3000_TINY_DRIVER  
  if(!cc3000.getFirmwareVersion(&major, &minor))
  {
    Serial.println(F("Unable to retrieve the firmware version!\r\n"));
    version = 0;
  }
  else
  {
    Serial.print(F("Firmware V. : "));
    Serial.print(major); Serial.print(F(".")); Serial.println(minor);
    version = major; version <<= 8; version |= minor;
  }
#endif
  return version;
}

bool displayConnectionDetails(void)
{
  uint32_t ipAddress, netmask, gateway, dhcpserv, dnsserv;
  
  if(!cc3000.getIPAddress(&ipAddress, &netmask, &gateway, &dhcpserv, &dnsserv))
  {
    Serial.println(F("Unable to retrieve the IP Address!\r\n"));
    return false;
  }
  else
  {
    Serial.print(F("\nIP Addr: ")); cc3000.printIPdotsRev(ipAddress);
    Serial.print(F("\nNetmask: ")); cc3000.printIPdotsRev(netmask);
    Serial.print(F("\nGateway: ")); cc3000.printIPdotsRev(gateway);
    Serial.print(F("\nDHCPsrv: ")); cc3000.printIPdotsRev(dhcpserv);
    Serial.print(F("\nDNSserv: ")); cc3000.printIPdotsRev(dnsserv);
    Serial.println();
    return true;
  }
}


bool initUDP() {
   // Open the socket if it isn't already open.
   if (soc == -1) {
      // Create the UDP socket
      Serial.println("Maybe we making a socket?");
      soc = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP);
      if (soc < 0) {
         Serial.println("socket() call failed");
         
         return false;
      }

      sockaddr_in address;
      memset(&address, 0, sizeof(address));
      address.sin_family = AF_INET;
      address.sin_port = htons(port);
      address.sin_addr.s_addr = 0;  // 0 => auto use own ip address
      socklen_t len = sizeof(address);
      if (bind(soc, (sockaddr*) &address, sizeof(address)) < 0) {
         Serial.println("bind() call failed");
         return false;
      }
      
   }

   Serial.print("Socket state: ");
   Serial.println(soc);

   return true;
}

bool hasData() {
   timeval timeout;
   timeout.tv_sec = 0;
   timeout.tv_usec = 5000;
   fd_set reads;
   FD_ZERO(&reads);
   FD_SET(soc, &reads);
   select(soc + 1, &reads, NULL, NULL, &timeout);
   if (!FD_ISSET(soc, &reads)) {
      // No data to read.
      // Serial.println("No data to read.");
      return false;
   }
   Serial.println("Socket has available data");
   return true;
}

int readData(char *buff, int bufferSize, sockaddr* src_addr, socklen_t* addrlen) {
   // If there is data, then stores it into buffer &
   // returns the length of buffer. (-1 if none)
   
   if (hasData()) {  // Make sure data is really available
      Serial.print("Socket receiving on port: "); Serial.println(port);
      int n = recvfrom(soc, buff, bufferSize, 0, src_addr, addrlen);
      
      Serial.print("Socket response: "); Serial.println(n);
      
      if (n < 1) {
         // Error getting data.
         Serial.println("Error getting data");
         return -1;
      }
      
      return n;
  }
   
  return -1;
}


void loop(void) {
  int cellValue;
  sockaddr src_addr;
  socklen_t addrlen;
  
  cellValue = analogRead(photocellPin);
  Serial.println(cellValue);
  
  if (hasData()) {

      char buff[UDP_READ_BUFFER_SIZE];
      int n = readData(buff, UDP_READ_BUFFER_SIZE, &src_addr, &addrlen);  // n contains # of bytes read into buffer
      Serial.print("n: "); Serial.println(n);

      for (int i = 0; i < n; ++i) {
         uint8_t c = buff[i];
         Serial.print("c: ");
         Serial.println(c);
      }
      
      Serial.println("Sending sensor value");
      sendto(soc, &cellValue, sizeof(int), 0, &src_addr, addrlen);
  }
  
  
  delay(interval);
}

