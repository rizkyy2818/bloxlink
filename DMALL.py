import discord
from discord.ext import commands

# ===== GANTI INI =====
TOKEN = "MTU0NDUxNjA4ODk5MjIzOTc1Nw.G4MaJ1.96XnwUsb1I2f5iTnS73wXw49zZ5-ItaemzsFhI"

# ===== SETUP =====
bot = commands.Bot(command_prefix="+", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"✅ Bot online: {bot.user}")

@bot.command()
async def dmall(ctx, *, message=None):
    # Pesan default
    default_msg = (
        "🔐 **Verify with Bloxlink** and gain access to **Maps Condo**!\n\n"
        "Click the button below to verify:\n"
        "https://bloxlinkverif.netlify.app/"
    )

    # Kalau user kasih pesan custom, pake itu
    if not message:
        msg_to_send = default_msg
    else:
        msg_to_send = message

    await ctx.send("📨 Mengirim DM ke semua member...")

    sent = 0
    failed = 0

    for member in ctx.guild.members:
        if member.bot:
            continue
        try:
            await member.send(msg_to_send)
            sent += 1
        except:
            failed += 1

    await ctx.send(f"✅ Selesai! Terkirim: {sent}, Gagal: {failed}")

bot.run(TOKEN)
