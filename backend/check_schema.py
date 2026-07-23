from sqlalchemy import create_engine, text
from app.core.config import settings

engine = create_engine(settings.DATABASE_URL)

with engine.connect() as conn:
    print("Database:", conn.execute(text("SELECT current_database()")).scalar())

    print("\nProject Files Columns:")
    rows = conn.execute(text("""
        SELECT column_name
        FROM information_schema.columns
        WHERE table_name='project_files'
        ORDER BY ordinal_position
    """))

    for row in rows:
        print("-", row[0])