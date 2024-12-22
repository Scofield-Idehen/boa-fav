import boa

def main():
    fav_contract = boa.load("fav.vy")
    first_retrieve= fav_contract.retrieve()
    print(f"First retrieve: {first_retrieve}")

    fav_contract.store(10)
    first_store_retrieve= fav_contract.retrieve()
    print(f"First retrieve: {first_store_retrieve}")



if __name__ == "__main__":
    main()