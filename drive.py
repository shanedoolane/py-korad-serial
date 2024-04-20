from koradserial import KoradSerial
import time
korad = KoradSerial(port='/dev/tty.usbmodem002738DB024C1')

model_info = korad.model
print(model_info)

current_setpoint = .1
voltage_setpoint = 5


korad.channels[0].current = current_setpoint
korad.channels[0].voltage = voltage_setpoint

korad.output.on()
time.sleep(1)
korad.over_current_protection.on()
korad.over_voltage_protection.on()
print(f"Voltage limit set to: {voltage_setpoint}, actual: {korad.channels[0].output_voltage}")
print(f"Current limit set to: {current_setpoint}, actual: {korad.channels[0].output_current}")

korad.close()