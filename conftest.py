import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, clear_mappers

from orm import mapper_registry, start_mappers


@pytest.fixture
def in_memory_db():
    engine = create_engine("postgresql+psycopg://test:test@localhost:5432/test")
    mapper_registry.metadata.drop_all(engine)
    mapper_registry.metadata.create_all(engine)
    return engine


@pytest.fixture
def session(in_memory_db):
    start_mappers()
    yield sessionmaker(bind=in_memory_db)()
    clear_mappers()
