# Handling nested loops
import json
import pprint
import re

with open(r'./4. Nested Loops, Regex/deviceConfigs.json') as file:
    device_configs = json.load(file)

pprint.pp(device_configs, indent=4)

for primKey in device_configs:
    
    for secKey in device_configs[primKey]:
        value = device_configs[primKey][secKey]
        
        eval = bool(re.search('_', value))
        
        if eval:
            new_value = re.sub('_', '', value)
            device_configs[primKey][secKey] = new_value
        
    print('\n')

pprint.pp(device_configs)

with open(r'./4. Nested Loops, Regex/deviceConfigs.json', 'w') as file:
    output = json.dumps(device_configs, indent=4)
    file.write(output)
# regex
# updateValue = re.sub(r'_', monitorNumber, mValue)
