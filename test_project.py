from unittest.mock import mock_open, patch
from project import Regex, read_photos

def test_search_keywords():
    assert Regex.search_keywords("2025-05-25_sunset.jpg") == "sunset"
    assert Regex.search_keywords("2025-05-26_friends.png") == "friends"
    assert Regex.search_keywords("selfie.jpg") == None


def test_check_photos_by_date():
    assert Regex.check_photos_by_date("2025-05-25_sunset.jpg") == "2025-05-25_"
    assert Regex.check_photos_by_date("2025-05-26_friends.png") == "2025-05-26_"
    assert Regex.check_photos_by_date("selfie.jpg") == None


def test_read_photos():

    mock_file = "2025-05-25_sunset.jpg\n2025-05-26_friends.png\n"
    mock = mock_open(read_data=mock_file)

    with patch("builtins.open", mock):
        result = read_photos()

    assert result == ["2025-05-25_sunset.jpg", "2025-05-26_friends.png"]
    mock.assert_called_once_with("photos.txt", "r")
