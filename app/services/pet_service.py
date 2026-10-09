from app.repositories.pet_repository import (
    add_pet,
    delete_pet,
    get_all_pets,
    get_pet_by_id,
    update_pet,
)


def list_pets():
    return get_all_pets()


def get_pet(pet_id):
    return get_pet_by_id(pet_id)


def create_pet(name, pet_type, breed, age, owner_name):
    return add_pet(name, pet_type, breed, age, owner_name)


def update_pet_service(
    pet_id,
    name,
    pet_type,
    breed,
    age,
    owner_name,
):
    return update_pet(pet_id, name, pet_type, breed, age, owner_name)


def delete_pet_service(pet_id):
    return delete_pet(pet_id)
