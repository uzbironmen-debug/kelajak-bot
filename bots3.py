import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.enums import ParseMode

# Botingiz toketi
API_TOKEN = '8453975864:AAEVK_dFmGHlg8zeOeK15xfB8P3XNt2vAEk'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Menyu
menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📊 Matematika"), KeyboardButton(text="🌍 Xorijiy tillar")],
        [KeyboardButton(text="🏆 Sport"), KeyboardButton(text="💻 IT & Texnika")],
        [KeyboardButton(text="🎭 Madaniyat va San'at"), KeyboardButton(text="🎨 Amaliy san'at")]
    ],
    resize_keyboard=True,
    input_field_placeholder="Yo'nalishni tanlang..."
)

@dp.message(CommandStart())
async def start_command(message: types.Message):
    welcome_text = (
        "<b>Yashnobod Tumani 'Kelajak Markazi'</b> 🚀\n"
        "━━━━━━━━━━━━━━━\n"
        "Assalomu alaykum! Markazimizdagi barcha to'garaklar va dars jadvali bilan tanishishingiz mumkin.\n\n"
        "📍 <b>Manzil:</b> Yashnobod tumani\n"
        "━━━━━━━━━━━━━━━\n"
        "<i>Yo'nalishni tanlang:</i>"
    )
    await message.answer(welcome_text, reply_markup=menu_keyboard, parse_mode=ParseMode.HTML)

@dp.message(F.text == "📊 Matematika")
async def math_info(message: types.Message):
    text = (
        "📊 <b>Matematika va Psixologiya</b>\n"
        "━━━━━━━━━━━━━━━\n"
        "1️⃣ <b>Математика (рус)</b>\n"
        "└ 👤 Рухшона | 📞 +998908262322\n"
        "└ ⏰ Сеш-Пай 09:00-10:30 | 💰 200 000\n\n"
        "2️⃣ <b>Математика (узб)</b>\n"
        "└ 👤 Мадина | 📞 +998944705522\n"
        "└ ⏰ Шан-Якш 13:00-14:00 | 💰 100 000\n\n"
        "3️⃣ <b>Подготовка к школе</b>\n"
        "└ 👤 Гулнара Абасовна | 📞 +998977407330\n"
        "└ ⏰ Душ-Чор-Пай 16:00-18:00 | 💰 300 000\n\n"
        "4️⃣ <b>Почемучка</b>\n"
        "└ 👤 Юлия Викторовна | 📞 +998909455300\n"
        "└ ⏰ Суббота-Воскресенье 11:00-12:30 | 💰 300 000\n\n"
        "5️⃣ <b>Мактабга тайёрлов</b>\n"
        "└ 👤 Гулзода | 📞 +998937497750\n"
        "└ ⏰ Душ-Чor / Шан-Якш | 💰 300 000\n\n"
        "6️⃣ <b>Ментал арифметика</b>\n"
        "└ 👤 Гулзоda | 📞 +998937497750\n"
        "└ ⏰ Душанба-Чоршанба | 💰 123 600\n\n"
        "7️⃣ <b>Ментал арифметика</b>\n"
        "└ 👤 Мохина | 📞 +998934507069\n"
        "└ ⏰ Шанба-Якшанба 17:00-18:00 | 💰 250 000\n\n"
        "8️⃣ <b>Менtal арифметика</b>\n"
        "└ 👤 Шахзода | 📞 +998997931940\n"
        "└ ⏰ Чоршанба-Жума 15:00-17:00 | 💰 250 000\n\n"
        "9️⃣ <b>Занятия с психологом</b>\n"
        "└ 👤 Лариса Васильевна | 📞 +998909575336\n"
        "└ 💰 По записи\n\n"
        "🔟 <b>Психолог билан сухбат</b>\n"
        "└ 👤 Феруза Хасановна | 📞 +998971550089\n"
        "└ 💰 По записи\n"
        "━━━━━━━━━━━━━━━"
    )
    await message.answer(text, parse_mode=ParseMode.HTML)

