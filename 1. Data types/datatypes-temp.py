#style guide: https://peps.python.org/pep-0008/

# debugging and information
#type() - returns the data type of the specified object
#print() - print the specified object on the terminal
#dir() - determines the properties and methods of a specified object

# variable

# data types
# STRING LITERAL
# can be written using single, double, triple quotes
String_1 = 'single quotes'
String_2 = "double quotes"
String_3 = '''
Multi
Line
String
'''

    # escape characters
escape_s = 'Hello, I\'m Arthur.' #escape chars: \' \\ \n \t \b
alternate_q = "    Hello, I'm Arthur.    "

    # string methods
raw_s = r'Hello, I\'m \nArthur'

name = 'Arthur'
format_s = f'Hello, this is {name}'

    # string concatenation
concatinate_1 = 'Hello '
concatinate_2 = 'I\'m Arthur'
output = concatinate_1 + concatinate_2

    # string index - string[start:stop]

    # split - string.split()
    # split values in a string and return a list
    
    # strip - string.strip(), lstrip(), rstrip()
    # remove leading and trailing whitespace



# INTEGERS & FLOATS
# int = whole numbers, floats = real/floating point numbers
Integer_1 = 40
Integer_2 = 0
Integer_3 = -5

Float_1 = 20.0
Float_2 = 5e10

# arithmetic operators
add_ = 5 + 2    # add
sub_ = 5 - 2    # subtract
mul_ = 5*2      # multiply
div_ = 5/2      # divide
mod_ = 5%2      # modulus
exp_ = 5**2     # exponent
flo_ = 5//2     # floor division

a = 0.1*3       #round() method

Sep = '~'*50



# BOOLEAN
# boolean outputs either true or false
Boolean_1 = True
Boolean_2 = False

output = bool(Integer_2)



# TUPLE
# a way to store multiple items in a single variable
# tuples are ordered, unchangeable, allow duplicate values
Tuple_1 = (40, 'ios', '10.21.1.4')
Tuple_2 = 20, 'Hello', True, "Hi", {4, 5}, {'key':'value'}, ['list1', 'item2']

a = 1,

    # tuple index - tuple[start:stop]



# LIST
# list are ordered, changeable, allow duplicate values
List_1 = ['item1', 'item2', 3, True]
devices = ["router1", "router2", "router3", "switch1", "switch2", "firewall1"]
commands = ["show run", "show ip interface brief", "show vlan"] 

    # list index - list[start:stop]
    
    # append - list.append()
    # add an object to the end of the list
    
    # insert - list.insert(index, object)
    # insert an object with a specified index



# SETS
# sets are unordered, unchangeable*, unindexed, do not allow duplicate values
# sets cannot contain list, set, and dictionary
Set_1 = {'vlan20', 'vlan30', 'vlan40'}
Set_2 = {'vlan18', 'vlan19', 'vlan20'}
Set_3 = {'vlan29', 'vlan30', 'vlan31', 'vlan32'}

    # union - x.union(y,z,..)
    # combine the contents of multiple sets, ommitting duplicates

    # intersection x.intersection(y,z,..)
    # return duplicates between multiple sets.



# DICTIONARY
# sets are ordered, changeable, unindexed, do not allow duplicate values
Dict_1 = {'key': 'value', 'device': 'cisco'}
Dict_2 = {
    'device': 'cisco',
    'ip': '10.21.1.1',
    'port': 22
}

    #obtaining values - dict['key']
    
    #alter values - dict['key'] = 'new value'
    
    # pop - dict.pop('key')
    # removes a specified key from a dictionary and returns that key’s value.
    
    # update - dict.update(dict2)
    # Merges two dictionaries
    
    # clear - dict.clear()
    # remove all contents of a dictionary
    


# navigating & handling data types
# index: string, tuple, list, dictionary
hello = 'Hello World'
device = ('csr1000v', 'firepower 1150', 'PA-220')
hostnames = ['R1', 'R2', 'R3', 'R4']
cli = {
    'device_type': 'cisco_ios',
    'ip': '192.168.108.1',
    'port': 22,
}

#-review index



#----

nested = [
    ('csr1000v', 'firepower 1150', 'PA-220', 'layer 3 switch', 'edgeRouter'),
    [
        'ASW',
        'EDGE',
        'CSW',
        {
            'device_type': 'cisco_ios',
            'ip': '200.0.0.m',
            'port': 22,
        }
    ]
]

# task 01 - obtain PA-220

# taks 02 - obtain the value of ip

# taks 03 - print the paragraph with the respective values using fstring

    # "The device we will be using is an {edgeRouter}. 
    # It uses a cisco_ios that has an ip of {200.0.0.m}
    # The hostname for the device will be {EDGE}."
    