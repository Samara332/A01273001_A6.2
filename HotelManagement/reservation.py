"""Module for hotel reservations."""

import json
import os


class HotelBooking:
    """This class models a hotel booking within the hotel management system.

    Properties:
        booking_id (int): Unique identifier for the booking.
        guest_id (int): The ID of the guest who made the booking.
        hotel_name (str): The name of the hotel where the booking was made.
        room_number (int): The reserved room's number.
        check_in_date (str): The date when the guest checks in.
        check_out_date (str): The date when the guest checks out.
    """

    def __init__(self, **kwargs):
        """Initializes a HotelBooking object with provided details."""
        self.booking_id = kwargs.get('booking_id')
        self.guest_id = kwargs.get('guest_id')
        self.hotel_name = kwargs.get('hotel_name')
        self.room_number = kwargs.get('room_number')
        self.check_in_date = kwargs.get('check_in_date')
        self.check_out_date = kwargs.get('check_out_date')

    def save_to_file(self):
        """Persists booking details to a file."""
        data = vars(self)
        filename = f"booking_{self.booking_id}.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f)

    @staticmethod
    def cancel_booking(booking_id):
        """Cancels a booking by deleting its associated file."""
        filename = f"booking_{booking_id}.json"
        os.remove(filename)

    @classmethod
    def create_booking(cls, **kwargs):
        """Creates a new booking and saves it to a file."""
        booking = cls(**kwargs)
        booking.save_to_file()
        return booking


def make_booking(**kwargs):
    """Factory function to generate a HotelBooking instance."""
    return HotelBooking(**kwargs)
