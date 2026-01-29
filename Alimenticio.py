from Produto import Produto

class Alimenticio(Produto):
    def __init__(self, codigo, descricao, preco, quantidade, validade):
        super().__init__(codigo, descricao, preco, quantidade)
        self.__validade = validade
        
    @property
    def validade(self):
        return self.__validade
    
    @validade.setter
    def validade(self,validade):
        self.__validade = validade; 