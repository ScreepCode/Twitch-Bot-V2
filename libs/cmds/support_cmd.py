from libs.data import get_relevant_information


def callables():
    return ["support", "spende", "tip"]


def support_cmd(user, message):
    json_data = get_relevant_information("support")
    text = json_data["text"]
    link = json_data["link"]

    return text.replace("LINK", link)
