# Discord Google Image Search

A simple Discord Bot that retrieves the first image from a Google image search query. 

## Prerequisites

- Python 3

## Setup

Rename config-sample.ini to config.ini and fill in the following:

- ***TOKEN*** : Discord bot token
    - More information at https://discord.com/developers/docs/intro
- ***GOOGLE_SEARCH_API_KEY***: Google custom search API key
    - More information at https://console.cloud.google.com/apis
- ***GOOGLE_CX_ID*** : Google custom search engine ID
    - More information at https://programmablesearchengine.google.com

#### Python Virtual Environment Setup

If you would not like to clutter your computer with a lot of random libraries, use this:

```bash
python -m virtualenv .venv/ && ./.venv/Scripts/activate && pip install -r requirements.txt
```

#### Run the Bot

```bash
python src/bot.py
```


### Authors

- Jack Shirley / www.github.com/jack-shirley
