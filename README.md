# Forensic Data Recovery Tool (JPG Carver)

## **Project Overview**
This project is a **low-level** forensic utility designed to recover deleted data from physical storage media. Unlike standard recovery software that relies on the File Allocation Table (FAT) or NTFS Master File Table (MFT), this tool uses **File Carving** (Header/Footer analysis). This technique allows for the retrieval of files even when the file system metadata has been corrupted or wiped.

## **Core Concept: Data Carving**
When a file is "deleted" in Windows, the actual data remains on the disk; only the reference to it is removed. This tool scans the raw binary sectors to find "Magic Numbers"—unique signatures that identify specific file types.

### **How it Works**
* **Binary Stream Access:** The script opens the physical drive as a raw device (`\\.\C:`).
* **Signature Detection:** It monitors the stream for the JPG Start-of-Image (SOI) marker: `\xff\xd8\xff\xe0`.
* **Extraction:** Once a header is found, it "carves" the data into a new file until it hits the End-of-Image (EOI) marker: `\xff\xd9`.

---

## **Technical Breakdown**

### **Listener**
The script functions as a real-time binary listener. It reads the drive in 512-byte blocks (standard sector size), acting as a "sniffer" for hexadecimal signatures.

### **Logging**
Every discovery is documented. The script logs the exact **Physical Hex Offset** to the console. This is critical for forensic verification to prove where the file was located on the hardware.

### **Persistence**
The tool utilizes a persistent `while byte:` loop. This ensures the script maintains its connection to the raw data stream and continues scanning until it hits the very last byte of the drive's capacity.

---

## **How to Run**
1. Open **Command Prompt** as an **Administrator**.
2. Run the script:
```bash
python dataretrieval.py
