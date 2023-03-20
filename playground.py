from machine import Pin, ADC
import time


# Initialiseren van sensoren, knoppen en belangrijke parameters
f_samping = 1
thermometer_internal = ADC(4)
button = Pin(16, Pin.IN)

# Aanmaken van lege lijsten voor opslag
tijdstippen = []
temperatuur_metingen = [] 

# Knop, om meting te starten (indrukken en loslaten)
print('Druk button in om experiment te starten')
while button.value() == False:
    # zolang knop niet ingedrukt is
    # Doe niets
    pass
while button.value() == True:
    # zolang knop niet losgelaten is
    # Doe niets
    pass

# Acquisitie start
# Tijdstip 0 bepalen
tijdstip0 = time.ticks_ms()

while True:
    # Tijdstip meting bepalen
    huidige_tijd = (time.ticks_ms() - tijdstip0) / 1000

    # Meting uitvoeren
    adc_voltage = thermometer_internal.read_u16() * (3.3 / (65535))
    temperature_celcius = 27 - (adc_voltage - 0.706) / 0.001721

    # Meting laten zien, en eventueel opslaan
    # Dit kan ook op een lcd of oled
    print(huidige_tijd, adc_voltage, temperature_celcius)

    # Opslaan in lijst (tijdelijke opslag)
    tijdstippen.append(huidige_tijd)
    temperatuur_metingen.append(temperature_celcius)
    
    # Als knop ingedrukt, stop meting
    if button.value() == True:
        print('button ingedrukt')
        break

    # Wacht tot volgende meting
    time.sleep(1/f_samping)

print('data acquisitie afgelopen')

# Opslaan in bestand
with open("data_01.txt", 'w') as out:
    for tijdstip, meting in zip(tijdstippen, temperatuur_metingen):
        out.write(f'{tijdstip}, {meting}\n')

# Eind