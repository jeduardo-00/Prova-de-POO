from abc import ABC, abstractmethod

class Metodo_Pagamento(ABC):
    @abstractmethod
    def pagar(self, valor:float):pass