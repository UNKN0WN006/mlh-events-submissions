from pydantic import BaseModel

class Incident(BaseModel):
    type: str
    desc: str
    level: str
