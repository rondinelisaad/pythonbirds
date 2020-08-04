class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos =  list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    rondineli = Pessoa(nome="Rondineli")
    alex = Pessoa(nome="alex")
    miguel = Pessoa(rondineli, alex, nome="Miguel")
    print(id(rondineli))
    print(rondineli.cumprimentar())
    print(rondineli.nome)
    print(rondineli.idade)
    for filho in miguel.filhos:
        print(filho.nome)