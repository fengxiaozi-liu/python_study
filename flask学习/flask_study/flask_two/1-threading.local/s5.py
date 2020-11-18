from threading import get_ident


class Local:
    storage = {}

    def set(self, key, value):
        ident = get_ident()
        if ident in Local.storage:
            Local.storage[ident][key] = value
        else:
            Local.storage[ident] = {key: value}

    def get(self, key):
        ident = get_ident()
        return Local.storage[ident][key]
