# Victron-Modbus-Class
A class to talk to a Victron GX Modbus module

![Victron](https://github.com/HarmvandenBrink/Victron-Modbus-Class/blob/main/Victron.jpg "Victron")

# How to use the code
## Import the class and connect to a Victron device [or Victron Energy Venus OS on a Raspberry Pi](https://github.com/victronenergy/venus/wiki/raspberrypi-install-venus-image)

```python

MultiPlussssBat = Battery("XYZ", "192.168.1.102", 502, 247, 10)
MultiPlussssBat.Measurements()

print(MultiPlussssBat.__dict__)

MultiPlussssVEBus = VEBus("XYZ", "192.168.1.102", 502, 246, 10)
MultiPlussssVEBus.Measurements()

print(MultiPlussssVEBus.__dict__)

MultiPlussssSystem = System("XYZ", "192.168.1.102", 502, 100, 10)
MultiPlussssSystem.Measurements()

print(MultiPlussssSystem.__dict__)

MultiPlussssGrid = Grid("XYZ", "192.168.1.102", 502, 30, 10)
MultiPlussssGrid.Measurements()

print(MultiPlussssGrid.__dict__)

MultiPlussssPVInverter = PVInverter("XYZ", "192.168.1.102", 502, 32, 10)
MultiPlussssPVInverter.Measurements()

print(MultiPlussssPVInverter.__dict__)

```


# Disclaimer

The code within this repository comes with no guarantee, the use of this code is your responsibility.

I take NO responsibility and/or liability for how you choose to use any of the source code available here. By using any of the files available in this repository, you understand that you are AGREEING TO USE AT YOUR OWN RISK.
