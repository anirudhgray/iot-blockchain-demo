from iot_simulation.data_simulator import generate_iot_data
from blockchain.interact_with_contract import store_iot_data_on_blockchain

if __name__ == "__main__":
    # Generate IoT data
    data_generator = generate_iot_data()
    
    # Process and store IoT data on the blockchain
    for iot_data in data_generator:
        print(f"Generated IoT data: {iot_data}")
        receipt = store_iot_data_on_blockchain(iot_data)
        print(f"IoT data stored on blockchain. Transaction receipt: {receipt}")
