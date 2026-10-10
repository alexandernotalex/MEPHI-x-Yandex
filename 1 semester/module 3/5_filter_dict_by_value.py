def filter_dict_by_value(d, threshold):
    if not isinstance(d, dict):
        raise TypeError("d must be a dictionary")
    if not isinstance(threshold, (int, float)):
        raise TypeError("threshold must be int or float")

    result = {}
    for key, value in d.items():
        # исключаем bool (он является подклассом int) и любые другие нечисловые типы
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError("All values in dictionary must be int or float")
        if value > threshold:
            result[key] = value
    return result