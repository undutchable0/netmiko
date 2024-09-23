from netmiko import ConnectHandler
import json

sshCli = ConnectHandler(
    device_type = 'cisco_ios',
    host = '10.99.2.1',
    port = 22,
    username = 'cisco',
    password = 'cisco'
)

router2 = ConnectHandler(
    device_type = 'cisco_ios',
    host = '192.1',
    port = 22,
    username = 'admin',
    password = '**'
)

output = sshCli.send_command('show version', use_textfsm=True)

print(json.dumps(output, indent=2))

for interfaces in output:
    print('####################')
    print(interfaces['hostname'])
    print("Version:", interfaces['version'])
    print("Uptime:", interfaces['uptime'])
    print("Model(s):", interfaces['hardware'])
    print('####################')
