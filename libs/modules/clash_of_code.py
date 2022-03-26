import requests
from libs.data import update_json, get_relevant_information


def find_clash_by_handel(public_handle):
    request_url = "https://www.codingame.com/services/ClashOfCode/findClashByHandle"
    r = requests.post(url=request_url, json=[public_handle])
    return r.json()


def is_last_clash_finished(public_handle):
    last_clash = find_clash_by_handel(public_handle)
    return last_clash["finished"]


def is_last_clash_running(public_handle):
    last_clash = find_clash_by_handel(public_handle)
    return last_clash["started"]


def check_start(public_handle):
    if public_handle != "":
        if is_last_clash_finished(public_handle):  # Wenn beendet, darf starten
            update_json("clash-of-code", {"last-clash": ""})
            return True
        else:
            if is_last_clash_running(public_handle) is False:  # Wenn nicht am Laufen, darf starten
                return False
            else:
                return True  # Darf nicht starten, wenn nicht beide bedingungen richtig sind
    else:
        return True


def start_clash(gamer_id, remember_me_cookie, modes=['FASTEST', 'SHORTEST', 'REVERSE'], languages=[]):
    last_clash_handle = get_relevant_information("clash-of-code")["last-clash"]
    if check_start(last_clash_handle):
        request_url = "https://www.codingame.com/services/ClashOfCode/createPrivateClash"
        json_data = [gamer_id, languages, modes]

        r = requests.post(request_url, cookies={"rememberMe": remember_me_cookie}, json=json_data)
        update_json("clash-of-code", {"last-clash": r.json()["publicHandle"]})
        return ["new", "https://www.codingame.com/clashofcode/clash/" + r.json()["publicHandle"]]
    else:
        return ["old", "https://www.codingame.com/clashofcode/clash/" + last_clash_handle]
