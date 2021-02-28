# PyDoorbell

The _PyDoorbell_ is a simple project that attempts to create something of a _smart_ doorbell that will not only ring the interior doorbell as one would expect but also send a push notification to mobile device(s).

# Information

The idea of the _PyDoorbell_ is to create a versitile home doorbell that will mimic the typical home doorbell but add it features such as mobile push notifications, image capture and perhaps even motion detection to trigger the doorbell and image capture even if the doorbell button is not pushed. Along with this, also maintain existing functionality in the way of also activating the existing interior doorbell ringer.

# Project Outline

- Activate doorbell as with the existing physical doorbell using a push button
- Connect to WiFi
- Send push notification to mobile device
- Activate existing interior doorbell
- Capture image snapshot of person ringing the doorbell and send with push notification
- If network connectivity is lost or fails, fallback to activating just the interior doorbell ringer
