from nonebot import on_notice, NoticeSession
import time


@on_notice('group_increase')
async def _(session: NoticeSession):
    # 延迟1秒
    time.sleep(2)
    # 发送欢迎消息
    await session.send('欢迎新猫猫~')
