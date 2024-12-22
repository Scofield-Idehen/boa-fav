import boa
from dotenv import load_dotenv
from boa.network import NetworkEnv, EthereumRPC
from eth_account import Account
import os

load_dotenv()


def main():
    rpc = os.getenv("RPC_URL") 
    env = NetworkEnv(rpc=EthereumRPC(rpc))
    boa.set_env(env)


    anvil_key = os.getenv("ANVL_KEY")
    myaccount = Account.from_key(anvil_key)
    boa.env.add_account(myaccount, force_eoa=True)

    fav_contract = boa.load("fav.vy")

    starting_fav_number = fav_contract.retrieve()
    print(f"Starting fav number: {starting_fav_number}")

    print("Storing 5 as the new fav number")
    fav_contract.store(5)

    end_fav_number = fav_contract.retrieve()
    print(f"Ending fav number: {end_fav_number}")


if __name__ == "__main__":
    main()
