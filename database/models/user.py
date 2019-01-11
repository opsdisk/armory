from .. import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class User(BaseModel):
    __tablename__ = "user"
    __repr_attrs__ = ["email"]
    id = Column(Integer, primary_key=True)
    email = Column(String(128), unique=True)
    first_name = Column(String(128), unique=False)
    last_name = Column(String(128), unique=False)
    user_name = Column(String(128), unique=False)
    domain_id = Column(Integer, ForeignKey("basedomain.id"))
    creds = relationship("Cred", backref="user")
    job_title = Column(String(128), unique=False)
    location = Column(String(128), unique=False)
