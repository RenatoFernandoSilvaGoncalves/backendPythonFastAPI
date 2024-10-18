from pydantic import BaseModel

class SchemaServico(BaseModel):
    id: int
    nome: str
    preco: float
    