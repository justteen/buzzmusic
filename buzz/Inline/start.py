from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)

from config import MUSIC_BOT_NAME, SUPPORT_CHANNEL, SUPPORT_GROUP
from buzz import BOT_USERNAME


def setting_markup2():
    buttons = [
        [
            InlineKeyboardButton(text="π Kualitas Audio", callback_data="AQ"),
            InlineKeyboardButton(text="π Volume Audio", callback_data="AV"),
        ],
        [
            InlineKeyboardButton(
                text="π₯ Pengguna Resmi", callback_data="AU"
            ),
            InlineKeyboardButton(
                text="π» Dashboard", callback_data="Dashboard"
            ),
        ],
        [
            InlineKeyboardButton(text="βοΈ Tutup", callback_data="close"),
        ],
    ]
    return f"π§  **Pengaturan {MUSIC_BOT_NAME} **", buttons


def start_pannel():
    if not SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="π Bantuan Menu Perintah", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="π§ Pengaturan", callback_data="settingm"
                )
            ],
        ]
        return f"π  **Ini adalah {MUSIC_BOT_NAME}**", buttons
    if not SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="π Bantuan Menu Perintah", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="π§ Pengaturan", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="π¨Support Group", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"π  **Ini adalah {MUSIC_BOT_NAME}*", buttons
    if SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="π Bantuan Menu Perintah", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="π§ Pengaturan", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="π¨Official Channel", url=f"{SUPPORT_CHANNEL}"
                ),
            ],
        ]
        return f"π  **Ini adalah {MUSIC_BOT_NAME}**", buttons
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="π Bantuan Menu Perintah", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="π§ Pengaturan", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="π¨Official Channel", url=f"{SUPPORT_CHANNEL}"
                ),
                InlineKeyboardButton(
                    text="π¨Support Group", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"π  **Ini adalah {MUSIC_BOT_NAME}**", buttons


def private_panel():
    if not SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="π Bantuan Menu Perintah", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    "β Add saya ke Group",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
        ]
        return f"π  **Ini adalah {MUSIC_BOT_NAME}**", buttons
    if not SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="π Bantuan Menu Perintah", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    "β Add saya ke Group",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="π¨Support Group", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"π  **Ini adalah {MUSIC_BOT_NAME}*", buttons
    if SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="π Bantuan Menu Perintah", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    "β Add saya ke Group",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="π¨Official Channel", url=f"{SUPPORT_CHANNEL}"
                ),
            ],
        ]
        return f"π  **Ini adalah {MUSIC_BOT_NAME}**", buttons
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="π Bantuan Menu Perintah", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    "β Add saya ke Group",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="π¨Official Channel", url=f"{SUPPORT_CHANNEL}"
                ),
                InlineKeyboardButton(
                    text="π¨Support Group", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"π  **Ini adalah {MUSIC_BOT_NAME}**", buttons


def setting_markup():
    buttons = [
        [
            InlineKeyboardButton(text="π Kualitas Audio", callback_data="AQ"),
            InlineKeyboardButton(text="π Audio Volume", callback_data="AV"),
        ],
        [
            InlineKeyboardButton(
                text="π₯ Pengguna Resmi", callback_data="AU"
            ),
            InlineKeyboardButton(
                text="π» Dashboard", callback_data="Dashboard"
            ),
        ],
        [
            InlineKeyboardButton(text="βοΈ Tutup", callback_data="close"),
            InlineKeyboardButton(text="π Kembali", callback_data="okaybhai"),
        ],
    ]
    return f"π§  **Pengaturan {MUSIC_BOT_NAME}**", buttons


def volmarkup():
    buttons = [
        [
            InlineKeyboardButton(
                text="π Reset Audio Volume π", callback_data="HV"
            )
        ],
        [
            InlineKeyboardButton(text="π Low Vol", callback_data="LV"),
            InlineKeyboardButton(text="π Medium Vol", callback_data="MV"),
        ],
        [
            InlineKeyboardButton(text="π High Vol", callback_data="HV"),
            InlineKeyboardButton(text="π Amplified Vol", callback_data="VAM"),
        ],
        [
            InlineKeyboardButton(
                text="π½ Custom Volume π½", callback_data="Custommarkup"
            )
        ],
        [InlineKeyboardButton(text="π Kembali", callback_data="settingm")],
    ]
    return f"π§  **Pengaturan {MUSIC_BOT_NAME}**", buttons


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
        [InlineKeyboardButton(text="πΌCustom Volume πΌ", callback_data="AV")],
    ]
    return f"π§  **Pengaturan {MUSIC_BOT_NAME}**", buttons


def usermarkup():
    buttons = [
        [
            InlineKeyboardButton(text="π₯ Semua", callback_data="EVE"),
            InlineKeyboardButton(text="π Admin", callback_data="AMS"),
        ],
        [
            InlineKeyboardButton(
                text="π Pengguna Resmi", callback_data="USERLIST"
            )
        ],
        [InlineKeyboardButton(text="π Kembali", callback_data="settingm")],
    ]
    return f"π§  **Pengaturan {MUSIC_BOT_NAME}**", buttons


def dashmarkup():
    buttons = [
        [
            InlineKeyboardButton(text="βοΈ Uptime", callback_data="UPT"),
            InlineKeyboardButton(text="πΎ Ram", callback_data="RAT"),
        ],
        [
            InlineKeyboardButton(text="π» Cpu", callback_data="CPT"),
            InlineKeyboardButton(text="π½ Disk", callback_data="DIT"),
        ],
        [InlineKeyboardButton(text="π Kembali", callback_data="settingm")],
    ]
    return f"π§  **Pengaturan {MUSIC_BOT_NAME}**", buttons
