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
    show_output = net_connect.send_command(show, use_textfsm=True)
    for values in show_output:
        print(values['hostname'])
        print("Version:", values['version'])
        print("Uptime:", values['uptime'])
        print("Model(s):", values['hardware'])
        print('####################')
        show_output_str = str(show_output)
        save_show = open('show_command.txt', 'w')
        save_show.write(show_output_str)
        save_show.close()
    net_connect.disconnect()
'''
show_output_str = str(show_output)
save_show = open('show_command.txt', 'w')
save_show.write(show_output_str)
save_show.close()
'''

    
'''
print(json.dumps(show_output, indent=2))



for interfaces in output:
    print('####################')
    print(interfaces['hostname'])
    print("Version:", interfaces['version'])
    print("Uptime:", interfaces['uptime'])
    print("Model(s):", interfaces['hardware'])
    print('####################')
'''
