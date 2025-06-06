
def main():
    from dao import Dao
    dao_of_main = Dao()

    contatos = dao_of_main.edit_contact("Fulano",)

    #print(contatos)

if __name__ == "__main__":
    main()