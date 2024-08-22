import discord

async def create_group(guild: discord.Guild, name: str):
    permissions = discord.Permissions.text()
    permissions.add_reactions = True
    permissions.stream = True
    permissions.read_messages = True
    permissions.send_messages = True
    permissions.send_tts_messages = True
    permissions.embed_links = True
    permissions.attach_files = True
    permissions.read_message_history = True
    permissions.manage_messages = False
    permissions.mention_everyone = True
    permissions.external_emojis = True
    permissions.connect = True
    permissions.speak = True
    permissions.use_voice_activation = True
    permissions.change_nickname = True
    permissions.manage_expressions = True
    permissions.manage_emojis_and_stickers = True
    permissions.use_application_commands = True
    permissions.send_messages_in_threads = True
    permissions.use_soundboard = True
    permissions.send_voice_messages = True
    permissions.send_polls = True
    permissions.create_private_threads = False
    permissions.create_public_threads = False
    permissions.manage_threads = False
    permissions.use_external_apps = True
    permissions.create_instant_invite = True


    await guild.create_role(
        name=name,
        hoist=True,
        mentionable=True,
        permissions=permissions
    )
