class MeninasSuperPoderosas:
    def __init__(self, nome, cabelo, vestido):
        self.nome = nome
        self.cabelo = cabelo
        self.vestido = vestido
                
    def get_nome(self):
        return self.nome
    
    def get_cabelo(self):
        return self.cabelo

    def get_vestido(self):
        return self.vestido
    
class Docinho(MeninasSuperPoderosas):
    def __init__(self, nome, cabelo, vestido, temperamento):
        self.temperamento = temperamento
        super().__init__(nome, cabelo, vestido)
                        
    def get_temperamento(self):
        return self.temperamento       

docinho = Docinho ('Docinho', 'preto','verde', 'agressivo')
print(f'{docinho.get_nome()} tem o cabelo {docinho.get_cabelo()}, o vestido {docinho.get_vestido()} e o temperamento {docinho.get_temperamento()}, é uma lutadora mas não tem um super poder exclusivo!')

class Lindinha(MeninasSuperPoderosas):
    def __init__(self, nome, cabelo, vestido):
        super().__init__(nome, cabelo, vestido)
                            
class SuperPoder:
    def __init__(self):
        pass

    def form_SuperPoder(self):
        return 'Indefinida'

class SuperPoderLindinha(SuperPoder):
    def __init__(self, power):
        self.power = power
        super().__init__()

    def form_SuperPoder(self):
        return f"seu super poder é {self.power}"
        
poder_lindinha = SuperPoderLindinha("se transformar em um grande tornado azul!")    
lindinha = Lindinha ('Lindinha', 'loiro','azul')
print(f'{lindinha.get_nome()} tem o cabelo {lindinha.get_cabelo()}, o vestido {lindinha.get_vestido()} e {poder_lindinha.form_SuperPoder()}')

class Florzinha(MeninasSuperPoderosas):
    def __init__(self, nome, cabelo, vestido):
        super().__init__(nome, cabelo, vestido)
       
    def __lider(self):
        return f'Você é a líder das meninas Superpoderosas!'

    def get_menina_lider(self, nome):
        if nome == 'Florzinha':
            return self.__lider()
        
        return f'Você não é a líder das meninas Superpoderosas!'
        

florzinha = Florzinha('Florzinha', 'ruivo', 'rosa')
print(f'{florzinha.get_nome()} tem o cabelo {florzinha.get_cabelo()}, o vestido {florzinha.get_vestido()} e lidera as meninas Superpoderosas!')

girl = florzinha.get_menina_lider('Florzinha')
print(girl)

girl = florzinha.get_menina_lider('Docinho')
print(girl)

girl = florzinha.get_menina_lider('Lindinha')
print(girl)