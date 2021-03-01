import time
import wifi
import urequests
import json
import config
from machine import Pin

# This will be the trigger to the Pushover notification
doorbell_button = Pin(33, Pin.IN)

# This triggers the physical doorbell chime
relay = Pin(26, Pin.OUT)


def pushover(msg, title):
    """
     Forms the Pushover notification
    """

    pushover_url = 'https://api.pushover.net/1/messages.json'
    pushover_headers = {'content-type': 'application/json'}

    pushover_data = json.dumps({
        'token': config.PUSHOVER_TOKEN,
        'user': config.PUSHOVER_USER,
        'title': title,
        'message': msg
    })

    push = urequests.post(url=pushover_url,
                          headers=pushover_headers,
                          data=pushover_data)

    pushover_response = json.loads(push.text)
    pushover_status_code = pushover_response['status']

    if pushover_status_code == 1:

        print('Notification Sent')

    else:

        print('Notification failed to send.  Status Code {}'.format(
            pushover_status_code))


# Connect to WiFi
wifi.wifi_connect()

while True:

    # When there is a WiFi connection and button is pressed
    if doorbell_button.value() == 0 and wifi.connection_status():

        # Send the pushover notifiation that the doorbell has been pressed
        pushover('The Doorbell Has Been Rung', 'Front Door')

        # Trigger the relay so that the interior doorbell ringer is also activated
        relay.value(1)

        # Sleep cycle to hold the relay high for one second
        time.sleep(1)

        # De-energize the relay
        relay.value(0)

        # I am not fond of all the sleep cycles but it is the easiest way
        # Pause the loop in case someone holds the button for a really long time.
        time.sleep(3)

    # When there is no WiFi connection and the button is pressed
    elif doorbell_button.value() == 0 and not wifi.connection_status():

        # Energize the physical relay to activate the interior doorbell ringer
        relay.value(1)

        # Hold the relay high for one second
        time.sleep(1)

        # De-energize the relay
        relay.value(0)

        # Sleep delay to reduce multiple consecutive rings
        time.sleep(3)
