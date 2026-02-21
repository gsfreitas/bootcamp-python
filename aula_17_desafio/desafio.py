from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.exc import SQLAlchemyError

Base = declarative_base()

class Fornecedor(Base):
    __tablename__ = 'fornecedores'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    telefone = Column(String(20))
    email = Column(String(50))
    endereco = Column(String(50))

class Produto(Base):
    __tablename__ = 'produtos'
    idd = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=True)
    descricao = Column(String(200))
    preco = Column(Integer)
    fornecedor_id = Column(Integer, ForeignKey('fornecedores.id'))

    # cria a relacao entre Produto e Fornecedor
    fornecedor = relationship("Fornecedor")

engine = create_engine('sqlite:///desafio.db', echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# insert nos fornecedores
try:
    with Session() as session:
        fornecedores = [
            Fornecedor(nome="Fornecedor A", telefone="12345678", email="ccontato@a.com", endereco="Rua A"),
            Fornecedor(nome="Fornecedor B", telefone="12345678", email="ccontato@b.com", endereco="Rua B"),
            Fornecedor(nome="Fornecedor C", telefone="12345678", email="ccontato@c.com", endereco="Rua C"),
            Fornecedor(nome="Fornecedor D", telefone="12345678", email="ccontato@d.com", endereco="Rua D"),
            Fornecedor(nome="Fornecedor E", telefone="12345678", email="ccontato@e.com", endereco="Rua E")
        ]
        session.add_all(fornecedores)
        session.commit()
except SQLAlchemyError as e:
    print(f"Erro ao inserir forneceddores: {e}")

# insert dos produtos
try:
    with Session() as session:
        produtos = [
        Produto(nome="Produto 1", descricao="Descrição do Produto 1", preco=100, fornecedor_id=1),
        Produto(nome="Produto 2", descricao="Descrição do Produto 2", preco=200, fornecedor_id=2),
        Produto(nome="Produto 3", descricao="Descrição do Produto 3", preco=300, fornecedor_id=3),
        Produto(nome="Produto 4", descricao="Descrição do Produto 4", preco=400, fornecedor_id=4),
        Produto(nome="Produto 5", descricao="Descrição do Produto 5", preco=500, fornecedor_id=5)
        ]
        session.add_all(produtos)
        session.commit()
except SQLAlchemyError as e:
    print(f"Erro ao inserir produtos: {e}")