@dp.message(F.text == "🌍 Xorijiy tillar")
async def foreign_languages(message: types.Message):
    text = (
        "🌍 <b>Xorijiy tillar bo'limi</b>\n"
        "━━━━━━━━━━━━━━━\n"
        "1️⃣ <b>Английский язык</b>\n"
        "└ 👤 Шахноза Миразизовна | 📞 +998330711770\n"
        "└ ⏰ По записи (12 yosh+) | 💰 400 000\n\n"
        "2️⃣ <b>Инглиз тили</b>\n"
        "└ 👤 Шахноза | 📞 +998948516633\n"
        "└ ⏰ Шанба-Якшанба (По записи)\n\n"
        "3️⃣ <b>Инглиз тили</b>\n"
        "└ 👤 Фаёза | 📞 +998935950662\n"
        "└ ⏰ По записи | 💰 123 600\n\n"
        "4️⃣ <b>Инглиз тили</b>\n"
        "└ 👤 Гулнора | 📞 +998933549604\n"
        "└ ⏰ Сеш-Пай 10:00-15:30 | 💰 123 600\n\n"
        "5️⃣ <b>Президент мактаби тайёрлов</b>\n"
        "└ 👤 Нодира | 📞 +998994779988\n"
        "└ ⏰ Шанба-Yakshanba (По записи)\n\n"
        "6️⃣ <b>Инглиз тили</b>\n"
        "└ 👤 Рухсора | 📞 +998990114189\n"
        "└ ⏰ Сеш-Пай 09:00-10:30 | 💰 123 600\n\n"
        "7️⃣ <b>Инглиз тили</b>\n"
        "└ 👤 Дилноза | 📞 +998909582204\n"
        "└ ⏰ Душ-Чор 08:00-09:30 | 💰 123 600\n\n"
        "8️⃣ <b>Рус тили</b>\n"
        "└ 👤 Гульнара | 📞 +998977407330\n"
        "└ ⏰ Душ-Чор 09:00-16:00 | 💰 123 600\n\n"
        "9️⃣ <b>Араб тили</b>\n"
        "└ 👤 Дилшод | 📞 +998974675161\n"
        "└ ⏰ Жума-Якш 09:30-11:30 | 💰 300 000\n\n"
        "🔟 <b>Корейс тили</b>\n"
        "└ 👤 Фаёза | 📞 +998935950662\n"
        "└ ⏰ По записи\n\n"
        "1️⃣1️⃣ <b>Узбекский язык</b>\n"
        "└ 👤 Жамиля | 📞 +998977210324\n"
        "└ ⏰ По записи\n"
        "━━━━━━━━━━━━━━━"
    )
    await message.answer(text, parse_mode=ParseMode.HTML)

@dp.message(F.text == "🏆 Sport")
async def sport_info(message: types.Message):
    text = (
        "🏆 <b>Sport to'garaklari</b>\n"
        "━━━━━━━━━━━━━━━\n"
        "1️⃣ <b>Шахматы</b>\n"
        "└ 👤 Бобур | 📞 +998909495629\n\n"
        "2️⃣ <b>Кунг-фу УШУ</b>\n"
        "└ 👤 Даниил | 📞 +9988500773694\n\n"
        "3️⃣ <b>Карате-До</b>\n"
        "└ 👤 Рустам | 📞 +998998104271\n\n"
        "4️⃣ <b>Худ. гимнастика</b>\n"
        "└ 👤 Дилнара | 📞 +998994808970\n\n"
        "5️⃣ <b>Худ. гимнастика</b>\n"
        "└ 👤 Гульмира | 📞 +998932656065\n\n"
        "6️⃣ <b>Худ. гимнастика</b>\n"
        "└ 👤 Юля | 📞 +998909376373\n\n"
        "7️⃣ <b>Пинчак силат</b>\n"
        "└ 👤 Юля | 📞 +998909376373\n\n"
        "8️⃣ <b>Фитнес</b>\n"
        "└ 👤 Юля | 📞 +998909376373\n\n"
        "9️⃣ <b>Худ. гимнастика</b>\n"
        "└ 👤 Дилnoza | 📞 +998939537773\n\n"
        "🔟 <b>Оздоровит. гимн.</b>\n"
        "└ 👤 Зулфизар | 📞 +998909782827\n\n"
        "1️⃣1️⃣ <b>Согломлаштириш</b>\n"
        "└ 👤 Ойгул | 📞 +998935182723\n\n"
        "1️⃣2️⃣ <b>Зумба+Танцы</b>\n"
        "└ 👤 Дилноza | 📞 +998946610134\n\n"
        "1️⃣3️⃣ <b>Фитнес/Танцы</b>\n"
        "└ ⏰ 11:00-12:30\n\n"
        "1️⃣4️⃣ <b>Фитнес</b>\n"
        "└ 👤 Зулфизар | ⏰ 20:00-21:30 | 💰 350 000\n"
        "━━━━━━━━━━━━━━━"
    )
    await message.answer(text, parse_mode=ParseMode.HTML)

