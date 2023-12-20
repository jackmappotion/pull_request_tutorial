def fillna_method(obj):
    obj.fillna(method='ffill',inplace=True)
    return obj