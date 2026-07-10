def generate_dictionary(name, dob):
    name = name.strip()
    dob = dob.strip()

    words = set()

    base_words = [
        name,
        name.lower(),
        name.upper(),
        name.capitalize(),
        dob,
        "password",
        "admin",
        "welcome",
        "letmein",
        "qwerty",
    ]

    for word in base_words:
        if word:
            words.add(word)
            words.add(word + "123")
            words.add(word + "@123")
            words.add(word + "2025")

    if name and dob:
        words.add(name + dob)
        words.add(name.capitalize() + dob)

    return sorted(words)





