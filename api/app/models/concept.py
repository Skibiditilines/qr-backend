from sqlalchemy import Column, Integer, String, DateTime, Boolean, Text, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.core.database import Base

class Concept(Base):
    __tablename__ = "concepts"

    concept_id = Column(Integer, primary_key=True, index=True)
    concept_date = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    content = Column(Text, nullable=False)
    concept_color = Column(String(30), nullable=True) # Hex format
    concept_image = Column(String(255), nullable=False) # Cloudinary URL
    is_active = Column(Boolean, default=True, nullable=False)
    concept_slug = Column(String(36), unique=True, index=True, nullable=False) # QR Identifier
    concept_note = Column(Text, nullable=True)
    
    account_id = Column(Integer, ForeignKey("accounts.account_id"), nullable=False)

    # Relationships
    account = relationship("Account", back_populates="concepts")
