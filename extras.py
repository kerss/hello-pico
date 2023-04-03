from machine import Pin, ADC
import os

try:
    from typing import List, Any
except ImportError:
    pass


class Button:
    def __init__(self, pin: Pin) -> None:
        self.pin = pin

    def wacht_op_knop_ingedrukt_en_los(self):
        while self.pin.value() == False:
            # zolang knop niet ingedrukt is
            # Doe niets
            
            pass
        while self.pin.value() == True:
            # zolang knop niet losgelaten is
            # Doe niets
            
            pass

    def is_ingedrukt(self):
        return self.pin.value()

    def wacht_op_knop_ingedrukt(self):
        while not self.is_ingedrukt():
            # zolang knop niet ingedrukt is
            # Doe niets
                        
            pass


class DataRecoder:
    def __init__(self, bestandsnaam: str, recorder_titels: List[str]) -> None:
        try: 
            os.listdir('recorded_data/')
        except OSError:
            os.mkdir('recorded_data')

        teller = 1
        for file in os.listdir('recorded_data/'):
            if bestandsnaam in file:
                teller += 1

        self.bestandsnaam = f'recorded_data/{bestandsnaam}_{teller:03}.txt'

        with open(self.bestandsnaam, 'w') as file:
            eerste_regel = str(recorder_titels)[1:-1] + '\n'
            file.write(eerste_regel)

    def record(self, recorder_values: List[Any]):
        with open(self.bestandsnaam, 'a') as file:
            file.write(str(recorder_values)[1:-1] + '\n')
