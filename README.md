# Project Description

### GSHEET | REST API - Python, Google Sheet
- Python - 3.12.7
- Postgres Database - pgAdmin - 17.0

### Usage (Command and Steps)

1. setup initial project structure
- This command will display a list of all installed Python packages along with their versions
```bash
pip freeze
```
- Run the following command to generate a list of installed packages
```bash
pip freeze > requirements.txt
```
- To install Python libraries listed in a requirements.txt file, you can use the following command
```bash
pip install -r requirements.txt
```
- uninstall all the packages
```bash
pip uninstall -r requirements.txt
```

2. create virtual envioronment (Do this if require)
```bash
python -m venv myenv
```
3. activate the envioronment (Do this if require)
```bash
.\myenv\Scripts\activate
```

4. create database in pgAdmin (check .env file for database name and other config)
```bash
pgAdmin 4 -> PostgresSQL 17 -> Databases -> Create -> Database -> (Your Database Name)
```

5. Initialize Alembic (Make Sure Alembic is on your requirements.txt file)
```bash
alembic init alembic
```
6. Make Changes in env.py file (import settings and schemas Base)
```bash
from app.database import settings
from app.user.user_schema import Base as UserBase
```

7. Setup SqlAlchemy URL in env.py
```bash
config = context.config
config.set_main_option(
    "sqlalchemy.url",
    f"postgresql+psycopg2://{settings.database_username}:{settings.database_password}@{
        settings.database_hostname}:{settings.database_port}/{settings.database_name}",
)
```

8. Target Metadata (Add All Schemas Base in Metadata if you have multiple Schemas File)
```bash
target_metadata = [UserBase.metadata]
```

9. Run Below Command (This will init the Version Folder in alembic directory)
```bash
alembic upgrade head
```
10. Generate Init Report (Check versions folder in alembic directory)
```bash
alembic revision --autogenerate -m "initial-report"
```

11. Now, Run this Command (This is made all the require changes in database)
```bash
alembic upgrade head
```

12. for starting api
```bash
uvicorn app.main:app --reload
```





<!-- {
  "type": "service_account",
  "project_id": "maalde-24342",
  "private_key_id": "db29ea43acbda05b8e88798a7da6c47b4c5f933c",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDBqNaUSYBz+fIH\nuM14qsng8VODSi8ypoIx54oLVO1bwRH2n2kGgIiK4DZQ15tMDQUpUIP9A4Lo1dxT\nVZO4svlM9LY3yshFmfyTDdjEfrFavrFUsf8Jt6Eg8l7cCz7TtaJpTmR4nNlwDiYI\nbKdEPrDM3s7vkxo8CH9j7z09WychAgEkyn2o1dgF4/cBe6D2kF/HJKRdzkBtYIgw\n2wP3XTMyTJ+/D8j/1OAJE2UxIejsb+TWi8EXyZga1sIctP00m44tDSL8FFOrOMcT\nsobH5JXvGzTfRo9Vy7NvrACUh5DdHi/FZkotcvUlOAJX4b5lgWasgetezMB4XYyz\n0OJglJX5AgMBAAECggEABRlKaQYUZTlP94cUldg9T3hbIApMetNqeyDjABBg3XkU\nXX9t9vdcYPetRmye0J5JJADUMM2uXS4ASotmw8amjLGmuIpUwoxe24pSSj4hskdy\nCM5U7i8RBXqMJ9P99/oAyDABsjFDAlHFC5S8xK233vUA0sr3Nlxs6jcq0Bo9yf8l\nLZ5MohFbGPnrs+6beY0hBd1hMW1kerWuaRXPVSk8Ltxze069ybRINrCfPDZQyzIA\nUByn7V0apstkHRtwnNUMTGkN00frZ66KjI1TZThAbqJUb6bN5c8NPStGAczQsPoF\nIREHmbUHT6vFc8TZYq7XwbHshxxNcIHWEHTcxmk4ZwKBgQD/eCu+Za6sPSSGMghh\nJRST7vFU/7GWobZsddRL4iJf9pxDi2AY8Uf5XPSfdPAqCWEjISgvPSDWbmMYukfB\n/Ok1xpA2x+wTHkW7x9YLlahPhFuBPlm2gc4NB3FM14jZFYLhSqdtqe7LIBBx6aWr\nS8xfEwDpxmOwbmf+uvBUDHTPQwKBgQDCD83Qo/Yc0w5q0tEHRL7+XOznPt5wXS8/\nAFpoapo+2yi0qXQIHkQ3Kc7Q4w7OKqxRFZtZLTfso8QpfvqDpwTjyxmPDm/PQrOo\nsgcRtBrx8PpxYyur232bGUxnw/6SIF7VQRVCCG4hKba3S7ITBX713VpmGySo9HrZ\nExL3CDy8EwKBgQD8vaHhUu21XyQ0U2lw2mN6W4mMgw7prIEy2nu2uzkw4WUFee0P\noB2JuYoV+3Xi0La2L4Z2/a3wFvOZMint5E3AsvpYCAApheiNd43ulhgW2yZAPjQ5\nWEBHKZbQ4+dyhVKfmuD7oIQrl0RNvk71oh7F7KIZpflYQlJGdCFxtYUWywKBgAqu\nQf6kt4v4lceNWNHUl8p6JNPJYwa+KjaGd3NdwqWI/GGNHgTAXbLHi0l15b+1G4zO\n6qDq2zQcA1ThVzpdu+gpqnt0KPU4T5kOS1NPHViJkc8hzSqFRxF9P/ZKFD3IqE+G\naHwc6KrMl/DYqrFfURCJIUuTXN4rroM6CIYuHuGfAoGAP5acuaseucjdiOo+aPa9\nOr4N00/mh4IQwAFv570Be1kGkxcIxJrIVS6ofjUjXrWYt9QFNcdXeW8Sr5IS8MZe\n7FMcPL9HRyygPJ2PyWsn+rcutoFQXVnql9qfxKjVAFmYe1VVk/jCtqPt8cErKQUQ\nK3zebi/0qWJjvP+lKXCsYh4=\n-----END PRIVATE KEY-----\n",
  "client_email": "maalde-2024@maalde-24342.iam.gserviceaccount.com",
  "client_id": "113306446335154628972",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/maalde-2024%40maalde-24342.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
} -->
