import random
import time

# Simulate IoT data collection
def generate_iot_data():
    while True:
        # Simulate temperature and humidity data
        temperature = random.uniform(15.0, 30.0)
        humidity = random.uniform(30.0, 70.0)
        
        # Simulate 5 device IDs and timestamps
        device_id = random.randint(1, 5)
        timestamp = int(time.time())
        
        # IoT data packet
        iot_data = {
            'device_id': device_id,
            'temperature': temperature,
            'humidity': humidity,
            'timestamp': timestamp
        }
        yield iot_data
        time.sleep(2)  # Generate data every 2 seconds
