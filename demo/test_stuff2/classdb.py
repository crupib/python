from typing import List

class CustomerDb:

    def __init__(self):
        print("Connected to db")

    def get_customer_membership(self, name: str) -> int:
        if name == "Cristiano Ronaldo":
            return 2
        elif name == "Ten Haag":
            return 0
        return 1

    def close(self):
        print("Connection Closed.")

class Flight:

    def __init__(self, capacity: int, unit_price: int) -> None:
        self.capacity: int = capacity
        self.unit_price: int = unit_price
        self.passengers: List[str] = []

    def add_passenger(self, name: str) -> None:
        """insert passenger into passenger list"""
        booked = self.number_of_passengers() 
        if booked == self.capacity:
            raise OverflowError("Flight is fully booked!")
        self.passengers.append(name)
        return

    def number_of_passengers(self) -> int:
        return len(self.passengers)

    def get_passenger_list(self) -> List[str]:
        return self.passengers

    def calculate_total_gross(self, customer_db_object) -> float:
        gross = 0
        for name in self.passengers:
            gross += round(self.unit_price / customer_db_object.get_customer_membership(name),1)
        return gross
