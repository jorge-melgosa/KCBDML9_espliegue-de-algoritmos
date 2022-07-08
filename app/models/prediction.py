from pydantic import BaseModel

from app.core.enums import PersonTroll


class TrollPredictionResult(BaseModel):
    label: PersonTroll
    score: float
    elapsed_time: float
