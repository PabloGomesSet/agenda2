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
           return  True

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

    def edit_contact(self, name):# editar um contato
        """EDITAR CONTATO: essa função oferece a possibilidade de editar, alterar, um contato. Deve-se procurá-lo a partir do
        nome e depois escolher entre mudar o nome ou número (lembrando que são estes dois elementos que forma um contato.)"""

        all_numbers_of_a_contact = self.search_contact(name) #pegando todos os contatos ligados a um mesmo nome.
        if type(all_numbers_of_a_contact) == list: #se a variável for do tipo list ...
            print(f'{name} possui os seguintes números: ')
            for contact in all_numbers_of_a_contact: #percorrendo a lista de contatos de uma mesma pessoa
                print(f'{contact["number_phone"]}') #exibindo os números dessa pessoa

            contact_for_edition = input(f'Qual o número de "{name}" a ser editado: ') #pede o número do contato a ser editado

            file_edited = File()# criando um objeto de FIle para usar os seus métodos de escrita e leitura
            name_or_number = int(input(f'Digite 1- Editar Nome/ 2- Editar Número:  ')) # o usuário escolhe que dados editar

            if name_or_number == 1: #editar somente o nome
                new_name = input(f'Novo nome:   ')

                self.delete_contacts(contact_for_edition) #apaga o contato que está lá no json
                dict_contact = self.return_a_dictionary(new_name,  contact_for_edition) #novo dict com o numero e novo nome

                content_json = file_edited.read_file()# lendo e armazenando numa lista o conteúdo do json
                content_json.append(dict_contact) #adicionando à lista o dicionário do contato editado

                file_edited.write_in_json(content_json) # escrevendo a lista no json

            elif name_or_number == 2: # editar o número
                new_number = input(f'Novo número:   ') #usuario passa o número novo

                self.delete_contacts(contact_for_edition) # removendo o contato que tá la no json com este número
                dict_contact = self.return_a_dictionary(name, new_number) #novo dict com o nome e número novo

                content_json = file_edited.read_file() #lendo e armazenando numa lista o conteúdo do json
                content_json.append(dict_contact) # adcionando na lista o dicionário que tem o contato editado

                file_edited.write_in_json(content_json) #  escrevendo a lista no json.

        else:
            print(all_numbers_of_a_contact)

    def return_a_dictionary(self, name, number_phone): # retorna um dicionario de contato
        """RETORNAR UM DICIONÁRIO: esta  função tem o papel de receber um nome e um número e retorná-los num dicionário.
        Para isso ela usa uma instância da classe Contact."""
        contact_edited = Contact(name, number_phone) #instanciando a classe contact
        return contact_edited._dictionary_contact() #retornando o dicionário formado pelos parâmetros passados na função.