#!/usr/bin/env python3
# This tool will obfuscate a payload for XSS+Social Engineering purposes.
# 2021 - Douglas Berdeaux
import sys # for arguments, exit()
import os # for file size
def print_encoded(byte):
    print("%" + str(hex(ord(byte))).replace('0x',''),end="")
    return
def usage():
    print("Usage: ./url-encoder.py (filename)")
    sys.exit() # done
# we require the file to read in:
if len(sys.argv) < 2:
    usage()
print("\n")
file_length = os.path.getsize(sys.argv[1]) # in bytes
# read in entire file and strip any unwanted garbage from end:
fh = open(sys.argv[1],"r")
lines = fh.readlines()
for line in lines:
    line = line.strip()
    # NOW we read it per byte
    for byte in line:
        print_encoded(byte)
print("\n")
