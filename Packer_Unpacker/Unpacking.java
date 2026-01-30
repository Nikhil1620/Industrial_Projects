// Unpacking Final Code
// This program extracts files from a packed file created by the packing program
// It reads headers, decrypts the data using XOR, and writes the extracted files

import java.io.*;
import java.util.*;

class program614
{
    public static void main(String A[]) throws Exception
    {
        // =========================
        // Variable Declarations
        // =========================
        int FileSize = 0;       // Size of each extracted file
        int i = 0;              // Loop variable
        int iRet = 0;           // Bytes read from packed file

        byte Key = 0x11;        // Encryption key (used for XOR)
        
        Scanner sobj = null;    // Scanner object for user input
        String FileName = null; // Name of the packed file
        String Header = null;   // Header info for each file
        String Tokens[] = null; // Header split into filename and size

        File fpackobj = null;   // Packed file object
        File fobj = null;       // Individual extracted file object
    
        FileInputStream fiobj = null;   // Stream to read from packed file
        FileOutputStream foobj = null;  // Stream to write extracted files
    
        byte bHeader[] = new byte[100]; // Buffer to read header (fixed size)
        byte Buffer[] = null;           // Buffer to read file data

        sobj = new Scanner(System.in);
        
        // =========================
        // Get packed file name from user
        // =========================
        System.out.println("Enter the name of packed file : ");
        FileName = sobj.nextLine();

        fpackobj = new File(FileName);

        // Check if packed file exists
        if(fpackobj.exists() == false)
        {
            System.out.println("Error : There is no such packed file");
            return;
        }
        
        fiobj = new FileInputStream(fpackobj);

        // =========================
        // Read headers and extract files
        // =========================
        while((iRet = fiobj.read(bHeader,0,100)) != -1)
        {
            // Convert header bytes to string
            Header = new String(bHeader);

            // Remove extra spaces from header
            Header = Header.trim();

            // Split header into filename and filesize
            Tokens = Header.split(" ");

            System.out.println("File name : "+Tokens[0]);
            System.out.println("File size : "+Tokens[1]);
            
            // Create a new file to extract data
            fobj = new File(Tokens[0]);
            fobj.createNewFile();

            // Open output stream to write the extracted file
            foobj = new FileOutputStream(fobj);

            // Get file size from header
            FileSize = Integer.parseInt(Tokens[1]);

            // Buffer to read the actual file data
            Buffer = new byte[FileSize];

            // Read data from packed file into buffer
            fiobj.read(Buffer,0,FileSize);

            // =========================
            // Decrypt the data using XOR key
            // =========================
            for(i = 0; i < FileSize ; i++)
            {
                Buffer[i] = (byte)(Buffer[i] ^ Key);
            }

            // Write decrypted data to the extracted file
            foobj.write(Buffer,0,FileSize);

            // Close output stream for this file
            foobj.close();

            System.out.println("File " + Tokens[0] + " extracted successfully!\n");
        }

        // Close input stream for packed file
        fiobj.close();
    }
}
