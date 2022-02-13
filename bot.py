from irc.bot import SingleServerIRCBot
import os

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

    def send_message(self, message):
        self.connection.privmsg(self.CHANNEL, message)

    def on_welcome(self, cxn, event):
        for req in ("membership", "tags", "commands"):
            cxn.cap("REQ", f":twitch.tv/{req}")

        cxn.join(self.CHANNEL)
        self.send_message("Now online.")
        print("Now online")

    def on_pubmsg(self, cxn, event):
        print(event)
        tags = {kvpair["key"]: kvpair["value"] for kvpair in event.tags}
        user = {"name": tags["display-name"], "id": tags["user-id"]}
        message = event.arguments[0]

        if user["name"] != self.USERNAME:
            # cmds.process(self, user, message.lower())
            pass