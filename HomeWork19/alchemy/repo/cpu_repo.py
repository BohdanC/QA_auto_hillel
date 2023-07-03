from HomeWork19.alchemy.models.table_models import CpuModel
from HomeWork19.alchemy.session import session


class CpuRepository:
    def __init__(self):
        self.__session = session
        self.__model = CpuModel

    def get_all(self):
        return self.__session.query(self.__model).all()

    def get_by_id(self, id):
        cpu = self.__session.get(self.__model, {'id': id})
        return cpu

    def add_item(self, cpu_name: CpuModel):
        self.__session.add(cpu_name)


    def remove_item_by_id(self, id):
        cpu = self.__session.get(self.__model, {'id': id})
        self.__session.delete(cpu)



if __name__ == "__main__":
    cpu_repo = CpuRepository()
    result = cpu_repo.get_all()
    for r in result:
        print(r)



    print(cpu_repo.get_by_id(2))
