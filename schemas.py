from pydantic import BaseModel, Field


class Text(BaseModel):
    text: str = Field(description="Text to translate", default="Текст, который требуется перевести")
