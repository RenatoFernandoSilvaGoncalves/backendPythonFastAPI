from DB.ServicoDAO import ServicoDAO
class Servico(object):
    
    def __init__(self, id, nome, preco):
        self.__id = id
        self.__nome = nome
        self.__preco = preco
        
    def __str__(self):
        return f"id: {self.__id}, nome: {self.__nome}, preco: {self.__preco}"
    def __repr__(self):
        return self.__str__()
    
    def to_dict(self):
        return {
            'id': self.__id,
            'nome': self.__nome,
            'preco': self.__preco
        }
    
       
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id):
        self.__id = id
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self, preco):
        self.__preco = preco
        
    def gravar(self):
        servDao = ServicoDAO()
        servDao.gravar(self)
        
    def alterar(self):
        servDao = ServicoDAO()
        servDao.alterar(self)
        
    def excluir(self):
        servDao = ServicoDAO()
        servDao.excluir(self)
        
    def consultar(self):
        servDao = ServicoDAO()
        return servDao.consultar()
        
    