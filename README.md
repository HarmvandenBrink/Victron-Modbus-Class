# Victron-Modbus-Class
A class to talk to a Victron GX Modbus module

![Victron](https://github.com/HarmvandenBrink/Victron-Modbus-Class/blob/main/Victron.jpg "Victron")

# How to use the code
## Import the class and connect to a Victron device [or Victron Energy Venus OS on a Raspberry Pi](https://github.com/victronenergy/venus/wiki/raspberrypi-install-venus-image)

Make sure to have the right unit ID of the device. You can find the unit ID per sub-device at the screen of the GX device.


### Reading measurements
```python

MultiPlussssSystem = System("XYZ", "192.168.1.XXX", 502, 100, 10)
MultiPlussssSystem.Measurements()

print(MultiPlussssSystem.Grid_L1)
print(MultiPlussssSystem.Grid_L2)
print(MultiPlussssSystem.Grid_L3)

print(MultiPlussssSystem.Battery_Voltage_System)
print(MultiPlussssSystem.Battery_Current_System)
print(MultiPlussssSystem.Battery_Power_System)

```

### Controlling the power flow (force charge/discharge)

Values are in Watts, negative is discharge.

```python

MultiPlussssVEBus = VEBus("XYZ", "192.168.1.XXX", 502, 246, 10)
MultiPlussssVEBus.Set("ESS_power_setpoint_phase_1", 1000)
MultiPlussssVEBus.Set("ESS_power_setpoint_phase_1", -2500)
MultiPlussssVEBus.Set("ESS_power_setpoint_phase_1", 1500)

```

# Disclaimer

The code within this repository comes with no guarantee, the use of this code is your responsibility.

I take NO responsibility and/or liability for how you choose to use any of the source code available here. By using any of the files available in this repository, you understand that you are AGREEING TO USE AT YOUR OWN RISK.
