import re

def renombrar(name):
    name = re.sub(r'[<>:"/\"|?*+]','', name)
    return name