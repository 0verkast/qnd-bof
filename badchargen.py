#!/bin/python3

print("HINT: Use non-hexadecimal formatting for bad characters, ie., 00 07 08 2e 2f a0 a1")
badchar_input = input("Bad Characters: ")

badchars_hex = ""
badchars = badchar_input.split(" ")

for i in range(len(badchars)):
    badchars[i] = "\\x" + badchars[i]

byte_string = ""

for x in range(0, 256):
    if ("\\x" + "{:02x}".format(x)) not in badchars:
        byte_string += ("\\x" + "{:02x}".format(x))
    else:
        badchars_hex += ("\\x" + "{:02x}".format(x))
    for char in badchars:
        byte_string.replace("\\x00", "")

print("Bad Characters(Hex): " + badchars_hex)
print(byte_string)
