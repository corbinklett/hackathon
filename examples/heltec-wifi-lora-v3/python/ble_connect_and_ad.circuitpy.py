import time
from adafruit_ble import BLERadio
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.nordic import UARTService
from adafruit_ble.uuid import StandardUUID
from adafruit_ble.services import Service
from adafruit_ble.characteristics import Characteristic
from adafruit_ble.characteristics.string import StringCharacteristic

# Define a custom service and characteristic
class CustomService(Service):
    uuid = StandardUUID(0x181C)  # Custom service UUID
    custom_characteristic = StringCharacteristic(
        uuid=StandardUUID(0x2A58),  # Custom characteristic UUID
        properties=(Characteristic.READ | Characteristic.WRITE),
        initial_value=b"Hello BLE!",
    )

# Initialize the BLE radio
ble = BLERadio()
ble.name = "MyBLEDevice"

# Create the custom service instance
custom_service = CustomService()

# Create the advertisement
advertisement = ProvideServicesAdvertisement(custom_service)
advertisement.complete_name = "MyBLEDeviceAdv"

# Start advertising
ble.start_advertising(advertisement)
print("Advertising Custom Service...")

while not ble.connected:
    time.sleep(0.1)

print("Device Connected")

while ble.connected:
    # Perform tasks while connected
    pass

print("Device Disconnected")

# Stop advertising when disconnected
ble.stop_advertising()
