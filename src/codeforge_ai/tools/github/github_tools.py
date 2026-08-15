import httpx
from langchain_core.tools import tool
import base64

GITHUB_API_BASE = "https://api.github.com"


@tool
def get_repository_info(owner: str, repo: str) -> dict:
    """
    Get basic information about a public GitHub repository.

    Args:
        owner: GitHub username or organization name.
        repo: Repository name.

    Returns:
        Repository metadata from GitHub.
    """

    url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}"

    response = httpx.get(
        url,
        headers={
            "Accept": "application/vnd.github+json",
        },
        timeout=10.0,
    )

    response.raise_for_status()

    data = response.json()

    return {
        "name": data["name"],
        "full_name": data["full_name"],
        "description": data["description"],
        "language": data["language"],
        "stars": data["stargazers_count"],
        "forks": data["forks_count"],
        "open_issues": data["open_issues_count"],
        "default_branch": data["default_branch"],
        "created_at": data["created_at"],
        "updated_at": data["updated_at"],
        "html_url": data["html_url"],
    }


@tool
def list_repository_files(owner: str, repo: str, path: str = "") -> list:
    """
    List files and directories in a GitHub repository.

    Args:
        owner: GitHub username or organization name.
        repo: Repository name.
        path: Directory path inside the repository. Empty string means root.

    Returns:
        List of files and directories.
    """

    url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}/contents/{path}"

    response = httpx.get(
        url,
        headers={
            "Accept": "application/vnd.github+json",
        },
        timeout=10.0,
    )

    response.raise_for_status()

    data = response.json()

    return [
        {
            "name": item["name"],
            "path": item["path"],
            "type": item["type"],
            "size": item.get("size", 0),
        }
        for item in data
    ]    


@tool
def read_file(owner: str, repo: str, path: str) -> str:
    """
    Read the contents of a file from a public GitHub repository.

    Args:
        owner: GitHub username or organization name.
        repo: Repository name.
        path: Path of the file inside the repository.

    Returns:
        The decoded contents of the file.
    """

    url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}/contents/{path}"

    response = httpx.get(
        url,
        headers={
            "Accept": "application/vnd.github+json",
        },
        timeout=10.0,
    )

    response.raise_for_status()

    data = response.json()

    if data.get("type") != "file":
        raise ValueError(f"{path} is not a file.")

    content = data.get("content")

    if not content:
        raise ValueError(f"No content returned for {path}.")

    decoded_content = base64.b64decode(content).decode("utf-8")

    return decoded_content

