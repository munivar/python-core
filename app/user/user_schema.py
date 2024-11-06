from app.database import Base
from sqlalchemy import Column, String
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from app.core.utils import generate_unique_id


class User(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True, nullable=False, default=generate_unique_id)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
