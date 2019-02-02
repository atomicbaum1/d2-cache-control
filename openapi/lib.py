"""Library functions"""

import re

# Thanks to https://stackoverflow.com/questions/1175208/elegant-python-function-to-convert-camelcase-to-snake-case
first_cap_re = re.compile(r'(.)([A-Z][a-z]+)')
all_cap_re = re.compile(r'([a-z0-9])([A-Z])')


def py_case_convert(name):
    s1 = first_cap_re.sub(r'\1_\2', name)
    return all_cap_re.sub(r'\1_\2', s1).lower()
