CONVERSIONS = {
    "1": ("km to miles", lambda x: x * 0.621371),
    "2": ("miles to km", lambda x: x / 0.621371),
    "3": ("kg to lb", lambda x: x * 2.20462),
    "4": ("lb to kg", lambda x: x / 2.20462),
    "5": ("C to F", lambda x: x * 9 / 5 + 32),
    "6": ("F to C", lambda x: (x - 32) * 5 / 9),
}

def main():
    for k, (name, _) in CONVERSIONS.items():
        print(f"{k}. {name}")
    c = input("Choose: ")
    if c not in CONVERSIONS:
        print("Invalid choice.")
        return
    value = float(input("Value: "))
    name, fn = CONVERSIONS[c]
    print(f"{value} ({name}) = {fn(value):.2f}")

if __name__ == "__main__":
    main()
