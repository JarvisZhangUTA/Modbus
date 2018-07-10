import serial.tools.list_ports
from ser import Ser

plist = list(serial.tools.list_ports.comports())

if len( plist ) == 0:
    print 'no port found'
    exit()

idx = 0
for port in list( plist ):
    print '%s %s' % (idx, port)
    idx += 1

idx = int( raw_input("Input port number:") )

if idx < 0 or idx >= len( plist ):
    print 'invalid number'
    exit()

port = plist[idx]
print port

ser = Ser( port[0] )
print ser.send_cmd('010591F50000F104')