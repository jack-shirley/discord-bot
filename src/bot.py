from configparser import ConfigParser
import discord
from google_images_search import GoogleImagesSearch

def loadConfig():
    config = ConfigParser()
    config.read('../config.ini')

    Keys = {'discord_token':config.get('Discord Token', 'TOKEN'),
            'google_search_api_key':config.get('Google GCP Keys', 'GOOGLE_SEARCH_API_KEY'),
            'google_cx_id':config.get('Google GCP Keys', 'GOOGLE_CX_ID')}

    return Keys
    

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

def run(Keys):
    gis = GoogleImagesSearch(Keys['google_search_api_key'], Keys['google_cx_id'])

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

    client.run(Keys['discord_token'])

if __name__ == "__main__":
    Keys = loadConfig()
    run(Keys)