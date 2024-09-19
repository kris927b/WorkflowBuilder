import uuid
from typing import Any

from fastapi import APIRouter, HTTPException

from app.api.deps import CurrentUser, SessionDep
from app.models.workflows import WorkflowsPublic, Workflow
from sqlmodel import select

router = APIRouter()

#


@router.get("/", response_model=WorkflowsPublic)
def read_workflows(
    session: SessionDep, current_user: CurrentUser, skip: int = 0, limit: int = 100
) -> Any:
    """
    Retrieve workfows.
    """

    if current_user.is_superuser:
        statement = select(Workflow).offset(skip).limit(limit)
        flows = session.exec(statement).all()
    else:
        statement = (
            select(Workflow)
            .where(Workflow.owner_id == current_user.id)
            .offset(skip)
            .limit(limit)
        )
        flows = session.exec(statement).all()

    return WorkflowsPublic(flows=flows)
