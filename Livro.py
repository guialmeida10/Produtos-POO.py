from Produto import Produto

class Livro(Produto):
    def __init__(self, codigo, descricao, preco, quantidade, autor, numeroPaginas):
        super().__init__(codigo, descricao, preco, quantidade)
        self.__autor = autor
        self.__numeroPaginas = numeroPaginas
        
    @property
    def autor(self):
        return self.__autor
    
    @autor.setter
    def autor(self,autor):
        self.__autor = autor; 

    @property
    def numeroPaginas(self):
        return self.__numeroPaginas
    
    @numeroPaginas.setter
    def numeroPaginas(self,numeroPaginas):
        self.__numeroPaginas = numeroPaginas 
                
                