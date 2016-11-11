
#include <Adafruit_CC3000.h>
#include <ccspi.h>
#include <SPI.h>
#include <stdlib.h>

#include "log.h"
#include "wifi.h"
#include "halt.h"

// These are the interrupt and control pins
#define CC3000_IRQ   3
#define CC3000_VBAT  5
#define CC3000_CS    10

#define DHCP_RETRY 			100
#define DHCP_RETRY_LIMIT 	5

#define IP_RETRY 		250
#define IP_RETRY_LIMIT 	5

#define dot_addr(addr) (uint8_t)(addr >> 24), (uint8_t)(addr >> 16), (uint8_t)(addr >> 8), (uint8_t)(addr)

// Use hardware SPI for the remaining pins
// On an UNO, SCK = 13, MISO = 12, and MOSI = 11
Adafruit_CC3000 driver = Adafruit_CC3000(CC3000_CS, CC3000_IRQ, CC3000_VBAT, SPI_CLOCK_DIVIDER);


uint16_t wifi_firmware (void) {
	uint8_t major, minor;
	uint16_t version;
  
	if (!driver.getFirmwareVersion(&major, &minor)) {
    	log_error("Unable to retrieve the firmware version!");
    	version = 0;
  	}
	else {
    	log_debug("Firmware Version: %d.%d", major, minor);
    	version = major; 
    	version <<= 8; 
    	version |= minor;
	}

	return version;
}

void wifi_init (void) {
	log_debug("Initializing the CC3000 driver");

  	if (!driver.begin()) {
		log_emerg("Unable to initialize the CC3000! Check your wiring? Program halted");
    	HALT;
	}	

	if (wifi_firmware() < 0x113) {
    	log_emerg("Wrong firmware version! Program halted");
    	HALT;
	}
}

void wifi_clear (void) {
	log_info("Deleting connection profiles");
	if (!driver.deleteProfiles()) {
    	log_emerg("Corrupt connection profiles! Program halted");
    	HALT;
  	}
}

int wifi_connect (char* ssid, char* pass, uint8_t security) {
	uint32_t ipAddress, netmask, gateway, dhcpserv, dnsserv, ipstate, dhcp_try = 0, ip_try = 0;
	
	log_debug("Attempting to connect to '%s'", ssid); 
	
	if (!driver.connectToAP(ssid, pass, security)) {
    	log_warn("Connection attempt to '%s' failed!", ssid);
    	return -1;
    }
   
	log_debug("Connected to '%s'", ssid);
	log_debug("Requesting DHCP");
	
  	while (!driver.checkDHCP()) {
		dhcp_try++;
    	
    	if (dhcp_try > DHCP_RETRY_LIMIT) {
    		log_error("DHCP retry limit exhausted");
    		return -1;
  		}
  		log_warn("DHCP request timeout ... Retrying");
  		delay(DHCP_RETRY);
  	}

	while (!driver.getIPAddress(&ipAddress, &netmask, &gateway, &dhcpserv, &dnsserv)) {
  		ip_try++;
  		
  		if (ip_try > IP_RETRY_LIMIT) {
  			log_error("IP assignment retry limit exhausted");
  			return -1;	
  		}  
  		log_warn("Unable to retrieve the IP address ... Retrying");		
		delay(IP_RETRY);
	}
  
  	log_debug("IP Address: %d.%d.%d.%d"		, dot_addr(ipAddress));
  	log_debug("Netmask: %d.%d.%d.%d"		, dot_addr(netmask)); 
	log_debug("Gateway: %d.%d.%d.%d"		, dot_addr(gateway)); 
	log_debug("DHCP Server: %d.%d.%d.%d"	, dot_addr(dhcpserv));
	log_debug("DNS Server: %d.%d.%d.%d"		, dot_addr(dnsserv));
	return 0;
	
}