@dp.message(F.text == "💻 IT & Texnika")
async def it_info(message: types.Message):
    text = (
        "💻 <b>IT va Texnik yo‘nalishlar</b>\n"
        "━━━━━━━━━━━━━━━\n"
        "1️⃣ <b>Робототехника</b>\n"
        "└ 👤 Амир | 📞 +998977337119\n"
        "└ 💰 250 000\n\n"
        "2️⃣ <b>Авто-авиа моделлаштириш</b>\n"
        "└ 👤 Бекир | 📞 +998994421928\n"
        "└ ⏰ По записи\n\n"
        "3️⃣ <b>Компьютер сабоқлари</b>\n"
        "└ 👤 Мадина | 📞 +998944705522\n"
        "└ 💰 123 600\n"
        "━━━━━━━━━━━━━━━"
    )
    await message.answer(text, parse_mode=ParseMode.HTML)

@dp.message(F.text == "🎭 Madaniyat va San'at")
async def culture_info(message: types.Message):
    text = (
        "🎭 <b>Madaniyat va San'at</b>\n"
        "━━━━━━━━━━━━━━━\n"
        "1️⃣ <b>Шарқ гавҳари (рақс)</b>\n"
        "└ 👤 Дилноза | 📞 +998946610134\n\n"
        "2️⃣ <b>Кўзмунчоқ (рақс)</b>\n"
        "└ 👤 Санобар | 📞 +998909258819\n\n"
        "3️⃣ <b>“Ассорти” рақслари</b>\n"
        "└ 👤 Кристина | 📞 +507791633\n\n"
        "4️⃣ <b>Бал рақслари</b>\n"
        "└ 👤 Светлана | 📞 +998909558806\n\n"
        "5️⃣ <b>Шарқ юлдузлари (Театр)</b>\n"
        "└ 👤 Маълумот учун | 📞 +998946855130\n\n"
        "6️⃣ <b>Ёш доирачилар</b>\n"
        "└ 👤 Бобур | 📞 +998998392443\n\n"
        "7️⃣ <b>Актёрлик маҳорати</b>\n"
        "└ 👤 Аҳад | 📞 +998943023332\n\n"
        "8️⃣ <b>Вокал</b>\n"
        "└ 👤 Фахриддин | 📞 +998909258834\n\n"
        "9️⃣ <b>Talents project</b>\n"
        "└ 👤 Замира | 📞 +998773263086\n\n"
        "🔟 <b>Вокал (рус)</b>\n"
        "└ 👤 Римма | 📞 +998903472340\n\n"
        "1️⃣1️⃣ <b>Фортепиано</b>\n"
        "└ 👤 Лола | 📞 +99883808009\n\n"
        "1️⃣2️⃣ <b>Гитара</b>\n"
        "└ 👤 Тимур | 📞 +998974243439\n"
        "━━━━━━━━━━━━━━━"
    )
    await message.answer(text, parse_mode=ParseMode.HTML)

@dp.message(F.text == "🎨 Amaliy san'at")
async def art_info(message: types.Message):
    text = (
        "🎨 <b>Amaliy san'at bo'limi</b>\n"
        "━━━━━━━━━━━━━━━\n"
        "1️⃣ <b>Тасвирий санъат, архитектура, либос дизайн</b>\n"
        "└ 👤 Чори ака | 📞 +998901754890\n"
        "└ ⏰ Шанба-якшанба 14:00-17:15\n\n"
        "2️⃣ <b>Шарк миниатюраси (расм)</b>\n"
        "└ 👤 Лола | 📞 +998946647315\n"
        "└ ⏰ Душ-Чор 09:00-10:30 / 14:00-15:30\n"
        "└ 💰 123 600\n\n"
        "3️⃣ <b>Изо / Расм</b>\n"
        "└ 👤 Ирода | 📞 +998200226320\n"
        "└ ⏰ Душ-Чор 16:00-17:00\n"
        "└ 💰 123 600 (7-12 ёш) / 150 000 (3-6 ёш)\n\n"
        "4️⃣ <b>Арт студия «Калибри»</b>\n"
        "└ 👤 Ольга Вячеславовна | 📞 +998901755153\n"
        "└ ⏰ Сеш-Пай 18:00-19:30 | Чор-Жум 09:00-10:30\n"
        "└ 💰 400 000\n\n"
        "5️⃣ <b>Ёш пазанда</b>\n"
        "└ 👤 Зухра | 📞 +998902886144\n"
        "└ ⏰ Шанба-якшанба | 💰 250 000\n\n"
        "6️⃣ <b>Тўқиш / Бисер / Каштачилик</b>\n"
        "└ 👤 Гулзода | 📞 +998937497750\n"
        "└ ⏰ Душ-Чор / Шан-Якш 11:00-12:30\n"
        "└ 💰 200 000\n"
        "━━━━━━━━━━━━━━━"
    )
    await message.answer(text, parse_mode=ParseMode.HTML)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    print("Bot muvaffaqiyatli ishga tushdi...")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
