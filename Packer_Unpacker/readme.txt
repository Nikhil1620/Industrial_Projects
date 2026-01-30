📦 Java File Packing & Unpacking System

🚀 Project Overview

This project demonstrates a simple file archiver in Java that can pack multiple .txt files from a folder into a single packed file with basic encryption and unpack them back to restore the original files.

Think of it as a mini ZIP tool with XOR encryption, designed for educational purposes.

✨ Features

Pack all .txt files from a folder into one packed file.

Fixed 100-byte headers for each file containing filename and size.

Basic XOR encryption for file content.

Unpack files to restore their original names and content.

Works efficiently with multiple files in a folder.

🗂 Files in this Repository
File	Purpose
program606.java	Packing program – combines .txt files into a single packed file
program614.java	Unpacking program – extracts files from the packed file
💻 Usage
1️⃣ Packing Files

Compile the program:

javac program606.java


Run the program:

java program606


Enter folder path containing .txt files.

Enter packed file name to create.

The packed file will be generated in the current directory.

2️⃣ Unpacking Files

Compile the program:

javac program614.java


Run the program:

java program614

Enter the name of the packed file.

All files will be extracted and decrypted in the current folder.

📁 Example
Folder Before Packing:
MarvellousFiles/
├── file1.txt
├── file2.txt
├── file3.txt

Packing Command:
java program606
Enter folder: MarvellousFiles
Enter packed file name: PackedFile.dat

Packed File Created:
PackedFile.dat

Unpacking Command:
java program614
Enter packed file name: PackedFile.dat

Files Restored:
file1.txt
file2.txt
file3.txt

🔒 Encryption

Each file byte is encrypted using XOR with key 0x11.

Ensures packed data is not human-readable.

⚠️ Notes

Only .txt files are considered for packing.

Each file uses a 100-byte header.

Ensure write permissions for the folder when unpacking.

📝 License

This project is open-source and free for educational purposes.
