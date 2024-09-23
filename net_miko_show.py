from netmiko import Netmiko
import json

host1 = {
    "host": "10.99.2.1",
    "username": "cisco",
    "password": "cisco",
    "device_type": "cisco_ios",
    "global_delay_factor": 0.1
}

host2 = {
    "host": "10.99.0.102",
    "username": "cisco",
    "password": "cisco",
    "device_type": "cisco_ios",
    "global_delay_factor": 0.1
}

devices = [host1, host2]

for host in devices:
    net_connect = Netmiko(**host)
    show = 'show version'
    show_output = net_connect.send_command(show)
    print(show_output)
    net_connect.disconnect()

'''
output = router1.send_command('show version', use_textfsm=True)

print(json.dumps(output, indent=2))



for interfaces in output:
    print('####################')
    print(interfaces['hostname'])
    print("Version:", interfaces['version'])
    print("Uptime:", interfaces['uptime'])
    print("Model(s):", interfaces['hardware'])
    print('####################')
'''
