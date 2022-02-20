from libs.data import get_relevant_information


def callables():
    return ["dc", "discord"]


def discord_cmd(user, message):
    json_data = get_relevant_information("discord")
    link = json_data["invite-link"]

    return f"Link zu meinem Community Discord: {link} ^^"
