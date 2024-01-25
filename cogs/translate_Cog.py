import discord
from discord.ext import commands
import deepl

class TranslateCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Cog connected as {self.bot.user.name}')

    async def send_translation(self, channel, translation, language):
        async with channel.typing():
            await channel.send(f"Traducción al {language}: {translation}")

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.user_id == self.bot.user.id:
            return 

        emoji_us = '🇺🇸'
        emoji_es = '🇪🇸'
        emoji_pt = '🇵🇹'

        channel = self.bot.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)

        # Español
        if emoji_es == str(payload.emoji):
            translation_en = deepl.translate(source_language="EN", target_language="ES", text=message.content)
            await self.send_translation(channel, translation_en, "Inglés")

        # Inglés
        elif emoji_us == str(payload.emoji):
            translation_es = deepl.translate(source_language="ES", target_language="EN", text=message.content)
            await self.send_translation(channel, translation_es, "Español")

        # Portugués
        elif emoji_pt == str(payload.emoji):
            translation_es = deepl.translate(source_language="ES", target_language="PT", text=message.content)
            await self.send_translation(channel, translation_es, "Portugués")

async def setup(bot):
    await bot.add_cog(TranslateCog(bot))
