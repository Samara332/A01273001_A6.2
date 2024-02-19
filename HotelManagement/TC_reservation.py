
import unittest
import os
from reservation import HotelBooking, create_booking


class TestReservation(unittest.TestCase):
    """Tests for functionality of the HotelBooking class."""
    def setUp(self):
        """Setup method to create a reservation instance before each test."""
        self.reservation_data = {
            'reservation_id': 123,
            'customer_id': 1,
            'hotel_name': 'Hotel California',
            'room_number': 101,
            'start_date': '2023-01-01',
            'end_date': '2023-01-05'
        }
        self.reservation = create_booking(**self.reservation_data)

    def test_reservation_initialization(self):
        """Test the initialization of a reservation."""
        for key, value in self.reservation_data.items():
            self.assertEqual(getattr(self.reservation, key), value)

    def test_save_to_file(self):
        """Test saving a reservation details to a file."""
        self.reservation.save_to_file()
        expected_filename = f"reservation_{self.reservation.reservation_id}.json"
        self.assertTrue(os.path.exists(expected_filename))
        # Clean up
        os.remove(expected_filename)

    def test_cancel_reservation(self):
        """Test canceling a reservation by removing its file."""
        self.reservation.save_to_file()
        HotelBooking.cancel_reservation(self.reservation.reservation_id)
        expected_filename = f"reservation_{self.reservation.reservation_id}.json"
        self.assertFalse(os.path.exists(expected_filename))



if __name__ == '__main__':
    unittest.main()