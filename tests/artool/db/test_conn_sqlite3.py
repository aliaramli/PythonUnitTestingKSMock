import unittest
import __init__
from unittest.mock import Mock, patch
from artool.db import conn_sqlite3


class TestFetchUserFunction(unittest.TestCase):
    @patch('sqlite3.connect')
    def test_fetch_user(self, mock_connect):
        """_summary_

        Args:
            mock_connect (_type_): _description_
        """
        # Create a mock connection object
        mock_conn = Mock()
        mock_connect.return_value = mock_conn

        # Create a mock cursor object
        mock_cursor = Mock()
        mock_conn.cursor.return_value = mock_cursor

        # Define the return value for cursor.fetchone()
        mock_cursor.fetchone.return_value = ('John Doe', 30)

        # Call the function with a test user_id
        result = conn_sqlite3.fetch_user(1)

        # Verify that the connection and cursor were used correctly
        mock_connect.assert_called_once_with('example.db')
        mock_conn.cursor.assert_called_once()
        mock_cursor.execute.assert_called_once_with(
            'SELECT * FROM users WHERE id=?', (1,))
        mock_cursor.fetchone.assert_called_once()
        mock_conn.close.assert_called_once()

        # Assert the expected result
        self.assertEqual(result, ('John Doe', 30))


if __name__ == '__main__':
    unittest.main()
