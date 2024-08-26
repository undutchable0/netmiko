import getpass
import telnetlib

HOST = "10.99.2.1"
user = input("Enter your remote account: ")
password = getpass.getpass()

print ("Configuring Switch " + (HOST))
tn = telnetlib.Telnet(HOST)
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
saveoutput = open("switch" + HOST, "w")
saveoutput.write(readoutput.decode('ascii'))
saveoutput.write("\n")
saveoutput.close
print(tn.read_all().decode('ascii'))
 
