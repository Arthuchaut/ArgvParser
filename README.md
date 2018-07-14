# ArgvParser

ArgvParser allows to format an argument vector in a structure easier to read and use for command line applications.

### Installation

    pip install argvparser
    
### Importation

    import argvparser
    
### Documentation

**ArgvParser.parse**

Formate arguments vector to a dictionnary

:param argv: The arguments vector
:type argv: list

:return: The formated arguments
:rtype: dict

:raise Exception: Argument assigned to any option

:Example:

*Parsing with several concatenated options*

    >>> self.parse(['app.py', 'ls', '-lar', '42', '--float', '3.14'])
    {
        'app': 'app',
        'command': 'ls',
        'options': {
            '-l': None,
            '-a': None,
            '-r': 42,
            '--float': 3.14
        }
    }

*Parsing without command specified*

    >>> self.parse(['app.py', '--print', 'My message I want to print', '-i'])
    {
        'app': 'app',
        'command': None,
        'options': {
            '--print': 'My message I want to print',
            '-i': None
        }
    }
    
*Parsing with duplicated options*
    
    >>> self.parse(['app.py', '-v', '/var/www', '-i', '-v', '/var/bin/bash'])
    {
        'app': 'app',
        'command': None,
        'options': {
            '-v': [
                '/var/www',
                '/var/bin/bash'
            ],
            '-i': None
        }
    }

**ArgvParser.parse_multi_options**

Retrieves multiple argument (like -li) and reconstruct it to a correct format

:param argv: The arguments vector
:type argv: list

:return: Correctly formated arguments vector
:rtype: list

:Example:

    >>> self.parse_multi_options(['app.py', '-liar', '--test'])
    ['app.py', '-l', '-i', '-a', '-r', '--test']

**ArgvParser.is_option**

Check if the argument in parameter is an option or not

:param arg: The argument to control
:type arg: str

:return: True if arg is an option, else false
:rtype: bool

:Example:

    >>> self.is_option('-t')
    True

    >>> self.is_option('--test')
    True

    >>> self.is_option('test')
    False

**ArgvParser.parse_type**

Convert the passed argument into the appropriate type

:param arg: The argument to convert
:type arg: str, None

:return: The converted argument
:rtype: int, float, str, None

:note: The default type returned is a str

:Example:

    >>> self.parse_type('test')
    'test'

    >>> self.parse_type('42')
    42

    >>> self.parse_type('3.14')
    3.14