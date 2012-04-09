#!/usr/bin/env python
# -*- coding: utf-8 -*-
import serial
import time
import sys
"""
class XBee 
"""

class XBee:
    def __init__(self):
        """
        initializing parameters
        """
        pass

    def read_data(self, handle):#strip escape sequence
        data = ord(handle.read())
        if(data == 0x7D):
            return 0x20 ^ ord(handle.read())
        else:
            return data
        
        
    def transmit_api_64(self, handle, dst64, dst16, data):
        """
        Transmiting to 64bit address with API mode
        """
        #Signal container
        payload = []
        #Start delimiter
        payload.append(0x7E)
        #API Identifier + Frame ID + AT Command + Parameter Value
        #11 means the length except Parameter Value
        length = 14 + len(data)
        #length of MSB & LSB        
        payload.append((length>>8) & 0xff)#MSB
        payload.append(length & 0xff)#LSB
        #API Identifier(For 64bit case, it's "0x01")
        payload.append(0x10)
        #Frame ID->response return value?->search it
        payload.append(1)
        #64bit destination address(MSB & LSB)
        payload.append((dst64>>56) & 0xff)#MSB(4)
        payload.append((dst64>>48) & 0xff)#MSB(3)
        payload.append((dst64>>40) & 0xff)#MSB(2)
        payload.append((dst64>>32) & 0xff)#MSB(1)
        payload.append((dst64>>24) & 0xff)#LSB(4)
        payload.append((dst64>>16) & 0xff)#LSB(3)
        payload.append((dst64>>8) & 0xff)#LSB(2)
        payload.append(dst64 & 0xff)#LSB(1)
        #16bit destination address(MSB & LSB)
        payload.append((dst16>>8) & 0xff)#LSB(2)
        payload.append(dst16 & 0xff)#LSB(1)
        #Broadcast radius(0x00=>Maximum hops)
        payload.append(0x00)
        #Options(Bitfield of supported transmission options)
        payload.append(0x00)
        for i in data:
            payload.append(ord(i))
        checksum = 0
        for i in payload[3:16]:
            checksum += i
        for i in data:
            checksum += ord(i) #data's type is str.
        #checksum
        payload.append(0xff - (checksum & 0xff))
        for i in payload:
            handle.write(chr(i))
            print hex(i)
    


    def receive_api_64(self, handle):
        """
        receive_api data
        """
        data = []
        all_received_data = []
        if(ord(handle.read())==0x7E):
            all_received_data.append(0x7E)
            #receive_apid datasize(MSB & LSB)
            data_size_MSB =  self.read_data(handle)
            data_size_LSB =  self.read_data(handle)
            all_received_data.append(data_size_MSB)
            all_received_data.append(data_size_LSB)
            #combine
            data_size = data_size_MSB << 8 | data_size_LSB
            #api identifier
            api_identifier = self.read_data(handle)
            all_received_data.append(api_identifier)
            #source address(MSB & LSB)
            src_addr_MSB = self.read_data(handle)
            src_addr_LSB = self.read_data(handle)
            all_received_data.append(src_addr_MSB)
            all_received_data.append(src_addr_LSB)
            #rssi => strength of signal
            rssi = self.read_data(handle)
            all_received_data.append(rssi)
            #option
            opt = self.read_data(handle)
            all_received_data.append(opt)
            for i in range(data_size - 5):
                d = self.read_data(handle)#extract one by one
                data.append(d)
                all_received_data.append(d)
            checksum = self.read_data(handle)
            all_received_data.append(checksum)

            hoge = [126, 0, 8, 129, 17, 17, 48, 0, 48, 48, 49, 155]
            received_str = []
            _hoge = []
            for j in hoge:
                _hoge.append(chr(j))
                
            for i in all_received_data:
                received_str.append(chr(i))
            print "==============="
            print "".join(received_str)
            print all_received_data
            print "==============="
            print "".join(_hoge)
            print hoge
        return data
    
    def receive(self, handle):
        while True:
            d = handle.read()
            print d
            #echo
            handle.write(d)
            
    def transmit(self, handle, contents):
        for i in contents:
            handle.write(chr(i))
            

def run():
    mode = int(sys.argv[1])

    if mode == 1 or mode == 4:
        #x1 = serial.Serial("/dev/tty.usbserial-A700eXfF", 9600)
        #x1 = serial.Serial("/dev/tty.usbserial-A7005EF1", 9600)
        x1 = serial.Serial("/dev/tty.usbmodem641", 115200)
    else:
        x2 = serial.Serial("/dev/tty.usbserial-A700eXfF", 9600)
        #x2 = serial.Serial("/dev/tty.usbserial-A7005EF1", 9600)
        #tty.usbserial-A7005EF1

    #x1 = 0
    xbee = XBee()
    data = "Tx2Coord"
    if mode == 1:
        xbee.transmit_api_64(x1, 0x0000000000000000, 0xFFFE, data)
    elif mode == 2:
        res =  xbee.receive_api(x2)
        for i in res:
            print chr(i)
    elif mode == 3:
        xbee.receive(x2)
    elif mode == 4:
        #OFF
        #contents = [126, 0, 8, 129, 17, 17, 49, 0, 48, 48, 48, 155]
        #PIN0 ON
        contents = [126, 0, 8, 129, 17, 17, 49, 0, 48, 48, 49, 154]
        #PIN1 ON
        #contents = [126, 0, 8, 129, 17, 17, 49, 0, 48, 49, 48, 154]
        #PIN2 ON
        #contents = [126, 0, 8, 129, 17, 17, 47, 0, 49, 48, 48, 156]
        #ALL PIN ON
        #contents = [126, 0, 8, 129, 17, 17, 48, 0, 49, 49, 49, 153]

        xbee.transmit(x1, contents)
    
    if mode == 1 or mode == 4:
        x1.close()
    else:
        x2.close()

    
if __name__ == "__main__":
    run()
