from gpiozero import LED, Button, PWMLED
from time import sleep


def led_on_off(pin_no, sleep_time):
    """
    Function to turn a pin on and off at a given interval
    :param pin_no: int, pin number
    :param sleep_time: int, time to sleep in seconds
    :return:
    """

    led = LED(pin_no)
    while True:
        led.on()
        sleep(sleep_time)
        led.off()
        sleep(sleep_time)

def led_w_button(bpin, lpin):
    """
    Function to activate LED with a push button
    wiring: button must be wired with pull-up resistor
    :param bpin: pin for button
    :param lpin: pin for led
    :return:
    """
    button = Button(bpin)
    led = LED(lpin)

    while True:
        if button.is_pressed and not led.is_active:
            led.on()
            print('turn on')
            print('button ', button.is_pressed)
            print('led ', led.is_active)
            sleep(0.3)
        elif button.is_pressed and led.is_active:
            led.off()
            print('turn off')
            print('button ', button.is_pressed)
            print('led ', led.is_active)
            sleep(0.3)

def pwm_led(pin, brightness):
    led = PWMLED(pin)
    led.value = brightness



if __name__ == '__main__':
    #led_on_off(16, 1)
    #led_w_button(17,16)
    while True:
        pwm_led(16, 1)
        sleep(5)