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

    def determine_language(self, path):
        """
        Determines the dominant programming language across all files
        in a given path. This function sets multiple attributes in the process:
            1) self.files - A list of all files present in the directory and
            any subdirectories. Filtered files are not in the list.
            2) self.language - The dominant language across all files.
            3) self.files_by_language - For each language present, a list of
            all files for each language.
            4) self.all_languages - A list of all languages across all files.
        """
        self.files = self._recursively_get_files_in_path(path)

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

    def _eval_file_extensions(self):
        """ Counts the extensions of each file in self.files """
        return
