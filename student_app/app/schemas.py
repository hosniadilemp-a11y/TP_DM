from typing import List, Optional
from pydantic import BaseModel, Field, ConfigDict

class TPInfo(BaseModel):
    id: int
    name: str

    model_config = ConfigDict(from_attributes=True)

class AttemptStartRequest(BaseModel):
    code: str = Field(..., description="Student code (e.g. IASD01, SIAD05, RSD02, CS10)")
    tp_id: int = Field(..., description="TP ID (1..6)")
    device_fingerprint: Optional[str] = None
    user_agent: Optional[str] = None

class AttemptStartResponse(BaseModel):
    attempt_id: int

class QuestionServeResponse(BaseModel):
    question_id: int
    text: str
    options: List[bool] = [True, False]
    position: int # 1..20
    total: int = 20

class AnswerSubmitRequest(BaseModel):
    question_id: int
    chosen: Optional[bool] = None

class AnswerSubmitResponse(BaseModel):
    received: bool = True

class FinishAttemptResponse(BaseModel):
    final_mark: float
    raw_score: float
    correct_count: int
    wrong_count: int
    skipped_count: int
    status: str
