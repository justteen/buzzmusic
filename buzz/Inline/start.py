from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)

from config import MUSIC_BOT_NAME, SUPPORT_CHANNEL, SUPPORT_GROUP
from buzz import BOT_USERNAME


def setting_markup2():
    buttons = [
        [
            InlineKeyboardButton(text="🔈 Kualitas Audio", callback_data="AQ"),
            InlineKeyboardButton(text="🎚 Volume Audio", callback_data="AV"),
        ],
        [
            InlineKeyboardButton(
                text="👥 Pengguna Resmi", callback_data="AU"
            ),
            InlineKeyboardButton(
                text="💻 Dashboard", callback_data="Dashboard"
            ),
        ],
        [
            InlineKeyboardButton(text="✖️ Tutup", callback_data="close"),
        ],
    ]
    return f"🔧  **Pengaturan {MUSIC_BOT_NAME} **", buttons


def start_pannel():
    if not SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 Bantuan Menu Perintah", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🔧 Pengaturan", callback_data="settingm"
                )
            ],
        ]
        return f"🎛  **Ini adalah {MUSIC_BOT_NAME}**", buttons
    if not SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 Bantuan Menu Perintah", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🔧 Pengaturan", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="📨Support Group", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"🎛  **Ini adalah {MUSIC_BOT_NAME}*", buttons
    if SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 Bantuan Menu Perintah", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🔧 Pengaturan", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="📨Official Channel", url=f"{SUPPORT_CHANNEL}"
                ),
            ],
        ]
        return f"🎛  **Ini adalah {MUSIC_BOT_NAME}**", buttons
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 Bantuan Menu Perintah", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🔧 Pengaturan", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="📨Official Channel", url=f"{SUPPORT_CHANNEL}"
                ),
                InlineKeyboardButton(
                    text="📨Support Group", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"🎛  **Ini adalah {MUSIC_BOT_NAME}**", buttons


def private_panel():
    if not SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 Bantuan Menu Perintah", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    "➕ Add saya ke Group",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
        ]
        return f"🎛  **Ini adalah {MUSIC_BOT_NAME}**", buttons
    if not SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 Bantuan Menu Perintah", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    "➕ Add saya ke Group",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="📨Support Group", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"🎛  **Ini adalah {MUSIC_BOT_NAME}*", buttons
    if SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 Bantuan Menu Perintah", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    "➕ Add saya ke Group",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="📨Official Channel", url=f"{SUPPORT_CHANNEL}"
                ),
            ],
        ]
        return f"🎛  **Ini adalah {MUSIC_BOT_NAME}**", buttons
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 Bantuan Menu Perintah", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    "➕ Add saya ke Group",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="📨Official Channel", url=f"{SUPPORT_CHANNEL}"
                ),
                InlineKeyboardButton(
                    text="📨Support Group", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"🎛  **Ini adalah {MUSIC_BOT_NAME}**", buttons


def setting_markup():
    buttons = [
        [
            InlineKeyboardButton(text="🔈 Kualitas Audio", callback_data="AQ"),
            InlineKeyboardButton(text="🎚 Audio Volume", callback_data="AV"),
        ],
        [
            InlineKeyboardButton(
                text="👥 Pengguna Resmi", callback_data="AU"
            ),
            InlineKeyboardButton(
                text="💻 Dashboard", callback_data="Dashboard"
            ),
        ],
        [
            InlineKeyboardButton(text="✖️ Tutup", callback_data="close"),
            InlineKeyboardButton(text="🔙 Kembali", callback_data="okaybhai"),
        ],
    ]
    return f"🔧  **Pengaturan {MUSIC_BOT_NAME}**", buttons


def volmarkup():
    buttons = [
        [
            InlineKeyboardButton(
                text="🔄 Reset Audio Volume 🔄", callback_data="HV"
            )
        ],
        [
            InlineKeyboardButton(text="🔈 Low Vol", callback_data="LV"),
            InlineKeyboardButton(text="🔉 Medium Vol", callback_data="MV"),
        ],
        [
            InlineKeyboardButton(text="🔊 High Vol", callback_data="HV"),
            InlineKeyboardButton(text="🔈 Amplified Vol", callback_data="VAM"),
        ],
        [
            InlineKeyboardButton(
                text="🔽 Custom Volume 🔽", callback_data="Custommarkup"
            )
        ],
        [InlineKeyboardButton(text="🔙 Kembali", callback_data="settingm")],
    ]
    return f"🔧  **Pengaturan {MUSIC_BOT_NAME}**", buttons


def custommarkup():
    buttons = [
        [
            InlineKeyboardButton(text="+10", callback_data="PTEN"),
            InlineKeyboardButton(text="-10", callback_data="MTEN"),
        ],
        [
            InlineKeyboardButton(text="+25", callback_data="PTF"),
            InlineKeyboardButton(text="-25", callback_data="MTF"),
        ],
        [
            InlineKeyboardButton(text="+50", callback_data="PFZ"),
            InlineKeyboardButton(text="-50", callback_data="MFZ"),
        ],
        [InlineKeyboardButton(text="🔼Custom Volume 🔼", callback_data="AV")],
    ]
    return f"🔧  **Pengaturan {MUSIC_BOT_NAME}**", buttons


def usermarkup():
    buttons = [
        [
            InlineKeyboardButton(text="👥 Semua", callback_data="EVE"),
            InlineKeyboardButton(text="🙍 Admin", callback_data="AMS"),
        ],
        [
            InlineKeyboardButton(
                text="📋 Pengguna Resmi", callback_data="USERLIST"
            )
        ],
        [InlineKeyboardButton(text="🔙 Kembali", callback_data="settingm")],
    ]
    return f"🔧  **Pengaturan {MUSIC_BOT_NAME}**", buttons


def dashmarkup():
    buttons = [
        [
            InlineKeyboardButton(text="✔️ Uptime", callback_data="UPT"),
            InlineKeyboardButton(text="💾 Ram", callback_data="RAT"),
        ],
        [
            InlineKeyboardButton(text="💻 Cpu", callback_data="CPT"),
            InlineKeyboardButton(text="💽 Disk", callback_data="DIT"),
        ],
        [InlineKeyboardButton(text="🔙 Kembali", callback_data="settingm")],
    ]
    return f"🔧  **Pengaturan {MUSIC_BOT_NAME}**", buttons
