import serial

class Ser(object):
    def __init__(self, port_name):
        self.port = serial.Serial(port=port_name, baudrate=9600, bytesize=8, parity='E', stopbits=1, timeout=2)
    
    def send_cmd(self, cmd):
        cmd = bytearray.fromhex(cmd)
        self.port.write(cmd)
        response = self.port.readall()
        response = self.num2hex(response)
        return response
    
    # 10 str list to 16 int list
    def num2hex(self, string):
        res = []
        result = []
        for item in string:
            res.append(item)
        for i in res:
            result.append(hex(i))
        return result
    
    # 16 str list format
    def hex2hex(self, string):
        result = []
        for item in string:
            result.append(  hex( int(item, 16) ) )
        return result
    
    def str_split(self, string):
        return [string[i:i+2] for i in range(0, len(string), 2)]