import dht
import machine
import time
import urequests
import network

# Function to read data from DHT22 sensor
def read_dht22(pin):
    d = dht.DHT22(machine.Pin(pin))  # Create DHT22 object
    d.measure()  # Perform measurement
    temperature_celsius = d.temperature()  # Read temperature in Celsius
    humidity = d.humidity()  # Read humidity
    # Convert temperature to Fahrenheit
    temperature_fahrenheit = (temperature_celsius * 9/5) + 32
    return temperature_fahrenheit, humidity

# Main function
def main():
    # Define DHT22 pin
    dht_pin = 15  # Replace with the GPIO pin connected to the DHT22 sensor

    sample_ip = ""
    port = "8080"
    station_id=001

    # Base URL for the GET request
    base_url = "http://" + sample_ip + ":" + port + "/inbound/"
    wlan = network.WLAN(network.STA_IF)
    #wlan.active(True)
    
    print("wlan status in temp.py:", wlan.status())

    while True:
        try:
            # Read data from DHT22 sensor
            temperature, humidity = read_dht22(dht_pin)
            print("Temperature:", temperature, "F")
            print("Humidity:", humidity, "%")

            # Construct URL with temperature and humidity as data points
            url = base_url + str(temperature) + "-" + str(humidity) + "-" + str(station_id) 
            print("URL:", url)

            # Send GET request
            response = urequests.get(url)
            print("Response:", response.text)
            response.close()

            time.sleep(0.5)  # Wait for 60 seconds before reading data again
        except Exception as e:
            print("Error:", e)
            time.sleep(10)  # Retry after 10 seconds if there's an error

# Run the main function
main()

