# SETUP WIFI CONECTION
import network
sta_if = network.WLAN(network.STA_IF)

SSID = 'WLAN'
PW = 'map1982.'

if not sta_if.isconnected():
  print('connecting to network...')
  sta_if.active(True)
  sta_if.connect(SSID, PW)

  while not sta_if.isconnected():
    pass

print('network config:', sta_if.ifconfig())



