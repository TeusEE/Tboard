from sqlmodel import Field, Session, SQLModel, create_engine, select
from datetime import datetime
from sqlalchemy import UniqueConstraint

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user_id: str = Field(index=True)
    user_pw: int | None = Field(default=None)
    regist_date: datetime = Field(default_factory=datetime.utcnow)
    
    __table_args__ = (UniqueConstraint('user_id', name='uq_user_id'),)



sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)