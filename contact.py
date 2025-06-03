class Contact:

    def __init__(self, name, number_phone): #construtuor da classe
        self.name = name
        self.number_phone = number_phone

    def _dictionary_contact(self): #função que criar e retorna um contato dicionarizado

        """nessa funcao os dados 'Nome' e 'Número' são reunidos
        para formar um contato. Eles são colocados num dicionário,
        que será retornado pela funcao e salvo, depois, num Json."""

        dict_contact = {
            "name": self.name,
            "number_phone": self.number_phone
        }

        return  dict_contact