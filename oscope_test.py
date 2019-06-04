'''
Function testing and debug for future use
Tested on Siglent SDS 1202X oscope
'''

import visa # Import VISA lib
import time # Import time for waits

# Init VISA and list avaible resources
rm = visa.ResourceManager()
available_resources = rm.list_resources()
available_resources # Print available resources

# Choose the instrument required
# TODO: Make this choosing automatic
oscope = rm.open_resource(available_resources[0])
oscope.write_termination = '\n'
oscope.read_termination = '\n'
oscope.timeout = 10000 # Wait 10s for response
oscope.query('*IDN?') # Print IDN to ensure correct instrument has been chosen

oscope.query('MENU ON')
oscope.query('MENU OFF')
