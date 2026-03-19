#ifndef WIFI_LOG_H
#define WIFI_LOG_H

#include <stdint.h> // To use uint

typedef struct __attribute__((aligned(64))) {
    char ts_iso[24];    // The biggest register has 23 characters
    char username[44];  // In development phase this value will be bigger
                        // in prod only work with what comes before @ua.pt
    char ap[16];        //
    uint8_t event;      // In this case maybe mapping an event to an integer would be best?
} wifi_log_entry_t;
#endif