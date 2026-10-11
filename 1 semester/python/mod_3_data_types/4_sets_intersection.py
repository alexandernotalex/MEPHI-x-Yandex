def sets_intersection(*sets):
    for s in sets:
        if not isinstance(s, set):
            raise TypeError("All arguments must be of type set")

    if len(sets) == 0:
        return set()
    if len(sets) == 1:
        return sets[0].copy()

    result = sets[0].copy()
    for s in sets[1:]:
        result &= s
    return result