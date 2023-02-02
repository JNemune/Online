from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pyrogram import Client, types
from pyrogram.raw import functions

app = Client("online")
scheduler = AsyncIOScheduler()


@app.on_user_status()
async def awake_on_status(client: Client, user: types.user_and_chats.user.User):
    if user.id == 0000000000: # your user id
        if user.status == user.status.OFFLINE:
            await app.invoke(functions.account.UpdateStatus(offline=False))


async def awake_on_schedule():
    await app.invoke(functions.account.UpdateStatus(offline=False))


scheduler.add_job(awake_on_schedule, "interval", seconds=300)


if __name__ == "__main__":
    scheduler.start()
    app.run()
