/*
 * Copyright (C) 2011-2021 Intel Corporation. All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 *
 *   * Redistributions of source code must retain the above copyright
 *     notice, this list of conditions and the following disclaimer.
 *   * Redistributions in binary form must reproduce the above copyright
 *     notice, this list of conditions and the following disclaimer in
 *     the documentation and/or other materials provided with the
 *     distribution.
 *   * Neither the name of Intel Corporation nor the names of its
 *     contributors may be used to endorse or promote products derived
 *     from this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 * "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 * LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
 * A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
 * OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
 * SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
 * LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
 * DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
 * THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
 * OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 *
 */

#include "Enclave.h"
#include "Enclave_t.h" /* print_string */
#include <stdarg.h>
#include <stdio.h> /* vsnprintf */
#include <string.h>

// Variable that stores the schedules and classes
schedule_entry_t enclave_full_schedule[100];
uint32_t current_schedule_count = 0;
student_enrollment_t enclave_enrollments[1000];
uint32_t total_enrollment_count = 0;


void ecall_load_schedule(schedule_entry_t* schedule_array, uint32_t count)
{
    // Safety check
    if (schedule_array == NULL || count == 0 || count > 100) {
        ocall_print_string("[Enclave Error] Invalid schedule data or size.\n");
        return;
    }

    // Load the data to the structure
    memcpy(enclave_full_schedule, schedule_array, sizeof(schedule_entry_t) * count);
    current_schedule_count = count;
    
    char buf[128];
    snprintf(buf, sizeof(buf), "[Enclave] Loaded %u schedules successfully.\n",  current_schedule_count);
    ocall_print_string(buf);
}

void ecall_load_classes(student_enrollment_t* enrollment_array, uint32_t num_entries)
{
    //Safety Checks
    if (enrollment_array == NULL || num_entries == 0 || num_entries > 1000) {
        ocall_print_string("[Enclave Error] Invalid class data or size.\n");
        return;
    }

    // Load data to struct
    memcpy(enclave_enrollments, enrollment_array, sizeof(student_enrollment_t) * num_entries);
    total_enrollment_count = num_entries;

    char buf[128];
    snprintf(buf, sizeof(buf), "[Enclave] Loaded %u student enrollments.\n", total_enrollment_count);
    ocall_print_string(buf);
}