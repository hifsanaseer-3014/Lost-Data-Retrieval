Forensic Data Recovery Tool (JPG Carver)
Project Overview:
This project is a low-level forensic utility designed to recover deleted data from physical storage media. Unlike standard recovery software that relies on the File Allocation Table (FAT) or NTFS Master File Table (MFT), this tool uses File Carving (Header/Footer analysis). This technique allows for the retrieval of files even when the file system metadata has been corrupted or wiped.

Core Concept: Data Carving
When a file is "deleted" in Windows, the actual data remains on the disk; only the reference to it is removed. This tool scans the raw binary sectors to find "Magic Numbers"—unique signatures that identify specific file types.

How it Works:
Binary Stream Access: The script opens the physical drive as a raw device (\\.\C:).

Signature Detection: It monitors the stream for the JPG Start-of-Image (SOI) marker: \xff\xd8\xff\xe0.

Extraction: Once a header is found, it "carves" the data into a new file until it hits the End-of-Image (EOI) marker: \xff\xd9.

Configuration & Setup:
Setting the Target and Destination
To use this project, you must manually configure the physical paths in the script. This ensures the tool knows where to look and where to save the recovered evidence:

Source Drive: Change the drive variable to your target (e.g., \\.\D: for a USB drive).

Recovery Path: Update the fileN path to a local folder (e.g., C:\Recovered_Photos\). Note: Never save recovered files to the same drive you are scanning, as this can overwrite the data you are trying to save.

How to Run:
Open Command Prompt as an Administrator.

Execute the script using the full path to your Python interpreter to avoid environment path issues:

Bash
C:\Users\Hifsa\AppData\Local\Programs\Python\Python314\python.exe dataretrieval.py
Technical Breakdown
Listener
The script functions as a real-time binary listener. It reads the drive in 512-byte blocks (standard sector size), acting as a "sniffer" for hexadecimal signatures.

Logging
Every discovery is documented. The script logs the exact Physical Hex Offset to the console. This is a critical forensic step, as it allows a researcher to verify the exact location of the file on the physical platter or flash chip.

Persistence
The tool utilizes a persistent while byte: loop. This ensures the script maintains its connection to the raw data stream and continues scanning until it hits the very last byte of the drive's total capacity.
