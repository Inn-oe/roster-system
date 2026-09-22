from pydantic import BaseModel
from typing import List, Optional, Any, Dict
from datetime import date

class WorkerBase(BaseModel):
    name: str
    is_active: bool = True

class WorkerCreate(WorkerBase):
    pass

class Worker(WorkerBase):
    id: int
    class Config:
        from_attributes = True

class SiteBase(BaseModel):
    name: str
    requires_specialist: bool = False

class SiteCreate(SiteBase):
    pass

class Site(SiteBase):
    id: int
    class Config:
        from_attributes = True

class RosterAssignmentBase(BaseModel):
    date: date
    worker_id: int
    site_id: int

class RosterAssignmentCreate(RosterAssignmentBase):
    pass

class RosterAssignment(RosterAssignmentBase):
    id: int
    worker: Worker
    site: Site
    class Config:
        from_attributes = True

class RosterWeekBase(BaseModel):
    start_date: date
    end_date: date
    is_partial: bool = False

class RosterWeekCreate(RosterWeekBase):
    pass

class RosterWeek(RosterWeekBase):
    id: int
    class Config:
        from_attributes = True

class GenerateRequest(BaseModel):
    start_date: date
    weeks: int = 1
