# MicroPython implementation of Lora sender
# Requires Python files from https://github.com/ehong-tl/micropySX126X to be copied to the device

from sx1262 import SX1262
import time


# Board config as defined in
# https://raw.githubusercontent.com/HelTecAutomation/Heltec_ESP32/598da3226246e7fffae7d4fa4a511fb9f31cad0a/src/driver/board-config.h
#define RADIO_DIO_1    14
#define RADIO_NSS      8
#define RADIO_RESET    12
#define RADIO_BUSY     13
#define LORA_CLK       9
#define LORA_MISO      11
#define LORA_MOSI      10

#The parameters below are:
#spi_bus : SPI bus ID
#clk : SPI CLK pin
#mosi : SPI MOSI pin
#miso : SPI MISO pin
#cs : NSS pin
#irq : DIO1 pin
#rst : RESET pin
#gpio : BUSY pin
sx = SX1262(spi_bus=1, clk=9, mosi=10, miso=11, cs=8, irq=14, rst=12, gpio=13)

# LoRa
sx.begin(freq=915, bw=125.0, sf=7, cr=5, syncWord=0x12,
         power=-5, currentLimit=60.0, preambleLength=8,
         implicit=False, implicitLen=0xFF,
         crcOn=True, txIq=False, rxIq=False,
         tcxoVoltage=1.7, useRegulatorLDO=False, blocking=False)

packet = 0
while True:
    packet += 1
    msg = f'Hello world!: {packet}'
    print('Sending:', msg)
    sx.send(msg.encode('ascii'))
    time.sleep(2)