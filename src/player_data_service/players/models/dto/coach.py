from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class Coach(BaseModel):
    coach_id: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    since: Optional[int] = None
    email: Optional[str] = None
    phone_number: Optional[str] = None
    imgurl: Optional[str] = None
    created: Optional[datetime] = None
    modified: Optional[datetime] = None
