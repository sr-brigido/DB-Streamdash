"""Módulo que contém o ORM do banco."""

# flake8: noqa

import os

from dotenv import load_dotenv
from sqlalchemy import Column, Float, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()  # Carrega as variáveis de ambiente do arquivo .env

db_user = os.getenv("POSTGRES_USER")
db_password = os.getenv("POSTGRES_PASSWORD")
db_name = os.getenv("POSTGRES_DB")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")

# Configurando a conexão com o banco de dados
# DATABASE_URL = "postgresql://meu_usuario:minha_senha@localhost:5432/meu_banco"

DATABASE_URL = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

# Criando a engine de conexão

engine = create_engine(DATABASE_URL)

# Criando a sessão

Session = sessionmaker(bind=engine)

Base = declarative_base()


# Definindo o modelo de dados
class Produto(Base):
    """Classe que define o schema da tabela de produtos na db."""

    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    descricao = Column(String)
    preco = Column(Float, nullable=False)


# Criando a tabela
Base.metadata.create_all(bind=engine)
