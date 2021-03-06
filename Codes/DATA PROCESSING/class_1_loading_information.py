import pandas as pd
from IPython.display import display

class LoadingInformations:

    def __init__(self):
        self.__dados_portugues__ = pd.read_csv("../data_sets/stackoverflow_portugues.csv")
        self.__dados_ingles__ = pd.read_csv("../data_sets/stackoverflow_ingles.csv")
        self.__dados_espanhol__ = pd.read_csv("../data_sets/stackoverflow_espanhol.csv")

    #Metodos para retorno de questoes especificas
    def get_questao_pt(self,numero_da_questao):
        if type(numero_da_questao) == int:
            return self.__dados_portugues__.Questão[numero_da_questao] 

    def get_questao_en(self,numero_da_questao):
        if type(numero_da_questao) == int:
            return self.__dados_ingles__.Questão[numero_da_questao] 

    def get_questao_es(self,numero_da_questao):
        if type(numero_da_questao) == int:
            return self.__dados_espanhol__.Questão[numero_da_questao] 
    
    #Metodos para adicionar coluna na tabela
    def add_coluna_pt(self,nome_da_coluna,dados):
        if nome_da_coluna not in self.__dados_portugues__:
            self.__dados_portugues__[nome_da_coluna] = dados
            self.__dados_portugues__.to_csv("data_sets/stackoverflow_portugues.csv")

    def add_coluna_en(self,nome_da_coluna,dados):
        if nome_da_coluna not in self.__dados_ingles__:
            self.__dados_ingles__[nome_da_coluna] = dados
            self.__dados_ingles__.to_csv("data_sets/stackoverflow_ingles.csv")

    def add_coluna_es(self,nome_da_coluna,dados):
        if nome_da_coluna not in self.__dados_espanhol__:
            self.__dados_espanhol__[nome_da_coluna] = dados
            self.__dados_espanhol__.to_csv("data_sets/stackoverflow_espanhol.csv")

    #Metodo para retorno da tabela
    @property
    def dados_portugues(self):
        return self.__dados_portugues__
    
    @property    
    def dados_ingles(self):
        return self.__dados_ingles__
    
    @property    
    def dados_espanhol(self):
        return self.__dados_espanhol__
    

if __name__ == "__main__":
    info = LoadingInformations()
    print("DATA PORTUGUESE")
    display(info.dados_portugues.head()) 

    print("DATA INGLES")
    display(info.dados_ingles.head())

    print("DATA ESPANHOL")
    display(info.dados_espanhol.head())