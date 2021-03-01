import network
import time
import config

wlan = network.WLAN(network.STA_IF)


def wifi_connect():
    """
    Connects to WiFi.  Will attempt three times to connect.
    """

    count = 1
    hostname = 'Doorbell_{}'.format(config.CLIENT_ID.decode('utf-8'))

    print('\nAttempting to connect to WiFi.  Attempt No. {}'.format(count))

    while not wlan.isconnected() and count < 4:

        wlan.active(True)
        wlan.config(dhcp_hostname=hostname)
        wlan.connect(config.SSID2, config.WIFI_PASSWD)
        count += 1
        time.sleep(2)

    if wlan.isconnected():

        print('\nSuccessfully connected to Wifi \nHostname: {} \nIP Address: {}'.format(
            hostname, wlan.ifconfig()[0]))

    else:

        print('Unable to connect to the Wifi network.')


def wifi_disconnect():
    """
    Function to disconnect from WiFi
    """

    wlan.disconnect()
    wlan.active(False)

    print('Disconnected from WiFi...')


def connection_status():
    """
    Function to get network connection status

    Returns:
        Bool: True for connected, False otherwise
    """

    return wlan.isconnected()
