from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String

# connect to SQLite in memory
engine = create_engine('sqlite:///meubanco.db', echo=True)

print("Connection to SQLite in memory created successfully")


Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

# create all tables
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

with session as session:
    novo_usuario = User(name="Ana", email="ana.doe@example.com")
    session.add(novo_usuario)
    print("User created successfully")
    session.commit()

usuario = session.query(User).filter(User.name == "Ana").first()
print(f"User: {usuario.name} - {usuario.email}")