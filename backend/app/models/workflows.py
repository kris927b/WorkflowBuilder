import uuid
from typing import Optional, Dict, Any

from sqlmodel import Field, Relationship, SQLModel
from sqlalchemy import JSON


from app.models.users import User


class WorkflowBase(SQLModel):
    title: str = Field(min_length=1, max_length=255)
    workflow: Optional[Dict[str, Any]] = Field(
        sa_column=Field(JSON), default={"input": "input.csv", "output": "output.csv"}
    )


class Workflow(WorkflowBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    title: str = Field(max_length=255)
    owner_id: uuid.UUID = Field(
        foreign_key="user.id", nullable=False, ondelete="CASCADE"
    )
    owner: User | None = Relationship(back_populates="items")


# Properties to return via API, id is always required
class WorkflowPublic(WorkflowBase):
    id: uuid.UUID
    owner_id: uuid.UUID


class WorkflowsPublic(SQLModel):
    data: list[WorkflowPublic]
    count: int
