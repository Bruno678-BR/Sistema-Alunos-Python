import sqlite3

class SistemaAlunos:
    def __init__(self):
        self.conexao = sqlite3.connect("alunos.db")
        self.cursor = self.conexao.cursor()
        self.criar_tabela()

    def criar_tabela(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS alunos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                nota REAL
            )
        """)
        self.conexao.commit()

    def adicionar_aluno(self):
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
        self.cursor.execute("INSERT INTO alunos (nome, nota) VALUES (?, ?)", (nome, nota))
        self.conexao.commit()

        print("Aluno salvo com sucesso!")

    def mostrar_alunos(self):
        self.cursor.execute("Select * from alunos")
        alunos = self.cursor.fetchall()

        if not alunos:
            print("Nenhum aluno cadastrado!")
            return

        for linha in alunos:
            print(linha)
    
    def alunos_cadastrados (self):
        self.cursor.execute("select count(*) from alunos")
        resultado = self.cursor.fetchone()
        
        return resultado[0]
    
    def buscar_aluno (self):
        nome = input("Qual o nome do aluno que você deseja pesquisar? ")        
        self.cursor.execute("select nome, nota from alunos where nome = ?",
            (nome,)
        )

        resultado = self.cursor.fetchone()
        
        if resultado:
            print("Aluno encontrado!")
            print(resultado)
        else:
            print("Aluno não encontrado!")

    def maior_nota (self):
        self.cursor.execute("SELECT nome, nota FROM alunos ORDER BY nota DESC LIMIT 1 ")
        resultado = self.cursor.fetchone()

        return resultado[0]
        
    def calcular_media(self):
        
        self.cursor.execute("Select AVG(nota) from alunos")
        resultado = self.cursor.fetchone()


        return resultado[0]
        

    def relatorio_aluno(self):
        
        self.cursor.execute("Select Avg(nota) from alunos")
        media = self.cursor.fetchone()[0]

        self.cursor.execute("Select nome, Max(nota) from alunos")
        maior = self.cursor.fetchone()

        self. cursor.execute("Select Count(*) from alunos")
        total = self.cursor.fetchone()[0]

        return media, total, maior

sistema = SistemaAlunos()
print("Conectado ao banco de dados!")

while True:

    print("-" * 30)
    print("SISTEMA DE ALUNOS")
    print("1 - Adicionar aluno")
    print("2 - Mostrar alunos")
    print("3 - Mostrar o total de alunos cadastrados")
    print("4 - Pesquisar um aluno")
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
        sistema.adicionar_aluno()
    elif opcao == 2:
        sistema.mostrar_alunos()
    elif opcao == 3:
        cadastrado = sistema.alunos_cadastrados()
        if cadastrado is not None:
            print(f"Possuem {cadastrado} alunos cadastrados")
    elif opcao == 4:
        sistema.buscar_aluno()
    elif opcao == 5:
        maior = sistema.maior_nota()
        if maior is not None:
            print(maior)
    elif opcao == 6:
        media = sistema.calcular_media()
        if media is not None:
            print(f"A media dos alunos é: {media:.2f}")
    elif opcao == 7:
        resultado = sistema.relatorio_aluno()
        if resultado is not None:
            media, contador, maior = resultado
            print(f"A quantidade de alunos: {contador}")
            print(f"A media da turma: {media:.2f}")
            print(f"Maior nota: {maior[1]}")
            print(f"Aluno com a maior nota: {maior[0]}")
    elif opcao == 8:
        sistema.conexao.close()
        print("Saindo...")
        break
        
