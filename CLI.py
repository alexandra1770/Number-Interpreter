from phone_logic import get_number, check_phone, find_interpretations, check_input

def main():
    print("Welcome to Number Interpreter")

    while True:
        text = input("\n Enter number (or 'exit'): ").strip()

        if text.lower() == "exit":
            print("Bye!")
            break
        if not check_input(text):
            print("Invalid inpuit. Use groups of 1 to 3 digits.")
            continue

        number = get_number(text)
        results = find_interpretations(text)

        print("\n Recognized number:", number)
        print("Total interpretations:", len(results))

        for result in results:
            status = "VALID" if check_phone(result) else "INVALID"
            print(result, "-", status)
if __name__ == "__main__":
    main()


