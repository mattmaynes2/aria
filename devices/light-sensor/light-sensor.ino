#include <Adafruit_CC3000.h>
#include <SPI.h>

#include "log.h"
#include "wifi.h"
#include "halt.h"
#include "udp.h"

#define SERIAL_BAUD_RATE 115200

#define WLAN_SSID "Sanibel"
#define WLAN_PASS "Coquina4b"

// Security can be WLAN_SEC_UNSEC, WLAN_SEC_WEP, WLAN_SEC_WPA or WLAN_SEC_WPA2
#define WLAN_SECURITY WLAN_SEC_WPA2

#define WLAN_ATTEMPTS 3

#define UDP_BUFFER_SIZE 256
#define UDP_PORT 1260
#define UDP_ADDR 0

#define CLOCK_INTERVAL 250 // 4 Hz

int sock;

// Sensor range constants
int photocellPin = A0;


void setup (void) {
	int attempt = 0;
	
	Serial.begin(SERIAL_BAUD_RATE);
	
	wifi_init();
	wifi_clear();
	while (0 > wifi_connect(WLAN_SSID, WLAN_PASS, WLAN_SECURITY)) {
		log_error("WLAN initialization failed. Attempting again ...");
		attempt++;
		if (attempt > WLAN_ATTEMPTS){
			log_emerg("WLAN connection attempts exhausted. Program halted");
			HALT;
		}
	}
	
	log_debug("Initializing UDP socket");
	sock = udp_bind(UDP_ADDR, UDP_PORT);
	log_debug("Setup complete!");
}





void loop(void) {
 	int cellValue;
	sockaddr src_addr;
	socklen_t addrlen;
  
	cellValue = analogRead(photocellPin);
  
  	if (udp_has_data(sock)) {
		char buff[UDP_BUFFER_SIZE];
		int n = udp_read(sock, buff, UDP_BUFFER_SIZE, &src_addr, &addrlen);  // n contains # of bytes read into buffer
		log_info("Received %d bytes on port %d", n, UDP_PORT);

		Serial.print("data: ");
		for (int i = 0; i < n; ++i) {
		   uint8_t c = buff[i];      	   
		   Serial.print(c);
		}
		Serial.println("");

		log_debug("Sending sensor value");
    	sendto(sock, &cellValue, sizeof(int), 0, &src_addr, addrlen);
  	}
  
  
	delay(CLOCK_INTERVAL);
  
}

