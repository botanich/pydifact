# -*- coding: utf-8 -*-

import string

alphabetic_char_set = set(string.ascii_letters).union({
    ".", ",", "-", "(", ")", "/", "=", "'", "+", ":", "?", "!", '"', "%", "&", "*", ";", "<", ">", " "})
numeric_char_set = set(string.digits).union({".", ","})
alphanumeric_char_set = set(alphabetic_char_set).union(numeric_char_set)
