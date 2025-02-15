import os
import asyncio

from aiogram.filters import CommandStart, Command
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [
        KeyboardButton(text="Button"),
        KeyboardButton(text="Button2"),
        KeyboardButton(text="Button3"),
    ],
    [
        KeyboardButton(text="Button4"),
        KeyboardButton(text="Button5"),
        KeyboardButton(text="Button6"),
    ]
])

inline_keyboard_1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Skin kanal - 1!", callback_data="inline_keyboard_1"), InlineKeyboardButton(text="Skin kanal - 2!", callback_data="inline_keyboard_1")],
        [InlineKeyboardButton(text="Skin kanal - 3!", callback_data="inline_keyboard_1", url="https://t.me/millidaskins")]
]
)




@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer("Assalomu alaykum siz Minecraft mode bot ga xush kelibsiz! "
                         "Iltimos ozizga qulay commandni tanlasez bo'ladi bizda /mode /help /skin /homiy - kanalar! commandalari bor!")

@dp.message(Command("help"))
async def _help(message: types.Message):
    await message.answer("Minecraft bot bu siz uchun bolgan qulay bot dur siz buyerda modlar yoki sovol bershingiz mumkin!")

@dp.message(Command("skin"))
async def _skin(message: types.Message):
    await message.answer("Minecraft skin bot ga xush kelibsiz! siz buyerda skin sayt ga kirolisiz!", reply_markup=inline_keyboard_1)
@dp.message(Command("mode"))
async def _mode(message: types.Message):
    await message.answer("Uzr xozircha bizda mode lar yoq lekin albatta bo'ladi!", reply_markup=inline_keyboard_1)

@dp.message(Command("homiy"))
async def _homiy(message: types.Message):
    await message.answer("Mashi kanalar bilan homiymiz!")

async def main():
    print("Starting...")
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run (main())























