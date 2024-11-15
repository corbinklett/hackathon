from ST7735 import TFT
from sysfont import sysfont
from machine import SPI,Pin
import time
import math

#https://github.com/HelTecAutomation/Heltec_ESP32/blob/598da3226246e7fffae7d4fa4a511fb9f31cad0a/src/HT_st7735.h#L17

vtft = Pin(3, Pin.OUT)
led_k = Pin(18, Pin.OUT)
vtft.value(1)
led_k.value(0)

spi = SPI(1, polarity=0, phase=0, sck=Pin(41), mosi=Pin(42), miso=None)
tft=TFT(spi,40,39,38)
tft.initr()
tft.rgb(True)

tft.fill(TFT.BLACK)
tft.text((2, 2), "Hello World!", TFT.WHITE, sysfont, 1)