========================================================
Concurrent FTP Server
Multi-Client File Transfer System
Technology: C Programming (Linux System Programming)
========================================================

Project Overview
--------------------------------------------------------
The Concurrent FTP Server is a Linux-based client-server
application developed using C and TCP socket programming.

This system allows multiple clients to connect to a server
and download files concurrently. The server uses
process-based concurrency (fork()) to handle multiple
client requests simultaneously.

Each client sends a file request to the server, and the
server validates the request and transfers the file
reliably using TCP communication.

This project demonstrates practical implementation of
Linux networking, file system operations, and process
management using system calls.


Key Features
--------------------------------------------------------

1. Multi-Client Support (Concurrency)
   - Supports multiple clients simultaneously.
   - Uses fork() to create a child process for each
     client connection.
   - Enables parallel file transfers.

2. File Transfer using TCP
   - Reliable communication using TCP sockets.
   - Client sends file request to the server.
   - Server validates and transfers the file.

3. Simple Protocol Design
   Communication protocol used:

       OK <file_size>
       ERR

   - "OK" indicates the file is available.
   - "ERR" indicates the file was not found.

   After sending the header, the server transfers
   the file in chunks.

4. Linux System Calls Used

   Networking:
   socket()
   bind()
   listen()
   accept()
   connect()

   File Handling:
   open()
   read()
   write()
   stat()
   close()

   Process Management:
   fork()
   exit()

5. Error Handling
   The system handles several cases:
   - File not found
   - Invalid file request
   - Client disconnection
   - Permission errors


Project Structure
--------------------------------------------------------

Concurrent-FTP-Server
│
├── server.c
├── client.c
├── README.txt
└── sample_files/


Compilation and Execution
--------------------------------------------------------

Step 1: Compile the Server

gcc server.c -o server

Step 2: Run the Server

./server 9000

Step 3: Compile the Client

gcc client.c -o client

Step 4: Run the Client

./client <server_ip> <port> <filename>

Example:

./client 127.0.0.1 9000 Demo.txt


Example Execution
--------------------------------------------------------

Server Terminal

$ gcc server.c -o server
$ ./server 9000

Server started...
Waiting for client connections...


Client Terminal

$ gcc client.c -o client
$ ./client 127.0.0.1 9000 Demo.txt

OK 1024
File received successfully.


Concurrency Test
--------------------------------------------------------

Multiple clients can download files simultaneously.

Example:

./client 127.0.0.1 9000 A.txt
./client 127.0.0.1 9000 B.txt
./client 127.0.0.1 9000 C.txt
