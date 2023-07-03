from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, INTEGER, VARCHAR, ForeignKey


Base = declarative_base()


class CpuModel(Base):
    __tablename__ = "cpu"
    id = Column(INTEGER, primary_key=True)
    cpu_name = Column(VARCHAR(50))



    def __str__(self):
        return f"id = {self.id}, cpu_name = {self.cpu_name}"

class LaptopModel(Base):
    __tablename__ = "laptop"
    id = Column(INTEGER, primary_key=True)
    name = Column(VARCHAR(50))
    cpu_id = Column(ForeignKey("cpu.id"))
    cpu = relationship(CpuModel)

    def __str__(self):
        return f"id = {self.id}, laptop_name = {self.name}, cpu_id = {self.cpu_id}"




