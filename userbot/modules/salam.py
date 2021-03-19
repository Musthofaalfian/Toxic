from time import sleep
from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern='^kntl(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**LU KONTOL**")
    sleep(3)
    await typew.edit("`KONTOL KONTOL KONTOL!!!`")
    sleep(3)
    await typew.edit("`DASAR LU KEPALA KONTOLL!!!`")
# Owner @Si_Dian


@register(outgoing=True, pattern='^G(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**JAKA SEMBUNG BAWA PISTOL**")
    sleep(3)
    await typew.edit("`NIMBRUNG LAH KONTOLLL!!!`")
# Owner @Si_Dian


@register(outgoing=True, pattern='^.g(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**JAKA SEMBUNG BAWA GOLOK**")
    sleep(3)
    await typew.edit("`NIMBRUNG ATUH BLOKK!!!`")
# Owner @Si_Dian


@register(outgoing=True, pattern='^Pe(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**Hallo, Gue {DEFAULTUSER} Salken**")
    sleep(2)
    await typew.edit("`ASSALAMU 'ALAIKUM Dulu Yakan.....`")
# Owner @Si_Dian


@register(outgoing=True, pattern='^p(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**Hallo Guys, {DEFAULTUSER} Masih Disini**")
    sleep(2)
    await typew.edit("`ASSALAMU 'ALAIKUM Ganteng.....`")
# Owner @Si_Dian


@register(outgoing=True, pattern='^L(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`Astaghfirulloh kok anda berdosa sekali...`")
    sleep(2)
    await typew.edit("`Wa'allaikumsalam Sayang......`")
# Owner @Si_Dian


@register(outgoing=True, pattern='^l(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`Astaghfirulloh anda berdosal sekali Yah...`")
    sleep(1)
    await typew.edit("`وَعَلَيْكُمُ السَّلاَمُ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ`")
# Owner @Si_Dian


CMD_HELP.update({
    "salam":
    "`P`\
\nUsage: Untuk Memberi Hujatan.\
\n\n`L`\
\nUsage: Untuk Menjawab Salam."
})
