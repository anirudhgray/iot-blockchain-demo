import json
from web3 import Web3

# Web3 connection setup
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))

# Load contract address and ABI from the JSON file
with open("blockchain/contract_info.json", "r") as f:
    contract_info = json.load(f)

contract_address = contract_info["address"]
abi = contract_info["abi"]

# Get the contract instance
contract = w3.eth.contract(address=contract_address, abi=abi)

# Function to store IoT data on the blockchain
def store_iot_data_on_blockchain(iot_data):
    tx_hash = contract.functions.storeData(
        iot_data['device_id'],
        int(iot_data['temperature']),
        int(iot_data['humidity']),
        # iot_data['timestamp']
    ).transact({
        'from': w3.eth.accounts[0],
        'gas': 3000000
    })
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    return receipt

# Function to get stored IoT data from the blockchain
def get_iot_data(index):
    return contract.functions.getData(index).call()

# if as main, get iot data
if __name__ == "__main__":
    # Get stored IoT data
    data_count = contract.functions.getDataCount().call()
    for i in range(data_count-1):
        iot_data = get_iot_data(i)
        print(f"Stored IoT data at index {i}: {iot_data}")
