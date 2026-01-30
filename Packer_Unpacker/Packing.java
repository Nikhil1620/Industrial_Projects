// Packing Final Code
// This program packs all .txt files from a specified folder into a single packed file.
// Each file is encrypted using XOR and preceded by a 100-byte header containing the filename and filesize.

import java.io.*;
import java.util.*;

class program606
{
    public static void main(String A[]) throws Exception
    {
        // =========================
        // Variable Declarations
        // =========================
        String Header = null;             // Stores header info for each file
        byte Key = 0x11;                  // Encryption key (used for XOR)
        int iRet = 0;                     // Bytes read from input files
        int i = 0, j = 0;                 // Loop variables

        byte Buffer[] = new byte[1024];   // Buffer for reading file data
        byte bHeader[] = new byte[100];   // Buffer to write 100-byte header

        Scanner sobj = new Scanner(System.in);

        // =========================
        // Get folder and packed file name from user
        // =========================
        System.out.println("Enter the name of folder : ");
        String FolderName = sobj.nextLine();

        System.out.println("Enter the name of packed file : ");
        String PackName = sobj.nextLine();
        
        File fobj = new File(FolderName);

        // Check if folder exists and is a directory
        if((fobj.exists()) && (fobj.isDirectory()))
        {
            File PackObj = new File(PackName);
            PackObj.createNewFile();                 // Create the packed file
            FileOutputStream foobj = new FileOutputStream(PackObj); // Output stream for packed file
            FileInputStream fiobj = null;            // Input stream for reading individual files

            System.out.println("Folder is present"); 

            File fArr[] = fobj.listFiles();          // List all files in the folder
            System.out.println("Number of files in the folder are : " + fArr.length);

            // =========================
            // Iterate over each file in the folder
            // =========================
            for(i = 0; i < fArr.length; i++)
            {
                fiobj = new FileInputStream(fArr[i]);  // Open input stream for current file

                // Only pack .txt files
                if(fArr[i].getName().endsWith(".txt"))
                {
                    // -------------------------
                    // Header Formation
                    // -------------------------
                    Header = fArr[i].getName() + " " + fArr[i].length();

                    // Pad header to 100 bytes
                    for(j = Header.length(); j < 100; j++)
                    {
                        Header = Header + " ";
                    }

                    bHeader = Header.getBytes();  // Convert header string to bytes

                    // Write header into packed file
                    foobj.write(bHeader, 0, 100);

                    // -------------------------
                    // Read file data and encrypt
                    // -------------------------
                    while((iRet = fiobj.read(Buffer)) != -1)
                    {
                        // Encryption using XOR
                        for(j = 0; j < iRet; j++)
                        {
                            Buffer[j] = (byte)(Buffer[j] ^ Key);
                        }

                        // Write encrypted data to packed file
                        foobj.write(Buffer, 0, iRet);
                    }
                }

                fiobj.close();  // Close input stream for current file
            }

            foobj.close();      // Close packed file stream
        }
        else
        {
            System.out.println("There is no such folder");
        }
    }
}
