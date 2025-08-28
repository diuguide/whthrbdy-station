import network
import utime

def connect_to_wifi(ssid, password, max_attempts=10, delay=2):
    """
    Attempts to connect to a WiFi network with the given SSID and password.
    
    :param ssid: The WiFi network SSID
    :param password: The WiFi network password
    :param max_attempts: The maximum number of connection attempts
    :param delay: The delay in seconds between connection attempts
    
    :return: True if connected, False if unable to connect after max_attempts
    """
    # Reset WiFi settings
    wlan = network.WLAN(network.STA_IF)
    wlan.active(False)  # Disable WiFi to reset state
    utime.sleep(5)       # Short delay to allow reset
    wlan.active(True)   # Re-enable WiFi
    utime.sleep(5)

# Ensure we start fresh
    wlan.disconnect()
    utime.sleep(2)
    print(f"Attempting to connect to WiFi network: {ssid}")

    wlan.connect(ssid, password)

    attempt = 0
    while attempt < max_attempts:
        print("Attempt:", attempt)
        status = wlan.status()
        print("Status:", status)
        
        # Check if the device is connected
        if status == 2:  # 2 is 'connected'
            print("Successfully connected to WiFi!")
            return True
        
        # Handle different statuses
        if status == 0:  # 0 is 'disconnected'
            print("Not connected, retrying...")
        elif status == 1:  # 1 is 'connecting'
            print("Connecting to WiFi...")
        elif status == 5:  # 5 is 'authentication failed'
            print("Authentication failed (wrong SSID or password).")
            break
        elif status == 6:  # 6 is 'no suitable AP found'
            print("No suitable access point found (wrong SSID or AP hidden).")
            break
        
        attempt += 1
        utime.sleep(delay)  # Wait before retrying

    print("Unable to connect to WiFi after multiple attempts.")
    return False
