import boa
from dotenv import load_dotenv
from boa.network import NetworkEnv, EthereumRPC
from eth_account import Account
import os

load_dotenv()


MY_CONTRACT = "0x5FbDB2315678afecb367f032d93F642f64180aa3"

def main():
    rpc = os.getenv("RPC_URL") 
    env = NetworkEnv(rpc=EthereumRPC(rpc))
    boa.set_env(env)


    anvil_key = os.getenv("ANVL_KEY")
    myaccount = Account.from_key(anvil_key)
    boa.env.add_account(myaccount, force_eoa=True)


    fav_partial = boa.load("fav.vy")
    #fav_contract = fav_partial.at(MY_CONTRACT)

    '''fav_number = fav_contract.retrieve()
    print(f"Current fav number: {fav_number}")


    fav_contract.store(14)
    retrieve_dear = fav_contract.retrieve()
    print(f"Dear contract: {retrieve_dear}")'''

    fav_partial.add_person("Valencia", 25)
    personal_data = fav_partial.list_of_people(0)
    print(f"Personal data: {personal_data}")
    print(f"Stored value: {store_value}")




if __name__ == "__main__":
    main()