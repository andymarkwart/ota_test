import credentials as c

from ota_updater import OTAUpdater


def download_and_install_update_if_available():
    o = OTAUpdater('https://github.com/andymarkwart/ota_test.git')
    o.download_and_install_update_if_available(c.ssid, c.psk)


def start():
    # from main.x import project
    # project = YourProject()
    # ...
    print("\n>>>\nProgram MAIN\nVersion: 0.0\n<<<\n")


def boot():
    download_and_install_update_if_available()
    start()


boot()




