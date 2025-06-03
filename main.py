
def main():
    from dao import Dao
    dao_of_main = Dao()

    dao_of_main.add_contacts("fulano", "99762514")
if __name__ == "__main__":
    main()