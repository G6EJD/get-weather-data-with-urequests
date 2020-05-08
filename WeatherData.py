from m5stack import *
from m5ui import *
from uiflow import *
import wifiCfg
import urequests
import ujson

while True:
  lcd.clear()
  wifiCfg.doConnect('mywifi', 'mypassword')
  req = urequests.get('http://dataservice.accuweather.com/currentconditions/v1/22889?apikey=ZFPeG8rPkVmqvZ8QrAOUNwG4mi334Yul')
  tempi = (ujson.loads((req.text)))[0]["Temperature"]["Metric"]
  time = (ujson.loads((req.text)))[0]["LocalObservationDateTime"]
  condition = (ujson.loads((req.text)))[0]["WeatherText"]
  lcd.print(str(tempi["Value"]),0,0)
  lcd.print(str(time),0,20)
  lcd.print(str(condition),0,40)
  lcd.print('''
      \   /
       .-.
   -- (   ) --
       `-’
      /   \
  ''',0,90,0xffff00)

  req.close()
  wait_ms(1800000)
# Write your code here :-)
