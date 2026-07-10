def generate_report(password, entropy, attempts, cracked):
    report = f"""
PASSWORD AUDIT REPORT
----------------------
Password: {password}
Entropy: {entropy}
Attempts: {attempts}
Status: {"WEAK (Cracked)" if cracked else "STRONG"}

Recommendation:
- Use 12+ characters
- Add symbols and uppercase
- Avoid personal info
"""

    with open("report.txt", "w") as f:
        f.write(report)
