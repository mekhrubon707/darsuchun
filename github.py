username = "usernameingiz"
bio = "Men dasturlash va texnologiyaga qiziqaman."
technologies = ["Python 🐍", "JavaScript ⚡", "HTML va CSS 🌐"]
contact_links = {
    "LinkedIn": "https://linkedin.com/in/username",
    "Elektron pochta": "username@example.com"
}

def create_github_readme(username, bio, technologies, contact_links):
    readme_content = f"""
# {username}

{bio}

## Texnologiyalar
{''.join([f"- {tech}\n" for tech in technologies])}

## Aloqa
{''.join([f"- [{key}]({value})\n" for key, value in contact_links.items()])}
"""
    with open("README.md", "w", encoding="utf-8") as file:
        file.write(readme_content)

create_github_readme(username, bio, technologies, contact_links)
