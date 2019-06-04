
import visa # Import VISA lib
import time # Import time for waits

# Init VISA and list avaible resources
rm = visa.ResourceManager()
available_resources = rm.list_resources()
available_resources # Print available resources

# Choose the instrument required
# TODO: Make this choosing automatic
func_gen = rm.open_resource(available_resources[0])
func_gen.read_termination = '\n'
func_gen.write_termination = '\n'
func_gen.query('*IDN?') # Print IDN to ensure correct instrument has been chosen

# Turn on output at 100Hz, 2.5Vpp, 1.25V offset into HiZ
func_gen.write('C2:OUTP OFF')
# Can I just put BSWV?
func_gen.write('C2:BaSic_WaVe WVTP,SQUARE,FRQ,100,AMP,2.5,OFST,1.25,DUTY,50')
func_gen.write('C2:OUTP ON,LOAD,HZ,PLRT,NOR')
