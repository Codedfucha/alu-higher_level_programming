#!/usr/bin/python3
"""
This script takes GitHub credentials (username and personal access token),
uses the GitHub API to display the user ID.

Usage:
    ./10-my_github.py <username> <personal_access_token>

Arguments:
    <username> : GitHub username.
    <personal_access_token> : GitHub personal access token (for Basic Authentication).

Dependencies:
    - requests: For sending HTTP requests.
    - sys: For handling command-line arguments.

Example:
    $ ./10-my_github.py your_username your_personal_access_token
    12345678
"""

import sys
import requests
from requests.auth import HTTPBasicAuth

def main():
    """Main function to fetch and display GitHub user ID."""
    if len(sys.argv) != 3:
        print("Usage: ./10-my_github.py <username> <personal_access_token>")
        return

    username = sys.argv[1]
    token = sys.argv[2]
    
    url = "https://api.github.com/user"
    response = requests.get(url, auth=HTTPBasicAuth(username, token))

    if response.status_code == 200:
        user_data = response.json()
        print(user_data.get('id'))
    else:
        print(None)

if __name__ == "__main__":
    main()
