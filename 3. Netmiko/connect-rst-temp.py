# send configs to multiple device
import netmiko
from netmiko import ConnectHandler

# default values
device_info = {
    'device_type': 'cisco_ios_telnet',
    'host': '192.168.101.128',
    'port': 2001,
    'secret': 'pass'
}

# order of config
device_list = input('What devices will be configured? ')
#device_list = ['D1', 'D2', 'A1', 'A2', 'P1', 'P2']
new = device_list.split(',')
print(new)
#for device in device_info:
#    print(device)

# WRITE
d1_config = [
    'ip dhcp excluded-add 10.2.1.1 10.2.1.100',
    'ip dhcp excluded-add 10.2.1.200 10.2.1.254',
    'ip dhcp pool ipPoolA',
    'network 10.2.1.0 255.255.255.0',
    'default-router 10.2.1.254',
    'exit'
]

d2_config = [
    'ip dhcp excluded-add 10.2.1.1 10.2.1.199',
    'ip dhcp excluded-add 10.2.1.250 10.2.1.254',
    'ip dhcp pool ipPoolB',
    'network 10.2.1.0 255.255.255.0',
    'default-router 10.2.1.254',
    'exit'
]

a1_config = [
    'int e0/0',
    'sw mo ac',
    'sw ac vlan 10',
    'exit'
]

a2_config = [
    'int e1/0',
    'sw mo ac',
    'sw ac vlan 10',
    'exit'
]

p1_config = [
    'int e0/0',
    'no shut',
    'ip add dhcp',
    'exit'
]

p2_config = [
    'int e1/0',
    'no shut',
    'ip add dhcp',
    'exit'
]

# netmiko exceptions
net_except = (ConnectionRefusedError, netmiko.exceptions.NetmikoAuthenticationException)

# initiate variable
log = []

# PUSH
for device in new:
    if device == 'P1':
        device_info['port'] = 2001
    elif device == 'P2':
        device_info['port'] = 2002
    elif device == 'A1':
        device_info['port'] = 2003
    elif device == 'A2':
        device_info['port'] = 2004
    elif device == 'D1':
        device_info['port'] = 2006
    elif device == 'D2':
        device_info['port'] = 2007
    
    #print('~'*50 + ' ' + device)
    #print(device_info)
    try:
        accessCLI = ConnectHandler(**device_info)
        #sh_ip = accessCLI.send_command('sh ip int br')
        #print('~'*20 + ' ' + device + '\n\n')
        #print(sh_ip)
        #print('~'*20 + ' ' + '\n\n')
        
        accessCLI.enable()
        print('-'*20 + '\nConfiguring ' + device + '\n')
        
        if device == 'P1':
            output = accessCLI.send_config_set(p1_config)
            sh_run = accessCLI.send_command('sh ip int br')
        elif device == 'P2':
            output = accessCLI.send_config_set(p2_config)
            sh_run = accessCLI.send_command('sh ip int br')
        elif device == 'A1':
            output = accessCLI.send_config_set(a1_config)
            sh_run = accessCLI.send_command('sh run')
        elif device == 'A2':
            output = accessCLI.send_config_set(a2_config)
            sh_run = accessCLI.send_command('sh run')
        elif device == 'D1':
            output = accessCLI.send_config_set(d1_config)
            sh_run = accessCLI.send_command('sh run')
        elif device == 'D2':
            output = accessCLI.send_config_set(d2_config)
            sh_run = accessCLI.send_command('sh run')
        
        # save to a txt file
        with open ('show_run_output.txt', 'a') as file:
            file.write('\n' + '-'*50 + device + '\n')
            file.write(sh_run)
            file.write('\n\n')
            
        print(output)
        print('\nConfigurations Successfull!!!\n\n')
    
    except net_except as ex:
        list_except = str(ex) + ' -'*3 + device
        log.append(list_except)

for i in log:
    print(i)

