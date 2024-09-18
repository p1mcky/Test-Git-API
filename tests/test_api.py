import os
import requests
from dotenv import load_dotenv


load_dotenv()

TOKEN = os.getenv("GITHUB_TOKEN")
USERNAME = os.getenv("GITHUB_USERNAME")
REPO_NAME = "test-api"

headers = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github+json"
}


def create_repo():
    url = "https://api.github.com/user/repos"
    data = {'name': REPO_NAME}
    response = requests.post(url, headers=headers, json=data)
    assert response.status_code == 201, f"Error creating repository: {response.content}"
    print(f"Repository '{REPO_NAME}' created successfully!")


def check_repo_exists():
    url = f"https://api.github.com/users/{USERNAME}/repos"
    response = requests.get(url, headers=headers)
    assert response.status_code == 200, f"Error fetching repositories: {response.content}"
    repo_names = [repo['name'] for repo in response.json()]
    assert REPO_NAME in repo_names, f"Repository '{REPO_NAME}' does not exist."
    print(f"Repository '{REPO_NAME}' exists!")


def delete_repo():
    url = f"https://api.github.com/repos/{USERNAME}/{REPO_NAME}"
    response = requests.delete(url, headers=headers)
    assert response.status_code == 204, f"Error deleting repository: {response.content}"
    print(f"Repository '{REPO_NAME}' deleted successfully!")


if __name__ == "__main__":
    create_repo()
    check_repo_exists()
    delete_repo()
