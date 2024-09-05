# IoT and Blockchain

## Project Overview
This project simulates an IoT system where sensor data (such as temperature, humidity, etc.) is generated and securely stored on the Ethereum blockchain using smart contracts. The application leverages Python for IoT data simulation and blockchain interaction (via Web3.py) to ensure data integrity and tamper-proof storage.

**The project consists of three main components:**

1. IoT Data Simulation: Simulates the generation of IoT data like temperature and humidity.
2. Smart Contract: A Solidity-based contract for storing IoT data on the blockchain, ensuring data immutability, and automating alerts.
3. Blockchain Integration: Uses Web3.py to deploy the smart contract and interact with the Ethereum blockchain (e.g., store, retrieve IoT data).

## How to run locally

### Prerequisites
- Python (version 3.x) installed.
- Ganache: For setting up a local Ethereum blockchain environment.
- Solidity Compiler: Install via Python's solcx library or a standalone version.

### Installation
1. Clone this repository.
2. Install dependencies.
```
pip install -r requirements.txt
```
3. Run Ganache to create a local blockchain network on `http://127.0.0.1:7545`

### Running the Application
1. Deploy the smart contract onto the local blockchain network.
```
python blockchain/deploy_contract.py
```
2. Run the IoT Data Simulation and Store Data on Blockchain
```
python app.py
```
3. You can now view blocks mined in the Ganache interface. You can also retrieve stored data using the helper functions in `interact_with_contract.py`
