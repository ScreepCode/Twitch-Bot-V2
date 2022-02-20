from irc.bot import SingleServerIRCBot
import os

import command_manager
import random_lines

BOT_NAME = "screepcodebot"
CHANNEL = "screepcode"


class Bot(SingleServerIRCBot):
    def __init__(self):
        self.HOST = "irc.chat.twitch.tv"
        self.PORT = 6667
        self.USERNAME = BOT_NAME.lower()
        self.CLIENT_ID = os.environ.get("Twitch_Client_ID")
        self.TOKEN = os.environ.get("Twitch_Token")
        self.CHANNEL = f"#{CHANNEL}"

        super().__init__([(self.HOST, self.PORT, f"oauth:{self.TOKEN}")], self.USERNAME, self.USERNAME)

        self.CommandManager = command_manager.CommandManager()
        self.CommandManager.get_all_callables()
        self.RandomLines = random_lines.RandomLines(self)

    def send_message(self, message: str):
        self.connection.privmsg(self.CHANNEL, message)

    def on_welcome(self, cxn, event):
        for req in ("membership", "tags", "commands"):
            cxn.cap("REQ", f":twitch.tv/{req}")

        cxn.join(self.CHANNEL)
        self.send_message("Now online.")
        print("Now online")

    def on_pubmsg(self, cxn, event):
        print(event)
        self.RandomLines.increment()

        tags = {kvpair["key"]: kvpair["value"] for kvpair in event.tags}
        user = {"name": tags["display-name"], "id": tags["user-id"]}
        message: str = event.arguments[0]

        if user["name"] != self.USERNAME:
            if message.startswith("!"):
                response = self.CommandManager.process_cmd(user, message[1:])
                if response is not None:
                    self.send_message(response)
