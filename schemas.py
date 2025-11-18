from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class Lead(BaseModel):
    name: str = Field(..., description="Nome do potencial cliente")
    email: EmailStr = Field(..., description="Email para contacto")
    message: str = Field(..., description="Mensagem enviada pelo formulário")
    source: Optional[str] = Field('site', description="Origem do contacto")

# Coleção será criada como "lead"
