from nonebot import on_command, CommandSession


@on_command('info')
async def weather(session: CommandSession):
    await session.send("github:https://github.com/EmptyDust/BaiYuxiu-QQbot")
