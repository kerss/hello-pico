from machine import UART, Pin
from api_gps import MicropyGPS


'''
Author: Stijn Kerst
Example usage:

    from machine import UART, Pin
    from lib.neo6m import NEO6M_GPS
    import time


    gps_uart = UART(1, baudrate=9600, tx=Pin(4), rx=Pin(5))
    gps = NEO6M_GPS(uart=gps_uart)

    while True:
        gps.update_gps()

        print(gps.latitude)
        print(gps.longitude)

        time.sleep(1)
'''


class NEO6M_GPS(MicropyGPS):
    def __init__(self, uart: UART) -> None:
        super().__init__()

        self.uart = uart
        
    def update_gps(self):
        while (line := self.uart.readline()) is not None:
            for byte in line:
                reply = self.update(chr(byte))

                # For debugging purposes
                # if reply is not None:
                    # print(f'Updated {reply}')



