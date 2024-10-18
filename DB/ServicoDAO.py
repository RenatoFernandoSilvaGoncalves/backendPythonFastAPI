from DB.Conexao import Conexao
class ServicoDAO(object):
    
    def __init__(self):
        self.__conexao = Conexao.obterInstancia()
        
    def gravar(self, servico):
        from Model.Servico import Servico
        if isinstance(servico, Servico):
            conexao = self.__conexao.obterConexao()
            cursor = conexao.cursor()
            sql = "INSERT INTO servico (nome, preco) VALUES (%s, %s)"
            parametros = (servico.nome, servico.preco)
            cursor.execute(sql, parametros)
            servico.id = cursor.lastrowid
            cursor.close()
            conexao.commit()
            conexao.close()
            
    
    def alterar(self, servico):
        from Model.Servico import Servico
        if isinstance(servico, Servico):
            conexao = self.__conexao.obterConexao()
            cursor = conexao.cursor()
            sql = "Update servico set nome = %s, preco = %s where id = %s"
            parametros = (servico.nome, servico.preco, servico.id)
            cursor.execute(sql, parametros)
            cursor.close()
            conexao.commit()
            conexao.close()

    def excluir(self, servico):
        from Model.Servico import Servico
        if isinstance(servico, Servico):
            conexao = self.__conexao.obterConexao()
            cursor = conexao.cursor()
            sql = "Delete from servico where id = %s"
            parametros = [servico.id]
            cursor.execute(sql, parametros)
            cursor.close()
            conexao.commit()
            conexao.close()
    
    def consultar(self) -> list:
        from Model.Servico import Servico
        conexao = self.__conexao.obterConexao()
        cursor = conexao.cursor()
        sql = "Select * from servico"
        cursor.execute(sql)
        listaServicos = []
        for (id, nome, preco) in cursor:
            servico = Servico(id, nome, float(preco))
            listaServicos.append(servico)
        cursor.close()
        conexao.commit()
        conexao.close()
        return listaServicos
