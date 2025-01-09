def create_github_readme(username, bio, technologies, projects, contact_links):
    content = f"""# Assalomu alaykum! 👋  
Men {username}man. {bio}

## Texnologiyalar:
{''.join([f"- {tech}\n" for tech in technologies])}

## Loyihalarim:
{''.join([f"- [{proj['name']}]({proj['link']})\n" for proj in projects])}

## Aloqa:
{''.join([f"- {link_type}: {link}\n" for link_type, link in contact_links.items()])}

---

Profilimga tashrif buyuring: [GitHub Profilim](https://github.com/{username})
"""
    with open("README.md", "w", encoding="utf-8") as file:
        file.write(content)

username = "mekhrubon707"
bio = "Men dasturlash qiziqaman."
technologies = ["Python 🐍", "HTML va CSS "]
projects = [
    {"name": "Portfolio Veb-sayti", "link": "https://github.com/usernameingiz/portfolio"},
    {"name": "Ob-havo Ilovasi", "link": "https://github.com/usernameingiz/weather-app"}
]

contact_links = {
    "Elektron pochta": "murodjonovmekhrubon@gmail.com"
}

create_github_readme(username, bio, technologies, projects, contact_links)
