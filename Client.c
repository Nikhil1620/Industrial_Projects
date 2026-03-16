// Client Application

#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<unistd.h>
#include<fcntl.h>
#include<sys/socket.h>
#include<arpa/inet.h>

/////////////////////////////////////////////////
//
//  Commandline Argument Application
//  1st Argument : Server IP Address
//  2nd Argument : Port Number
//  3rd Argument : File Name
//
//  Example:
//  ./client 127.0.0.1 9000 Demo.txt
//
/////////////////////////////////////////////////

int main(int argc, char *argv[])
{
    int ClientSocket = 0;
    int Port = 0;
    int iRet = 0;
    int fd = 0;

    char Buffer[1024];
    char Header[64] = {'\0'};
    int BytesRead = 0;

    struct sockaddr_in ServerAddr;

    //////////////////////////////////////////////////
    //  Check number of arguments
    //////////////////////////////////////////////////

    if((argc < 4) || (argc > 4))
    {
        printf("Invalid number of arguments\n");
        printf("Usage : %s <ServerIP> <Port> <FileName>\n",argv[0]);
        return -1;
    }

    // Get port number from argument
    Port = atoi(argv[2]);

    //////////////////////////////////////////////////
    //  Step 1 : Create TCP socket
    //////////////////////////////////////////////////

    ClientSocket = socket(AF_INET, SOCK_STREAM, 0);

    if(ClientSocket < 0)
    {
        printf("Unable to create client socket\n");
        return -1;
    }

    //////////////////////////////////////////////////
    //  Step 2 : Initialise server address structure
    //////////////////////////////////////////////////

    memset(&ServerAddr, 0, sizeof(ServerAddr));

    ServerAddr.sin_family = AF_INET;
    ServerAddr.sin_port = htons(Port);
    ServerAddr.sin_addr.s_addr = inet_addr(argv[1]);

    //////////////////////////////////////////////////
    //  Step 3 : Connect to the server
    //////////////////////////////////////////////////

    iRet = connect(ClientSocket,(struct sockaddr *)&ServerAddr,sizeof(ServerAddr));

    if(iRet < 0)
    {
        printf("Unable to connect to server\n");
        close(ClientSocket);
        return -1;
    }

    printf("Connected to server successfully\n");

    //////////////////////////////////////////////////
    //  Step 4 : Send requested file name to server
    //////////////////////////////////////////////////

    write(ClientSocket, argv[3], strlen(argv[3]));

    //////////////////////////////////////////////////
    //  Step 5 : Read header sent by server
    //////////////////////////////////////////////////

    BytesRead = read(ClientSocket, Header, sizeof(Header)-1);

    if(BytesRead <= 0)
    {
        printf("Failed to receive response from server\n");
        close(ClientSocket);
        return -1;
    }

    Header[BytesRead] = '\0';

    //////////////////////////////////////////////////
    //  Check if server returned error
    //////////////////////////////////////////////////

    if(strncmp(Header,"ERR",3) == 0)
    {
        printf("Server error : File not found\n");
        close(ClientSocket);
        return -1;
    }

    printf("Server response : %s",Header);

    //////////////////////////////////////////////////
    //  Step 6 : Create local file to store received data
    //////////////////////////////////////////////////

    fd = open(argv[3], O_WRONLY | O_CREAT | O_TRUNC, 0666);

    if(fd < 0)
    {
        printf("Unable to create local file\n");
        close(ClientSocket);
        return -1;
    }

    //////////////////////////////////////////////////
    //  Step 7 : Receive file contents in chunks
    //////////////////////////////////////////////////

    while((BytesRead = read(ClientSocket, Buffer, sizeof(Buffer))) > 0)
    {
        write(fd, Buffer, BytesRead);
    }

    printf("File received successfully\n");

    //////////////////////////////////////////////////
    //  Step 8 : Close file and socket
    //////////////////////////////////////////////////

    close(fd);
    close(ClientSocket);

    return 0;
}