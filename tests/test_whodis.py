from os import getcwd
import pytest
from whodis import WhoDis


def test_determine_language_with_valid_path():
    """ Determine the language using a valid path with files in it """
    path = getcwd()  # TODO this should be a mocked filesystem
    blah = WhoDis()
    blah.determine_language(path)
    assert len(blah.files) > 0


def test_determine_language_with_invalid_path():
    """ An invalid path should raise an IOError """
    path = "/lol_i-DONT(EXIST)"
    blah = WhoDis()
    with pytest.raises(IOError):
        blah.determine_language(path)
