from discord.ext import commands
from discord.utils import get
from main import cml_manager
from src.message import *
from src.dc_manage import *
import json

@commands.command()
async def ping(ctx: commands.Context, msg: str):
    msg = f'{ctx.author} send message in {ctx.channel}: {ctx.command} {ctx.args}'
    print(msg)
    await ctx.send(msg)

@commands.command()
async def bind(ctx: commands.Context, username: str):
    with open('accounts.json') as fp:
        accounts = json.load(fp)

    if username in accounts:
        await ctx.send(BIND_BINDED.format(ctx.author.display_name, username))
        return

    # find user from CML database
    user = cml_manager.find_user(username)
    print(user)

    if user == None:
        await ctx.send(BIND_CANNOT_FIND_ACCOUNT.format(ctx.author.display_name, username))
        return

    # get user information
    group = user[2].upper()
    teacher = user[3]
    first_name = user[8]
    last_name = user[7]

    # 確認 dc 名稱是不是正確
    # 並且確認 CML 登陸的姓名是否跟 dc 一致
    full_name = last_name + first_name
    if f'-{full_name}' not in ctx.author.display_name:
        await ctx.send(BIND_DIFFERENT_NAME.format(ctx.author.display_name, username))
        return
        
    uid = ctx.author.id

    accounts[username] = {
        'name': ctx.author.display_name,
        'uid': uid
    }
    with open('accounts.json', 'w') as fp:
        json.dump(accounts, fp, ensure_ascii=False)

    '''
    user = ctx.guild.get_member(uid)
    await user.send("Hello, this is CML bot")
    '''

    # dc 分組
    # 給 dc 身份組別
    dc_group = None
    if group == 'MIRA':
        dc_group = 'R 組'
    elif group == 'DSP':
        dc_group = 'DSP 組'
    elif group == 'GRAPHICS':
        if teacher == 'robin':
            dc_group = 'Robin 組'
        else:
            dc_group = 'G 組'
    elif group == 'NETWORK':
        dc_group = 'N 組'
    elif group == 'AIMM':
        dc_group = 'A 組'
    elif group == 'SYSTEM':
        dc_group = 'SYSTEM 組'


    if dc_group != None:
        # build group & add the user to the group
        guild = ctx.guild
        if not get(guild.roles, name=dc_group):
            await create_group(guild, dc_group)

        target_role = get(guild.roles, name=dc_group)
        await ctx.author.add_roles(target_role)
        msg = BIND_SUCCESS.format(first_name, group, dc_group, username)
    else:
        msg = BIND_GROUP_ERROR.format(first_name)

    await ctx.send(msg)


    

