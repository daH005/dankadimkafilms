import discord
from discord.ext import commands
from discord_slash import SlashCommand

from googlesheet import GoogleSheet
from random import choice

import os
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv()

# Реквизиты для работы с google-таблицей
credentials = {
    "type": "service_account",
    "project_id": "dankadimkafilms",
    "private_key_id": os.environ.get('PRIVATE_KEY_ID'),
    "private_key": os.environ.get('PRIVATE_KEY').replace('\\n', '\n'),
    "client_email": "filmbot-551@dankadimkafilms.iam.gserviceaccount.com",
    "client_id": "114018269873706955026",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/filmbot-551%40dankadimkafilms.iam.gserviceaccount.com"
}

# Объект google-таблицы
gs = GoogleSheet(credentials)

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='/', intents=intents)
bot.remove_command('help')
slash = SlashCommand(bot, sync_commands=True)


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


@slash.slash(description='Случайный фильм')
async def random_film(ctx):
    await ctx.send('**Случайный фильм** - _%s_' % gs.get_random_film())


@slash.slash(description='Все фильмы')
async def all_films(ctx):
    await ctx.send('**Все фильмы:**\n' + gs.get_all_films())


@slash.slash(description='Просмотренные фильмы')
async def viewed_films(ctx):
    await ctx.send('**Просмотренные фильмы:**\n' + gs.get_viewed_films())


@slash.slash(description='Непросмотренные фильмы')
async def not_viewed_films(ctx):
    await ctx.send('**Непросмотренные фильмы:**\n' + gs.get_not_viewed_films())


@slash.slash(description='Количество всех фильмов')
async def all_films_count(ctx):
    await ctx.send('**Количество всех фильмов** - _%s_' % gs.get_all_films_count())


@slash.slash(description='Количество просмотренных фильмов')
async def viewed_films_count(ctx):
    await ctx.send('**Количество просмотренных фильмов** - _%s_' % gs.get_viewed_films_count())


@slash.slash(description='Количество непросмотренных фильмов')
async def not_viewed_films_count(ctx):
    await ctx.send('**Количество непросмотренных фильмов** - _%s_' % gs.get_not_viewed_films_count())


@slash.slash(description='Орёл или решка')
async def heads_or_tails(ctx):
    await ctx.send(choice(['Орёл', 'Решка']))


@slash.slash(description='Доступные команды')
async def help(ctx):
    await ctx.send('**Доступные команды:**\n \
/random_film - Случайный фильм\n \
/all_films - Список всех фильмов\n \
/viewed_films - Список просмотренных фильмов\n \
/not_viewed_films - Список непросмотренных фильмов\n \
/all_films_count - Количество всех фильмов\n \
/viewed_films_count - Количество просмотренных фильмов\n \
/not_viewed_films_count - Количество непросмотренных фильмов\n \
/heads_or_tails - Орёл или решка')    


if __name__ == '__main__':
    bot.run(os.environ.get('BOT_TOKEN'))