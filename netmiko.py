import netmiko
from netmiko import ConnectHandler

sshCli = ConnectHandler(
    device_type = 'cisco_ios',
    host = '10.99.0.101',
    port = 22,
    username = 'cisco'
    password = 'cisco'
)

output = sshCli.send_command('show ip int brief')
print(output)