from sqlalchemy.orm import Session
from .models import models
from .schemas import schemas

def get_worker(db: Session, worker_id: int):
    return db.query(models.Worker).filter(models.Worker.id == worker_id).first()

def get_workers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Worker).offset(skip).limit(limit).all()

def create_worker(db: Session, worker: schemas.WorkerCreate):
    db_worker = models.Worker(**worker.model_dump())
    db.add(db_worker)
    db.commit()
    db.refresh(db_worker)
    return db_worker

def get_site(db: Session, site_id: int):
    return db.query(models.Site).filter(models.Site.id == site_id).first()

def get_sites(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Site).offset(skip).limit(limit).all()

def create_site(db: Session, site: schemas.SiteCreate):
    db_site = models.Site(**site.model_dump())
    db.add(db_site)
    db.commit()
    db.refresh(db_site)
    return db_site

def get_roster_assignments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.RosterAssignment).offset(skip).limit(limit).all()

def create_roster_assignment(db: Session, assignment: schemas.RosterAssignmentCreate):
    db_assignment = models.RosterAssignment(**assignment.model_dump())
    db.add(db_assignment)
    db.commit()
    db.refresh(db_assignment)
    return db_assignment
