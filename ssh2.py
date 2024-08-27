from netmiko import ConnectHandler

SPOKE1 = {
    'device_type': 'cisco_ios',
    'ip': '10.99.2.1',
    'username': 'cisco',
    'password': 'cisco'
}

SPOKE2 = {
    'device_type': 'cisco_ios',
    'ip': '10.99.0.102',
    'username': 'cisco',
    'password': 'cisco'
}


all_devices = [SPOKE1, SPOKE2]

with open('commands.txt') as f:
    lines = f.read().splitlines()
print(lines)

with open('hosts.txt') as f:
    switches = f.read()
print(switches)

'''
for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    for n in range (1,6):
       print ("Creating LOOPBACK " + str(n))
       output = net_connect.send_config_set(lines)
       print (output)
'''







'''
for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    for n in range (1,6):
       print ("Creating LOOPBACK " + str(n))
       config_commands = ['int loo' + str(n), 'description Loopback ' + str(n)]
       output = net_connect.send_config_set(config_commands)
       print (output)
'''


