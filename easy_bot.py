import discord
from discord.ext import commands
import tkinter as tk
import threading

bot=commands.Bot(command_prefix='')#建立BOT實體 前綴
token=' your server token '
channel_id=your channel id

win=tk.Tk()
win.title("匿名BOT")
win.geometry("250x150")
win.resizable(0,0)
win.config(bg='#1E1E1E')

@bot.event #事件
async def on_ready():#當啟動時觸發
    win.config(bg='#C3602C')
    print('---Bot is online---')

@bot.command()
async def dm(ctx,content):
    channel=bot.get_channel(channel_id)#抓取頻道ID
    await channel.send(f'{content}')

def start_bot():
    bot.run(token)
    
def thread(func):
    t=threading.Thread(target=func)
    t.setDaemon(True)
    t.start()

start=tk.Button(text="Start",font="50")
start.config(bg='#252526',fg='#CCCCCC')
start.config(command=lambda : thread(start_bot))
start.pack()

win.mainloop()
