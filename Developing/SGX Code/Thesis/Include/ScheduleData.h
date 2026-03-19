#ifndef SCHEDULE_DATA_H
#define SCHEDULE_DATA_H

#include <stdint.h> // To use uint

#define MAX_SCHEDULES 200

typedef struct __attribute__((aligned(64))) {
    uint32_t course_code;    // 4 bytes, e.g., 41948
    char acronym[8];         // 8 bytes, e.g., AC1
    char class_id[8];        // 8 bytes, e.g., TP1
    char room[13];           // 13 bytes, 04.3.17
    uint8_t day;             // 1 byte, 2 (Monday)
    char time_interval[16];  // 16 bytes, "09:00 - 11:00"
    
    uint8_t padding[14];     // 14 bytes to allign with a cache line (64 bytes)
} schedule_entry_t;
#endif