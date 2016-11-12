#ifndef _UDP_H
#define _UDP_H

#include <utility/socket.h>

int udp_bind (int addr, int port);
int udp_has_data (int sock);
int udp_read (int sock, char *buff, int bufferSize, sockaddr* src_addr, socklen_t* addrlen);

#endif