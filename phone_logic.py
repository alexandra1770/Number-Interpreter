def get_number(text):
    parts = text.split()
    number = "".join(parts)
    return number

def check_phone(number):
    if len(number) == 10:
        if number.startswith("2") or number.startswith("69"):
            return True

    if len(number) == 14:
        if number.startswith("00302") or number.startswith("003069"):
            return True

    return False

def get_options(number):
    options = [number]

    if len(number) == 2 and number[0] in "23456789" and number[1] != "0":
        options.append(number[0] + "0" + number [1])

    if len(number) == 3 and number[1] == "0" and  number[2] != "0":
        options.append(number[0] + number[2])
    return options

def find_interpretations(text):
    parts= text.split()
    results = []

    def generate(index, number):
        if index == len(parts):
            results.append(number)
            return
        part= parts[index]

        for option in get_options(part):
            generate( index + 1, number + option)
        if index +1 < len(parts):
            next_part =parts[index + 1]

            zeros = len(part) - len(part.rstrip("0"))

            if zeros > 0 and int(part) > 20:
                if len(next_part) <= zeros and int(next_part) < 10 ** zeros:
                    combined = str(int(part) + int(next_part))
                    generate(index +2, number + combined)
    generate(0, "")
    return list(dict.fromkeys(results))

def check_input(text):
    parts = text.split()

    if not parts:
        return False
    for part in parts:
        if not part.isdigit() or len(part) > 3:
            return False
    return True


