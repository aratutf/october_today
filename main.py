import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command  # Обратите внимание, что используется фильтр команд
from aiogram import Router
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import WebAppInfo

API_TOKEN = '7847156503:AAFV9KDkIe7jOoIv72TRBFP4knHqApRJTnY'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Создаем маршрутизатор
router = Router()

# Хэндлер для команды /start
@router.message(Command('start'))
async def start_command(message: types.Message):

    button = InlineKeyboardButton(text="site", web_app=WebAppInfo(url="https://aratutf.github.io/october_today/"))
    # Создаем разметку клавиатуры и добавляем кнопку
    markup = InlineKeyboardMarkup(inline_keyboard=[[button]])   
    await message.answer("hi my dear", reply_markup =markup)

    # Регистрируем маршрутизатор
dp.include_router(router)

async def main():
    print("Запуск бота...")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
