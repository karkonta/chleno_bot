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
    # # name = msg.from_user.mention_markdown(msg.from_user.full_name)
    # print(name)
    # print(f'{msg.from_user.id}, {msg.from_user.last_name}, {msg.from_user.first_name}')
    # print(type(name))
    # print(msg.from_user.mention_markdown(msg.from_user.full_name))
    # if name is None:
    #     name = msg.from_user.mention_markdown(msg.from_user.full_name)
    await msg.reply(f"{msg.from_user.mention_markdown()}"
                    f"{bot_code.check_new_member(id_tg, name, fullname)}", parse_mode="Markdown")


@router.message(Command("top"))
async def message_handler(msg: Message):
    await msg.answer(f"{bot_code.check_top()}")
