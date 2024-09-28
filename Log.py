import requests
import hashlib

def find_leaked_credentials(url, compromised_hashes):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            content = response.text
            hash_value = hashlib.sha1(content.encode()).hexdigest()
            print(f"SHA-1 hash of the website content: {hash_value}")

            # Check if the hash exists in the compromised hashes list
            if hash_value in compromised_hashes:
                print("Your account has been compromised!")
            else:
                print("Your account has not been compromised.")
        else:
            print(f"Failed to retrieve the website content. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching the website: {e}")

# List of known compromised SHA-1 hashes (replace with actual hashes)
compromised_hashes = [
    "8ba47658b7c0d9a815673b0373609e9",  # Example compromised hash
    "45c48cce2e2d7fbdea1afc51c7c6ad26"  # Another example compromised hash
]

# Prompt the user for the website URL
url = input("Enter the website URL to check for leaked credentials: ")
find_leaked_credentials(url, compromised_hashes)
