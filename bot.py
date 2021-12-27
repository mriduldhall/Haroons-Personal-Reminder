import os
import random
from datetime import datetime
from dotenv import load_dotenv
from discord.ext import commands, tasks

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
USERID1 = os.getenv('USERID1')
USERID2 = os.getenv('USERID2')
CHANNEL = os.getenv('CHANNEL')

BIOLOGY = datetime(year=2022, month=1, day=5, hour=8, minute=45)
CHEMISTRY = datetime(year=2022, month=1, day=5, hour=11, minute=5)
PHYSICS = datetime(year=2022, month=1, day=5, hour=13, minute=50)
ENGLISH_2 = datetime(year=2022, month=1, day=6, hour=8, minute=45)
MATH_1 = datetime(year=2022, month=1, day=6, hour=11, minute=5)
MATH_2 = datetime(year=2022, month=1, day=7, hour=11, minute=5)
ENGLISH_1 = datetime(year=2022, month=1, day=10, hour=8, minute=45)
EXAMS = {
    (
        "Biology Exam",
        "https://cdn.discordapp.com/attachments/924055963412090890/924056693069971476/Screen_Shot_2021-12-24_at_9.51.01_PM.png"
    ): BIOLOGY,
    (
        "Chemistry Exam",
        "https://cdn.discordapp.com/attachments/924055963412090890/924056941095948298/Screen_Shot_2021-12-24_at_9.52.05_PM.png"
    ): CHEMISTRY,
    (
        "Physics Exam",
        "https://cdn.discordapp.com/attachments/924055963412090890/924057209556594728/Screen_Shot_2021-12-24_at_9.53.10_PM.png"
    ): PHYSICS,
    (
        "English Paper 1",
        "https://cdn.discordapp.com/attachments/924055963412090890/924057396870000690/Screen_Shot_2021-12-24_at_9.53.57_PM.png"
    ): ENGLISH_1,
    (
        "Math paper 1",
        "https://cdn.discordapp.com/attachments/924055963412090890/924057593050185768/Screen_Shot_2021-12-24_at_9.54.39_PM.png"
    ): MATH_1,
    (
        "Math paper 2",
        "https://cdn.discordapp.com/attachments/924055963412090890/924057792757780500/unknown.png"
    ): MATH_2,
    (
        "English Paper 2",
        "https://cdn.discordapp.com/attachments/924055963412090890/924057938040066058/unknown.png"
    ): ENGLISH_2,
}

bot = commands.Bot(command_prefix='!')


def convert_to_hours(duration):
    hours = duration.days * 24
    hours += duration.seconds // 3600
    return hours


@tasks.loop(hours=1)
async def test():
    channel = bot.get_channel(int(CHANNEL))
    subject_data, exam_time = random.choice(list(EXAMS.items()))
    subject_name, subject_image = subject_data
    time_remaining = exam_time - datetime.now()
    hours_remaining = convert_to_hours(time_remaining)
    await channel.send(f"Hi <@{USERID1}> and <@{USERID2}>,\n"
                       f"This is your personal reminder's hourly reminder\n"
                       f"You have T-{hours_remaining} hours remaining until your {subject_name}\n"
                       f"{subject_image}")


@bot.event
async def on_ready():
    test.start()


bot.run(TOKEN)
