from wxpy import *

bot = Bot(cache_path=True)

# 确定获取唯一的好友
friend = bot.friends().search("黄伟杰")

weijie = ensure_one(friend)

weijie.send('hello world')
