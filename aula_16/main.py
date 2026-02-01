from typing import Optional
from sqlmodel import Field, Session, SQLModel, create_engine
from sqlalchemy import text

class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None

engine = create_engine("sqlite:///database.db", echo=True)

SQLModel.metadata.create_all(engine)

# hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson", age=45)
# hero_2 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)
# hero_3 = Hero(name="Spider-Girl", secret_name="Miral Lagoon", age=16)

#  with Session(engine) as session:
#     session.add(Hero(name="Deadpond", secret_name="Dive Wilson", age=45))
#     session.add(Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48))
#     session.add(Hero(name="Spider-Girl", secret_name="Miral Lagoon", age=16))
#     session.commit()

with Session(engine) as session:
    # select * from hero
    statement = text("SELECT * FROM hero")
    result = session.exec(statement)
    
    # fetch all
    heroes = result.fetchall()
    
    for hero in heroes:
        print(f"Hero: {hero.name} - {hero.secret_name} - {hero.age}")