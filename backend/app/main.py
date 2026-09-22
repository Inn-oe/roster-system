from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List

from . import crud
from .models import models
from .schemas import schemas
from .database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Roster System API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Roster System API"}

@app.post("/workers/", response_model=schemas.Worker)
def create_worker(worker: schemas.WorkerCreate, db: Session = Depends(get_db)):
    return crud.create_worker(db=db, worker=worker)

@app.get("/workers/", response_model=List[schemas.Worker])
def read_workers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_workers(db, skip=skip, limit=limit)

@app.get("/workers/{worker_id}", response_model=schemas.Worker)
def read_worker(worker_id: int, db: Session = Depends(get_db)):
    db_worker = crud.get_worker(db, worker_id=worker_id)
    if db_worker is None:
        raise HTTPException(status_code=404, detail="Worker not found")
    return db_worker

@app.post("/sites/", response_model=schemas.Site)
def create_site(site: schemas.SiteCreate, db: Session = Depends(get_db)):
    return crud.create_site(db=db, site=site)

@app.get("/sites/", response_model=List[schemas.Site])
def read_sites(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_sites(db, skip=skip, limit=limit)

@app.post("/assignments/", response_model=schemas.RosterAssignment)
def create_assignment(assignment: schemas.RosterAssignmentCreate, db: Session = Depends(get_db)):
    return crud.create_roster_assignment(db=db, assignment=assignment)

@app.get("/assignments/", response_model=List[schemas.RosterAssignment])
def read_assignments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_roster_assignments(db, skip=skip, limit=limit)
