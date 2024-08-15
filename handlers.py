from aiogram import types, F, Router, Bot
# from aiogram.client import bot
from aiogram.types import Message
from aiogram.filters import Command
import bot_code
import config
from aiogram.enums.parse_mode import ParseMode

router = Router()
bot = Bot(token=config.TOKEN, parse_mode=ParseMode.HTML)

@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("Привет! Раз в сутки игрок может прописать команду /dick@Biggest_chleno_bot, "
                     "где в ответ получит от бота рандомное число от -5 до +10 см.")


@router.message(Command("dick"))
async def message_handler(msg: Message):
    name = msg.from_user.username
    fullname = msg.from_user.full_name
    id_tg = msg.from_user.id
    if msg.entities:
        for entity in msg.entities:
            if entity.type == 'text_mention':
                user_id = entity.user.id
                await msg.reply(f"ID - {user_id}")

    await msg.reply(f"{msg.from_user.mention_markdown()}"
                    f"{bot_code.check_new_member(id_tg, name, fullname, group_id=msg.chat.id)}", parse_mode="Markdown")


@router.message(Command("top"))
async def message_handler(msg: Message):
    await msg.answer(f"{bot_code.check_top(group_id=msg.chat.id)}")


@router.message(Command("duel"))
async def message_handler(msg: Message):
    name = msg.from_user.username
    fullname = msg.from_user.full_name
    id_tg = msg.from_user.id
    user_id = False
    username = False
    if msg.entities:
        for entity in msg.entities:
            if entity.type == 'text_mention':
                user_id = entity.user.id
                # return user_id
            elif entity.type == 'mention':
                mention_entity = entity
                if mention_entity:
                    username = msg.text[mention_entity.offset + 1:mention_entity.offset + mention_entity.length]
                    try:
                        # Пытаемся получить информацию о пользователе в чате
                        members = await bot.get_chat_administrators(msg.chat.id)
                        for member in members:
                            if member.user.username == username:
                                user_id = member.user.id
                    except Exception as e:
                        await msg.reply(f"Failed to get user info: {e}")
            if user_id:
                msg1, msg2 = bot_code.duel(group_id=msg.chat.id, id_tg1=id_tg, id_tg2=user_id)
                await msg.reply(f"{msg.from_user.mention_markdown()}"
                                f"{msg1}",
                                parse_mode="Markdown")
                if msg2:
                    if username:
                        mention = f"[{username}](tg://user?id={user_id})"
                        await msg.reply(f"{mention}"
                                        f"{msg2}", parse_mode="Markdown")
                    else:
                        mention = f"[{entity.user.first_name}](tg://user?id={user_id})"
                        await msg.reply(f"{mention}"
                                        f"{msg2}", parse_mode="Markdown")