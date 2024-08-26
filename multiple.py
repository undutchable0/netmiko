import getpass
import telnetlib

HOST = "localhost"
user = input("Enter your remote account: ")
password = getpass.getpass()

f = open ('hosts.txt')

for IP in f:
  IP=IP.strip()
  print ("Configuring Switch " + (IP))
  HOST = IP
  tn = telnetlib.Telnet(HOST)
  tn.read_until(b"Username: ")
  tn.write(user.encode('ascii') + b"\n")
  if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")
  tn.write(b"enable\n")
  tn.write(b"conf t\n")
  tn.write(b"int loo 200\n")
  tn.write(b"description HellYah\n")
  tn.write(b"end\n")
  tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
