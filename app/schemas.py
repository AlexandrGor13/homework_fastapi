from pydantic import BaseModel, Field


class Text(BaseModel):
    """Schema for text"""
    text: str = Field(description="Text to translate", default="Текст, который требуется перевести")

class UserLogin(BaseModel):
    """Scheme for a credential"""
    username: str
    password: str

