from os import getcwd
import pytest
from whodis import WhoDis


def test_determine_language_with_valid_path():
    """ Determine the language using a valid path with files in it """
    path = '/home/josh/repos/alppb'  # TODO this should be a mocked filesystem
    blah = WhoDis()
    blah.determine_language(path)

    # Tests for self.files.
    assert type(blah.files) is list
    assert len(blah.files) > 0

    # Tests for self.files_by_language.
    assert type(blah.files_by_language) is dict
    assert len(blah.files_by_language.keys()) > 0
    assert len(blah.files_by_language['py']) > 0

    # Tests for self.language.
    assert type(blah.language) is str
    assert blah.language != ""
    assert blah.language == 'py'

    # Tests for self.all_languages.
    assert type(blah.all_languages) is list
    assert blah.all_languages != []
    assert blah.all_languages == ['py', 'md']


def test_determine_language_with_invalid_path_raises_exception():
    """ An invalid path should raise an IOError """
    path = "/lol_i-DONT(EXIST)"
    blah = WhoDis()
    with pytest.raises(IOError):
        blah.determine_language(path)


def test_determine_language_with_no_source_code_raises_exception():
    """ A path with recognizable source code should raise an IOError """
    path = "/tmp"
    blah = WhoDis()
    with pytest.raises(IOError):
        blah.determine_language(path)
