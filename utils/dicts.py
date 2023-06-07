def get_val(collection, key, default='git'):
    value_ = collection.get(key)
    if value_ is not None:
        return value_
    else:
        return default
