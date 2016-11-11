#ifndef _WIFI_H
#define _WIFI_H

#include <stdint.h>

void wifi_init (void);
void wifi_clear (void);
int wifi_connect (char* SSID, char* pass, uint8_t security);

#endif