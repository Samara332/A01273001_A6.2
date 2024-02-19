"""Module for representing hotel rooms."""

class HotelRoom:
    """Represents a room within a hotel.

    Attributes:
        number (int): The room number.
        type (str): The type of room (e.g., single, double, suite).
        available (bool): Availability status of the room.
        nightly_price (float): Price per night for the room.
    """

    def __init__(self, number, type_, nightly_price, available=True):
        """Initializes a HotelRoom with number, type, price, and availability.
           By default, all rooms are available.

        Parameters:
            number (int): The room number.
            type_ (str): The type of the room.
            nightly_price (float): Price per night for the room.
            available (bool): Availability status of the room.
        """
        self.number = number
        self.type = type_
        self.nightly_price = nightly_price
        self.available = available

    def reserve(self):
        """Marks the room as reserved (unavailable)."""
        self.available = False

    def cancel_reservation(self):
        """Marks the room as available (cancels reservation)."""
        self.available = True

    def update_price(self, new_price):
        """Updates the room's nightly price.

        Parameters:
            new_price (float): The new price of the room per night.
        """
        self.nightly_price = new_price

    @classmethod
    def from_dict(cls, data):
        """Creates a HotelRoom instance from a dictionary.

        Parameters:
            data (dict): A dictionary containing room properties.

        Returns:
            HotelRoom: An instance of the HotelRoom class.
        """
        return cls(
            number=data['number'],
            type_=data['type'],
            nightly_price=data['nightly_price'],
            available=data.get('available', True)  # Default to True if not specified
        )

    def to_dict(self):
        """
        Converts the HotelRoom instance into a dictionary representation.

        This method allows the HotelRoom object's current state to be represented
        as a dictionary, making it easier to serialize, especially for saving
        the room data in formats like JSON.

        Returns:
            dict: A dictionary containing the room's properties, including
                'number', 'type', 'nightly_price', and 'available'.
        """
        return {
            'number': self.number,
            'type': self.type,
            'nightly_price': self.nightly_price,
            'available': self.available
        }
