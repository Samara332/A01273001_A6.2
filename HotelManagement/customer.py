"""Module for representing customers."""
import json
import os

class Client:
    """Represents a client with specified ID, full name, and email address."""

    def __init__(self, client_id, full_name, email_address):
        """Creates an instance of a client with specified ID, full name, and email address."""
        self.client_id = client_id
        self.full_name = full_name
        self.email_address = email_address
        self.file = f"client_{client_id}.json"

    def save_to_file(self):
        """Saves client data to a JSON file."""
        data = {
            'client_id': self.client_id,
            'full_name': self.full_name,
            'email_address': self.email_address
        }
        with open(self.file, 'w', encoding='utf-8') as file:
            json.dump(data, file)

    @staticmethod
    def create_client(client_id, full_name, email_address):
        """Creates a new client instance and saves its data to a file."""
        client = Client(client_id, full_name, email_address)
        client.save_to_file()
        return client

    @staticmethod
    def remove_client(client_id):
        """Removes the data file associated with a client."""
        file = f"client_{client_id}.json"
        os.remove(file)

    def display_info(self):
        """Displays the client's information."""
        print(f"""Client ID: {self.client_id},
              Full Name: {self.full_name}, Email Address: {self.email_address}""")

    def update_info(self, full_name=None, email_address=None):
        """Updates client information and saves it to the file."""
        if full_name:
            self.full_name = full_name
        if email_address:
            self.email_address = email_address
        self.save_to_file()

    @staticmethod
    def load_client(client_id):
        """Loads client data from a file."""
        file = f"client_{client_id}.json"
        with open(file, 'r', encoding='utf-8') as data_file:
            data = json.load(data_file)
        return Client(data['client_id'], data['full_name'], data['email_address'])
