from HomeWork19.alchemy.models.table_models import LaptopModel
from HomeWork19.alchemy.session import session


class LaptopRepository:
    def __init__(self):
        self.__session = session
        self.__model = LaptopModel

    def get_all(self):
        return self.__session.query(self.__model).all()

    def get_by_id(self, id):
        laptop = self.__session.get(self.__model, {'id': id})
        return laptop

    def add_item(self, name, cpu_id):
        self.__session.add(name,cpu_id)


    def remove_item_by_id(self, id):
        laptop = self.__session.get(self.__model, {'id': id})
        self.__session.delete(laptop)



if __name__ == "__main__":
    laptop_repo = LaptopRepository()
    result = laptop_repo.get_all()
    for r in result:
        print(r)



    print(laptop_repo.get_by_id(2))

    laptop_repo.remove_item_by_id(2)
    result = laptop_repo.get_all()
    for r in result:
        print(r)