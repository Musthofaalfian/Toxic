from datetime import datetime
import time
from time import sleep
from platform import uname
from userbot import ALIVE_NAME, CMD_HELP, StartTime
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["Dtk", "Mnt", "Jam", "Hari"]

    while count < 4:
        count += 1
        remainder, result = divmod(
            seconds, 60) if count < 3 else divmod(
            seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


@register(outgoing=True, pattern="^.sping$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("**γπππππππγ**")
    await pong.edit("**ββππππ ππππππππββ**")
    await pong.edit("**ππππ ππππππ πππ**")
    await pong.edit("**ππππ ππππππππ πππππ ππππππ**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"   β«Έ π±πΈπΉπΈ πΏπ΄π»π΄π π³ `%sms`"
                    f"\nβ«Έ**γπΌπ΄π»π΄π³ππΆγ** \n" % (duration))


@register(outgoing=True, pattern='^knt(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**SUSU KENTAL**")
    sleep(3)
    await typew.edit("`Kental Manis ? Itu SUSU APA KAMU!!!`")
    sleep(3)
    await typew.edit("`SUSU SAYA SUSU BENDERA!!!`")
# Owner @Si_Dian


@register(outgoing=True, pattern='^G(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**JAKA SEMBUNG BAWA GOLOK**")
    sleep(3)
    await typew.edit("`NIMBRUNG ATUH BLOKK!!!`")
# Owner @Si_Dian


@register(outgoing=True, pattern='^ass(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**γ Π½Ξ±ΞΉ Ξ±ΟΞ± ΠΊΞ±Π²Ξ±Ρ γ**")
    sleep(3)
    await typew.edit("`Ψ§ΩΨ³ΩΩΩΨ§ΩΩΩ ΨΉΩΩΩΩΩΩΩΩΩ ΩΩΨ±ΩΨ­ΩΩΩΨ©Ω Ψ§ΩΩΩΩ ΩΩΨ¨ΩΨ±ΩΩΩΨ§ΨͺΩΩΩ`")
# Owner @mixiologist


@register(outgoing=True, pattern='^wass(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**Hallo Gue {DEFAULTUSER} Salken**")
    sleep(2)
    await typew.edit("`ΩΩΨΉΩΩΩΩΩΩΩΩΩ Ψ§ΩΨ³ΩΩΩΨ§ΩΩΩ ΩΩΨ±ΩΨ­ΩΩΩΨ©Ω Ψ§ΩΩΩΩ ΩΩΨ¨ΩΨ±ΩΩΩΨ§ΨͺΩΩΩ`")
# Owner @Si_Dian


@register(outgoing=True, pattern='^.usange(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`Getting Information...`")
    sleep(1)
    await typew.edit("**Ancient Usage π©Έ**:\n\nβ­βββββββββββββββββββββ?\n" f"-> `Penggunaan Kealayan ` **{ALIVE_NAME}**:\n" f" β’**0 jam - " f"0 menit - 0%**" "\n ββββββββββββββββββββββ\n" "-> `Sisa Alay Bulan Ini`:\n" f" β’**9999 jam - 9999 menit " f"- 100%**\n" "β°βββββββββββββββββββββ―"
                     )
# @mixiologist


CMD_HELP.update({
    "fakedyno":
    "`.usange`\
\nUsage: tipu tipu anjeeeng.\
\n\n`L`\
\nUsage: Untuk Menjawab Salam."
})
