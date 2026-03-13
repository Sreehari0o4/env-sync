import requests

GITHUB_API = "https://api.github.com/gists"


def create_gist(token, content):
    headers = {
        "Authorization": f"token {token}"
    }

    data = {
        "description": "EnvSync encrypted secrets",
        "public": False,
        "files": {
            "envsync.enc": {
                "content": content
            }
        }
    }

    response = requests.post(GITHUB_API, json=data, headers=headers)

    return response.json()

def get_gist(gist_id, token):

    url = f"https://api.github.com/gists/{gist_id}"

    headers = {
        "Authorization": f"token {token}"
    }

    response = requests.get(url, headers=headers)

    data = response.json()

    return data["files"]["envsync.enc"]["content"]

def update_gist(token, gist_id, content):

    url = f"https://api.github.com/gists/{gist_id}"

    headers = {
        "Authorization": f"token {token}"
    }

    data = {
        "files": {
            "envsync.enc": {
                "content": content
            }
        }
    }

    requests.patch(url, json=data, headers=headers)