from datetime import datetime
import uuid
from sqlmodel import Field, SQLModel
from typing import Optional


class StepBase(SQLModel):
    name: str
    input: str
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: Optional[datetime]


class Step(StepBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    workflow_id: uuid.UUID = Field(
        foreign_key="workflow.id", nullable=False, ondelete="CASCADE"
    )


class FilterStep(Step):
    column: str
    condition: str
    value: str


class AggregateStep(Step):
    column: str
    aggregate_function: str
