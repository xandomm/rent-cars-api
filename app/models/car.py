from sqlmodel import Field, SQLModel


class Car(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    make: str
    model: str
    year: int = Field(ge=1900, le=2100)
    fuel_type: str