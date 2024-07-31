import RPi.GPIO as GPIO
import time

# Set GPIO numbering mode
GPIO.setmode(GPIO.BCM)

# Define GPIO pins
LED_PINS = [17, 27]  # GPIO pins for 2 LEDs
BUTTON_PIN = 4  # GPIO pin for button

# Set up the pins
for led in LED_PINS:
    GPIO.setup(led, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def turn_off_all_leds():
    for led in LED_PINS:
        GPIO.output(led, GPIO.LOW)

print("Program is running. Press Ctrl+C to exit.")
print("Press and release the button to see LEDs change.")

try:
    while True:
        if GPIO.input(BUTTON_PIN) == GPIO.LOW:  # Button is pressed
            turn_off_all_leds()
            GPIO.output(LED_PINS[0], GPIO.HIGH)  # Turn on the first LED
            print("Button pressed - LED 1 on")
        else:  # Button is released
            turn_off_all_leds()
            GPIO.output(LED_PINS[1], GPIO.HIGH)  # Turn on the second LED
            print("Button released - LED 2 on")
        
        time.sleep(0.1)  # Wait a bit to reduce CPU usage

except KeyboardInterrupt:
    print("\nProgram ended.")

finally:
    turn_off_all_leds()
    GPIO.cleanup()  # Clean up GPIO on program exit
