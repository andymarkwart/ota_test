import credentials as c
import sys
from machine import Pin

from ota_updater import OTAUpdater

btn0 = Pin(0, Pin.IN, Pin.PULL_UP)

def download_and_install_update_if_available():
    o = OTAUpdater('https://github.com/andymarkwart/ota_test')
    #o.using_network(c.ssid, c.psk)
    #o.check_for_update_to_install_during_next_reboot()
    o.download_and_install_update_if_available("OnePlus5", "andyandy)


def start():
    # from main.x import project
    # project = YourProject()
    # ...
    print("\n>>>\nProgram MAIN\nVersion: 0.2\n<<<\n")


def boot():
    if btn0.value() == 0:
        print("Button 0 low, exiting...")
        sys.exit()
    else:
        download_and_install_update_if_available()
        start()


boot()




