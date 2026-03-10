import re

def extract_emails():
    # Ensure you have a file named 'data.txt' in the same folder
    try:
        with open("data.txt", "r") as file:
            content = file.read()
        
        # Regex to find email addresses
        emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', content)

        with open("extracted_emails.txt", "w") as output:
            for email in emails:
                output.write(email + "\n")
        
        print(f"Success! {len(emails)} emails extracted to extracted_emails.txt")
    except FileNotFoundError:
        print("Error: Please create a 'data.txt' file first.")

extract_emails()