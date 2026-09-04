from binary_search import BinarySearch
import unittest
import json
import time
from pathlib import Path


bs = BinarySearch()


# Load items.json from the same directory as this test file
items_file = Path(__file__).parent / "items.json"

with open(items_file, "r") as file:
    data = json.load(file)


# Setting values to created variables
simple_list = data["simple_list"]
list_with_10_items = data["list_with_10_items"]
list_with_100_items = data["list_with_100_items"]
list_with_1000_items = data["list_with_1000_items"]


# Test cases to test Binary Search algorithm
class TestBinarySearch(unittest.TestCase):

    def setUp(self):
        # Start timer for each test
        self.start_time = time.perf_counter()

    def tearDown(self):
        # Calculate elapsed time for each test
        elapsed_time = time.perf_counter() - self.start_time

        print(
            f"{self._testMethodName:<55} "
            f"{elapsed_time:.9f} seconds"
        )

    # Checking the implementation of iterative binary search
    def test_iterative_binary_search_with_simple_list(self):
        item, expected_index = 3, 1

        index = bs.search_iterative(simple_list, item)

        self.assertEqual(expected_index, index)

    # Checking the implementation of recursive binary search
    def test_recursive_binary_search_with_simple_list(self):
        item, expected_index = 3, 1

        low, high = 0, len(simple_list) - 1

        index = bs.search_recursive(simple_list, low, high, item)

        self.assertEqual(expected_index, index)

    # Checking search for an item that does not exist
    def test_search_for_nonexistent_item(self):
        item, expected_result = 100, None

        index = bs.search_iterative(simple_list, item)

        self.assertEqual(expected_result, index)

    # Comparing binary search and linear search
    def test_binary_search_and_linear_search_execution_time(self):
        item, expected_index = 9887, 990

        # Binary search
        start_time = time.perf_counter()

        binary_search_index = bs.search_iterative(
            list_with_1000_items,
            item
        )

        bs_time = time.perf_counter() - start_time

        # Linear search
        start_time = time.perf_counter()

        linear_search_index = list_with_1000_items.index(item)

        ls_time = time.perf_counter() - start_time

        self.assertEqual(expected_index, binary_search_index)
        self.assertEqual(expected_index, linear_search_index)

        print(
            f"    Binary Search: {bs_time:.9f} seconds"
        )
        print(
            f"    Linear Search: {ls_time:.9f} seconds"
        )

    # Checking performance for an item near the beginning
    def test_execution_time_for_item_at_the_beginning(self):
        item, expected_index = 55, 10

        # Binary search
        start_time = time.perf_counter()

        binary_search_index = bs.search_iterative(
            list_with_1000_items,
            item
        )

        bs_time = time.perf_counter() - start_time

        # Linear search
        start_time = time.perf_counter()

        linear_search_index = list_with_1000_items.index(item)

        ls_time = time.perf_counter() - start_time

        self.assertEqual(expected_index, binary_search_index)
        self.assertEqual(expected_index, linear_search_index)

        print(
            f"    Binary Search: {bs_time:.9f} seconds"
        )
        print(
            f"    Linear Search: {ls_time:.9f} seconds"
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)