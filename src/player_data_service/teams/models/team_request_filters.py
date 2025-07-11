from typing import Optional

from pydantic import BaseModel


class TeamRequestFilters(BaseModel):
    team_id: Optional[str] = None
    name: Optional[str] = None
    limit: Optional[int] = None
    offset: Optional[int] = None
    order: Optional[str] = None
    order_by: Optional[str] = None


class CompositeTeamRequestFilters(BaseModel):
    team_id: Optional[str] = None
    player_id: Optional[str] = None
    year: Optional[int] = None
    name: Optional[str] = None
