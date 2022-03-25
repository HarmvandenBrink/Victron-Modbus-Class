#!/usr/bin/env python

"""
Victron GX Modbus Class
MIT License
Copyright (c) 2022 Harm van den Brink
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

__author__  = 'Harm van den Brink'
__email__   = 'harmvandenbrink@gmail.com'
__license__ = 'MIT License'

__version__ = '2.42'
__status__  = 'Production'
__name__    = 'Victron GX Modbus Class'

from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.payload import BinaryPayloadBuilder
from pymodbus.client.sync import ModbusTcpClient as ModbusClient

class Victron():
	def __init__(self, id):
		self.id = id

class Battery(Victron):
	def __init__(self, id, ip, port, unitid, mqttid):
		super().__init__(id)
		self.ip = ip
		self.port = port
		self.unitid = unitid
		self.mqttid = mqttid

		self.Battery_voltage = None
		self.Starter_battery_voltage = None
		self.Current = None
		self.Battery_temperature = None
		self.Mid_point_voltage_of_the_battery_bank = None
		self.Mid_point_deviation_of_the_battery_bank = None
		self.Consumed_Amphours = None
		self.State_of_charge = None
		self.Alarm = None
		self.Low_voltage_alarm = None
		self.High_voltage_alarm = None
		self.Low_starter_voltage_alarm = None
		self.High_starter_voltage_alarm = None
		self.Low_State_of_charge_alarm = None
		self.Low_temperature_alarm = None
		self.High_temperature_alarm = None
		self.Mid_voltage_alarm = None
		self.Low_fused_voltage_alarm = None
		self.High_fused_voltage_alarm = None
		self.Fuse_blown_alarm = None
		self.High_internal_temperature_alarm = None
		self.Relay_status = None
		self.Deepest_discharge = None
		self.Last_discharge = None
		self.Average_discharge = None
		self.Charge_cycles = None
		self.Full_discharges = None
		self.Total_Ah_drawn = None
		self.Minimum_voltage = None
		self.Maximum_voltage = None
		self.Time_since_last_full_charge = None
		self.Automatic_syncs = None
		self.Low_voltage_alarms = None
		self.High_voltage_alarms = None
		self.Low_starter_voltage_alarms = None
		self.High_starter_voltage_alarms = None
		self.Minimum_starter_voltage = None
		self.Maximum_starter_voltage = None
		self.Low_fused_voltage_alarms = None
		self.High_fused_voltage_alarms = None
		self.Minimum_fused_voltage = None
		self.Maximum_fused_voltage = None
		self.Discharged_Energy = None
		self.Charged_Energy = None
		self.Time_to_go = None
		self.State_of_health = None
		self.Max_charge_voltage = None
		self.Min_discharge_voltage = None
		self.Max_charge_current = None
		self.Max_discharge_current = None
		self.Capacity = None
		self.Diagnostics_1st_last_error_timestamp = None
		self.Diagnostics_2nd_last_error_timestamp = None
		self.Diagnostics_3rd_last_error_timestamp = None
		self.Diagnostics_4th_last_error_timestamp = None
		self.Minimum_cell_temperature = None
		self.Maximum_cell_temperature = None
		self.High_charge_current_alarm = None
		self.High_discharge_current_alarm = None
		self.Cell_imbalance_alarm = None
		self.Internal_failure_alarm = None
		self.High_charge_temperature_alarm = None
		self.Low_charge_temperature_alarm = None
		self.Low_cell_voltage_alarm = None

		self.State = None
		self.Error = None
		self.System_switch = None
		self.Balancing = None
		self.System_number_of_batteries = None
		self.System_batteries_parallel = None
		self.System_batteries_series = None
		self.System_number_of_cells_per_battery = None
		self.System_minimum_cell_voltage = None
		self.System_maximum_cell_voltage = None
		self.Diagnostics_shutdowns_due_to_error = None
		self.Diagnostics_1st_last_error = None
		self.Diagnostics_2nd_last_error = None
		self.Diagnostics_3rd_last_error = None
		self.Diagnostics_4th_last_error = None
		self.IO_allow_to_charge = None
		self.IO_allow_to_discharge = None
		self.IO_external_relay = None
		self.History_Min_cell_voltage = None
		self.History_Max_cell_voltage = None

	def Measurements(self):
		client = ModbusClient(self.ip, port=self.port, unit_id=self.unitid, auto_open=True, auto_close=True)

		# Register addresses
		# com.victronenergy.battery
		# Start 259 - End 326
		# Start 1282 - End 1301

		address = 259
		count = 68
		result = client.read_holding_registers(address, count, unit=self.unitid)
		decoder = BinaryPayloadDecoder.fromRegisters(result.registers, byteorder=Endian.Big, wordorder=Endian.Big)

		self.Battery_voltage = decoder.decode_16bit_uint()
		self.Starter_battery_voltage = decoder.decode_16bit_uint()
		self.Current = decoder.decode_16bit_int()
		self.Battery_temperature = decoder.decode_16bit_int()
		self.Mid_point_voltage_of_the_battery_bank = decoder.decode_16bit_uint()
		self.Mid_point_deviation_of_the_battery_bank = decoder.decode_16bit_uint()
		self.Consumed_Amphours = decoder.decode_16bit_uint()
		self.State_of_charge = decoder.decode_16bit_uint()
		self.Alarm = decoder.decode_16bit_uint()
		self.Low_voltage_alarm = decoder.decode_16bit_uint()
		self.High_voltage_alarm = decoder.decode_16bit_uint()
		self.Low_starter_voltage_alarm = decoder.decode_16bit_uint()
		self.High_starter_voltage_alarm = decoder.decode_16bit_uint()
		self.Low_State_of_charge_alarm = decoder.decode_16bit_uint()
		self.Low_temperature_alarm = decoder.decode_16bit_uint()
		self.High_temperature_alarm = decoder.decode_16bit_uint()
		self.Mid_voltage_alarm = decoder.decode_16bit_uint()
		self.Low_fused_voltage_alarm = decoder.decode_16bit_uint()
		self.High_fused_voltage_alarm = decoder.decode_16bit_uint()
		self.Fuse_blown_alarm = decoder.decode_16bit_uint()
		self.High_internal_temperature_alarm = decoder.decode_16bit_uint()
		self.Relay_status = decoder.decode_16bit_uint()
		self.Deepest_discharge = decoder.decode_16bit_uint()/-10
		self.Last_discharge = decoder.decode_16bit_uint()/-10
		self.Average_discharge = decoder.decode_16bit_uint()/-10
		self.Charge_cycles = decoder.decode_16bit_uint()
		self.Full_discharges = decoder.decode_16bit_uint()
		self.Total_Ah_drawn = decoder.decode_16bit_uint()/-10
		self.Minimum_voltage = decoder.decode_16bit_uint()/100
		self.Maximum_voltage = decoder.decode_16bit_uint()/100
		self.Time_since_last_full_charge = decoder.decode_16bit_uint()*100
		self.Automatic_syncs = decoder.decode_16bit_uint()
		self.Low_voltage_alarms = decoder.decode_16bit_uint()
		self.High_voltage_alarms = decoder.decode_16bit_uint()
		self.Low_starter_voltage_alarms = decoder.decode_16bit_uint()
		self.High_starter_voltage_alarms = decoder.decode_16bit_uint()
		self.Minimum_starter_voltage = decoder.decode_16bit_uint()/100
		self.Maximum_starter_voltage = decoder.decode_16bit_uint()/100
		self.Low_fused_voltage_alarms = decoder.decode_16bit_uint()
		self.High_fused_voltage_alarms = decoder.decode_16bit_uint()
		self.Minimum_fused_voltage = decoder.decode_16bit_uint()/100
		self.Maximum_fused_voltage = decoder.decode_16bit_uint()/100
		self.Discharged_Energy = decoder.decode_16bit_uint()/10
		self.Charged_Energy = decoder.decode_16bit_uint()/10
		self.Time_to_go = decoder.decode_16bit_uint()*100
		self.State_of_health = decoder.decode_16bit_uint()/10
		self.Max_charge_voltage = decoder.decode_16bit_uint()/10
		self.Min_discharge_voltage = decoder.decode_16bit_uint()/10
		self.Max_charge_current = decoder.decode_16bit_uint()/10
		self.Max_discharge_current = decoder.decode_16bit_uint()/10
		self.Capacity = decoder.decode_16bit_uint()/10
		self.Diagnostics_1st_last_error_timestamp = decoder.decode_32bit_int()
		self.Diagnostics_2nd_last_error_timestamp = decoder.decode_32bit_int()
		self.Diagnostics_3rd_last_error_timestamp = decoder.decode_32bit_int()
		self.Diagnostics_4th_last_error_timestamp = decoder.decode_32bit_int()
		self.Minimum_cell_temperature = decoder.decode_16bit_int()/10
		self.Maximum_cell_temperature = decoder.decode_16bit_int()/10
		self.High_charge_current_alarm = decoder.decode_16bit_uint()
		self.High_discharge_current_alarm = decoder.decode_16bit_uint()
		self.Cell_imbalance_alarm = decoder.decode_16bit_uint()
		self.Internal_failure_alarm = decoder.decode_16bit_uint()
		self.High_charge_temperature_alarm = decoder.decode_16bit_uint()
		self.Low_charge_temperature_alarm = decoder.decode_16bit_uint()
		self.Low_cell_voltage_alarm = decoder.decode_16bit_uint()

		address = 1282
		count = 20
		result = client.read_holding_registers(address, count, unit=self.unitid)
		decoder = BinaryPayloadDecoder.fromRegisters(result.registers, byteorder=Endian.Big, wordorder=Endian.Big)

		self.State = decoder.decode_16bit_uint()
		self.Error = decoder.decode_16bit_uint()
		self.System_switch = decoder.decode_16bit_uint()
		self.Balancing = decoder.decode_16bit_uint()
		self.System_number_of_batteries = decoder.decode_16bit_uint()
		self.System_batteries_parallel = decoder.decode_16bit_uint()
		self.System_batteries_series = decoder.decode_16bit_uint()
		self.System_number_of_cells_per_battery = decoder.decode_16bit_uint()
		self.System_minimum_cell_voltage = decoder.decode_16bit_uint()/100
		self.System_maximum_cell_voltage = decoder.decode_16bit_uint()/100
		self.Diagnostics_shutdowns_due_to_error = decoder.decode_16bit_uint()
		self.Diagnostics_1st_last_error = decoder.decode_16bit_uint()
		self.Diagnostics_2nd_last_error = decoder.decode_16bit_uint()
		self.Diagnostics_3rd_last_error = decoder.decode_16bit_uint()
		self.Diagnostics_4th_last_error = decoder.decode_16bit_uint()
		self.IO_allow_to_charge = decoder.decode_16bit_uint()
		self.IO_allow_to_discharge = decoder.decode_16bit_uint()
		self.IO_external_relay = decoder.decode_16bit_uint()
		self.History_Min_cell_voltage = decoder.decode_16bit_uint()/100
		self.History_Max_cell_voltage = decoder.decode_16bit_uint()/100

class MultiPlusGX(Victron):
	def __init__(self, id, ip, port, unitid, mqttid):
		super().__init__(id)
		self.ip = ip
		self.port = port
		self.unitid = unitid
		self.mqttid = mqttid

		self.Input_voltage_phase_1 = None
		self.Input_voltage_phase_2 = None
		self.Input_voltage_phase_3 = None
		self.Input_current_phase_1 = None
		self.Input_current_phase_2 = None
		self.Input_current_phase_3 = None
		self.Input_power_phase_1 = None
		self.Input_power_phase_2 = None
		self.Input_power_phase_3 = None
		self.Input_frequency = None
		self.Output_voltage_phase_1 = None
		self.Output_voltage_phase_2 = None
		self.Output_voltage_phase_3 = None
		self.Output_current_phase_1 = None
		self.Output_current_phase_2 = None
		self.Output_current_phase_3 = None
		self.Output_power_phase_1 = None
		self.Output_power_phase_2 = None
		self.Output_power_phase_3 = None
		self.Output_frequency = None
		self.AC_input_1_source_type = None
		self.AC_input_2_source_type = None
		self.Ac_input_1_current_limit = None
		self.Ac_input_2_current_limit = None
		self.Phase_count = None
		self.Active_AC_input = None
		self.Battery_voltage = None
		self.Battery_current = None
		self.Battery_temperature = None
		self.Battery_State_of_Charge = None
		self.Inverter_state = None
		self.Switch_position = None
		self.Temperature_alarm = None
		self.High_voltage_alarm = None
		self.High_AC_Out_voltage_alarm = None
		self.Low_battery_temperature_alarm = None
		self.Low_voltage_alarm = None
		self.Low_AC_Out_voltage_alarm = None
		self.Overload_alarm = None
		self.High_DC_ripple_alarm = None
		self.PV_power = None
		self.User_yield = None
		self.Relay_on_the_Multi_RS = None
		self.MPP_operation_mode = None
		self.PV_voltage = None
		self.Error_code = None
		self.Energy_from_AC_in_1_to_AC_out = None
		self.Energy_from_AC_in_1_to_battery = None
		self.Energy_from_AC_in_2_to_AC_out = None
		self.Energy_from_AC_in_2_to_battery = None
		self.Energy_from_AC_out_to_AC_in_1 = None
		self.Energy_from_AC_out_to_AC_in_2 = None
		self.Energy_from_battery_to_AC_in_1 = None
		self.Energy_from_battery_to_AC_in_2 = None
		self.Energy_from_battery_to_AC_out = None
		self.Energy_from_AC_out_to_battery = None
		self.Energy_from_solar_to_AC_in_1 = None
		self.Energy_from_solar_to_AC_in_2 = None
		self.Energy_from_solar_to_AC_out = None
		self.Energy_from_solar_to_battery = None
		self.Yield_today = None
		self.Maximum_charge_power_today = None
		self.Yield_yesterday = None
		self.Maximum_charge_power_yesterday = None
		self.Yield_today_for_tracker_0 = None
		self.Yield_today_for_tracker_1 = None
		self.Yield_today_for_tracker_2 = None
		self.Yield_today_for_tracker_3 = None
		self.Yield_yesterday_for_tracker_0 = None
		self.Yield_yesterday_for_tracker_1 = None
		self.Yield_yesterday_for_tracker_2 = None
		self.Yield_yesterday_for_tracker_3 = None
		self.Maximum_charge_power_today_for_tracker_0 = None
		self.Maximum_charge_power_today_for_tracker_1 = None
		self.Maximum_charge_power_today_for_tracker_2 = None
		self.Maximum_charge_power_today_for_tracker_3 = None
		self.Maximum_charge_power_yesterday_tracker_0 = None
		self.Maximum_charge_power_yesterday_tracker_1 = None
		self.Maximum_charge_power_yesterday_tracker_2 = None
		self.Maximum_charge_power_yesterday_tracker_3 = None
		self.PV_voltage_for_tracker_0 = None
		self.PV_voltage_for_tracker_1 = None
		self.PV_voltage_for_tracker_2 = None
		self.PV_voltage_for_tracker_3 = None
		self.PV_power_for_tracker_0 = None
		self.PV_power_for_tracker_1 = None
		self.PV_power_for_tracker_2 = None
		self.PV_power_for_tracker_3 = None

	def Measurements(self):
		client = ModbusClient(self.ip, port=self.port, unit_id=self.unitid, auto_open=True, auto_close=True)

		# Register addresses
		# com.victronenergy.multi 
		# Start 4500 - End 4601

		address = 4500
		count = 102
		result = client.read_holding_registers(address, count, unit=self.unitid)

		decoder = BinaryPayloadDecoder.fromRegisters(result.registers, byteorder=Endian.Big, wordorder=Endian.Big)

		self.Input_voltage_phase_1 = decoder.decode_16bit_uint()
		self.Input_voltage_phase_2 = decoder.decode_16bit_uint()
		self.Input_voltage_phase_3 = decoder.decode_16bit_uint()
		self.Input_current_phase_1 = decoder.decode_16bit_uint()
		self.Input_current_phase_2 = decoder.decode_16bit_uint()
		self.Input_current_phase_3 = decoder.decode_16bit_uint()
		self.Input_power_phase_1 = decoder.decode_16bit_int()
		self.Input_power_phase_2 = decoder.decode_16bit_int()
		self.Input_power_phase_3 = decoder.decode_16bit_int()
		self.Input_frequency = decoder.decode_16bit_uint()
		self.Output_voltage_phase_1 = decoder.decode_16bit_uint()
		self.Output_voltage_phase_2 = decoder.decode_16bit_uint()
		self.Output_voltage_phase_3 = decoder.decode_16bit_uint()
		self.Output_current_phase_1 = decoder.decode_16bit_uint()
		self.Output_current_phase_2 = decoder.decode_16bit_uint()
		self.Output_current_phase_3 = decoder.decode_16bit_uint()
		self.Output_power_phase_1 = decoder.decode_16bit_int()
		self.Output_power_phase_2 = decoder.decode_16bit_int()
		self.Output_power_phase_3 = decoder.decode_16bit_int()
		self.Output_frequency = decoder.decode_16bit_uint()
		self.AC_input_1_source_type = decoder.decode_16bit_uint()
		self.AC_input_2_source_type = decoder.decode_16bit_uint()
		self.Ac_input_1_current_limit = decoder.decode_16bit_uint()
		self.Ac_input_2_current_limit = decoder.decode_16bit_uint()
		self.Phase_count = decoder.decode_16bit_uint()
		self.Active_AC_input = decoder.decode_16bit_uint()
		self.Battery_voltage = decoder.decode_16bit_uint()
		self.Battery_current = decoder.decode_16bit_int()
		self.Battery_temperature = decoder.decode_16bit_int()
		self.Battery_State_of_Charge = decoder.decode_16bit_uint()
		self.Inverter_state = decoder.decode_16bit_uint()
		self.Switch_position = decoder.decode_16bit_uint()
		self.Temperature_alarm = decoder.decode_16bit_uint()
		self.High_voltage_alarm = decoder.decode_16bit_uint()
		self.High_AC_Out_voltage_alarm = decoder.decode_16bit_uint()
		self.Low_battery_temperature_alarm = decoder.decode_16bit_uint()
		self.Low_voltage_alarm = decoder.decode_16bit_uint()
		self.Low_AC_Out_voltage_alarm = decoder.decode_16bit_uint()
		self.Overload_alarm = decoder.decode_16bit_uint()
		self.High_DC_ripple_alarm = decoder.decode_16bit_uint()
		self.PV_power = decoder.decode_16bit_uint()
		self.User_yield = decoder.decode_16bit_uint()
		self.Relay_on_the_Multi_RS = decoder.decode_16bit_uint()
		self.MPP_operation_mode = decoder.decode_16bit_uint()
		self.PV_voltage = decoder.decode_16bit_uint()
		self.Error_code = decoder.decode_16bit_uint()
		self.Energy_from_AC_in_1_to_AC_out = decoder.decode_32bit_uint()
		self.Energy_from_AC_in_1_to_battery = decoder.decode_32bit_uint()
		self.Energy_from_AC_in_2_to_AC_out = decoder.decode_32bit_uint()
		self.Energy_from_AC_in_2_to_battery = decoder.decode_32bit_uint()
		self.Energy_from_AC_out_to_AC_in_1 = decoder.decode_32bit_uint()
		self.Energy_from_AC_out_to_AC_in_2 = decoder.decode_32bit_uint()
		self.Energy_from_battery_to_AC_in_1 = decoder.decode_32bit_uint()
		self.Energy_from_battery_to_AC_in_2 = decoder.decode_32bit_uint()
		self.Energy_from_battery_to_AC_out = decoder.decode_32bit_uint()
		self.Energy_from_AC_out_to_battery = decoder.decode_32bit_uint()
		self.Energy_from_solar_to_AC_in_1 = decoder.decode_32bit_uint()
		self.Energy_from_solar_to_AC_in_2 = decoder.decode_32bit_uint()
		self.Energy_from_solar_to_AC_out = decoder.decode_32bit_uint()
		self.Energy_from_solar_to_battery = decoder.decode_32bit_uint()
		self.Yield_today = decoder.decode_16bit_uint()
		self.Maximum_charge_power_today = decoder.decode_16bit_uint()
		self.Yield_yesterday = decoder.decode_16bit_uint()
		self.Maximum_charge_power_yesterday = decoder.decode_16bit_uint()
		self.Yield_today_for_tracker_0 = decoder.decode_16bit_uint()
		self.Yield_today_for_tracker_1 = decoder.decode_16bit_uint()
		self.Yield_today_for_tracker_2 = decoder.decode_16bit_uint()
		self.Yield_today_for_tracker_3 = decoder.decode_16bit_uint()
		self.Yield_yesterday_for_tracker_0 = decoder.decode_16bit_uint()
		self.Yield_yesterday_for_tracker_1 = decoder.decode_16bit_uint()
		self.Yield_yesterday_for_tracker_2 = decoder.decode_16bit_uint()
		self.Yield_yesterday_for_tracker_3 = decoder.decode_16bit_uint()
		self.Maximum_charge_power_today_for_tracker_0 = decoder.decode_16bit_uint()
		self.Maximum_charge_power_today_for_tracker_1 = decoder.decode_16bit_uint()
		self.Maximum_charge_power_today_for_tracker_2 = decoder.decode_16bit_uint()
		self.Maximum_charge_power_today_for_tracker_3 = decoder.decode_16bit_uint()
		self.Maximum_charge_power_yesterday_tracker_0 = decoder.decode_16bit_uint()
		self.Maximum_charge_power_yesterday_tracker_1 = decoder.decode_16bit_uint()
		self.Maximum_charge_power_yesterday_tracker_2 = decoder.decode_16bit_uint()
		self.Maximum_charge_power_yesterday_tracker_3 = decoder.decode_16bit_uint()
		self.PV_voltage_for_tracker_0 = decoder.decode_16bit_uint()
		self.PV_voltage_for_tracker_1 = decoder.decode_16bit_uint()
		self.PV_voltage_for_tracker_2 = decoder.decode_16bit_uint()
		self.PV_voltage_for_tracker_3 = decoder.decode_16bit_uint()
		self.PV_power_for_tracker_0 = decoder.decode_16bit_uint()
		self.PV_power_for_tracker_1 = decoder.decode_16bit_uint()
		self.PV_power_for_tracker_2 = decoder.decode_16bit_uint()
		self.PV_power_for_tracker_3 = decoder.decode_16bit_uint()

class VEBus(Victron):
	def __init__(self, id, ip, port, unitid, mqttid):
		super().__init__(id)
		self.ip = ip
		self.port = port
		self.unitid = unitid
		self.mqttid = mqttid

		self.Input_voltage_phase_1 = None
		self.Input_voltage_phase_2 = None
		self.Input_voltage_phase_3 = None
		self.Input_current_phase_1 = None
		self.Input_current_phase_2 = None
		self.Input_current_phase_3 = None
		self.Input_frequency_1 = None
		self.Input_frequency_2 = None
		self.Input_frequency_3 = None
		self.Input_power_1 = None
		self.Input_power_2 = None
		self.Input_power_3 = None
		self.Output_voltage_phase_1 = None
		self.Output_voltage_phase_2 = None
		self.Output_voltage_phase_3 = None
		self.Output_current_phase_1 = None
		self.Output_current_phase_2 = None
		self.Output_current_phase_3 = None
		self.Output_frequency = None
		self.Active_input_current_limit = None
		self.Output_power_1 = None
		self.Output_power_2 = None
		self.Output_power_3 = None
		self.Battery_voltage = None
		self.Battery_current = None
		self.Phase_count = None
		self.Active_input = None
		self.VEBus_state_of_charge = None
		self.VEBus_state = None
		self.VEBus_Error = None
		self.Switch_Position = None
		self.Temperature_alarm = None
		self.Low_battery_alarm = None
		self.Overload_alarm = None
		self.ESS_power_setpoint_phase_1 = None
		self.ESS_disable_charge_flag_phase = None
		self.ESS_disable_feedback_flag_phase = None
		self.ESS_power_setpoint_phase_2 = None
		self.ESS_power_setpoint_phase_3 = None
		self.Temperatur_sensor_alarm = None
		self.Voltage_sensor_alarm = None
		self.Temperature_alarm_L1 = None
		self.Low_battery_alarm_L1 = None
		self.Overload_alarm_L1 = None
		self.Ripple_alarm_L1 = None
		self.Temperature_alarm_L2 = None
		self.Low_battery_alarm_L2 = None
		self.Overload_alarm_L2 = None
		self.Ripple_alarm_L2 = None
		self.Temperature_alarm_L3 = None
		self.Low_battery_alarm_L3 = None
		self.Overload_alarm_L3 = None
		self.Ripple_alarm_L3 = None
		self.Disable_PV_inverter = None
		self.VEBus_BMS_allows_battery_to_be_charged = None
		self.VEBus_BMS_allows_battery_to_be_discharged = None
		self.VEBus_BMS_is_expected = None
		self.VEBus_BMS_error = None
		self.Battery_temperature = None
		self.VEBus_Reset = None
		self.Phase_rotation_warning = None
		self.Grid_lost_alarm = None
		self.Feed_DC_overvoltage_into_grid = None
		self.Maximum_overvoltage_feed_in_power_L1 = None
		self.Maximum_overvoltage_feed_in_power_L2 = None
		self.Maximum_overvoltage_feed_in_power_L3 = None
		self.AC_input_1_ignored = None
		self.AC_input_2_ignored = None
		self.AcPowerSetpoint_acts_as_feed_in_limit = None
		self.Solar_offset_voltage = None

	def Set(self, command, value):

		client = ModbusClient(self.ip, port=self.port, unit_id=self.unitid, auto_open=True, auto_close=True)
		builder = BinaryPayloadBuilder(byteorder=Endian.Big, wordorder=Endian.Big)
		
		#self.ESS_power_setpoint_phase_1  = decoder.decode_16bit_int()
		#self.ESS_disable_charge_flag_phase  = decoder.decode_16bit_uint()
		#self.ESS_disable_feedback_flag_phase  = decoder.decode_16bit_uint()
		#self.ESS_power_setpoint_phase_2  = decoder.decode_16bit_int()
		#self.ESS_power_setpoint_phase_3  = decoder.decode_16bit_int()

		if(command == "ESS_power_setpoint_phase_1"):
			builder.add_16bit_int(value)
			registers = builder.to_registers()
			client.write_registers(37, registers, unit=self.unitid)

		if(command == "ESS_power_setpoint_phase_2"):
			builder.add_16bit_int(value)
			registers = builder.to_registers()
			client.write_registers(40, registers, unit=self.unitid)

		if(command == "ESS_power_setpoint_phase_3"):
			builder.add_16bit_int(value)
			registers = builder.to_registers()
			client.write_registers(41, registers, unit=self.unitid)

		if(command == "ESS_disable_charge_flag_phase"):
			builder.add_16bit_int(value)
			registers = builder.to_registers()
			client.write_registers(38, registers, unit=self.unitid)

		if(command == "ESS_disable_feedback_flag_phase"):
			builder.add_16bit_int(value)
			registers = builder.to_registers()
			client.write_registers(39, registers, unit=self.unit_id)


	def Measurements(self):
		client = ModbusClient(self.ip, port=self.port, unit_id=self.unitid, auto_open=True, auto_close=True)
	
		# Register addresses
		# com.victronenergy.vebus 
		# Start 3 - End 72

		address = 3
		count = 66
		result = client.read_holding_registers(address, count, unit=self.unitid)
		decoder = BinaryPayloadDecoder.fromRegisters(result.registers, byteorder=Endian.Big, wordorder=Endian.Big)

		self.Input_voltage_phase_1  = decoder.decode_16bit_uint()
		self.Input_voltage_phase_2  = decoder.decode_16bit_uint()
		self.Input_voltage_phase_3  = decoder.decode_16bit_uint()
		self.Input_current_phase_1  = decoder.decode_16bit_int()
		self.Input_current_phase_2  = decoder.decode_16bit_int()
		self.Input_current_phase_3  = decoder.decode_16bit_int()
		self.Input_frequency_1  = decoder.decode_16bit_int()
		self.Input_frequency_2  = decoder.decode_16bit_int()
		self.Input_frequency_3  = decoder.decode_16bit_int()
		self.Input_power_1  = decoder.decode_16bit_int()
		self.Input_power_2  = decoder.decode_16bit_int()
		self.Input_power_3  = decoder.decode_16bit_int()
		self.Output_voltage_phase_1  = decoder.decode_16bit_uint()
		self.Output_voltage_phase_2  = decoder.decode_16bit_uint()
		self.Output_voltage_phase_3  = decoder.decode_16bit_uint()
		self.Output_current_phase_1  = decoder.decode_16bit_int()
		self.Output_current_phase_2  = decoder.decode_16bit_int()
		self.Output_current_phase_3  = decoder.decode_16bit_int()
		self.Output_frequency  = decoder.decode_16bit_int()
		self.Active_input_current_limit  = decoder.decode_16bit_int()
		self.Output_power_1  = decoder.decode_16bit_int()
		self.Output_power_2  = decoder.decode_16bit_int()
		self.Output_power_3  = decoder.decode_16bit_int()
		self.Battery_voltage  = decoder.decode_16bit_uint()
		self.Battery_current  = decoder.decode_16bit_int()
		self.Phase_count  = decoder.decode_16bit_uint()
		self.Active_input  = decoder.decode_16bit_uint()
		self.VEBus_state_of_charge  = decoder.decode_16bit_uint()
		self.VEBus_state  = decoder.decode_16bit_uint()
		self.VEBus_Error  = decoder.decode_16bit_uint()
		self.Switch_Position  = decoder.decode_16bit_uint()
		self.Temperature_alarm  = decoder.decode_16bit_uint()
		self.Low_battery_alarm  = decoder.decode_16bit_uint()
		self.Overload_alarm  = decoder.decode_16bit_uint()
		self.ESS_power_setpoint_phase_1  = decoder.decode_16bit_int()
		self.ESS_disable_charge_flag_phase  = decoder.decode_16bit_uint()
		self.ESS_disable_feedback_flag_phase  = decoder.decode_16bit_uint()
		self.ESS_power_setpoint_phase_2  = decoder.decode_16bit_int()
		self.ESS_power_setpoint_phase_3  = decoder.decode_16bit_int()
		self.Temperatur_sensor_alarm  = decoder.decode_16bit_uint()
		self.Voltage_sensor_alarm  = decoder.decode_16bit_uint()
		self.Temperature_alarm_L1  = decoder.decode_16bit_uint()
		self.Low_battery_alarm_L1  = decoder.decode_16bit_uint()
		self.Overload_alarm_L1  = decoder.decode_16bit_uint()
		self.Ripple_alarm_L1  = decoder.decode_16bit_uint()
		self.Temperature_alarm_L2  = decoder.decode_16bit_uint()
		self.Low_battery_alarm_L2  = decoder.decode_16bit_uint()
		self.Overload_alarm_L2  = decoder.decode_16bit_uint()
		self.Ripple_alarm_L2  = decoder.decode_16bit_uint()
		self.Temperature_alarm_L3  = decoder.decode_16bit_uint()
		self.Low_battery_alarm_L3  = decoder.decode_16bit_uint()
		self.Overload_alarm_L3  = decoder.decode_16bit_uint()
		self.Ripple_alarm_L3  = decoder.decode_16bit_uint()
		self.Disable_PV_inverter  = decoder.decode_16bit_uint()
		self.VEBus_BMS_allows_battery_to_be_charged  = decoder.decode_16bit_uint()
		self.VEBus_BMS_allows_battery_to_be_discharged  = decoder.decode_16bit_uint()
		self.VEBus_BMS_is_expected  = decoder.decode_16bit_uint()
		self.VEBus_BMS_error  = decoder.decode_16bit_uint()
		self.Battery_temperature  = decoder.decode_16bit_int()
		self.VEBus_Reset  = decoder.decode_16bit_uint()
		self.Phase_rotation_warning  = decoder.decode_16bit_uint()
		self.Grid_lost_alarm  = decoder.decode_16bit_uint()
		self.Feed_DC_overvoltage_into_grid  = decoder.decode_16bit_uint()
		self.Maximum_overvoltage_feed_in_power_L1  = decoder.decode_16bit_uint()
		self.Maximum_overvoltage_feed_in_power_L2  = decoder.decode_16bit_uint()
		self.Maximum_overvoltage_feed_in_power_L3  = decoder.decode_16bit_uint()
		#self.AC_input_1_ignored  = decoder.decode_16bit_uint()
		#self.AC_input_2_ignored  = decoder.decode_16bit_uint()
		#self.AcPowerSetpoint_acts_as_feed_in_limit  = decoder.decode_16bit_uint()
		#self.Solar_offset_voltage  = decoder.decode_16bit_uint()

class System(Victron):
	def __init__(self, id, ip, port, unitid, mqttid):
		super().__init__(id)
		self.ip = ip
		self.port = port
		self.unitid = unitid
		self.mqttid = mqttid

		self.Serial_System = None
		self.CCGX_Relay_1_state = None
		self.CCGX_Relay_2_state = None
		self.PV_AC_coupled_on_output_L1 = None
		self.PV_AC_coupled_on_output_L2 = None
		self.PV_AC_coupled_on_output_L3 = None
		self.PV_AC_coupled_on_input_L1 = None
		self.PV_AC_coupled_on_input_L2 = None
		self.PV_AC_coupled_on_input_L3 = None
		self.PV_AC_coupled_on_generator_L1 = None
		self.PV_AC_coupled_on_generator_L2 = None
		self.PV_AC_coupled_on_generator_L3 = None
		self.AC_Consumption_L1 = None
		self.AC_Consumption_L2 = None
		self.AC_Consumption_L3 = None
		self.Grid_L1 = None
		self.Grid_L2 = None
		self.Grid_L3 = None
		self.Genset_L1 = None
		self.Genset_L2 = None
		self.Genset_L3 = None
		self.Active_input_source = None
		self.Battery_Voltage_System = None
		self.Battery_Current_System = None
		self.Battery_Power_System = None
		self.Battery_State_of_Charge_System = None
		self.Battery_state_System = None
		self.Battery_Consumed_Amphours_System = None
		self.Battery_Time_to_Go_System = None
		self.PV_DC_coupled_power = None
		self.PV_DC_coupled_current = None
		self.Charger_power = None
		self.DC_System_Power = None
		self.VEBus_charge_current_System = None
		self.VEBus_charge_power_System = None

	def Measurements(self):
		client = ModbusClient(self.ip, port=self.port, unit_id=self.unitid, auto_open=True, auto_close=True)

		# Register addresses
		# com.victronenergy.system 
		# Start 800 - End 826

		address = 800
		count = 27
		result = client.read_holding_registers(address, count, unit=self.unitid)
		decoder = BinaryPayloadDecoder.fromRegisters(result.registers, byteorder=Endian.Big, wordorder=Endian.Big)

		self.Serial_System = decoder.decode_string(12)
		self.CCGX_Relay_1_state = decoder.decode_16bit_uint()
		self.CCGX_Relay_2_state = decoder.decode_16bit_uint()
		self.PV_AC_coupled_on_output_L1 = decoder.decode_16bit_uint()
		self.PV_AC_coupled_on_output_L2 = decoder.decode_16bit_uint()
		self.PV_AC_coupled_on_output_L3 = decoder.decode_16bit_uint()
		self.PV_AC_coupled_on_input_L1 = decoder.decode_16bit_uint()
		self.PV_AC_coupled_on_input_L2 = decoder.decode_16bit_uint()
		self.PV_AC_coupled_on_input_L3 = decoder.decode_16bit_uint()
		self.PV_AC_coupled_on_generator_L1 = decoder.decode_16bit_uint()
		self.PV_AC_coupled_on_generator_L2 = decoder.decode_16bit_uint()
		self.PV_AC_coupled_on_generator_L3 = decoder.decode_16bit_uint()
		self.AC_Consumption_L1 = decoder.decode_16bit_uint()
		self.AC_Consumption_L2 = decoder.decode_16bit_uint()
		self.AC_Consumption_L3 = decoder.decode_16bit_uint()
		self.Grid_L1 = decoder.decode_16bit_int()
		self.Grid_L2 = decoder.decode_16bit_int()
		self.Grid_L3 = decoder.decode_16bit_int()
		self.Genset_L1 = decoder.decode_16bit_int()
		self.Genset_L2 = decoder.decode_16bit_int()
		self.Genset_L3 = decoder.decode_16bit_int()
		self.Active_input_source = decoder.decode_16bit_uint()

		# Register addresses
		# com.victronenergy.system 
		# Start 840 - End 846

		address = 840
		count = 7
		result = client.read_holding_registers(address, count, unit=self.unitid)
		decoder = BinaryPayloadDecoder.fromRegisters(result.registers, byteorder=Endian.Big, wordorder=Endian.Big)

		self.Battery_Voltage_System = decoder.decode_16bit_uint()
		self.Battery_Current_System = decoder.decode_16bit_int()
		self.Battery_Power_System = decoder.decode_16bit_int()
		self.Battery_State_of_Charge_System = decoder.decode_16bit_uint()
		self.Battery_state_System = decoder.decode_16bit_uint()
		self.Battery_Consumed_Amphours_System = decoder.decode_16bit_uint()
		self.Battery_Time_to_Go_System = decoder.decode_16bit_uint()

		# Register addresses
		# com.victronenergy.system 
		# Start 850 - End 851

		address = 850
		count = 2
		result = client.read_holding_registers(address, count, unit=self.unitid)
		decoder = BinaryPayloadDecoder.fromRegisters(result.registers, byteorder=Endian.Big, wordorder=Endian.Big)

		self.PV_DC_coupled_power = decoder.decode_16bit_uint()
		self.PV_DC_coupled_current = decoder.decode_16bit_int()

		# Register addresses
		# com.victronenergy.system 
		# Start 855 - End 855

		address = 855
		count = 1
		result = client.read_holding_registers(address, count, unit=self.unitid)
		decoder = BinaryPayloadDecoder.fromRegisters(result.registers, byteorder=Endian.Big, wordorder=Endian.Big)

		self.Charger_power = decoder.decode_16bit_uint()

		# Register addresses
		# com.victronenergy.system 
		# Start 860 - End 860

		address = 860
		count = 1
		result = client.read_holding_registers(address, count, unit=self.unitid)
		decoder = BinaryPayloadDecoder.fromRegisters(result.registers, byteorder=Endian.Big, wordorder=Endian.Big)

		self.DC_System_Power = decoder.decode_16bit_int()

		# Register addresses
		# com.victronenergy.system 
		# Start 865 - End 866

		address = 865
		count = 2
		result = client.read_holding_registers(address, count, unit=self.unitid)
		decoder = BinaryPayloadDecoder.fromRegisters(result.registers, byteorder=Endian.Big, wordorder=Endian.Big)

		self.VEBus_charge_current_System = decoder.decode_16bit_int()
		self.VEBus_charge_power_System = decoder.decode_16bit_int()

class Grid(Victron):
	def __init__(self, id, ip, port, unitid, mqttid):
		super().__init__(id)
		self.ip = ip
		self.port = port
		self.unitid = unitid
		self.mqttid = mqttid

		self.Grid_L1_Power = None
		self.Grid_L2_Power = None
		self.Grid_L3_Power = None
		self.Grid_L1_Energy_from_net = None
		self.Grid_L2_Energy_from_net = None
		self.Grid_L3_Energy_from_net = None
		self.Grid_L1_Energy_to_net = None
		self.Grid_L2_Energy_to_net = None
		self.Grid_L3_Energy_to_net = None
		self.Serial = None
		self.Grid_L1_Voltage = None
		self.Grid_L1_Current = None
		self.Grid_L2_Voltage = None
		self.Grid_L2_Current = None
		self.Grid_L3_Voltage = None
		self.Grid_L3_Current = None
		self.Grid_L1_Energy_from_net = None
		self.Grid_L2_Energy_from_net = None
		self.Grid_L3_Energy_from_net = None
		self.Grid_L1_Energy_to_net = None
		self.Grid_L2_Energy_to_net = None
		self.Grid_L3_Energy_to_net = None
		self.Total_Energy_from_net = None
		self.Total_Energy_to_net = None

	def Measurements(self):
		client = ModbusClient(self.ip, port=self.port, unit_id=self.unitid, auto_open=True, auto_close=True)

		# Register addresses
		# com.victronenergy.battery
		# Start 2600 - End 2636

		address = 2600
		count = 34
		result = client.read_holding_registers(address, count, unit=self.unitid)
		decoder = BinaryPayloadDecoder.fromRegisters(result.registers, byteorder=Endian.Big, wordorder=Endian.Big)

		self.Grid_L1_Power = decoder.decode_16bit_int()
		self.Grid_L2_Power = decoder.decode_16bit_int()
		self.Grid_L3_Power = decoder.decode_16bit_int()
		self.Grid_L1_Energy_from_net = decoder.decode_16bit_uint()/100
		self.Grid_L2_Energy_from_net = decoder.decode_16bit_uint()/100
		self.Grid_L3_Energy_from_net = decoder.decode_16bit_uint()/100
		self.Grid_L1_Energy_to_net = decoder.decode_16bit_uint()/100
		self.Grid_L2_Energy_to_net = decoder.decode_16bit_uint()/100
		self.Grid_L3_Energy_to_net = decoder.decode_16bit_uint()/100
		self.Serial = decoder.decode_string(14)
		self.Grid_L1_Voltage = decoder.decode_16bit_uint()/10
		self.Grid_L1_Current = decoder.decode_16bit_int()/10
		self.Grid_L2_Voltage = decoder.decode_16bit_uint()/10
		self.Grid_L2_Current = decoder.decode_16bit_int()/10
		self.Grid_L3_Voltage = decoder.decode_16bit_uint()/10
		self.Grid_L3_Current = decoder.decode_16bit_int()/10
		self.Grid_L1_Energy_from_net = decoder.decode_32bit_uint()/100
		self.Grid_L2_Energy_from_net = decoder.decode_32bit_uint()/100
		self.Grid_L3_Energy_from_net = decoder.decode_32bit_uint()/100
		self.Grid_L1_Energy_to_net = decoder.decode_32bit_uint()/100
		self.Grid_L2_Energy_to_net = decoder.decode_32bit_uint()/100
		self.Grid_L3_Energy_to_net = decoder.decode_32bit_uint()/100
		#self.Total_Energy_from_net = decoder.decode_32bit_uint()
		#self.Total_Energy_to_net = decoder.decode_32bit_uint()

class PVInverter(Victron):
	def __init__(self, id, ip, port, unitid, mqttid):
		super().__init__(id)
		self.ip = ip
		self.port = port
		self.unitid = unitid
		self.mqttid = mqttid

		self.Position = None
		self.L1_Voltage = None
		self.L1_Current = None
		self.L1_Power = None
		self.L1_Energy = None
		self.L2_Voltage = None
		self.L2_Current = None
		self.L2_Power = None
		self.L2_Energy = None
		self.L3_Voltage = None
		self.L3_Current = None
		self.L3_Power = None
		self.L3_Energy = None
		self.Serial = None
		self.L1_Energy = None
		self.L2_Energy = None
		self.L3_Energy = None
		self.Total_Power = None
		self.Maximum_Power_Capacity = None
		self.Power_limit = None


	def Measurements(self):
		client = ModbusClient(self.ip, port=self.port, unit_id=self.unitid, auto_open=True, auto_close=True)

		# Register addresses
		# com.victronenergy.battery
		# Start 1026 - End 1050

		address = 1026
		count = 26
		result = client.read_holding_registers(address, count, unit=self.unitid)
		decoder = BinaryPayloadDecoder.fromRegisters(result.registers, byteorder=Endian.Big, wordorder=Endian.Big)

		self.Position = decoder.decode_16bit_uint()
		self.L1_Voltage = decoder.decode_16bit_uint()/10
		self.L1_Current = decoder.decode_16bit_int()/10
		self.L1_Power = decoder.decode_16bit_uint()
		self.L1_Energy = decoder.decode_16bit_uint()/100
		self.L2_Voltage = decoder.decode_16bit_uint()/10
		self.L2_Current = decoder.decode_16bit_int()/10
		self.L2_Power = decoder.decode_16bit_uint()
		self.L2_Energy = decoder.decode_16bit_uint()/100
		self.L3_Voltage = decoder.decode_16bit_uint()/10
		self.L3_Current = decoder.decode_16bit_int()/10
		self.L3_Power = decoder.decode_16bit_uint()
		self.L3_Energy = decoder.decode_16bit_uint()/100
		self.Serial = decoder.decode_string(14)
		self.L1_Energy = decoder.decode_32bit_uint()/100
		self.L2_Energy = decoder.decode_32bit_uint()/100
		self.L3_Energy = decoder.decode_32bit_uint()/100
		#self.Total_Power = decoder.decode_32bit_int()
		#self.Maximum_Power_Capacity = decoder.decode_32bit_uint()
		#self.Power_limit = decoder.decode_32bit_uint()


MultiPlussssBat = Battery("XYZ", "192.168.1.102", 502, 247, 10)
MultiPlussssBat.Measurements()

#print(MultiPlussssBat.__dict__)

MultiPlussssVEBus = VEBus("XYZ", "192.168.1.102", 502, 246, 10)
MultiPlussssVEBus.Measurements()
MultiPlussssVEBus.Set("ESS_power_setpoint_phase_1", 1000)

#print(MultiPlussssVEBus.__dict__)

MultiPlussssSystem = System("XYZ", "192.168.1.102", 502, 100, 10)
MultiPlussssSystem.Measurements()

#print(MultiPlussssSystem.__dict__)

MultiPlussssGrid = Grid("XYZ", "192.168.1.102", 502, 30, 10)
MultiPlussssGrid.Measurements()

#print(MultiPlussssGrid.__dict__)

MultiPlussssPVInverter = PVInverter("XYZ", "192.168.1.102", 502, 32, 10)
MultiPlussssPVInverter.Measurements()

print(MultiPlussssPVInverter.__dict__)
