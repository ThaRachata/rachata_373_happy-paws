from app.database.connection import get_connection
def main():
    print("🐾 Happy Paws Pet Hotel")
    connection = get_connection()
    print("Connected to MariaDB successfully!")
    connection.close()


if __name__ == "__main__":
    main()
