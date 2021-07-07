from time import sleep
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.sadboy(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`Pertama-tama kamu cantik`")
    sleep(2)
    await typew.edit("`Kedua kamu manis`")
    sleep(1)
    await typew.edit("`Dan yang terakhir adalah kamu bukan jodohku`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.punten(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`\n┻┳|―-∩`"
                     "`\n┳┻|     ヽ`"
                     "`\n┻┳|    ● |`"
                     "`\n┳┻|▼) _ノ`"
                     "`\n┻┳|￣  )`"
                     "`\n┳ﾐ(￣ ／`"
                     "`\n┻┳T￣|`"
                     "\n**Permisi Aku mau nimbrung Kk..**")


@register(outgoing=True, pattern='^.efr(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**MAJUJ JELEK🤪**")
    sleep(1)
    await typew.edit("**MICIN APALAGI🤪**")
    sleep(2)
    await typew.edit("**ONET STRESS😁**")
    sleep(2)
    await typew.edit("**BALE PEDOFIL😱**")
    sleep(2)
    await typew.edit("**ABEL CANTIK**")
    sleep(2)
    await typew.edit("**GITA JUGA**")
    sleep(2)
    await typew.edit("**SYILA APALAGI**")
    sleep(2)
    await typew.edit("**NAFLA JUGA**")
    sleep(3)
    await typew.edit("**TAPI BOONG YAHAHA WAGYU!**")
    sleep(3)
    await typew.edit("**GALE DOANG YANG GANTENG😎**")

# Create by myself @localheart

CMD_HELP.update({
    "gbot":
    "`.gbot`\
    \nUsage: menampilkan alive bot.\
    \n\n`.sadboy`\
    \nUsage: hiks\
    \n\n`.punten` ; `.efr`\
    \nUsage: misi."
})
