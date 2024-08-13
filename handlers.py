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
            if entity.type == 'mention':
                # Извлекаем username из текста сообщения
                username = msg.text[entity.offset:entity.offset + entity.length].strip('@')
                print(username)
                try:
                    # Получаем информацию о пользователе по username
                    user = await msg.bot.get_chat(username)
                    id_tg_mentioned = user.id  # ID упомянутого пользователя
                    print(f"ID упомянутого пользователя: {id_tg_mentioned}")
                except Exception as e:
                    print(f"Ошибка при получении пользователя: {e}")
                    await msg.reply(
                        "Не удалось найти упомянутого пользователя. Пожалуйста, проверьте правильность username.")
                    return  # Завершаем выполнение функции, если произошла ошибка


    await msg.reply(f"{msg.from_user.mention_markdown()}"
                    f"{bot_code.check_new_member(id_tg, name, fullname, group_id=msg.chat.id)}", parse_mode="Markdown")


@router.message(Command("top"))
async def message_handler(msg: Message):
    await msg.answer(f"{bot_code.check_top(group_id=msg.chat.id)}")
