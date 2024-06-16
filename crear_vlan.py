from netmiko import ConnectHandler

# Define the device information
device = {
    'device_type': 'cisco_ios',
    'host': '192.168.56.102',
    'username': 'cisco',
    'password': 'cisco123!',
}

# Connect to the device
net_connect = ConnectHandler(**device)
net_connect.enable()  # Enter enable mode

# Define the VLAN ID and name
vlan_id = 100
vlan_name = 'VLAN100'

# Build the configuration commands
config_commands = [
    f'vlan {vlan_id}',
    f'name {vlan_name}',
]

# Send configuration commands
output = net_connect.send_config_set(config_commands)
print(output)

# Disconnect from the device
net_connect.disconnect()