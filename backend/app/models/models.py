from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey, JSON, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..database import Base

class Worker(Base):
    __tablename__ = "workers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Site(Base):
    __tablename__ = "sites"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    requires_specialist = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class AvailabilityRule(Base):
    __tablename__ = "availability_rules"
    id = Column(Integer, primary_key=True, index=True)
    worker_id = Column(Integer, ForeignKey("workers.id"))
    rule_type = Column(String) # e.g., 'FIXED_DAYS', 'EXCLUDE_DAYS', 'MAX_DAYS_PER_WEEK'
    rule_value = Column(JSON) # e.g., ["Tuesday", "Thursday", "Saturday"]
    
    worker = relationship("Worker")

class RosterWeek(Base):
    __tablename__ = "roster_weeks"
    id = Column(Integer, primary_key=True, index=True)
    start_date = Column(Date, unique=True, index=True)
    end_date = Column(Date)
    is_partial = Column(Boolean, default=False)

class RosterAssignment(Base):
    __tablename__ = "roster_assignments"
    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, index=True)
    worker_id = Column(Integer, ForeignKey("workers.id"))
    site_id = Column(Integer, ForeignKey("sites.id"))
    
    worker = relationship("Worker")
    site = relationship("Site")

class WorkerDayOff(Base):
    __tablename__ = "worker_days_off"
    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, index=True)
    worker_id = Column(Integer, ForeignKey("workers.id"))
    
    worker = relationship("Worker")
