import json
from  pathlib import Path
from configparser import ConfigParser

class File:
    def __init__(self): #construtor da classe File
        self.file_bd = Path(self._returning_file_path()) #caminho do arquivo
        if  not self.file_bd.exists(): # se o arquivo que guarda os dados ainda nao existir...
            self._create_file() #cria  arquivo do banco, caso ele ainda nao exista.

    # Funções de uso interno (somente usadas aqui dentro desta classe)
    def _create_file(self):#cria um arquivo
        """FUNÇÂO INTERNA: Se ainda nao houver um arquivo json com os dicionários de contatos,
        esta função, quando chamada, tem a responsabilidade de criá-lo."""

        inicializador = [{"":""}] #lista com um dicionário vazio responsável por inicializar o json.
        with open(self.file_bd, "w", encoding='utf-8') as data_base:
            data_base.write(json.dumps(inicializador, indent= 5))

    def _returning_file_path(self):  # retorna o caminho do json
        """FUNÇÃO INTERNA: esta função lê um arquivo de configuração do tipo config.ini,
        depois lê uma seção específica dele, através do get(), retornando o caminho do json."""

        path_file_config = ConfigParser()  # variável que lerá o arquivo de configuração.
        path_file_config.read("config.ini")  # lendo o arquivo de configuração (config.ini)

        return path_file_config.get("paths", "file_bd_json")  # pegando a seção em que está o json.

    # Funções de uso externo (que aparecem noutros módulos)
    def read_file(self): #ler o arquivo json
        """FUNÇÃO EXTERNA: Esta funcao lê o conteúdo que estiver armazenado no json e o retorna numa lista.
        Ela é necessária para ações como as de adicionar, editar e excluir contatos."""

        with open(self.file_bd, "r", encoding="utf-8") as content: #lendo-o, caso ele exista.
            current_bank_contacts = json.load(content)

        return current_bank_contacts #retornando a lista de contato que houver.

    def write_in_json(self, list): # grava no json uma lista de dicionarios de contatos.
        """FUNÇÃO EXTERNA: sempre que se precisar escrever algo num arquivo, especiamente um json,
        deve-se usar esta função, que serve pra adicionar e editar dados pelo menos. """

        with open(self.file_bd, "w", encoding="utf-8") as writing_bd:
            writing_bd.write(json.dumps(list, indent= 5))


