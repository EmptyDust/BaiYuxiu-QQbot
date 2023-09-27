from nonebot.command import CommandSession
from nonebot.experimental.plugin import on_command
from aiocqhttp.message import MessageSegment
import aiohttp
import json

__plugin_name__ = '在线'
__plugin_usage__ = '用法： 对我说 "ping"，我会回复 "pong!"'


@on_command('猫猫图', aliases=('猫', '猫猫', '猫图'))
async def _(session: CommandSession):
    async with aiohttp.request(
            "GET", "https://api.thecatapi.com/v1/images/search"
    ) as resp:
        json_str = await resp.text()
    if resp.status != 200:
        await session.send('网络错误')
    else:
        doc = json.loads(json_str)
        url = doc[0]['url']
        await session.send(MessageSegment.image(url))
