#include<stdio.h>
#include<fcntl.h>
#include<unistd.h>
#include<string.h>
#include<dirent.h>

// 	./lsx	  -i
// 	argv[0]  argv[1]

// 	argc = 2
//  To list files in the current directory with optional flags:
// -a = show all files (including hidden)
// -i = show inode number + file name

/*
	Open the current directory (".")
	read all entries from that directory
	print the name of files
	Close the directory
*/

int main(int argc, char *argv[])
{
	int Option = 0;
	// 1 : ls -a
	// 2 : ls -i
	
	if(argc == 1)
	{
		Option = 1;
	}
	else if(strcmp(argv[1],"-a") == 0)
	{
		Option = 1;
	}	
	else if(strcmp(argv[1],"-i") == 0)
	{
		Option = 2;
	}
	else
	{
		printf("Error : There is no such option\n");
		return -1;
	}
	
	char *path = ".";

	DIR *dp = NULL;	

	dp = opendir(path);
	if(dp == NULL)
	{
		printf("Error : Unable to open directory\n");
		return -1;
	}
		
	struct dirent *dobj;
	
	while((dobj = readdir(dp)) != NULL)
	{
		if(Option == 1)
		{
			printf("%s\n",dobj->d_name);		
		}
		else if(Option == 2)
		{
			printf("%ld\t%s\n",dobj->d_ino,dobj->d_name);
		}
	}
	
	closedir(dp);
	
	return 0;
}

