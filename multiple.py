import getpass
import telnetlib

HOST = "localhost"
user = input("Enter your remote account: ")
password = getpass.getpass()

f = open ('hosts.txt')

for IP in f:
  IP=IP.strip()
  print ("Configuring Switch " + (IP))
  tn = telnetlib.Telnet(IP)
  tn.read_until(b"Username: ")
  tn.write(user.encode('ascii') + b"\n")
  if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")
  tn.write(b"enable\n")
  tn.write(b"terminal lenth 0\n")
  tn.write(b"show run\n")
  tn.write(b"exit\n")
  readoutput = tn.read_all()
  saveoutput = open("switch" = HOST, "w")
  saveoutput.write(readoutput.decode('ascii'))
  saveoutput.write("\n")
  saveoutput.close
  print(tn.read_all().decode('ascii'))
 
