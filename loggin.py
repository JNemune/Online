from pyrogram import Client

api_id = 12345
api_hash = "0123456789abcdef0123456789abcdef"

app = Client("online", api_id=api_id, api_hash=api_hash)

app.run()