import os
import requests
from git import Repo

GITLAB_URL = "https://gitlab-new.vndirect.com.vn"
USERNAME = "security-ops"
PASSWORD = "ATTTVND@2025"
REPO_URL = "https://gitlab.com/devops/network-policy.git"
LOCAL_DIR = "network-policy"
def authenticate():
    response = requests.get(f"{GITLAB_URL}/api/v4/user", auth=(USERNAME, PASSWORD))
    if response.status_code == 200:
        print("Đăng nhập thành công!")
    else:
        print("Đăng nhập thất bại!", response.content)
        exit()

def pull_project():
    if not os.path.exists(LOCAL_DIR):
        os.makedirs(LOCAL_DIR)
    try:
        repo = Repo(LOCAL_DIR)
        repo.remotes.origin.pull()
        print("Pull project thành công!")
    except Exception as e:
        print(f"Lỗi khi pull project: {e}")

if __name__ == "__main__":
    authenticate()
    pull_project()
