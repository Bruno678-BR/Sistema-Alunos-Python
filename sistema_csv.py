import csv

def adicionar_aluno():

    nome = input("Digite o nome do aluno: ")
    if nome.strip() == "":
        print("O nome não pode ser vazio!")
        return
    if any(char.isdigit() for char in nome):
        print("O nome não pode conter números!")
        return
    
    while True:
        try:
            nota = float(input("Digite uma nota para registrar: "))
            if nota < 0 or nota > 10:
                print("Nota inválida!A nota deve estar em 0 e 10!")
            else:
                print("Nota cadastrada com sucesso!")
                break
        except ValueError:
            print("Digite apenas numeros!")
       
    with open("alunos.csv", "a", newline="") as arquivo:

        escritor = csv.writer(arquivo)

        escritor.writerow([nome, nota])

    print("Aluno salvo com sucesso!")

def mostrar_alunos():
    try:
        with open("alunos.csv", "r") as arquivo:
            leitor = csv.reader(arquivo)
            for linha in leitor:
                print(linha)
    except FileNotFoundError:
        print("Não possuem alunos cadastrados!")
                 
def calcular_media():
    try:
        with open("alunos.csv", "r") as arquivo:
            leitor = csv.reader(arquivo)

            soma = 0
            contador = 0

            for linha in leitor:
                soma += float(linha[1])
                contador += 1
            media = soma / contador

            return media
    except FileNotFoundError:
        print("Nennhum Aluno Cadastrado para calcular a media!")

def buscar_aluno ():
    try:
        nome = input("Qual o nome do aluno que você deseja pesquisar? ")
        encontrou = False

        with open ("alunos.csv","r") as arquivo:
            leitor = csv.reader(arquivo)
    
            for linha in leitor:
                if nome == linha[0]:
                    print("Aluno encontrado!")
                    print(linha[0])
                    print(linha[1])
                    encontrou = True
            if not encontrou:
                print("Aluno não encontrado!")
    except FileNotFoundError:
        print("Não possuem Alunos Cadastrados!")


def maior_nota ():
    try:
        maior = None

        with open("alunos.csv", "r") as arquivo:
            leitor = csv.reader(arquivo)

            for linha in leitor:

                if maior is None:
                    maior = linha

                elif float(linha[1]) > float(maior[1]):
                    maior = linha
            return maior
    except FileNotFoundError:
        print("Cadastre um aluno primeiramente!")

def alunos_cadastrados ():
    try:
        contador = 0

        with open("alunos.csv","r") as arquivo:
            leitor = csv.reader(arquivo)

            for _ in leitor:
                contador+= 1

            return contador
    except FileNotFoundError:
        print("Cadastre alguns aluno primeiro!")

def relatorio_aluno():
    try:
        contador = 0
        maior = None
        soma = 0

        with open("alunos.csv","r") as arquivo:
            leitor = csv.reader(arquivo)

            for linha in leitor:
                soma += float(linha[1])
                contador += 1
            
                if maior is None:
                    maior = linha
                elif float(linha[1]) > float(maior[1]):
                    maior = linha
            media = soma / contador

            return media,contador,maior
    except FileNotFoundError:
        print("Faça alguns registros primeiramente!")

while True:

    print("-" * 30)
    print("SISTEMA DE ALUNOS")
    print("1 - Adicionar aluno")
    print("2 - Mostrar alunos")
    print("3 - Pesquisar um aluno")
    print("4 - Mostrar o total de alunos cadastrados")
    print("5 - Mostrar a maior nota")
    print("6 - Mostrar a media de alunos")
    print("7 - Relatorio atual")
    print("8 - Sair")

    try:
        opcao =int(input("Escolha uma opção: "))
    except ValueError:
        print("Apenas numeros!")
        continue

    if opcao == 1:
        adicionar_aluno()
    elif opcao == 2:
        mostrar_alunos()
    elif opcao == 3:
        buscar_aluno()
    elif opcao == 4:
        cadastrado = alunos_cadastrados()
        if cadastrado is not None:
            print(f"Possuem {cadastrado} alunos cadastrados")
    elif opcao == 5:
        maior = maior_nota()
        if maior is not None:
            print(maior)
    elif opcao == 6:
        media = calcular_media()
        if media is not None:
            print(f"A media dos alunos é: {media:.2f}")
    elif opcao == 7:
        resultado = relatorio_aluno()
        if resultado is not None:
            media, contador, maior = resultado
            print(f"A quantidade de alunos: {contador}")
            print(f"A media da turma: {media:.2f}")
            print(f"Maior nota: {maior[1]}")
            print(f"Aluno com a maior nota: {maior[0]}")
    elif opcao == 8:
        print("Saindo...")
        break