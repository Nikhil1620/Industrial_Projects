🗂️ Kernel CVFS – Custom Virtual File System in C

A Linux-inspired Custom Virtual File System (CVFS) implemented in C, which simulates core file system operations such as file creation, deletion, reading, writing, and metadata management using in-memory data structures.

This project demonstrates Operating System internals, inode-based file management, and command-line shell design.

📌 Key Highlights

✔ Fully implemented in C (System Programming)
✔ Linux-like Virtual File System architecture
✔ Inode-based file management
✔ Interactive command-line shell
✔ Dynamic memory management
✔ Robust macro-based error handling
✔ Interview-ready project (OS + C fundamentals)

🧠 Architecture Overview

The project mimics a Linux VFS layer using the following core components:

🔹 Core Structures
Component	Description
BootBlock	Holds kernel boot information
SuperBlock	Tracks total and free inodes
DILB (Dynamic Inode List Block)	Linked list of inodes
Inode	Stores file metadata
FileTable	Maintains open file information
UFDT (UAREA)	Per-process file descriptor table
🗃️ Data Structures Used

Linked List → Inode Management

Arrays → UFDT

Structures → Inode, FileTable, SuperBlock

Dynamic Memory Allocation → malloc, free

📂 Project Constraints
Parameter	Value
Maximum File Size	50 bytes
Maximum Inodes	5
Maximum Open Files	20
File Types	Regular files
Storage	In-Memory
🔐 File Permissions
Value	Permission
1	Read
2	Write
3	Read + Write
⚙️ Supported Commands
🔹 General Commands
Command	Description
help	Displays help menu
man <command>	Displays manual page
ls	Lists all files
clear	Clears terminal
exit	Terminates CVFS
🔹 File Commands
Command	Description
creat <filename> <permission>	Create new file
write <fd>	Write data into file
read <fd> <size>	Read data from file
unlink <filename>	Delete file
🚀 Compilation & Execution
🔹 Compile
gcc cvfs.c -o cvfs

🔹 Run
./cvfs

🖥️ Sample Execution
Kernel CVFS started successfully

Marvellous CVFS : > creat Demo.txt 3
File gets successfully created with FD 3

Marvellous CVFS : > write 3
Enter the data that you want to write :
Hello CVFS
11 bytes gets successfully written

Marvellous CVFS : > read 3 11
Read operation is successful
Data from file is : Hello CVFS

Marvellous CVFS : > ls
1   Demo.txt    11

❗ Error Handling

The project uses macro-based error codes for clarity and robustness:

ERR_INVALID_PARAMETER

ERR_FILE_ALREADY_EXIST

ERR_FILE_NOT_EXIST

ERR_PERMISSION_DENIED

ERR_NO_INODES

ERR_INSUFFICIENT_SPACE

ERR_MAX_FILES_OPEN

🧪 Learning Outcomes

✔ Deep understanding of inode-based file systems
✔ Hands-on experience with OS-level abstractions
✔ Mastery of memory management in C
✔ Implementation of Linux-style shell commands
✔ Strong foundation for System Programming interviews

📈 Future Enhancements

lseek() support

Directory handling

Multi-process simulation

Persistent disk-based storage

User-based permission model

👨‍💻 Author

Nikhil Ramesh Ahire
📅 January 2026
