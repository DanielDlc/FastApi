from typing import Optional

from pydantic import BaseModel as SCBasemodel



class CursoSchema(SCBasemodel):
    id: Optional[int]
    titulo: str
    aulas: int
    horas: int

    class Config:
        orm_mode=True