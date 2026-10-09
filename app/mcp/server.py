import sys
from pathlib import Path

from fastmcp import FastMCP

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from app.services.pet_service import (
    create_pet,
    delete_pet_service,
    get_pet as get_pet_service,
    list_pets,
    update_pet_service,
)


mcp = FastMCP("Happy Paws MCP")


@mcp.tool
def hello_happy_paws() -> str:
    """Return a health message for the Happy Paws MCP server."""
    return "Hello from Happy Paws MCP"


@mcp.tool
def get_all_pets():
    """Return all pets from the Happy Paws database."""
    return list_pets()


@mcp.tool
def get_pet(pet_id: int):
    """Return one pet by its database ID."""
    return get_pet_service(pet_id)


@mcp.tool
def add_pet(
    name: str,
    pet_type: str,
    breed: str,
    age: int,
    owner_name: str,
):
    """Add a pet and return its new database ID."""
    return create_pet(name, pet_type, breed, age, owner_name)


@mcp.tool
def update_pet(
    pet_id: int,
    name: str,
    pet_type: str,
    breed: str,
    age: int,
    owner_name: str,
):
    """Update a pet and return the affected row count."""
    return update_pet_service(
        pet_id,
        name,
        pet_type,
        breed,
        age,
        owner_name,
    )


@mcp.tool
def delete_pet(pet_id: int):
    """Delete a pet and return the affected row count."""
    return delete_pet_service(pet_id)


if __name__ == "__main__":
    mcp.run()
