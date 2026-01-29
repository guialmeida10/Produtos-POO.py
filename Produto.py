class Produto:
    def __init__(self, codigo, descricao, preco, quantidade):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__preco = preco
        self.__quantidade = quantidade
        
    def mudaEstoque(self, acrescimo):
        self.__quantidade += acrescimo
        return self.__quantidade
    
    def imprimeProduto(self):
        print ("Codigo: ", self.__codigo, "\nDescricao: ", self.__descricao, "\nPreco: ", self.__preco, "\nQuantidade: ", self.__quantidade)
        
    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self,codigo):
        self.__codigo = codigo

    @property
    def descricao(self):
        return self.__descricao
    
    @descricao.setter
    def descricao(self,descricao):
        self.__descricao = descricao
        
    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self,preco):
        self.__preco = preco
        
    @property
    def quantidade(self):
        return self.__quantidade
    
    @quantidade.setter
    def quantidade(self,quantidade):
        self.__quantidade = quantidade  
            
            
    
    
