import asyncio
import os
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import CommandStart

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_INVITE_LINK = os.getenv("CHANNEL_INVITE_LINK")  # например: https://t.me/+abcXYZ123

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# ─── Текст правил ────────────────────────────────────────────────
CLAN_NAME = "⚔️ [Название клана]"

RULES_WORLD = """
⚔️ *А) Правила поведения в мире*

1\. Клан имеет строгое PVE\-направление, агры на других кланов — запрещены\. Отвечать на агры — *можно и нужно*\.
2\. Агры на игроков без кланов разрешены только на БД\. Остальные фри\-пвп зоны, морай ивенты — строго по договорённости\.
3\. По любым аграм, оскорблениям, проблемам с сокланами — обращаться к офицерам \(ТГ \+ скрины\)\.
4\. Игнорировать срач в ЛС от \*НИК\* — не тратьте время, силы и нервы\.
5\. 🚫 Запрещено кидать личный вар или вар от лица клана\.
6\. 🚫 Запрещены срачи в мировой чат — не начинать, не поддерживать, не пытаться закончить\.
7\. 🚫 Запрещено ставить 100 карт в кубе\.
8\. 🚫 Запрещены политические выяснения и разборки в любых чатах \(кроме личного\)\.
9\. Отсутствие более 10 дней без предупреждения — кик\. Более 30 дней — перевод во второй состав\.
10\. Торговля в клан\-чате: своим — дешевле, либо не спамьте чат\. Для торговли есть отдельная ветка в ТГ\.
"""

RULES_KH = """
🏰 *Б) Правила поведения на КХ*

1\. КХ — добровольное мероприятие\. Пришёл — работаешь наравне со всеми, не стоишь в афк у стенки \(кроме этапов, где проводящий разрешает\)\.
2\. Строго слушать указания проводящего КХ — никакой личной импровизации\.
3\. Не бегать "сам себе пати" — КХ командный ивент\.
4\. Твины на КХ разрешены, если они тоже работают, а не стоят у стенки\.
5\. 🚫 Полный запрет на масс\-скилы на запрещённых этапах \(проводящий сообщает\)\. Создайте отдельный макрос без масс\-скилов\.
6\. По возможности зайти в голосовую связь на время КХ — разговаривать не обязательно\.
7\. Нужна помощь по КХ — обращайся к проводящему \(в ТГ есть краткий гайд\)\.
"""

RULES_TEXT = (
    f"👋 Добро пожаловать в {CLAN_NAME}\\!\n\n"
    "Перед вступлением внимательно ознакомься с правилами:\n\n"
    + RULES_WORLD
    + "\n"
    + RULES_KH
    + "\n─────────────────────────\n"
    "_Нажав кнопку ниже, ты подтверждаешь, что ознакомился с правилами и согласен их соблюдать\\._"
)

# ─── Клавиатуры ──────────────────────────────────────────────────
def rules_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="✅ Принимаю правила", callback_data="accept_rules")]
    ])

def join_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🚀 Вступить в канал", url=CHANNEL_INVITE_LINK)]
    ])

# ─── Хэндлеры ────────────────────────────────────────────────────
@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        RULES_TEXT,
        parse_mode="MarkdownV2",
        reply_markup=rules_keyboard()
    )

@dp.callback_query(F.data == "accept_rules")
async def accept_rules(callback: CallbackQuery):
    await callback.message.edit_reply_markup(reply_markup=None)
    await callback.message.answer(
        "✅ *Отлично\!* Ты принял правила клана\.\n\n"
        "Теперь можешь вступить в наш канал по кнопке ниже 👇",
        parse_mode="MarkdownV2",
        reply_markup=join_keyboard()
    )
    await callback.answer()

# ─── Запуск ──────────────────────────────────────────────────────
async def main():
    print("Бот запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
