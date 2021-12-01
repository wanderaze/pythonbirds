class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)
    def cumprimentar(self):
        return f'olá {id(self)}'

if __name__ == '__main__':
    wander = Pessoa(nome='Wander')
    william = Pessoa(wander, nome='william')
    print(Pessoa.cumprimentar(william))
    print(id(william))
    print(william.cumprimentar())
    print(william.nome)
    print(william.idade)
    for filho in william.filhos:
        print(filho.nome)
    william.sobrenome = 'Azevedo'
    del william.filhos
    print(william.__dict__)
    print(wander.__dict__)