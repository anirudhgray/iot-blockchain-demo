import json
from web3 import Web3
from solcx import compile_standard, install_solc

# Connect to local Ethereum blockchain (e.g., Ganache)
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))

def compile_contract():
    install_solc("0.8.0")
    
    with open("contracts/IoTData.sol", "r") as file:
        contract_code = file.read()

    compiled_sol = compile_standard(
        {
            "language": "Solidity",
            "sources": {"IoTData.sol": {"content": contract_code}},
            "settings": {"outputSelection": {"*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}}},
        },
        solc_version="0.8.0",
    )

    return compiled_sol

def deploy_contract():
    compiled_sol = compile_contract()
    abi = compiled_sol['contracts']['IoTData.sol']['IoTData']['abi']
    bytecode = compiled_sol['contracts']['IoTData.sol']['IoTData']['evm']['bytecode']['object']

    # Create contract object
    contract = w3.eth.contract(abi=abi, bytecode=bytecode)

    # Deploy the contract
    tx_hash = contract.constructor().transact({
        'from': w3.eth.accounts[0],
        'gas': 5000000
    })
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    
    # Get contract address
    contract_address = tx_receipt.contractAddress
    return contract_address, abi

if __name__ == "__main__":
    # Deploy the contract and store contract address and ABI
    contract_address, abi = deploy_contract()

    # Save contract address and ABI to a JSON file
    contract_data = {
        "address": contract_address,
        "abi": abi
    }

    with open("blockchain/contract_info.json", "w") as f:
        json.dump(contract_data, f)

    print(f"Contract deployed at address: {contract_address}")
    print(f"Contract ABI saved to contract_info.json")
