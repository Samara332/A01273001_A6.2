"""Module for representing hotels"""
import json
import os
from room import HotelRoom
from reservation import make_booking


class Hotel:
    """Represents a hotel within the reservation system, with persistence."""

    def __init__(self, hotel_name, hotel_location):
        """Initializes a Hotel object with a name and location."""
        self.hotel_name = hotel_name
        self.hotel_location = hotel_location
        self.rooms = []  # Could be a list of HotelRoom objects
        self.data_filename = f"{hotel_name}_data.json"

    @staticmethod
    def create_new_hotel(hotel_name, hotel_location):
        """Creates a new hotel and saves it to a file."""
        hotel = Hotel(hotel_name, hotel_location)
        hotel.save_to_file()
        return hotel

    @staticmethod
    def remove_hotel(hotel):
        """Deletes hotel data file."""
        os.remove(hotel.data_filename)

    def show_information(self):
        """Returns hotel information as a string."""
        return f"Hotel Name: {self.hotel_name}, Location: {self.hotel_location}"

    def change_information(self, new_name=None, new_location=None):
        """Modifies hotel information and updates the file."""
        if new_name:
            self.hotel_name = new_name
        if new_location:
            self.hotel_location = new_location
        self.save_to_file()

    def save_to_file(self):
        """Saves hotel data to a file."""
        data = {
            'name': self.hotel_name,
            'location': self.hotel_location,
            'rooms': [room.to_dict() for room in self.rooms]
        }
        with open(self.data_filename, 'w', encoding='utf-8') as file:
            json.dump(data, file)

    def load_from_file(self):
        """Loads hotel data from a file."""
        with open(self.data_filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
        self.hotel_name = data['name']
        self.hotel_location = data['location']
        # Assume a from_dict class method for HotelRoom to reconstruct room objects
        self.rooms = [HotelRoom.from_dict(room_data) for room_data in data['rooms']]  # pylint: disable=no-member

    def reserve_room(self, reservation_id, customer_id, room_number,
                     start_date, end_date):
        """Reserve a room if available."""
        room = next((room for room in self.rooms if room.room_number == room_number and room.is_available), None)
        if room:
            room.reserve()
            reservation = make_booking(
                reservation_id=reservation_id,
                customer_id=customer_id,
                hotel_name=self.hotel_name,
                room_number=room_number,
                start_date=start_date,
                end_date=end_date
            )
            reservation.save_to_file()
            self.save_to_file()
            return True
        return False

    def cancel_reservation(self, reservation_id):
        """Cancel a room reservation."""
        # This assumes reservation data includes the room number and can be matched to a room in this hotel
        try:
            with open(f"reservation_{reservation_id}.json", 'r', encoding='utf-8') as file:
                data = json.load(file)
            room_number = data['room_number']
            room = next((room for room in self.rooms if room.room_number == room_number), None)
            if room:
                room.cancel_reservation()
                os.remove(f"reservation_{reservation_id}.json")
                self.save_to_file()
                return True
        except FileNotFoundError:
            pass
        return False
