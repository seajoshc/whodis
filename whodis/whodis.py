"""
whodis
"""
from os import walk


FILTERED_DIRS = [
    ".git",  # Git
    "venv",  # Common Python Virtual Environment
    "__pycache__",  # Python Cache
    "build",
    "dist",
    "alppb.egg-info",
]


class WhoDis():
    def __init__(self):
        self.files = []
        self.language = ""
        self.files_by_language = {}
        self.all_languages = []

    def determine_language(self, path):
        """
        Determines the dominant programming language across all files
        in a given path. This function sets multiple attributes in the process:
            1) self.files - A list of all files present in the directory and
            any subdirectories. Filtered files are not in the list.
            2) self.files_by_language - For each language present, a list of
            all files for each language.
            3) self.language - The dominant language across all files.
            4) self.all_languages - A list of all languages across all files.

        Parameters
        ----------
        path : str
            The path to walk through. For example, "/home/user/source_code".

        Returns
        -------
        """
        self.files = self._recursively_get_files_in_path(path)
        self.files_by_language = self._breakdown_by_language()
        self.language = self._determine_dominant_language()
        self.all_languages = self._determine_all_languages()

    def _recursively_get_files_in_path(self, path: str):
        """
        Use os.walk to recurse through a path and return a list of files.
        Filters out files from any directory in FILTERED_DIRS. If no files
        are returned, an IOError exception is raised.

        Parameters
        ----------
        path : str
            The filepath to walk through.

        Returns
        -------
        list : str
            A list of filenames from the filtered path.
        """
        files = []
        for _dirpath, dirnames, filenames in walk(path):
            # First, remove any filtered directories.
            for dir_to_filter in FILTERED_DIRS:
                if dir_to_filter in dirnames:
                    dirnames.remove(dir_to_filter)

            files.extend(filenames)

        if files == []:
            raise IOError("No files in {}. Is it a valid directory?"
                          .format(path))

        return files

    def _breakdown_by_language(self):
        """
        Breaks self.files down by language.

        Parameters
        ----------

        Returns
        -------
        dict
            A dict that maps language to a list of files for that language.
            e.g.
            {
                "python": ['file1.py', 'file2.py', 'file3.py'],
                "javascript": ['blah.js', 'blorp.js'],
                "typscript": ['something.ts']
            }
        """
        return {}

    def _determine_dominant_language(self):
        """
        Looks at self.files_by_language and determines the dominant language.

        Parameters
        ----------

        Returns
        -------
        str
            The dominant language among all source code files.
        """
        return ""

    def _determine_all_languages(self):
        """
        Looks at self.files_by_language and determines all languages.

        Parameters
        ----------

        Returns
        -------
        list
            A list of all languages present among all source code files.
        """
        return []
