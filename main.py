from app.services.pet_service import list_pets


def main():
    print("Happy Paws Pet Hotel")
    print("--------------------")

    pets = list_pets()
    print("All pets:")
    for pet in pets:
        print(pet)


if __name__ == "__main__":
    main()
