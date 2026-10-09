## Happy Paws

This folder is already the `happy-paws` project. Do not run `cd happy-paws`
again while the terminal is at `C:\rachata_373_happy-paws`.

Create the virtual environment once:

```powershell
uv venv
```

If `.venv` already exists, use:

```powershell
uv venv --allow-existing
```

Activate it in PowerShell and run the project:

```powershell
.venv\Scripts\Activate.ps1
uv run python main.py
```

Start MariaDB before running the application:

```powershell
docker compose up -d
```

The expected output is:

```text
Happy Paws Pet Hotel
Connected to MariaDB successfully!
```

Create the application tables once the database is running:

```powershell
uv run python -m app.database.create_tables
```
