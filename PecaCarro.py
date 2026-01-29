from Produto import Produto

class PecaCarro(Produto):
    def __init__(self, codigo, descricao, preco, quantidade, tipoCarro, marca):
        super().__init__(codigo, descricao, preco, quantidade)
        self.__tipoCarro = tipoCarro
        self.__marca = marca
        
    @property
    def tipoCarro(self):
        return self.__tipoCarro
    
    @tipoCarro.setter
    def tipoCarro(self,tipoCarro):
        self.__tipoCarro = tipoCarro; 

    @property
    def marca(self):
        return self.__marca
    
    @marca.setter
    def marca(self,marca):
        self.__marca = marca
                
                