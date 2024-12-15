
import unittest
from src.components.TestingComponent import TestingComponent
from ..common import load_ini_and_set_env

class TestTestingComponent(unittest.TestCase):
    
    def setUp(self):
        load_ini_and_set_env()
        super().setUp()

    def test_create_unit_test(self):
        testing_component = TestingComponent()
        customer_code = """
        class Customer:
            def __init__(self, name, last_name):
                self.name = name
                self.last_name = last_name

            def full_name(self):
                return self.name + " " + self.last_name
        """
        # Add assertions to verify the behavior of create_unit_test method
        result = testing_component.create_unit_test('Customer', customer_code)
        self.assertIsNotNone(result)
        self.assertIn('Customer', result)
        self.assertIn('def test_', result)
        self.assertIn('self.assertEqual', result)
        print(result)

    def test_create_unit_test_existing_one(self):
        testing_component = TestingComponent()
        separator = "*" * 55
        customer_code = f"""
        class Customer:
            def __init__(self, name, last_name):
                self.name = name
                self.last_name = last_name

            def full_name(self):
                return self.name + " " + self.last_name
        {separator}
        import unittest
        from src.core.Customer import Customer
        class TestCustomer(unittest.TestCase):
            def test_customer_juan(self):
                customer = Customer('juan', 'perez')
                result = customer.full_name()
                self.assertEqual(result, 'juan perez')
        """
        # Add assertions to verify the behavior of create_unit_test method
        result = testing_component.create_unit_test('Customer', customer_code)
        self.assertIsNotNone(result)
        self.assertIn('Customer', result)
        self.assertIn('def test_customer_juan', result)        
        print(result)

