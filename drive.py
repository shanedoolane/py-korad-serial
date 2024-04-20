import time

from koradserial import KoradSerial

korad = KoradSerial(port='/dev/tty.usbmodem002738DB024C1')

## print info about psu
model_info = korad.model
print(model_info)

## pick the Setpoints
current_setpoint = .1
voltage_setpoint = 5

## Set the values over Serial
korad.channels[0].current = current_setpoint
korad.channels[0].voltage = voltage_setpoint

## Ensure protections are on
korad.over_current_protection.on()
korad.over_voltage_protection.on()

## Turn on the output
korad.output.on()
time.sleep(.5)  ## wait .5 s before reading the output

## Let the user know the output
print(f"Voltage limit set to: {voltage_setpoint}, actual: {korad.channels[0].output_voltage}")
print(f"Current limit set to: {current_setpoint}, actual: {korad.channels[0].output_current}")

## Close the serial connection
korad.close()
