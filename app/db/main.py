from sqlmodel import Session, SQLModel, create_engine
import os

engine = create_engine(os.getenv("DATABASE_URL", "sqlite:///./dev.db"))
SQLModel.metadata.create_all(engine)

with Session(engine) as session:
    print("Database connected and tables created.")