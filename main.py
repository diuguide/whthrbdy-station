import machine
import utime
import bluetooth
import network


# Define GPIO pins for button and LED
button_pin = machine.Pin(18, machine.Pin.IN, machine.Pin.PULL_UP)
led_pin = machine.Pin(16, machine.Pin.OUT)
print('Listening for button....')
click_count = 0
last_click_time = utime.ticks_ms()

# Main loop to listen for button press
while True:
    if button_pin.value() == 0:
        # Button pressed (pull-up resistor configuration)
        led_pin.on()  # Turn on the LED
        utime.sleep(0.1)  # Wait for debounce time or perform other actions
        while button_pin.value() == 0:
            pass  # Wait for button release
        led_pin.off()  # Turn off the LED once the button is released
        
        click_count += 1
        current_time = utime.ticks_ms()
        if utime.ticks_diff(current_time, last_click_time) > 1000:
            # If more than 1 second has elapsed since last click, reset count
            click_count = 1
        last_click_time = current_time
        
        print("Button clicked. Count:", click_count)
        
        if click_count == 5:
            print("Button clicked 5 times! Creating Access Point...")
            import new_1.py
            
    utime.sleep(0.1)  # Small delay to debounce and reduce CPU usage
