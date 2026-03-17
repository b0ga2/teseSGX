#ifndef CLASS_DATA_H
#define CLASS_DATA_H

#include <stdint.h>

typedef struct __attribute__((aligned(32))) {
    char class_id[4]; // 4 bytes
    char email[28];   // 28 bytes
} student_enrollment_t;

#endif