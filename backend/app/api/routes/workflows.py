import uuid
from typing import Any

from fastapi import APIRouter, HTTPException

from app.api.deps import CurrentUser, SessionDep
from app.models.workflows import WorkflowPublic

router = APIRouter()

#


@router.get("/", response_model=WorkflowPublic)
def read_workflows(
    session: SessionDep, current_user: CurrentUser, skip: int = 0, limit: int = 100
) -> Any:
    """
    Retrieve items.
    """
    return {"hello": "workflows"}
