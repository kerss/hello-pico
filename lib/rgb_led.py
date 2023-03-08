from machine import Pin, PWM


class RGBLed:
    def __init__(self, r_pin, g_pin, b_pin) -> None:
        self.r = PWM(Pin(r_pin))
        self.g = PWM(Pin(g_pin))
        self.b = PWM(Pin(b_pin))

        for pwm_pin in [self.r, self.g, self.b]:
            pwm_pin.freq(10000)
            pwm_pin.duty_u16(int(.5 * 65535))

    def set(self, red = 0., green = 0., blue = 0.):
        red = min(max(0, int(red * 65535)), 65535)
        green = min(max(0, int(green * 65535)), 65535)
        blue = min(max(0, int(blue * 65535)), 65535)

        self.r.duty_u16(red)
        self.g.duty_u16(green)
        self.b.duty_u16(blue)

