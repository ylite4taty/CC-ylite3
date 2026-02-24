OPERATORS = {
    "Joaquim": "authorized",
    "Landira": "authorized",
    "Alice": "suspended",
    "Cipriano": "authorized",
    "Miguel": "suspendeed",
}

def check_operator_status(name: str) -> str:
    name = name.lower().strip()
    if name in OPERATORS:
        return OPERATORS[name]
    return "not found"