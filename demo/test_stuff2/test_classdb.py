import pytest
from unittest.mock import Mock
from classdb import Flight, CustomerDb

@pytest.fixture
def app():
    plane = Flight(5, 10)
    plane.add_passenger("Cristiano Ronaldo")
    plane.add_passenger("Ten Hag")
    plane.add_passenger("Harry Maguire")
    d = CustomerDb()
    yield plane, d
    d.close()

def test_adding_a_passenger(app):
    app[0].add_passenger("Luke Shaw")
    assert app[0].number_of_passengers() == 4

def test_plane_contains_booked_passenger(app):
    app[0].add_passenger("Bruno Fernandes")
    assert "Bruno Fernandes" in app[0].get_passenger_list()

def test_overbooking_not_allowed(app):
    for _ in range(2):
        app[0].add_passenger("Harry Maguire")

    with pytest.raises(OverflowError):
        app[0].add_passenger("Harry Maguire")


def test_total_gross_wo_mock(app):
    gross = app[0].calculate_total_gross(app[1])
    assert gross == 25

def test_total_gross_mocking_constant(app):
    d = app[1]
    d.get_customer_membership = Mock(return_value=1) 
    gross = app[0].calculate_total_gross(d)
    assert gross == 30

def test_total_gross_mocking_w_se(app):
    """with side effect"""
    def mock_members(name: str) -> int:
        if name == "Cristiano Ronaldo":
            return 2
        elif name == "Ten Haag":
            return 0
        return 1

    d = app[1]
    d.get_customer_membership = Mock(side_effect=mock_members) 
    gross = app[0].calculate_total_gross(d)
    assert gross == 25
