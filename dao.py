from contact import  Contact
from  file import  File


class Dao:

    def add_contacts(self, name, number): #adicionar um novo contato no sistema.
        new_contact = Contact(name, number) #instância de Contact
        file_json = File() #instância da classe File

        json_content_list = file_json.read_file() #aqui fica a lista de contatos advinda do json.

        validator = True
        for dict_contact in json_content_list: #percorre a lista dicionários
            if number in dict_contact. values(): # se o numero de telefone já estiver num dos dicionários...
                print("Não dá pra adicionar. Este número já está salvo.")
                validator = False
                break

        if validator == True:  #caso número ainda nao esteja num dos dicionarios.
                json_content_list.append(new_contact._dictionary_contact()) #adiciona à lista o dicionario criado na classe
                file_json.write_in_json(json_content_list)
                print("novo contato foi salvo.")

    def delete_contacts(self, number): #remove um contato a partir do número passado.
        """ APAGAR UM CONTATO: essa funḉão remove do banco (json) um contato a partir do número de telefone
        passado. Ela recebe o número por parâmetro, o procura dentro do banco e, se o encontrar o remove."""

        file_bd = File() #instância da classe File
        list_contacts = file_bd.read_file() # uso do read_file() para receber a lista de contatos do banco.

        validator = False #variável de validação, controle, verificação...

        for contact in list_contacts: # percorrendo a lista de dicionários de contato
            if number in contact.values(): # se o número passado via parâmetro estiver num dos dicionários...
                list_contacts.remove(contact) # removendo o dicionário cujo o número bate com o passado no parâmetro.
                validator = True

        if validator == False: #se o número passado bater com nennhum dos números dos contatos...
            print("número não encontrado")
        else:
           file_bd.write_in_json(list_contacts) #escrevendo no json a nova lista de contato, agora sem aquele que foi removido.
           print("contato removido. lista atualizada.")

    def search_contact(self, name): #funcao que pesquisa um contato a partir do número passado.
        """PESQUISAR CONTATOS: essa funcão faz pesquisa por um ou mais contatos dentro do banco (json). A partir de um nome
        recebido por parâmetro, ela retorna uma lista com todos os contatos cujos nomes sejam iguais ao parametro passado."""

        new_file = File() #instância da classe File
        bd = new_file.read_file() #lendo o json e armazenando os dados numa lista
        all_contacts_of_number = [] # criando a lista que armazenará todos os contatos que tenham o mesmo nome.

        validator =  False #variavel de validacao

        for contact in bd: #percorrendo a lista de contatos
            if name in contact.values(): #verificando se o nome passado é igual aos nomes dos dicionarios
                all_contacts_of_number.append(contact) #salvando na lista os contatos cujos nomes sao iguais ao parametro
                validator = True

        if validator == False: #quando o nome passado por parâmetro nao estiver em nenhum dicionario
            return f'não tem ninguem que se chame "{name}" aqui.'
        else:
            return all_contacts_of_number #retornando a lista se ela tive pelo meno um dicionario.
