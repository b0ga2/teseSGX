#include "Enclave_u.h"
#include <errno.h>

typedef struct ms_ecall_load_schedule_t {
	const char* ms_schedule_data;
	size_t ms_schedule_data_len;
} ms_ecall_load_schedule_t;

typedef struct ms_ocall_print_string_t {
	const char* ms_str;
} ms_ocall_print_string_t;

static sgx_status_t SGX_CDECL Enclave_ocall_print_string(void* pms)
{
	ms_ocall_print_string_t* ms = SGX_CAST(ms_ocall_print_string_t*, pms);
	ocall_print_string(ms->ms_str);

	return SGX_SUCCESS;
}

static const struct {
	size_t nr_ocall;
	void * table[1];
} ocall_table_Enclave = {
	1,
	{
		(void*)Enclave_ocall_print_string,
	}
};
sgx_status_t ecall_load_schedule(sgx_enclave_id_t eid, const char* schedule_data)
{
	sgx_status_t status;
	ms_ecall_load_schedule_t ms;
	ms.ms_schedule_data = schedule_data;
	ms.ms_schedule_data_len = schedule_data ? strlen(schedule_data) + 1 : 0;
	status = sgx_ecall(eid, 0, &ocall_table_Enclave, &ms);
	return status;
}

