from machine import Pin, I2C
import ssd1306

# Pins taken from here - https://github.com/ropg/heltec_esp32_lora_v3/blob/25791aa932a4ef4fe587834144ad6c5470c990ff/boards/variants/ht_u_esp32_lora_v3/pins_arduino.h#L80-L82

rst = Pin(21, Pin.OUT)
rst.value(1)

i2c = I2C(scl=Pin(18), sda=Pin(17), freq=500000)
display = ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3c)

display.text('Hello World!', 0, 0, 1)
display.show()