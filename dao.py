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

