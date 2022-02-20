from libs.data import get_relevant_information


def callables():
    return ["prime", "twitchprime"]


def prime_cmd(user, message):
    json_data = get_relevant_information("prime")
    text = json_data["text"]

    return text
