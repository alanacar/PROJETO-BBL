class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True  # Inicia como disponível para empréstimo

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            return True
        return False

    def devolver(self):
        self.disponivel = True


class Usuario:
    def __init__(self, id_usuario, nome):
        self.id_usuario = id_usuario
        self.nome = nome
        self.livros_emprestados = []

    def pegar_livro_emprestado(self, livro):
        if livro.emprestar():
            self.livros_emprestados.append(livro)
            print(f"{self.nome} pegou o livro '{livro.titulo}' emprestado.")
        else:
            print(f"O livro '{livro.titulo}' não está disponível para empréstimo.")

    def devolver_livro(self, livro):
        if livro in self.livros_emprestados:
            livro.devolver()
            self.livros_emprestados.remove(livro)
            print(f"{self.nome} devolveu o livro '{livro.titulo}'.")
        else:
            print(f"{self.nome} não tem o livro '{livro.titulo}' para devolver.")


class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def adicionar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def listar_livros(self):
        if not self.livros:
            print("Não há livros na biblioteca.")
        for livro in self.livros:
            disponibilidade = "Disponível" if livro.disponivel else "Indisponível"
            print(f"Livro: '{livro.titulo}' | Autor: {livro.autor} | Ano: {livro.ano_publicacao} | Status: {disponibilidade}")

    def buscar_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo.lower() == titulo.lower():
                return livro
        print(f"Livro '{titulo}' não encontrado.")
        return None



# Criando a biblioteca
biblioteca = Biblioteca()

# Criando livros
livro1 = Livro("E assim que acaba", "Collen hoover", 2022)
livro2 = Livro("O lado frio do amor", "Collen hoover", 2022)
livro3 = Livro("Se nao fosse voce", "collen hoover", 2019)
# Adicionando livros à biblioteca
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
# Criando usuários
usuario1 = Usuario(1, "alana")
usuario2 = Usuario(2, "vitoria")

# Adicionando usuários à biblioteca
biblioteca.adicionar_usuario(usuario1)
biblioteca.adicionar_usuario(usuario2)

# Listando livros disponíveis
print("Livros disponíveis na biblioteca:")
biblioteca.listar_livros()

# Gabriela tenta pegar o livro "1984" emprestado
usuario1.pegar_livro_emprestado(livro1)

# Listando livros novamente
print("\nApós o empréstimo de vitoria:")
biblioteca.listar_livros()

# Gabriela tenta pegar o livro "1984" emprestado
usuario2.pegar_livro_emprestado(livro1)

# Maria tenta pegar o livro "Dom Casmurro" emprestado
usuario2.pegar_livro_emprestado(livro2)

# João devolve o livro "1984"
usuario1.devolver_livro(livro1)

# Listando livros novamente
print("\apos a devoluçao de vitoria:")
biblioteca.listar_livros()

class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True  # Inicia como disponível para empréstimo

    def emprestar(self):
        """Método para emprestar o livro, se disponível."""
        if self.disponivel:
            self.disponivel = False
            return True
        return False

    def devolver(self):
        """Método para devolver o livro e deixá-lo disponível novamente."""
        self.disponivel = True



class Biblioteca:
    def __init__(self):
        self.livros = []  # Lista para armazenar os livros na biblioteca

    def adicionar_livro(self, livro):
        """Adiciona um livro à biblioteca."""
        self.livros.append(livro)
        print(f"Livro '{livro.titulo}' adicionado à biblioteca.")

    def listar_livros(self):
        """Lista todos os livros da biblioteca com seu status."""
        if not self.livros:
            print("Não há livros na biblioteca.")
            return
        print("Livros disponíveis na biblioteca:")
        for livro in self.livros:
            status = "Disponível" if livro.disponivel else "Indisponível"
            print(f"Livro:")
            opcao = input("LIVROS VARIAVEIS(1-6): ")

        if opcao == "1":
            biblioteca.listar_livros()
        
        elif opcao == "2":
            titulo = input(" o título do livro a ser buscado: ")
            biblioteca.buscar_livro(titulo)
        
        elif opcao == "3":
            titulo = input(" o título do livro a ser emprestado: ")
            biblioteca.emprestar_livro(titulo)
        
        elif opcao == "4":
            titulo = input("o título do livro a ser devolvido: ")
            biblioteca.devolver_livro(titulo)
        
        elif opcao == "5":
            titulo = input("Se nao fosse voce: ")
            autor = input(" Collen Hoover: ")
            ano = input("2019: ")
            livro = Livro(titulo, autor, int(ano))
            biblioteca.adicionar_livro(livro)
        
        elif opcao == "6":
            print("Saindo do sistema. Até logo!")
            
        
        else:
            print("Opção inválida. Tente novamente.")

