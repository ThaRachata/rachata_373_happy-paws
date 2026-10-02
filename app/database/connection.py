import os

import mariadb
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    required_variables = ("DB_HOST", "DB_USER", "DB_PASSWORD", "DB_NAME")
    missing_variables = [
        name for name in required_variables if not os.getenv(name)
    ]
    if missing_variables:
        names = ", ".join(missing_variables)
        raise RuntimeError(f"Missing database environment variables: {names}")

    try:
        port = int(os.getenv("DB_PORT", "3306"))
    except ValueError as error:
        raise ValueError("DB_PORT must be a number") from error

    return mariadb.connect(
        host=os.getenv("DB_HOST"),
        port=port,
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
    )
