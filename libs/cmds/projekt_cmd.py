from libs.data import get_relevant_information


def callables():
    return ["projekt", "project"]


def projekt_cmd(user, message):
    json_data = get_relevant_information("project")
    text = json_data["text"]
    link = json_data["link"]
    link_text = json_data["link-text"]

    return f"{text} {link_text} {link}" if link != "" else text
