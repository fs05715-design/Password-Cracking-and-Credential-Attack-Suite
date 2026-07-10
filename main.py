from dictionary import generate_dictionary
from analyzer import check_strength
from simulator import simulate_dictionary_test
from report import generate_report

print("Password Security Toolkit")
print("--------------------------")

name = input("Enter username: ")
dob = input("Enter DOB (DDMM): ")
password = input("Enter password: ")

wordlist = generate_dictionary(name, dob)

found, attempts = simulate_dictionary_test(password, wordlist)

score, entropy = check_strength(password)

print("\n--- RESULTS ---")
print("Score:", score, "/4")
print("Entropy:", entropy)

if found:
    print("Password cracked in", attempts, "attempts")
else:
    print("Password not found in dictionary")

generate_report(password, entropy, attempts, found)

print("\nReport saved as report.txt")
