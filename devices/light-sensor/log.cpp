#include <stdarg.h>
#include <stdio.h>
#include <Arduino.h>
#include "log.h"

#define PRINTF_BUF 256

void log_printf(const __FlashStringHelper *fmt, ...) {
	char buf[PRINTF_BUF];
	va_list args;
	va_start (args, fmt);
	
	#ifdef __AVR__
		vsnprintf_P(buf, sizeof(buf), (const char *)fmt, args);
	#else
    	vsnprintf(buf, sizeof(buf), (const char *)fmt, args);
  	#endif
	va_end(args);
	Serial.print(buf);
}

