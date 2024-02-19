
import unittest
from room import HotelRoom


class TestRoom(unittest.TestCase):
    """Tests for functionality of the HotelRoom class."""
    def setUp(self):
        """Setup method to create a room instance before each test."""
        self.room = HotelRoom(room_number=101, room_type='single', price=100.00, is_available=True)

    def test_room_initialization(self):
        """Test the initialization of a room."""
        self.assertEqual(self.room.room_number, 101)
        self.assertEqual(self.room.room_type, 'single')
        self.assertEqual(self.room.price, 100.00)
        self.assertTrue(self.room.is_available)

    def test_make_reservation(self):
        """Test making a reservation."""
        self.room.make_reservation()
        self.assertFalse(self.room.is_available)

    def test_cancel_reservation(self):
        """Test canceling a reservation."""
        self.room.make_reservation()  
        self.room.cancel_reservation()
        self.assertTrue(self.room.is_available)

    def test_update_price(self):
        """Test updating the room's price."""
        new_price = 150.00
        self.room.update_price(new_price)
        self.assertEqual(self.room.price, new_price)

   


if __name__ == '__main__':
    unittest.main()