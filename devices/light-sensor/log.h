#ifndef _LOG_H
#define _LOG_H
#include <Arduino.h>

#define log_emerg(fmt, ...)		log_printf(F("[PANIC] " fmt "\n"), ##__VA_ARGS__)
#define log_alert(fmt, ...)		log_printf(F("[ALERT] " fmt "\n"), ##__VA_ARGS__)
#define log_critical(fmt, ...)	log_printf(F("[CRIT]  " fmt "\n"), ##__VA_ARGS__)
#define log_error(fmt, ...) 	log_printf(F("[ERROR] " fmt "\n"), ##__VA_ARGS__)
#define log_warn(fmt, ...)		log_printf(F("[WARN]  " fmt "\n"), ##__VA_ARGS__)
#define log_info(fmt, ...)		log_printf(F("[INFO]  " fmt "\n"), ##__VA_ARGS__)
#define log_debug(fmt, ...)		log_printf(F("[DEBUG] " fmt "\n"), ##__VA_ARGS__)

void log_printf(const __FlashStringHelper *fmt, ...);


#endif /* _CLOG_H */
