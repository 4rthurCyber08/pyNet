import netmiko
from netmiko import ConnectHandler

# default values
device_info = {
    'device_type': 'cisco_ios_telnet',
    'host': '192.168.101.128',
    'port': 2006,
    'secret': 'pass'
}

accessCLI = ConnectHandler(**device_info)
output = accessCLI.send_command('delete vlan.dat', expect_string='vlan.dat')
output = accessCLI.send_command(' ', expect_string='confirm')

print(output)