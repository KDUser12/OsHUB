from core.management.commands.special_commands import about_command, exit_command, changelog_command

commands = {
    "1": "Username",
    "2": "Email Address",
    "3": "IP Address",
    "4": "Telephone Numbers",
    "5": "Exploits",
    "6": "Archives",
    "7": "Browser",
    "8": "Transportation",
    "9": "Data Leaks",
    "10": "Phishing",
    "11": "DDoS",
    "12": "Search Engine",
    "13": "Face/Image Search Engine",
    "14": "Data Viewer",
    "15": "Social Network",
    "16": "Geolocation"
}

special_commands = {
    ":": about_command,
    "!": exit_command,
    "?": changelog_command
}