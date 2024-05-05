import model

from abc import ABC, abstractmethod

from sqlalchemy.orm import Session


class AbstractRepository(ABC):
    @abstractmethod
    def add(self, batch: model.Batch):
        raise NotImplementedError
    
    @abstractmethod
    def get(self, reference: str) -> model.Batch:
        raise NotImplementedError

class SQLAlchemyRepository(AbstractRepository):
    def __init__(self, session: Session):
        ...

    def add(self, batch: model.Batch):
        ...
    
    def get(self, reference: str):
        ...