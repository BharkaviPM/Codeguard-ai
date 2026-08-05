from sqlalchemy import create_engine, text
from app.core.config import DATABASE_URL

print("DATABASE_URL:", DATABASE_URL)

engine = create_engine(DATABASE_URL)

try:
    with engine.connect() as conn:
        result = conn.execute(text("SELECT version();"))
        print("✅ Connected Successfully!")
        print(result.fetchone()[0])
except Exception as e:
    print("❌ Connection Failed")
    print(e)