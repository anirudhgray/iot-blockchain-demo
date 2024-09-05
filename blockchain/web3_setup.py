from web3 import Web3

# Function to set up Web3 connection (to Ganache in this example)
def setup_web3():
    w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
    
    # Check connection
    if w3.isConnected():
        print("Connected to Ethereum node")
    else:
        raise ConnectionError("Failed to connect to Ethereum node")
    
    return w3
