from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)

TOKEN = "8278748538:AAHa0LvgJsiPK7OA-9vMj14nEaja2L1Fz_s"


# ذخیره کاربران
def save_user(user):
    try:
        with open("users.txt", "a", encoding="utf-8") as f:
            f.write(
                f"{user.id} | {user.username} | {user.first_name}\n"
            )
    except:
        pass


# منوی اصلی
def main_menu():

    keyboard = [

        [
            InlineKeyboardButton(
                "📢 Join Channel",
                url="https://t.me/TheHacker521"
            )
        ],

        [
            InlineKeyboardButton(
                "💬 Join Group",
                url="https://t.me/TheHacker522"
            )
        ],

        [
            InlineKeyboardButton(
                "🌐 I want your platform address",
                callback_data="platform"
            )
        ],

        [
            InlineKeyboardButton(
                "🎮 I want a Free Fire panel from you",
                callback_data="panel"
            )
        ],

        [
            InlineKeyboardButton(
                "👤 How can I connect with the bot creator?",
                callback_data="creator"
            )
        ]

    ]

    return InlineKeyboardMarkup(keyboard)


# استارت
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.effective_user

    save_user(user)

    await update.message.reply_text(
        """
✨ I am MuhaMye.

Why did you start the bot?
""",
        reply_markup=main_menu()
    )


# دکمه ها
async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query

    await query.answer()

    # PLATFORM
    if query.data == "platform":

        keyboard = [

            [
                InlineKeyboardButton(
                    "🚀 Open Platform",
                    url="http://preeminent-seahorse-e9cfcc.netlify.app"
                )
            ],

            [
                InlineKeyboardButton(
                    "🏠 Home",
                    callback_data="home"
                )
            ]

        ]

        await query.edit_message_text(
            text="🌐 Click below to open the platform.",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    # PANEL
    elif query.data == "panel":

        keyboard = [

            [
                InlineKeyboardButton(
                    "🏠 Home",
                    callback_data="home"
                )
            ]

        ]

        await query.edit_message_text(
            text="""
🎮 Free Fire Panel

Stay tuned for further information.

Our iPhone and Android panels are currently sold out.
""",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    # CREATOR
    elif query.data == "creator":

        keyboard = [

            [
                InlineKeyboardButton(
                    "💬 Contact MuhaMye",
                    url="https://t.me/MohaMyegoats"
                )
            ],

            [
                InlineKeyboardButton(
                    "🏠 Home",
                    callback_data="home"
                )
            ]

        ]

        await query.edit_message_text(
            text="👤 Connect with the creator:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    # HOME
    elif query.data == "home":

        await query.edit_message_text(
            text="""
✨ I am MuhaMye.

Why did you start the bot?
""",
            reply_markup=main_menu()
        )


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(buttons))

print("Bot Started...")

app.run_polling()