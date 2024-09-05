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
2. Run the IoT Data Simulation and Store That Data on the Blockchain
```
python app.py
```
3. You can now view blocks mined in the Ganache interface. You can also retrieve stored data using the helper functions in `interact_with_contract.py`
```
python3 blockchain/interact_with_contract.py
```

## Evaluation of the Project

### Performance and Functionality

1. **Transaction Speed**

   - Observation: In the current setup, using Ganache for local blockchain simulation, transaction times are relatively fast (sub-second) because there is no real network latency or complex consensus mechanisms like in public blockchains (e.g., Ethereum Mainnet).

   - Real-World Scenario: On public blockchains, transaction times would be much slower due to network congestion, proof-of-work (PoW) mining, or gas price variations. For example, Ethereum Mainnet typically takes around 15-30 seconds for transaction confirmation, depending on the gas price and network conditions.

   - **Challenges for Transaction Speed:**

     - Latency: Delays in IoT data being stored on the blockchain, especially in high-frequency data generation scenarios.
     - Scalability: With multiple IoT devices, thousands of transactions would need to be recorded, which can increase costs and delays.

2. **Security**

   - Immutability: Once data is stored on the blockchain, it cannot be altered, which ensures the integrity of IoT data. This prevents tampering or unauthorized access, providing trust in a distributed system.
   - Smart Contract Security: Smart contracts were kept simple to avoid security vulnerabilities like reentrancy attacks. However, this requires further audits and checks to prevent issues like integer overflows or unauthorized access.
   - Private vs Public Blockchain: On a public chain, security relies on the blockchain network itself, but a private chain (e.g., Hyperledger) could offer more control over permissions and access.

### Challenges Faced During Implementation

1. Exploring methods for running an ethereum network locally for development of this app (to avoid using a deployed testnet, which might have required further complications with MetaMask integration, etc.)
2. I modularized the interaction functions (store_iot_data_on_blockchain, get_iot_data) and used Web3.py’s transact and call methods to handle transactions properly. Gas limits and accounts were explicitly specified to avoid errors during contract execution.

### Potential Improvements

1. Implementing a proper interface for listening to events emitted by the deployed smart contract via some sort of dashboard.
2. General-purpose blockchains like Ethereum are not optimized for IoT data, which can lead to performance bottlenecks. Therefore one could consider using blockchains such as IOTA, which are designed to handle high-frequency IoT data efficiently. IOTA, for example, is based on a DAG (Directed Acyclic Graph) rather than a traditional blockchain, allowing for feeless microtransactions and faster data processing.
