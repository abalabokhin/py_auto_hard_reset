#!/usr/bin/python3

import RPi.GPIO as GPIO
import time
import subprocess

def setup_pins(pins):
    GPIO.setmode(GPIO.BCM)
    for i in pins:
        GPIO.setup(i, GPIO.OUT)
        GPIO.output(i, GPIO.HIGH)

def check_host(host):
    line = "ping -c1 -w2 " + str(host)
    print(line)
    status,result = subprocess.getstatusoutput(line)
    if status == 0:
        return True
    else:
        return False

def down_host(pin):
    GPIO.output(pin, GPIO.LOW)
    time.sleep(6)
    GPIO.output(pin, GPIO.HIGH)
    print(pin, "down")

def up_host(pin):
    GPIO.output(pin, GPIO.LOW)
    time.sleep(0.2)
    GPIO.output(pin, GPIO.HIGH)
    print(pin, "up")

def main():
    pins = [16]
    hosts = ["192.168.0.102"]
    sleep_time = 300 

    setup_pins(pins)

    while True:
        for i in range(len(pins)):
            if check_host(hosts[i]):
                print(hosts[i], "ok")
            else:
                print(hosts[i], "is bad, reseting")
                down_host(pins[i])
                time.sleep(0.5)
                up_host(pins[i])

        time.sleep(sleep_time)

main()


