# Twitch-Bot-V2

[![GitHub last commit](https://img.shields.io/github/last-commit/ScreepCode/Twitch-Bot-V2?logo=github)](https://github.com/ScreepCode/Twitch-Bot-V2/)

## About Twitch-Bot-V2

This Project is a Twitch Bot based on [irc.bot](https://github.com/jaraco/irc).
It is a multifunctional Bot with following features:
- Greeting user
- Show information after command: (discord/prime/project/support/streamplan)
- Write information for viewers at random times
- Comands for creating rooms and share links for [Clash of Code from CodinGame](https://www.codingame.com/multiplayer/clashofcode) 

... and it is easy extensible!

## Pre requisites

[![GitHub top language](https://img.shields.io/github/languages/top/ScreepCode/Twitch-Bot-V2?label=Python&logo=Python)](https://github.com/ScreepCode/Twitch-Bot-V2/) [![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/ScreepCode/Twitch-Bot-V2?logo=github&color=teal)](https://github.com/ScreepCode/Twitch-Bot-V2/)

## How to run?

Fill out libs/data/data.json with commands and data.
Example: 
```
"support": {
        "text": "You like my content and want to support me? Then you can leave a small donation via LINK ^^",
        "link": "https://streamelements.com/screepcode/tip"
},
```

It needs a name (e.g. support) and content needed for the command (e.g: text and link)
For the "random lines" it needs a ``text`` or a reference with ``cmd`` to an specific command.

You need to setup following enviroment variables:
- Twitch_Client_ID
- Twitch_Token
- COC_Rememberme_Cookie (advanced, used for Clash of Code Extension)

Install required packages with ```pip install -r ./requirements.txt```

Replace name and channel in ``bot.py``

## How to use?

When the Bot is invited to a server, you can use following commands:

- General commands
    - "hi", "hello", "hallo" -> Greeting the user
    - "prime", "twitchprime" -> Twitch Prime Annoncement
    - "support", "spende", "tip" -> Tipping Text
    - "projekt", "project" -> Shows project text
    - "dc", "discord" -> Discord invite Link

- Clash of Code - Can still lead to errors!
    - "coc", "clashofcode" -> Creating a Clash of Code Lobby
    - "coc-link", "link" -> Spreading the Clash of Code Link in Chat


## Author
### [Niklas Buse](https://github.com/ScreepCode) [![GitHub followers](https://img.shields.io/github/followers/ScreepCode.svg?label=Follow%20@ScreepCode&style=social)](https://github.com/ScreepCode/)

Feel free to reach out to me via email. Shoot your doubts at [mail@niklas-buse.de](mailto:mail@niklas-buse.de?Subject=Twitch-Bot-V2).

> Glad to see you here! **Show some ❤️ by starring [this](https://github.com/ScreepCode/Twitch-Bot-V2/) repository.**
