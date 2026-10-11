import string

def is_valid_ipv6(addr: str) -> bool:
    """Проверяет валидность IPv6-адреса."""
    if not isinstance(addr, str):
        return False
    s = addr.strip()
    if s == "":
        return False

    # запретим встраивание IPv4 (точки) — задача не учитывает mixed формы
    if "." in s:
        return False

    # не более одного :: разрешено
    if s.count("::") > 1:
        return False

    hexdigits = set(string.hexdigits)

    def valid_group(g: str) -> bool:
        if not (1 <= len(g) <= 4):
            return False
        return all(ch in hexdigits for ch in g)

    if "::" in s:
        left, right = s.split("::")
        left_groups = left.split(":") if left != "" else []
        right_groups = right.split(":") if right != "" else []

        # никаких пустых групп (кроме эффекта ::)
        if "" in left_groups or "" in right_groups:
            return False

        total_groups = len(left_groups) + len(right_groups)
        # :: заменяет хотя бы одну группу, поэтому суммарно не должно быть >7
        if total_groups > 7:
            return False

        for g in left_groups + right_groups:
            if not valid_group(g):
                return False

        return True
    else:
        groups = s.split(":")
        # без :: должно быть ровно 8 групп
        if len(groups) != 8:
            return False
        if "" in groups:
            return False
        for g in groups:
            if not valid_group(g):
                return False
        return True
