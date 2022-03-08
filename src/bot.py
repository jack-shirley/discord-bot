from os import getenv
from dotenv import load_dotenv
import discord
from google_images_search import GoogleImagesSearch

def getPic(search_query: str, gis) -> str:
    _search_params = {
    'q': search_query,
    'num': 1,
    'fileType': 'jpg|gif|png',
    'rights': 'cc_publicdomain|cc_attribute|cc_sharealike|cc_noncommercial|cc_nonderived'
}
    gis.search(search_params=_search_params)
    print(gis.results()[0].url)
    return gis.results()[0].url

def run():
    """
    Load environment variables from .env

    TOKEN=
    GOOGLE_SEARCH_API_KEY=
    GOOGLE_CX_ID=
    """
    load_dotenv()
    gis = GoogleImagesSearch(getenv('GOOGLE_SEARCH_API_KEY'), getenv('GOOGLE_CX_ID'))

    client = discord.Client()

    @client.event
    async def on_ready():
        print('Logged in as {0.user}'.format(client))

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.content.startswith('$'):
            search_query = message.content.replace("$","")
            img_url = getPic(search_query, gis)
            await message.channel.send(img_url)

    client.run(getenv('TOKEN'))

if __name__ == "__main__":
    run()