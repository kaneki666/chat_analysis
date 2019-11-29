import re

def Sender(s):
    patterns = ['([\w]+):',             # First Name
        '([\w]+[\s]+[\w]+):',           # First Name + Last Name
        '([\w]+[\s]+[\w]+[\s]+[\w]+):', # First Name + Middle Name + Last Name
        '([+]\d{3} \d{4}-\d{6}):'       # Number(BD)
    ]
	pattern = '^' + '|'.join(patterns)
    result = re.match(pattern, s)
    if result:
        return True
    return False
