from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command
import bot_code

router = Router()


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
            mentioned_user_id = entity.user.id  # Get the ID from the entity
            print(f"ID of the mentioned user: {mentioned_user_id}")
            # Now you can use mentioned_user_id as needed
            break


    await msg.reply(f"{msg.from_user.mention_markdown()}"
                    f"{bot_code.check_new_member(id_tg, name, fullname, group_id=msg.chat.id)}", parse_mode="Markdown")


@router.message(Command("top"))
async def message_handler(msg: Message):
    await msg.answer(f"{bot_code.check_top(group_id=msg.chat.id)}")
