========================================================
Concurrent FTP Server
Multi-Client File Transfer System
Technology: C Programming (Linux System Programming)
========================================================

Project Overview
--------------------------------------------------------
This project is a Concurrent FTP Server implemented in C
on Linux that allows multiple clients to connect to the
server and download files simultaneously.

The server uses TCP socket programming and process-based
concurrency using fork() to handle multiple client
connections at the same time.

This project demonstrates practical implementation of
Linux networking, file system operations, and process
management using system calls.

It also implements a simple protocol-based file transfer
mechanism where the server first sends a header and then
transmits the file data in chunks.

--------------------------------------------------------
Key Features
--------------------------------------------------------

1. Multi-Client Support (Concurrency)
   - Supports multiple clients at the same time
   - Uses fork() to create a child process for each client
   - Enables parallel file transfers

2. Reliable File Transfer using TCP
   - Uses TCP socket communication
   - Client sends a file request
   - Server validates and sends the requested file

3. Simple Protocol Design
   The server sends a header before file transfer:

       OK <file_size>

   If the file is not available:

       ERR

4. Linux System Call Usage

   File Subsystem
   - open()
   - read()
   - close()
   - stat()

   Network Subsystem
   - socket()
   - bind()
   - listen()
   - accept()
   - connect()
   - send()
   - recv()

   Process Subsystem
   - fork()
   - exit()

5. Error Handling
   Handles different error conditions such as:
   - File not found
   - Invalid file request
   - Client disconnect
   - Permission errors

--------------------------------------------------------
Learning Outcomes
--------------------------------------------------------

• Understanding of Linux TCP/IP socket programming
• Practical implementation of client-server architecture
• Experience with process-based concurrency using fork()
• File transfer implementation using chunk-based reading
• Protocol design (header + payload communication)
• Hands-on practice with Linux system calls

--------------------------------------------------------
Project Structure
--------------------------------------------------------

server.c
    Concurrent FTP server implementation

client.c
    Client application to request and download files

README.txt
    Project documentation

--------------------------------------------------------
Compilation and Execution
--------------------------------------------------------

Step 1: Compile the Server

    gcc server.c -o server

Step 2: Run the Server

    ./server 9090

Step 3: Compile the Client

    gcc client.c -o client

Step 4: Run the Client

    ./client <server_ip> <port> <filename>

Example:

    ./client 127.0.0.1 9090 Demo.txt

--------------------------------------------------------
Example Execution
--------------------------------------------------------

Server Terminal

    $ gcc server.c -o server
    $ ./server 9090

    Server started...
    Waiting for clients...

Client Terminal

    $ gcc client.c -o client
    $ ./client 127.0.0.1 9090 Demo.txt

    OK 1234
    File received successfully.

--------------------------------------------------------
Concurrency Test
--------------------------------------------------------

Multiple clients can download files simultaneously:

    ./client 127.0.0.1 9090 A.txt
    ./client 127.0.0.1 9090 B.txt
    ./client 127.0.0.1 9090 C.txt

Each client is handled by a separate process.

--------------------------------------------------------
Interview Explanation
--------------------------------------------------------

"I developed a Concurrent FTP Server in C on Linux that
allows multiple clients to download files simultaneously
using TCP socket programming.

The server uses Linux system calls like socket, bind,
listen, and accept for networking operations and open,
read, stat, and close for file handling.

To support concurrency, the server creates a new child
process using fork() for each client request. This
ensures that multiple clients can download files in
parallel.

I also designed a simple protocol where the server first
sends a header such as 'OK <file_size>' and then
transfers the file in chunks.

This project helped me gain hands-on experience with
Linux networking, system programming, process
management, and client-server architecture."
