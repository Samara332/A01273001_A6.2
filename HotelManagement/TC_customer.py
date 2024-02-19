
import unittest
import os
import io
from unittest.mock import patch
from customer import Client


class TestCustomer(unittest.TestCase):
    """Tests for functionality of the Client class."""
    def setUp(self):
        """Setup method to create a customer instance before each test."""
        self.customer = Client(customer_id=1, name='Samara Garcia', email='samaragarcia@tec.com')

    def test_customer_initialization(self):
        """Test the initialization of a customer."""
        self.assertEqual(self.customer.customer_id, 1)
        self.assertEqual(self.customer.name, 'Samara Garcia')
        self.assertEqual(self.customer.email, 'samaragarcia@tec.com')

    def test_delete_customer(self):
        """Test deleting a customer removes their data file."""
        # Setup: Create a new customer and ensure their data file exists
        customer_id = "cust1001"
        Client.create_customer(customer_id, "Samara Garcia", "samaragarcia@tec.com")
        expected_filename = f"customer_{customer_id}.json"
        self.assertTrue(os.path.exists(expected_filename), "Client data file should exist after creation.")

        # Act: Delete the customer
        Client.delete_customer(customer_id)

        # Assert: Verify the customer's data file has been deleted
        self.assertFalse(os.path.exists(expected_filename), "Client data file should be deleted.")

    def test_display_customer_info(self):
        """Test displaying customer information prints the correct details."""
        customer = Client("TC210", "Samara Garcia", "samaragarcia@tec.com")
        expected_output = "Client ID: TC210,\n              Name: Samara Garcia, Email: samaragarcia@tec.com\n"

        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            customer.display_customer_info()
            self.assertEqual(fake_out.getvalue(), expected_output,
                             "The output should match the expected customer details.")

    def test_update_details(self):
        """Test updating customer's details."""
        new_name = 'Samara Garcia'
        new_email = 'samaragarcia@tec.com'
        self.customer.update_details(name=new_name, email=new_email)
        self.assertEqual(self.customer.name, new_name)
        self.assertEqual(self.customer.email, new_email)

    def test_load_customer(self):
        """Test loading a customer retrieves the correct information."""
        # Setup: Create a customer and write their data to a file
        customer_id = "TC230"
        original_customer = Client.create_customer(customer_id, "Marisol Sanchez", "marisol@tec.com")

        # Act: Load the customer from the file
        loaded_customer = Client.load_customer(customer_id)

        # Assert: Verify the loaded customer matches the original
        self.assertEqual(loaded_customer.customer_id, original_customer.customer_id, "Client IDs should match.")
        self.assertEqual(loaded_customer.name, original_customer.name, "Client names should match.")
        self.assertEqual(loaded_customer.email, original_customer.email, "Client emails should match.")

        # Cleanup: Delete the customer file to clean up test environment
        os.remove(f"customer_{customer_id}.json")


if __name__ == '__main__':
    unittest.main()