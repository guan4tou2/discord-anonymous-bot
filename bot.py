import discord
from discord.ext import commands
import tkinter as tk
import threading

bot=commands.Bot(command_prefix='')
channel_id=0

win=tk.Tk()
win.title("AnonymousBOT")
win.geometry("270x225")
win.resizable(0,0)
win.config(bg='#1E1E1E')

@bot.event 
async def on_ready():
    win.config(bg='#C3602C')
    print('---Bot is online---')

@bot.command()
async def dm(ctx,content):
    channel=bot.get_channel(channel_id)
    await channel.send(f'{content}')

def start_bot():
    channel_id=chen.get()
    token=toen.get()
    if len(channel_id)==18 and len(token)>50:
        bot.run(token)

def thread(func):
    t=threading.Thread(target=func)
    t.setDaemon(True)
    t.start()

chlab=tk.Label(text='Channel ID',bg='#1E1E1E',fg='#CCCCCC',font="20")
chlab.place(x=10,y=10,height=30)

chen=tk.Entry(bg='#CCCCCC')
chen.place(x=110,y=10,height=30)

tolab=tk.Label(text='Token',bg='#1E1E1E',fg='#CCCCCC',font="20")
tolab.place(x=10,y=45,height=30)

toen=tk.Entry(bg='#CCCCCC')
toen.place(x=110,y=45,height=30)

start=tk.Button(text="Start",font="50")
start.config(bg='#252526',fg='#CCCCCC')
start.config(command=lambda : thread(start_bot))
start.place(anchor='center',x=135,y=150)

win.mainloop()
