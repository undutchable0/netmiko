from netmiko import ConnectHandler
import json

sshCli = ConnectHandler(
    device_type = 'cisco_ios',
    host = '10.99.2.1',
    port = 22,
    username = 'cisco',
    password = 'cisco'
)

config_command = [
    'int lo5',
    'ip add 1.1.1.1 255.255.255.0',
    'descrip HPDM'
    ]
'''
for loop in range(55,60,1):
    loop_commands = ['int loop ' + str(loop), 'description HPDM ' + str(loop)]
    sshCli.send_config_set(loop_commands)
'''

loopback = sshCli.send_config_set(config_command)

output = sshCli.send_command('show version', use_textfsm=True)

print(json.dumps(output, indent=2))


for interfaces in output:
    print(interfaces['interface'] , ' is ' , interfaces['status'])


