def to_rna(dna):
    if not isinstance(dna, str):
        raise TypeError("Input must be a string")

    mapping = {"G": "C", "C": "G", "T": "A", "A": "U"}

    result = []
    for char in dna:
        if char not in mapping:
            raise ValueError("Недопустимый символ")
        result.append(mapping[char])

    return "".join(result)