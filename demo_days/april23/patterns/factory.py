from abc import ABC, abstractmethod


class Builder(ABC):

    @property
    @abstractmethod
    def product(self):
        pass

    @abstractmethod
    def build_case(self):
        pass

    @abstractmethod
    def build_mainboard(self):
        pass

    @abstractmethod
    def build_cpu(self):
        pass


class ComputerBuilder(Builder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._product = Computer()

    @property
    def product(self):
        product = self._product
        self.reset()
        return product

    def build_case(self):
        self._product.add("Coolermaster N300")

    def build_mainboard(self):
        self._product.add(" MSI 970")

    def build_servermainboard(self):
        self._product.add(" Big 1170")

    @abstractmethod
    def build_cpu(self):
        pass


class GamingComputerBuilder(ComputerBuilder):
    def build_cpu(self):
        self._product.add(" Intel Core i7")


class OfficeComputerBuilder(ComputerBuilder):
    def build_cpu(self):
        self._product.add(" Intel Core i5")

class OfficeServerComputerBuilder(ComputerBuilder):
     def build_cpu(self):
         self._product.add(" 4TH GEN INTEL XEON")


class Computer:
    def __init__(self):
        self._parts = []

    def add(self, part):
        self._parts.append(part)

    def __str__(self):
        return ''.join(self._parts)


class Director:
    def __init__(self):
        self._builder = None

    @property
    def builder(self):
        return self._builder

    @builder.setter
    def builder(self, builder):
        self._builder = builder

    def build_minimal_viable_product(self):
        self.builder.build_case()

    def build_full_featured_product(self):
        self.builder.build_case()
        self.builder.build_mainboard()
        self.builder.build_cpu()

    def build_full_featured_server_product(self):
        self.builder.build_case()
        self.builder.build_servermainboard()
        self.builder.build_cpu()


if __name__ == "__main__":
    director = Director()
    print("Build a full featured Gaming machine for nerds")
    print()
    builder = GamingComputerBuilder()
    director.builder = builder
    director.build_full_featured_product()
    print(builder.product)

    print("Build a full featured office machine for good employees")
    print()
    builder = OfficeComputerBuilder()
    director.builder = builder
    director.build_full_featured_product()
    print(builder.product)

    print("Build a full featured server machine for new datacenter")
    print()
    builder = OfficeServerComputerBuilder()
    director.builder = builder
    director.build_full_featured_server_product()
    print(builder.product)

    print("Build a bare minimum Gaming Computer for kids for cheap ass parents")
    print()
    builder = GamingComputerBuilder()
    director.builder = builder
    director.build_minimal_viable_product()
    print(builder.product)
