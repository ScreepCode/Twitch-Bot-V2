from libs.data import get_relevant_information
from libs.modules import is_last_clash_finished
import os


def callables():
    return ["coc-link", "link"]


def link_cmd(user, message):
    last_clash = get_relevant_information("clash-of-code")["last-clash"]
    if is_last_clash_finished(last_clash):
        return f"Der Clash ist bereits beendet. Du kannst mit '!coc' einen neuen Raum erstellen ^^"
    else:
        return f"Der Clash of Code Link ist: https://www.codingame.com/clashofcode/clash/{last_clash}"
