from sqlmodel import SQLModel, create_engine
import os

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./dev.db")

engine = create_engine(DATABASE_URL, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
    print("📦 Database initialized.")

def test_connection():
    try:
        with engine.connect() as conn:
            print("✅ Database connected!")
    except Exception as e:
        print("❌ Database connection failed:", e)
