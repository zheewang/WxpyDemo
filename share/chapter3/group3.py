from wxpy import *

bot = Bot(cache_path=True)

# 获取目标群
group = bot.groups().search("网银监控报警")

jiankong = ensure_one(group)

members = jiankong.members

for member in members:
    print(member)

# print("群主：")
print(jiankong.owner)

# print("是否群主：" + jiankong.is_owner)
