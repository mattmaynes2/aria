#include <Adafruit_CC3000.h>
#include "log.h"
#include "udp.h"

int udp_bind (int addr, int port) {
	int sock = 0;
	sockaddr_in address;
	socklen_t len;
	unsigned long aucDHCP       = 14400;
  	unsigned long aucARP        = 3600;
  	unsigned long aucKeepalive  = 30;
  	unsigned long aucInactivity = 0;

	if (netapp_timeout_values(&aucDHCP, &aucARP, &aucKeepalive, &aucInactivity) != 0)  {
		log_warn("Error setting the socket timeout limit. Socket will use default timeout of 60 seconds");
	}

	log_debug("Creating datagram socket");
	sock = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP);
	if (sock < 0) {
		log_debug("socket() call failed");
		return -1;
	}
	
	memset(&address, 0, sizeof(address));
	address.sin_family = AF_INET;
	address.sin_port = htons(port);
	address.sin_addr.s_addr = 0;  // 0 => auto use own ip address
	len = sizeof(address);
	

  	
	
	if (bind(sock, (sockaddr*) &address, sizeof(address)) < 0) {
		log_debug("bind() call failed");
		return -1;
	}
    log_debug("Bound socket to port %d", port);
	return sock;
}


int udp_has_data (int sock) {
	timeval timeout;
	timeout.tv_sec = 0;
	timeout.tv_usec = 5000;
	fd_set reads;
	FD_ZERO(&reads);
	FD_SET(sock, &reads);

	select(sock + 1, &reads, NULL, NULL, &timeout);
	if (!FD_ISSET(sock, &reads)) {
		return 0;
	}
	log_debug("Socket has available data");
	return 1;
}

int udp_read (int sock, char *buff, int bufferSize, sockaddr* src_addr, socklen_t* addrlen) {
	int n;
	// If there is data, then stores it into buffer &
	// returns the length of buffer. (-1 if none)

	if (udp_has_data(sock)) {  // Make sure data is really available
		n = recvfrom(sock, buff, bufferSize, 0, src_addr, addrlen);

		log_debug("Socket response: %d", n); 
		
		if (n < 1) {
			// Error getting data.
			log_warn("Error reading data from socket");
			return -1;
		}

		return n;
	}

	return -1;
}