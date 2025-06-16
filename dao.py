from contact import  Contact
from  file import  File


class Dao:

#Funções de uso externo (que aparecem noutros módulos)
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

    def search_contacts(self, name):
        file = File()
        list_of_all_contacts = file.read_file()  # lendo todos os contatos armazenados no json

        list_contacts_selected_by_name = []
        validator = False
        for contact in list_of_all_contacts:
            if name in contact["name"]:
                 list_contacts_selected_by_name.append(contact)

        if list_contacts_selected_by_name:
            self._show_contacts(list_contacts_selected_by_name)
            validator = True

        if not validator:
            print(f'"{name}" não encontrado.')

    def  view_all_contacts(self):
        """VER TODOS OS CONTATOS: esta função exibe todos os contatos que houver no banco de dados.
        Ela é diferente da função search_contacts(), que busca um contato a partir de um nome."""

        file = File()
        list_all_contacts = file.read_file()

        self._show_contacts(list_all_contacts)

    def delete_contacts(self, name): #remove um contato a partir do número passado.
        """ APAGAR UM CONTATO: essa funḉão remove do banco (json) um contato a partir do número de telefone
        passado. Ela recebe o número por parâmetro, o procura dentro do banco e, se o encontrar o remove."""

        list_contacts = self._search_numbers_by_name(name) # usando a função search_contact pra pegar os números
        # relacionados ao nome passado por parâmetro.

        if not list_contacts: # se list_contacts for um booleano Falso...
            print(f'Não há ninguem chamado "{name}" nesta agenda.')
        else: # se list_contacts for uma lista ...
            self._show_contacts(list_contacts) #exibindo todos os contatos que o fulano possui
            number_for_delete = input("Digite o número a ser excluido:  ") #solicitando o numero a ser apagado

            file = File()
            list_json = file.read_file() #lendo o contatos todos do banco

            result = self._remove_a_dictionary_from_a_list(number_for_delete, list_json) #removendo o contato
            return  result

    def edit_contact(self, name):# editar um contato
        """EDITAR CONTATO: essa função oferece a possibilidade de editar, alterar, um contato. Deve-se procurá-lo a partir do
        nome e depois escolher entre mudar o nome ou número (lembrando que são estes dois elementos que forma um contato.)"""

        file_edited = File()  # criando um objeto de File para usar os seus métodos de escrita e leitura
        list_all_contacts = file_edited.read_file()  # lista que guarda todos os contatos do banco
        all_numbers_of_a_name = self._search_numbers_by_name(name) #pegando todos os contatos ligados a um
        # mesmo nome.

        if type(all_numbers_of_a_name) == list: #se a variável for do tipo list ...

            print(f'{name} possui os seguintes números: ') # o fulano tem os seguintes numeros...
            self._show_contacts(all_numbers_of_a_name) # exibindo os números dessa pessoa

            number_for_edition = input(f'Qual o número de "{name}" a ser editado : ') #pede o número do contato a ser
            # editado

            number_is_in_a_list =  self._check_if_a_number_is_in_a_list(number_for_edition, all_numbers_of_a_name)
            if number_is_in_a_list: # Se o número passado estiver na lista de números do fulano...

                new_name = input(f'Novo nome: "{name}?" ')  # recebendo o novo nome
                if new_name == "":  # caso nada for digitado...
                    new_name = name

                new_number = input(f'Novo número:  "{number_for_edition}?" ')  # recebendo o novo número
                if new_number == "":  # se nada for digitado...
                    new_number = number_for_edition

                dict_contact = self._return_a_dictionary(new_name, new_number)  # novo dict com o numero e novo nome

                for contact in list_all_contacts:
                    if number_for_edition == contact["number_phone"]:
                        contact.update(dict_contact)
                        break

                file_edited.write_in_json(list_all_contacts)
                print("Edição realizada com sucesso!")
            else:
                print( f'Opa! Este número "{number_for_edition}" NÃO é um dos números de "{name}."')
        else:
            print(f'Não foi encontrado ninguém com o nome "{name}"')
    
#Funções de uso interno (somente usadas aqui dentro desta classe)
    def _search_numbers_by_name(self, name): #funcao que pesquisa um contato a partir do número passado.
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

        if not validator: #quando o nome passado por parâmetro nao estiver em nenhum dicionario
            return False
        else:
            return all_contacts_of_number #retornando a lista se ela tive pelo menos um dicionario.

    def _return_a_dictionary(self, name, number_phone): # retorna um dicionario de contato
        """RETORNAR UM DICIONÁRIO: esta  função tem o papel de receber um nome e um número e retorná-los num dicionário.
        Para isso ela usa uma instância da classe Contact."""

        contact_edited = Contact(name.title(), number_phone) #instanciando a classe contact
        return contact_edited._dictionary_contact() #retornando o dicionário formado pelos parâmetros passados na função.

    def _show_contacts(self, list_contact):
        """MOSTRAR CONTATOS: esta função exibe todos os contatos de qualquer lista passada via parâmetro."""
        list_contact.sort(key=lambda key: key["name"])

        column_name = 20
        column_number = 40
        names = 30
        numbers = 5

        print("\n\t\tAGENDA DO FULANO DE TAL")
        print("")
        print("NOME".center(column_name),"NÚMERO\n".center(column_number))

        for index, dictionary in enumerate( list_contact):
           print(f"{index + 1}".rjust(numbers) , f' {dictionary["name"]}'.ljust(names),  f'{dictionary["number_phone"]}'.center(numbers))

    def _remove_a_dictionary_from_a_list (self, number_for_delete, list_contacts):
        """REMOVER UM DICIONÁRIO DE UMA LISTA:  essa função recebe por parametro um numero e uma lista qualquer,
        procura o primeiro dentro da segunda; e apaga o dicionário no qual ele estiver."""

        file_bd = File() #criando um objeto de Flie para usar, mais abaixo, a sua função write,  função de escrita.
        validator = False  # variável de validação, controle, verificação...

        for contact in list_contacts:  # percorrendo a lista de dicionários de contato
            if number_for_delete in contact.values():  # se o número passado via parâmetro estiver num dos dicionários...
                list_contacts.remove(contact)  # removendo o dicionário cujo o número bate com o passado no parâmetro.
                validator = True

        if not validator:  # se o número passado não bater com nenhum dos números dos contatos...
            print("número não encontrado")
        else:
            file_bd.write_in_json(list_contacts)  # escrevendo no json a nova lista de contato, agora sem aquele que foi removido.
            return True

    def _check_if_a_number_is_in_a_list(self, number, list_numbers):
        """VERIFICAR SE UM NÚMERO ESTÁ NUMA LISTA: essa recebe um número e uma lista por parâmetro e tem a
        responsabilidade de verificar se este número está nessa lista, retornando True se estiver e False se nao."""

        validator = False
        for dictionary  in list_numbers:
            if number  in dictionary.values():
                validator = True
        return  validator