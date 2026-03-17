#include<stdio.h>
#include<fcntl.h>
#include<unistd.h>
#include<string.h>
#include<sys/utsname.h>

// 	./unamex
// 	argv[0]	
// 	argc = 1

//	Call the system call uname
//	Print the information from utsname structure

//struct utsname {
//               char sysname[];    /* Operating system name (e.g., "Linux") */
//               char nodename[];   /* Name within communications network
//                                     to which the node is attached, if any */
//               char release[];    /* Operating system release
//                                     (e.g., "2.6.28") */
//               char version[];    /* Operating system version */
//               char machine[];    /* Hardware type identifier */
//           #ifdef _GNU_SOURCE
//               char domainname[]; /* NIS or YP domain name */
//           #endif
//           };


int main(int argc, char *argv[])
{
	struct utsname obj;
	int iRet = 0;
	
	iRet = uname(&obj);
	
	if(iRet == -1)
	{
		printf("Error : Unable to fetch system information\n");
		
		return -1;
	}
	
	printf("Operating system name : %s\n",obj.sysname);
	printf("Node name : %s\n",obj.nodename);
	printf("Operating system version : %s\n",obj.release);

	return 0;
}