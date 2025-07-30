from typing import Annotated
from pydantic import Field
from meu_projeto_fastapi.contrib.schemas import BaseSchema

class CentroTreinamento(BaseSchema):
    nome: Annotated[str, Field(decription='Nome do Centro de Treinamento', examples='CT King', max_legth=20)]
 