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
    await msg.answer(f"@{msg.from_user.username}{bot_code.check_new_member(msg.from_user.username)}")


@router.message(Command("top"))
async def message_handler(msg: Message):
    await msg.answer(f"@{msg.from_user.username}{bot_code.check_new_member(msg.from_user.username)}")
