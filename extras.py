from machine import Pin, ADC


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