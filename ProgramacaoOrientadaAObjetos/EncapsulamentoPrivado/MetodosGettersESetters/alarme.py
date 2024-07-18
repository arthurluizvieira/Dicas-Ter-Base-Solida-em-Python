class Alarme:
    def __init__(self, estado: bool) -> None: # retorna None pois não retorna nada, apenas recebe
        self.__estado = estado
    
    def get_estado(self) -> bool: # retorna um valor booleano
        return self.__estado
    
    def set_estado(self, valor: bool) -> None:
        if isinstance(valor, bool): # verificando se a entrada é uma instância de um valor booleano
            self.__estado = valor
    
# set para alteração de um atributo de uma instância
# get para acessar os atributos