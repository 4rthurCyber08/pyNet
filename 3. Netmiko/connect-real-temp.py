# netmiko documentation: https://ktbyers.github.io/netmiko/docs/netmiko/index.html

# 3 steps to configure devices using python (CONNECT via Netmiko, WRITE commands, PUSH configs)

# Step 1 - CONNECT to the device via Netmiko, ConnectHandler

    # ConnectHandler args: device_type, host/ip, port, username, password, secret
#accessCLI = ConnectHandler(device_type = 'cisco_ios', host = '200.0.0.m', username = 'admin', password = 'pass', secret = 'pass')

    # **kwargs

    # verify connectivity - send command

    #for telnet connections use 'cisco_ios_telnet' as device_type.
        #issue exclusive to rst lab: make sure other connections to devices are closed before running script.
    
# Step 2 - WRITE commands


# Step 3 - PUSH configurations