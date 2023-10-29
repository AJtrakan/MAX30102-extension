import time
from machine import I2C
from hrcalc import calc_hr_and_spo2
from MAX30105 import ParticleSensor


MAX30105 = ParticleSensor(HEX_ADDRESS=0x57)
part_id = MAX30105.i2c_read_register(0xFF)
rev_id = MAX30105.i2c_read_register(0xFE)
print("MAX30105: part ID", hex(ord(part_id)), "revision:", ord(rev_id))
print("Setting up sensor now:", '\n')
MAX30105.setup_sensor()
MAX30105.setPulseAmplitudeRed(0x0A)
MAX30105.setPulseAmplitudeGreen(0x00)

def detect_SPO2():
    red_list = []
    ir_list = []

    while True:
        red_reading, ir_reading = MAX30105.read_sensor_multiLED(1)
        #print("sensor_data", red_reading, ir_reading)
        #time.sleep_ms(10)

        if red_reading >= 20000 and ir_reading >= 80000 :
            red_list.append(red_reading)
            ir_list.append(ir_reading)
            red_list = red_list[-100:]
            ir_list = ir_list[-100:]
            if len(red_list) == 100 and len(ir_list) == 100:
                hr, hrb, sp, spb = calc_hr_and_spo2(red_list, ir_list)
                if hrb is True and spb is True:
                    if sp != -999:
                        SPO2 = int(sp)
                if sp == -999:
                    #print("่just a moment")
                    return ("่just a moment")
                else:
                    #print("PSO2", sp)
                    return (sp)
        else :
            #print("No finger?")
            return ("No finger?")