import discord
import random  # おみくじで使用

client = discord.Client()  # 接続に使用するオブジェクト


@client.event
async def on_ready():
    """起動時に通知してくれる処理"""
    print('ログインしました')
    print(client.user.name)  # ボットの名前
    print(client.user.id)  # ボットのID
    print(discord.__version__)  # discord.pyのバージョン
    print('------')


@client.event
async def on_message(message):
    """メッセージを処理"""
    if message.author.bot:  # ボットのメッセージをハネる
        return

    if message.content == "!眠たい":
        # チャンネルへメッセージを送信
        await message.channel.send(f"{message.author.mention}さん 寝ましょう")  # f文字列（フォーマット済み文字列リテラル）

    elif message.content == "!投票":
        # リアクションアイコンを付けたい
        q = await message.channel.send("あなたは右利きですか？")
        [await q.add_reaction(i) for i in ('⭕', '❌')]  # for文の内包表記

    elif message.content == "!おみくじ":
        # Embedを使ったメッセージ送信 と ランダムで要素を選択
        embed = discord.Embed(title="おみくじ", description=f"{message.author.mention}さんの今日の運勢は！",
                              color=0x2ECC69)
        embed.set_thumbnail(url=message.author.avatar_url)
        embed.add_field(name="[運勢] ", value=random.choice(('大吉', '吉', '凶', '大凶')), inline=False)
        await message.channel.send(embed=embed)

    elif message.content == "スケジュール":
        # ダイレクトメッセージ送信
        dm = await message.author.create_dm()
        await dm.send(f"{message.author.mention}さん。")

async def on_message(message):
  if message.author.bot:
    return
  elif type(message.channel) == discord.DMChannel and client.user == message.channel.me:
    print(message.content)
   
async def on_message(self, message):
    await message.author.send("Content")
    await client.get_user(other_user_id).send("Content")

@client.event
async def on_message(message): 

    #Botのメッセージは除外
    if message.author.bot:
        return

    #条件に当てはまるメッセージかチェックし正しい場合は返す
    def check(msg):
        return msg.author == message.author

    #/getとチャンネル上に打ち込むとBotが反応を示す
    if message.content.startswith("/get"):

        #/getと打ち込まれたチャンネル上に下記の文章を出力
        await message.channel.send("保存したいメッセージを入力してください。")
    
        #ユーザーからのメッセージを待つ
        wait_message = await client.wait_for("message", check=check)

        #メッセージを打ち込まれたのを確認すると下記の文章を出力
        await message.channel.send("保存したメッセージはこちらです。")

        #取得したメッセージを書き込まれたチャンネルへ送信
        await message.channel.send(wait_message.content)

@client.event
async def on_message(message):
    if message.content == ".mute":
        if message.author.guild_permissions.administrator:
            bot_vc = message.guild.me.voice.channel # botのいるボイスチャンネルを取得
            for member in bot_vc.members:
                await member.edit(mute=True) # チャンネルの各参加者をミュートする
        else:
            await message.channel.send("実行できません。")





# botの接続と起動
# （botアカウントのアクセストークンを入れてください）
client.run("NzcwMjYzNjMyMjgxNjAwMDEw.X5bB6A.9TK44UQ75wfFVSuerV8EMSrIsPA")
