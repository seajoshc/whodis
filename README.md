# WhoDis
Parses the contents of a source code directory and determines the programming languages in use.

# Languages Supported:
* Go
* Java
* JavaScript
* Python
* Ruby

# Usage
Import the module and create a new instance of WhoDis:
```python
from whodis import WhoDis
blah = WhoDis()
```

WhoDis objects have a single method, parse(), which takes a single filepath (string) parameter:
```
blah.parse("/some/valid/path/with/source/code")
```

After parsing a valid path with at least one file in a supported language, the object will have four attributes:
```python
# language - The dominant programming language in the source path.
# String.
# Possible string values are "go", "java", "js", "py", "rb".
blah.language
>> "py"

 # all_languages - All languages present in the source path.
 # List of strings.
 # Possible list values are "go", "java", "js", "py", "rb".
blah.all_languages
>> ["rb", "js"]

# files - All non-filtered files in the source path.
# List of strings.
blah.files
>> ["__init__.py", "main.py", "README.md", "LICENSE.md", "requirements.txt"]

# files_by_language - All non-filtered files in the source path broken down by language.
# Dictionary with strings for keys and lists of strings for values.
# Possible key names are "go", "java", "js", "py", "rb".
blah.files_by_language
>> {"rb": ["application_controller.rb", "model.rb"], "js": ["app.js"]}
```
