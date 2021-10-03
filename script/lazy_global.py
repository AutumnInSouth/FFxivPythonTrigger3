def _re():
    if "re" not in globals():
        globals()['re'] = __import__('re')
_re()
re.match(r"1","1")
