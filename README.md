
# Introduction

This repository contains MicroPython and Arduino based applications for ESP32 based boards from Heltec Automation. 
Specifically, we have evaluated these applications on following two boards:

## (1) [Heltec Automation Wireless Tracker v1.1](https://resource.heltec.cn/download/Wireless_Tracker/Wireless_Tracker%20_1.1.pdf)

<img src="figs/WirelessTracker.jpg" width="250">

This board contains following components:

- CPU - ESP32-S3FN8 ([datasheet](https://www.espressif.com/sites/default/files/documentation/esp32-s3_datasheet_en.pdf)). ESP32-S3 is a low-power MCU-based system on a chip (SoC) with integrated 2.4 GHz Wi-Fi and Bluetooth® Low Energy (Bluetooth LE). It consists of a high-performance dual-core microprocessor (Xtensa® 32-bit LX7), a ULP coprocessor, a Wi-Fi baseband, a Bluetooth LE baseband, RF module, and numerous peripherals.
- LCD Display: Onboard 0.96-inch 160*80 dot matrix TFT LCD display, based on [ST7735](https://www.displayfuture.com/Display/datasheet/controller/ST7735.pdf)
- [UC6580](https://en.unicore.com/products/dual-band-gps-chip-uc6580/) (GPS SoC): via GNSS (also other satellite systems - QZSS, GLONASS, NAVIC, Galileo)
- [SX1262](https://www.semtech.com/products/wireless-rf/lora-connect/sx1262) (LoRa transceiver) - 868MHz frequency, about -139dBm high sensitivity, +20 dBm power output, high reliability, transmission distance (measured open area communication distance 3.6Km).

Additional Details:

- [Official development doc from Heltec](https://resource.heltec.cn/download/Wireless_Tracker/Wireless_Tracker%20_1.1.pdf)
- [Pin diagram](https://cdn.shopify.com/s/files/1/0084/7465/6845/files/diagram.png?v=1694250615)
- [MicroPython firmware for ESP32](https://micropython.org/download/ESP32_GENERIC_S3/)
- [Arduino library from Heltec](https://github.com/HelTecAutomation/Heltec_ESP32/tree/master)

## (2) [Heltec Automation Wifi LoRa V3](https://heltec.org/project/wifi-lora-32-v3/)

<img src="figs/wifi_lora_v3.jpg" width="250">

This board contains following components:

- CPU - ESP32-S3FN8 ([datasheet](https://www.espressif.com/sites/default/files/documentation/esp32-s3_datasheet_en.pdf)). ESP32-S3 is a low-power MCU-based system on a chip (SoC) with integrated 2.4 GHz Wi-Fi and Bluetooth® Low Energy (Bluetooth LE). It consists of a high-performance dual-core microprocessor (Xtensa® 32-bit LX7), a ULP coprocessor, a Wi-Fi baseband, a Bluetooth LE baseband.
- OLED Display: Onboard 0.96-inch 128*64 dot matrix OLED display, based on [SSD1306](https://www.digikey.com/htmldatasheets/production/2047793/0/0/1/ssd1306.html)
- [SX1262](https://www.semtech.com/products/wireless-rf/lora-connect/sx1262) (LoRa transceiver) - 868MHz frequency, about -139dBm high sensitivity, +20 dBm power output, high reliability, transmission distance (measured open area communication distance 3.6Km).
- Integrated [CP2102](https://www.silabs.com/interface/usb-bridges/classic/device.cp2102?tab=specs) USB to serial port chip,
- Onboard 32MByte Flash


# Applications

Below we list the applications, their language, and necessary library dependencies to get them working.

