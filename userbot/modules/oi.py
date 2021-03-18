from time import sleep
from userbot.events import register


@register(outgoing=True, pattern='^.oi(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Punten Abang Teteh...`")
    sleep(3)
    await typew.edit("`Permisi dulu atuh biar sopan`")
    sleep(1)
    await typew.edit("`Salken Yaa, Nyumem`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.io(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Hai Sayang...`")
    sleep(3)
    await typew.edit("`Sayang-Sayang Ai Lop Yu`")
    sleep(1)
    await typew.edit("`Udah Di Sayang Terus Dianya Ilang`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.ll(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Lahh Kok Lu Galak ... .`")
    sleep(3)
    await typew.edit("`Gua sukaa Kok`")
    sleep(1)
    await typew.edit("`Suka Kegalakan Lu, Tapi Kok Sangat Goblokkk`")
# Create by myself @localheart
