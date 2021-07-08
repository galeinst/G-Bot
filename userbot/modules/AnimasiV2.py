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
    await typew.edit("**Majuj Pantek😁**")
    sleep(1)
    await typew.edit("**Micin Juga pantek😁**")
    sleep(2)
    await typew.edit("**Bale Pedofil🤥**")
    sleep(2)
    await typew.edit("**Onet Stresszz🥴**")
    sleep(2)
    await typew.edit("**Abel Jele😝**")
    sleep(2)
    await typew.edit("**Gita Juga🤪**")
    sleep(2)
    await typew.edit("**Nafla Gila😜**")
    sleep(2)
    await typew.edit("**Syilaa Batak😆**")
    sleep(3)
    await typew.edit("**GALE DOANG YANG SEMPURNA ANJAY😎!**")

# Create by myself @localheart

CMD_HELP.update({
    "AnimasiV2":
    "`.AnimasiV2`\
    \nUsage: menampilkan alive bot.\
    \n\n`.sadboy`\
    \nUsage: hiks\
    \n\n`.punten` ; `.efr`\
    \nUsage: misi."
})
