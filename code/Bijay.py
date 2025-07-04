hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}


# Converts a string hexadecimal number into an integer decimal
# If hexNum is not a valid hexadecimal number, returns None
def hexToDec(hexNum):
    if not isinstance(hexNum, str):
        return None

    hexNum = hex.Num.upper()
    if len(hexNum) > 3:
        return None

    decimal = 0
    power = 0

    for char in reversed(hexNum):
        if char not in hexNumbers:
            return None

        value = hexNumbers[char]
        decimal += value * (16 ** power)
        power += 1

    return decimal