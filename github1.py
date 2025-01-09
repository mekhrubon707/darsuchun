# Faylni Python kodini yozib yaratish
from github import Github

def upload_readme_to_github(token, repo_name, file_path):
    g = Github(token)
    user = g.get_user()
    repo = user.create_repo(repo_name)  # Yangi repo yaratish
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    repo.create_file("README.md", "README fayli qo'shildi", content)
    print(f"README.md fayli yuklandi: https://github.com/{user.login}/{repo_name}")

token = "github_tokeningizni_bu_yerga_joylang"
repo_name = "usernameingiz"
file_path = "README.md"  # README faylingiz manzili

upload_readme_to_github(token, repo_name, file_path)
