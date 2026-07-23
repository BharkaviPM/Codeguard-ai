import requests

BASE_URL = "http://127.0.0.1:8000/api/v1"


def _handle_response(response):

    try:
        response.raise_for_status()
    except requests.HTTPError:

        print("=" * 60)
        print("REQUEST URL :", response.request.url)
        print("STATUS      :", response.status_code)
        print("RESPONSE    :", response.text)
        print("=" * 60)

        raise

    return response.json()


# --------------------------------------------------
# Upload
# --------------------------------------------------

def upload_project(file):

    files = {
        "file": (
            file.name,
            file,
            file.type or "application/octet-stream",
        )
    }

    response = requests.post(
        f"{BASE_URL}/upload/file",
        files=files,
        timeout=120,
    )

    return _handle_response(response)


# --------------------------------------------------
# Projects
# --------------------------------------------------

def get_projects():

    response = requests.get(
        f"{BASE_URL}/projects",
        timeout=30,
    )

    return _handle_response(response)


def get_project(project_id):

    response = requests.get(
        f"{BASE_URL}/projects/{project_id}",
        timeout=30,
    )

    return _handle_response(response)


def delete_project(project_id):

    response = requests.delete(
        f"{BASE_URL}/projects/{project_id}",
        timeout=30,
    )

    return _handle_response(response)


# --------------------------------------------------
# Files
# --------------------------------------------------

def get_project_files(project_id):

    response = requests.get(
        f"{BASE_URL}/projects/{project_id}/files",
        timeout=30,
    )

    return _handle_response(response)


# --------------------------------------------------
# Results
# --------------------------------------------------

def get_results(project_id):

    response = requests.get(
        f"{BASE_URL}/results/{project_id}",
        timeout=30,
    )

    return _handle_response(response)


def get_summary(project_id):

    response = requests.get(
        f"{BASE_URL}/summary/{project_id}",
        timeout=30,
    )

    return _handle_response(response)


# --------------------------------------------------
# Chat
# --------------------------------------------------

def ask_chat(question, project_id=None):

    payload = {
        "question": question
    }

    if project_id:
        payload["project_id"] = project_id

    response = requests.post(
        f"{BASE_URL}/chat",
        json=payload,
        timeout=120,
    )

    return _handle_response(response)