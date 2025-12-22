from sqlalchemy import Column, Integer, String, DateTime, Boolean, Text
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.core.database import Base

class Account(Base):
    __tablename__ = "accounts"

    account_id = Column(Integer, primary_key=True, index=True)
    acc_creation_date = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    account_password = Column(Text, nullable=False)
    account_type = Column(String(30), nullable=False) # e.g., 'Administrador'
    is_active = Column(Boolean, default=True, nullable=False)
    account_email = Column(String(50), unique=True, index=True, nullable=True)

    # Relationships
    concepts = relationship("Concept", back_populates="account")
