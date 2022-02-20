from libs.data import get_relevant_information


def callables():
    return ["streamplan", "schedule"]


def stream_plan_cmd(user, message):
    json_data = get_relevant_information("stream-plan")
    text = json_data["text"]

    return f"{user['name']} {text}"
