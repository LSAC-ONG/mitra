# Mitra

[![Build Status](https://i.imgur.com/MIVBYbA.png)](https://i.imgur.com/MIVBYbA.png)

### Discord bot for automated online team building activities, aiming to improve interaction between members in a friendly manner.

#
#
#
#
#

#### An open source discord bot developed using discord.py

### Chapters
- ##### Setting up
- ##### Commands & usage

## Features

-  ##### Random speed dating with your team
-  ##### Random matchups of teams for many games

# Setting up
##### Simply use this link to add Mitra to your server:

https://discord.com/api/oauth2/authorize?client_id=815122501276663817&permissions=8&scope=bot



# Commands and usage
Mitra commands listen to the "!mitra" key at the beggining of your message
Mitra features 3 sets of commands grouped this way:
#### Info commands:
- ##### !mitra help --- displays the list of available commands
- ##### !mitra status --- displays the status of the bot(selected game and channel connected to)
- ##### !mitra list --- lists the available games

#### Setup and play:
- ##### !mitra init --- connects Mitra to the voice channel you are in
- ##### !mitra game name_of_game --- tells Mitra that you are going to play name_of_game
- ##### !mitra start --- Mitra will start the selected game for you

#### Cleaning up and closing:
- ##### !mitra reset --- mitra will clear the voice/text channels it created.
##### !!WARNING!! Mitra will not delete the channels created in previous sessions, so use this command before disconnecting it via GUI admin rights or the disconnect command
#
- ##### !mitra disconnect --- disconnect Mitra from your voice channel
#### Special command:
- ##### !mitra joke --- Mitra writes a random joke