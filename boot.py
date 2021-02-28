import esp
import esp32
import gc
import config
import network

esp.osdebug(None)
print('CPU Temp.:', esp32.raw_temperature())
gc.collect()
