# Kernel Interface Utility Suit

## 🔹 Project Title

**Kernel Interface Utility Suit (Custom Command Line Interpreter in C)**

---

## 🔹 Project Description

This project is a custom implementation of a **Kernel Interface Utility Suitl** developed using the C programming language. It replicates basic functionalities of standard Linux commands by directly using **system calls** such as `open()`, `read()`, `write()`, `fork()`, `exec()`, and `chdir()`.

The project is designed to provide a deeper understanding of **Operating System concepts**, including process management, file handling, and directory operations.

---

## 🔹 Features

* Custom shell prompt (`MyShell >`)
* Execution of user-defined commands
* Process creation using `fork()`
* Command execution using `exec()`
* Built-in support for directory change (`cdx`)
* Error handling for invalid commands and arguments
* Modular command design (each command implemented separately)

---

## 🔹 Commands Implemented

| Command  | Description                                    |
| -------- | ---------------------------------------------- |
| `lsx`    | Lists files in directory (supports `-a`, `-i`) |
| `catx`   | Displays contents of a file                    |
| `cpx`    | Copies content from one file to another        |
| `mvx`    | Moves or renames files                         |
| `rmx`    | Deletes a file                                 |
| `cdx`    | Changes current directory                      |
| `pwdx`   | Displays current working directory             |
| `psx`    | Displays running processes                     |
| `touchx` | Creates a new file                             |

---

## 🔹 Project Structure

Kernel Interface Utility Suit/
│
├── commands/
│   ├── lsx.c
│   ├── catx.c
│   ├── cpx.c
│   ├── mvx.c
│   ├── rmx.c
│   ├── cdx.c
│   ├── pwdx.c
│   ├── psx.c
│   ├── touchx.c
│
├── shell/
│   └── myshell.c
│
├── Makefile
├── README.txt

---

## 🔹 Compilation Instructions

Use the following commands to compile:

```
gcc commands/lsx.c -o lsx
gcc commands/catx.c -o catx
gcc commands/cpx.c -o cpx
gcc commands/mvx.c -o mvx
gcc commands/rmx.c -o rmx
gcc commands/pwdx.c -o pwdx
gcc commands/psx.c -o psx
gcc commands/touchx.c -o touchx
gcc shell/myshell.c -o myshell
```

OR simply run:

```
make
```

---

## 🔹 How to Run

1. Add current directory to PATH:

```
export PATH=$PATH:.
```

2. Start the shell:

```
./myshell
```

3. Execute commands:

```
MyShell > lsx
MyShell > touchx file.txt
MyShell > catx file.txt
MyShell > cpx file.txt newfile.txt
MyShell > mvx file.txt moved.txt
MyShell > rmx moved.txt
MyShell > pwdx
MyShell > psx
MyShell > cdx ..
MyShell > exit
```

---

## 🔹 Concepts Used

* System Calls (`open`, `read`, `write`, `close`)
* Process Management (`fork`, `exec`, `wait`)
* Directory Handling (`opendir`, `readdir`)
* File Handling in Linux
* Command Parsing
* Memory and Buffer Management

---

## 🔹 Challenges Faced

* Handling `cd` as a built-in command inside the shell
* Parsing user input into command and arguments
* Managing multiple processes
* Error handling for invalid inputs and system call failures

---

## 🔹 Future Enhancements

* Add support for piping (`|`)
* Add input/output redirection (`>`, `<`)
* Implement command history
* Add colored shell prompt
* Support multiple command execution (`;`)

---

## 🔹 Conclusion

This project demonstrates a practical implementation of core **Operating System concepts** by building a functional shell environment. It provides hands-on experience with low-level programming and system-level interactions in Linux.

---

## 🔹 Author

Nikhil Ramesh Ahire

---

