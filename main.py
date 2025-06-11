"""
Agenda Telefônica 2 (orientada a objetos)

Descrição do projeto:

Registrar em arquivo local nome e número de telefone
- Funcionalidades: inserir, excluir, alterar, "olhar"
- "Olhar": lista tabular de contatos em ordem alfabética com nome e telefone
- Busca de contatos por nome insensível

Desenvolvedores: Pablo Gomes

 início: 02/06/2025 ;  fim:  11/06/2025

 Desenvolvedores: Pablo Gomes

 Coisas a resolver:
#exibir os contatos todos ou por nome por ordem alfabética

"""

def main():
    from dao import Dao
    import  argparse

    dao_of_main = Dao()
    parser = argparse.ArgumentParser()

    parser.add_argument("itens_menu", choices= ['adicionar', 'pesquisar',
                                                'editar', 'excluir'])

    parser.add_argument(f'--nome')
    parser.add_argument(f'--numero')

    args = parser.parse_args()
    option = args.itens_menu

    if option == "adicionar":
        if args.nome is None or args.numero is None:
            print("Você não passou todos os dados. Não dá criar um contato sem um NOME ou sem um NÚMERO. "
                  "Tente novamente.")
        else:
            dao_of_main.add_contacts(args.nome, args.numero)

    elif option == 'pesquisar':
        dao_of_main.search_all_contacts()
    elif option == "editar":
        dao_of_main.edit_contact(args.nome)

    elif option == "excluir":
        retorno = dao_of_main.delete_contacts(args.nome)
        if retorno:
            print("Contato removido com sucesso!")

if __name__ == "__main__":
    main()