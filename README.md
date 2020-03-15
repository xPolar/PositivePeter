
# **Positive Peter**

![Positive Peter Banner](https://cdn.discordapp.com/attachments/651676721027743754/665786771228983327/SPB.png)

Welcome to the **Positive Peter** GitHub. Positive Peter is a Discord bot created by [Polar#6969](https://discordapp.com/users/619284841187246090). This bot is designed to try and prevent suicides from occurring either by giving positive compliments or providing the resources to contact professionals. If you would like to invite the bot feel free to use [this](https://discordapp.com/api/oauth2/authorize?client_id=649535694145847301&permissions=26688&scope=bot) invite link or get help with the Positive Peter bot feel free to join our [Discord](https://discord.gg/VwMWj2B).

[![Discord Bots](https://top.gg/api/widget/649535694145847301.svg)](https://top.gg/bot/649535694145847301)

# Table of contents

- [Important Links](https://github.com/xPolar/PositivePeter#important-links)
- [How to use the Positive Peter bot](https://github.com/xPolar/PositivePeter#how-to-use-the-positive-peter-bot)
- [Command List](https://github.com/xPolar/PositivePeter#command-list)
- [Self hosting](https://github.com/xPolar/PositivePeter#self-hosting)

# Important links
- [Bot Invite Link](https://discordapp.com/api/oauth2/authorize?client_id=649535694145847301&permissions=26688&scope=bot)
- [Support Server](https://discord.gg/VwMWj2B)
- [Vote for the bot](https://top.gg/bot/649535694145847301/vote)
- [Trello](https://trello.com/b/7xd2iXJB)

# How to use the Positive Peter Bot
This bot is triggered by certain [keywords](https://github.com/xPolar/PositivePeter/wiki/Triggers), once the bot has been triggered it will respond with the appropriate response.

# Command List
| Command | Description |
| ------- | ----------- |
| help | Show a list of all the commands and information on how to use them. |
| changelog | View all the updates that have been made to the bot. |
| hug | Send a hug to someone or receive one from the bot. |
| invite | View all of the bot's relevant links. |
| ping | Show the bot's current latency. |
| suggesttrigger | Suggest a trigger to be added to the detection system. |
| triggers | View all of the words that triggers the bot. |
| config | Edit the bot's configuration settings. |

## Configuration list

| Configuration | Description |
| ------------- | ----------- |
| compliment | Disable or enable the compliment responses. |
| hotline | Set the custom hotline in the suicidal response message. |
| prefix | Set a server's custom prefix. |

# Self Hosting

## Prerequisites
For Positive Peter to function correctly you must have all the proper libraries installed as well as [Python](https://www.python.org/downloads/release/python-381/) 3.6+. A guide on how to install all of the libraries can be found below.

```
pip3 install discord.py
```
```
pip3 install motor
```
```
pip3 install dnspython
```

## Setup
After you have installed all of the prerequisites listed above you can start on setting up the bot by downloading this repository onto your PC. From there please rename the `ConfigExample.py` file to `Config.py` then open it and enter all of the proper values. If you need help with setting a value please join the [Support Server](https://discord.gg/VwMWj2B).

After you have setup the configuration file you can start the bot by doing the following while in the main file.
```
python3 Main.py
```
