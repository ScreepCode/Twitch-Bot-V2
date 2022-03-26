from libs.modules import start_clash
import os


def callables():
    return ["coc", "clashofcode"]


def coc_cmd(user, message):
    response = start_clash("3897442", os.environ.get("COC_Rememberme_Cookie"))
    status = response[0]
    link = response[1]
    if status == "new":
        return f"Der Raum ist unter {link} nun erreichbar ^^"
    elif status == "old":
        return f"Es besteht bereits ein Raum({link})"
