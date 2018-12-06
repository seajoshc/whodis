from unittest.mock import patch
import pytest
from whodis import WhoDis


@patch('os.walk')
def test_determine_language_with_valid_path(mockwalk):
    """ Determine the language using a valid path with files in it """
    mockwalk.return_value = [
        ('/foo', ('bar',), ('README.md', 'requirements.txt')),
        ('/foo/bar', (), ('__init__.py', 'main.py',)),
    ]
    blah = WhoDis()
    blah.determine_language("/fake_path_yo")

    # Tests for self.files.
    assert type(blah.files) is list
    assert len(blah.files) > 0

    # Tests for self.files_by_language.
    assert type(blah.files_by_language) is dict
    assert len(blah.files_by_language.keys()) == 2
    assert "py" in blah.files_by_language.keys()
    assert "md" in blah.files_by_language.keys()
    assert len(blah.files_by_language['py']) == 2

    # Tests for self.language.
    assert type(blah.language) is str
    assert blah.language != ""
    assert blah.language == 'py'

    # Tests for self.all_languages.
    assert type(blah.all_languages) is list
    assert blah.all_languages != []
    assert "py" in blah.all_languages
    assert "md" in blah.all_languages


def test_determine_language_with_invalid_path_raises_exception():
    """ An invalid path should raise an IOError """
    path = "/lol_i-DONT_exist"
    blah = WhoDis()
    with pytest.raises(IOError):
        blah.determine_language(path)


@patch('os.walk')
def test_determine_language_with_no_source_code_raises_exception(mockwalk):
    """ A path without recognizable source code should raise an IOError """
    mockwalk.return_value = [
        ('/foo', ('bar',), ('baz',)),
        ('/foo/bar', (), ('qux', 'quux',)),
    ]
    path = "/fake_path_yo"
    blah = WhoDis()
    with pytest.raises(IOError):
        blah.determine_language(path)
