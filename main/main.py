import credentials as c
import sys
from machine import Pin


from main.ota_updater import OTAUpdater
o = OTAUpdater('https://github.com/andymarkwart/ota_test')

btn0 = Pin(0, Pin.IN, Pin.PULL_UP)
btn1 = Pin(35, Pin.IN, Pin.PULL_UP)


def download_and_install_update_if_available(ssid, psk):
    o.download_and_install_update_if_available(ssid, psk)

def check_for_updates(ssid, psk):
    print("Checking for updates...")
    o.using_network(ssid, psk)
    o.check_for_update_to_install_during_next_reboot()
    

def start():
    # from main.x import project
    # project = YourProject()
    # ...
    print("\n>>>\nProgram MAIN\nVersion: 0.5.2\n<<<\n")


def boot():
    if btn0.value() == 0:
        print("Button 0 low, exiting...")
        sys.exit()
    elif btn1.value() == 0:
        check_for_updates(c.ssid, c.psk)
    else:
        download_and_install_update_if_available(c.ssid, c.psk)
        start()


boot()




