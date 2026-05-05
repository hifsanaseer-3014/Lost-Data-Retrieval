drive = r"\\.\C:"
fileD = open(drive, "rb")
size = 512
byte = fileD.read(size)
offs = 0
drec = False
rcvd = 0

print("Scanning for deleted photos...")

while byte:
    found = byte.find(b'\xff\xd8\xff\xe0\x00\x10\x4a\x46')
    if found >= 0:
        drec = True
        print('=== Found JPG at location: ' + str(hex(found+(size*offs))) + ' ===')
        
        # Save directly to C:\Users\Hifsa\Downloads\pics\
        fileN = open("C:\\Users\\Hifsa\\Downloads\\pics\\" + str(rcvd) + ".jpg", "wb")
        fileN.write(byte[found:])
        
        while drec:
            byte = fileD.read(size)
            bfind = byte.find(b'\xff\xd9')
            if bfind >= 0:
                fileN.write(byte[:bfind+2])
                print('=== Wrote JPG: ' + str(rcvd) + '.jpg to your pics folder ===\n')
                drec = False
                rcvd += 1
                fileN.close()
            else:
                fileN.write(byte)
        byte = fileD.read(size)
    offs += 1
    byte = fileD.read(size)

fileD.close()
print(f"Done! Check C:\\Users\\Hifsa\\Downloads\\pics\\ for {rcvd} recovered photos")