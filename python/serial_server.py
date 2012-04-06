#! /usb/bin/env python
#-*- coding: utf-8 -*-

import serial

baudrate = 115200
dev_path = "/dev/tty.FireFly-16E2-SPP"

#===============================================================================

def init():
    serial_handler = serial.Serial(dev_path, baudrate)
    return serial_handler

#===============================================================================

def run():
    serial_handler = init()
    while True:
        print ord(serial_handler.read())


if __name__ == "__main__":
    run()
