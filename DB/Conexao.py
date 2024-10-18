from dotenv import load_dotenv
import os
import mysql.connector

#Padrão de projeto Singleton
class Conexao(object):
    
    __instancia = None
    
    def __init__(self):
        
        if Conexao.__instancia is None:
            load_dotenv()
            self.__config = {
                                'host': os.getenv('DB_HOST'),
                                'port': os.getenv('DB_PORT'),
                                'user': os.getenv('DB_USER'),
                                'password': os.getenv('DB_PASSWORD'), 
                                'database': os.getenv('DB_DATABASE')
                            }
            self.__poolConexoes = mysql.connector.pooling.MySQLConnectionPool(pool_name="conexoes", 
                                                                              pool_size=10,
                                                                              **self.__config)
            Conexao.__instancia = self
        else:
            raise Exception('Conexão ja criada')
        
    def obterConexao(self):
        return self.__poolConexoes.get_connection()
    
    @staticmethod
    def obterInstancia():
        if Conexao.__instancia is None:
            Conexao()
        return Conexao.__instancia
        
        