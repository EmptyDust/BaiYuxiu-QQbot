from nonebot import on_command, CommandSession


@on_command('weather', aliases=('天气', '天气预报', '查天气'))
async def weather(session: CommandSession):
    city = session.current_arg_text.strip()
    if not city:
        city = (await session.aget(prompt='你想查询哪个城市的天气呢？')).strip()
        # 如果用户只发送空白符，则继续询问
        while not city:
            city = (await session.aget(prompt='要查询的城市名称不能为空呢，请重新输入')).strip()
    weather_report = await get_weather_of_city(city)
    await session.send(weather_report)


async def get_weather_of_city(city: str) -> str:
    return f'{city}的天气是，我不知道，长大后再学习。'
