from datetime import datetime
import uuid
from typing import Optional

from sqlmodel import Field, SQLModel


class WorkflowBase(SQLModel):
    name: str
    description: Optional[str]
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: Optional[datetime]


class Workflow(WorkflowBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    owner_id: uuid.UUID = Field(
        foreign_key="user.id", nullable=False, ondelete="CASCADE"
    )


class WorkflowPublic(WorkflowBase):
    id: uuid.UUID
    owner_id: uuid.UUID


class WorkflowsPublic(SQLModel):
    flows: list[Workflow]
