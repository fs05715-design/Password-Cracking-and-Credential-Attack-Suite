def simulate_dictionary_test(password, wordlist):
    attempts = 0

    for word in wordlist:
        attempts += 1
        if word == password:
            return True, attempts

    return False, attempts
