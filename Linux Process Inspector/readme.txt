========================================================
Linux Process Inspector
Process Information and Memory Layout Analyzer
Technology: C Programming (Linux System Programming)
========================================================

Project Overview
--------------------------------------------------------
Linux Process Inspector is a system programming project
developed in C that analyzes running processes in a
Linux system using the /proc filesystem.

The tool allows a user to inspect a process by providing
its PID (Process ID). It retrieves important process
information such as process name, state, PID, and thread
count. It also parses the memory layout of the process
by reading the /proc/<pid>/maps file.

The program classifies memory segments into sections
like TEXT, DATA, HEAP, STACK, VDSO, and VVAR based on
memory permissions and mapping details.

This project demonstrates practical usage of Linux
system interfaces and helps understand how operating
systems manage process memory.

--------------------------------------------------------
Key Features
--------------------------------------------------------

1. Process Information Retrieval
   - Reads process metadata from /proc/<pid>/status
   - Displays important fields such as:
     • Process Name
     • Process ID
     • Process State
     • Number of Threads

2. Memory Layout Analysis
   - Reads the memory mapping information from
     /proc/<pid>/maps
   - Displays memory segments including:
     • Start Address
     • End Address
     • Segment Size
     • Permissions
     • Section Type
     • Mapping Details

3. Memory Section Classification
   The program categorizes memory segments into:

   • TEXT   (Executable Code Section)
   • DATA   (Writable Data Section)
   • HEAP   (Dynamic Memory Allocation)
   • STACK  (Function Call Stack)
   • VDSO   (Virtual Dynamic Shared Object)
   • VVAR   (Kernel Provided Variables)
   • OTHER  (Other mappings)

4. Linux System Programming Concepts
   This project demonstrates usage of:

   File System Interface:
   • fopen()
   • fgets()
   • fclose()

   String Processing:
   • sscanf()
   • strcmp()
   • strcpy()
   • strncmp()

   Linux Proc Filesystem:
   • /proc/<pid>/status
   • /proc/<pid>/maps

--------------------------------------------------------
Learning Outcomes
--------------------------------------------------------

• Understanding of the Linux /proc filesystem
• Practical knowledge of process metadata inspection
• Hands-on experience parsing system files
• Understanding process memory layout
• Experience with system-level programming in C

--------------------------------------------------------
Project Structure
--------------------------------------------------------

Linux-Process-Inspector
│
├── process_inspector.c
└── README.txt

--------------------------------------------------------
Compilation
--------------------------------------------------------

Compile the program using GCC:

gcc process_inspector.c -o inspector

--------------------------------------------------------
Execution
--------------------------------------------------------

Run the program and provide a process ID (PID):

./inspector

Example:

Enter the PID of a process that you want to inspect
1234

The program will display process information and
its memory layout.

--------------------------------------------------------
Example Output
--------------------------------------------------------

----------- Marvellous Process Inspector -----------

Process Information
Name: bash
Pid: 1234
State: Running
Threads: 1

Memory Layout
StartAddr   EndAddr   Size(KB)   Perms   Section   Details
00400000    00452000   328       r-xp    TEXT      /usr/bin/bash
00651000    00652000   4         rw-p    DATA      /usr/bin/bash
7ffde000    7fffe000   128       rw-p    STACK     [stack]
