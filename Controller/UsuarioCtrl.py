from fastapi import APIRouter
from fastapi.responses import JSONResponse
from Model.Servico import Servico
from schemas.Servico import SchemaServico
import json
router = APIRouter()

@router.get("/servico") 
async def consultar(): 
    servico = Servico(0,"",0)
    lista= [serv.to_dict() for serv in servico.consultar()]
    
    return JSONResponse({
                'status': True, 'servicos': lista
           })

@router.post("/servico")
async def gravar(servico: SchemaServico):
    serv = Servico(servico.id, servico.nome, servico.preco)
    serv.gravar()
    return {
                'status': True, 
                'mensagem': 'Servico gravado com sucesso',
                'id': serv.id
           }
    
@router.put("/servico")
async def alterar(servico: SchemaServico):
    serv = Servico(servico.id, servico.nome, servico.preco)
    serv.alterar()
    return {
                'status': True, 
                'mensagem': 'Servico alterado com sucesso'
    }

@router.delete("/servico")
async def excluir(servico: SchemaServico):
    serv = Servico(servico.id, servico.nome, servico.preco)
    serv.excluir()
    return {
                'status': True, 
                'mensagem': 'Servico excluido com sucesso'
    }

