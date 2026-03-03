#ifndef SCHEDULE_DATA_H
#define SCHEDULE_DATA_H

#include <stdint.h>

typedef struct __attribute__((aligned(64))) {
    uint32_t course_code;    // e.g., 41948
    char course_name[48];    // e.g., "Arquitetura de Computadores I"
    char class_id[8];        // e.g., "TP1"
    char room[12];           // e.g., "04.3.17"
    uint8_t day;             // e.g., 2 (Monday)
    char time_interval[16];  // e.g., "09:00 - 11:00"
    uint8_t padding[39];     // Adjusting to keep total size a power of 2
} schedule_entry_t;


// Or instead of this (See what is the most perforamnt one)

#define MAX_CLASSES_PER_COURSE 10
#define MAX_COURSES 50

typedef struct {
    char id[8];             // e.g., "TP1"
    char room[12];          // e.g., "04.3.17"
    uint8_t day;            // e.g., 2
    char time_interval[16]; // e.g., "09:00 - 11:00"
} class_session_t;

typedef struct __attribute__((aligned(64))) {
    uint32_t course_code;                   // e.g., 41948
    char name[64];                          // e.g., "Arquitetura de Computadores I"
    char acronym[8];                        // e.g., "AC1"
    uint32_t num_classes;                   // How many classes are actually in the array
    class_session_t classes[MAX_CLASSES_PER_COURSE]; 
    uint8_t padding[44];                    // Pad to keep the total struct size clean
} course_t;

typedef struct {
    uint32_t num_courses;
    course_t courses[MAX_COURSES];
} full_schedule_t;

#endif