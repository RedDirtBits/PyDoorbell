import time
import wifi
import urequests
import json
import config
from machine import Pin

# TODO:
# - Handle No WiFi
# - Handle failed response or message send
# - Wait state/time between doorbell press
# - Debounce the switch
# - Set pin for physical relay that will trigger physical doorbell
# - Can it be differentiated between someone pushing the button and activating a motion sensor?

# - Set up two functions baseed on net connectivity
#     - If net connected, trigger pushover and physical doorbell
#     - Use while loop to check connectivity.  If connected, send both.
#     - If not connected, call function to ring only physical doorbell then try to connect
#         - If connection made, call function governing net connection actions

# Is a method needed to prevent multiple triggers if the button is held for a long period of time?

# This will be the trigger to the Pushover notification
doorbell_button = Pin(33, Pin.IN)

# This triggers the physical doorbell chime
relay = Pin(26, Pin.OUT)

def pushover(msg, title):
    
    pushover_url = 'https://api.pushover.net/1/messages.json'
    
    pushover_headers = {'content-type': 'application/json'}
    
    pushover_data = json.dumps({
        'token': config.PUSHOVER_TOKEN,
        'user': config.PUSHOVER_USER,
        'title': title,
        'message': msg
        })
    
    push = urequests.post(url = pushover_url,
                          headers = pushover_headers,
                          data=pushover_data)
    
    pushover_response = json.loads(push.text)
    
    pushover_status_code = pushover_response['status']
    
    print('Pushover Status Code:', pushover_status_code)
    

wifi.wifi_connect()

while True:
    
    if doorbell_button.value() == 0 and wifi.connection_status():
               
        print('doorbell pressed with active WiFi') # This is just a debug statement.  Remove after testing.
        pushover('The Doorbell Has Been Rung', 'Front Door')
        relay.value(1)
        time.sleep(1)
    
        relay.value(0)
        
    elif doorbell_button.value() == 0 and not wifi.connection_status():
        
        print('doorbell pressed with no WiFi') # This is just a debug statement.  Remove after testing.
        relay.value(1)
        time.sleep(1)
        
        relay.value(0)



