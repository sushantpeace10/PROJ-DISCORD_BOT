# MACHO BOT
## A simple Discord BOT

A discord bot that fetches meme form explore feed from an exsisting instagram account.

## Requirements

```sh
import instaloader
import json
import lzma
import emoji
import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from flask import Flask
from threading  import Thread
```

## Features

- `.mc meme` Gets Fresh and trendy memes.
- `.mc clear` Clear all messages in a channel.
- `.mc clean <value>` or give a value to delete that much.
- `.mc hangman` play hangman game.
