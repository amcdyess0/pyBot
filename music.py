import discord
from discord.ext import commands
import youtube_dl
from youtube_search import YoutubeSearch
import discord.voice_client

class music(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def join(self, ctx):
        await ctx.send("General commands:\n\n"+
        "?assistance - shows this comment again\n\n"+
        "?join - places bot into channel\n\n?"+
        "play <keywords> - finds the song on youtube and plays it in your current channel. Will resume playing the current song if it was paused\n"+
        "?pause - pauses the current song being played or resumes if already paused\n\n"+
        "?resume - resumes playing the current song\n\n"+
        "?disconnect - disconnects bot from server\n\n"+
        "NOTE: THIS BOT ONLY WORKS IN VOICE CHANNELS!!!!!!")

        if ctx.author.voice is None:
            await ctx.send("OOPS! This is not a voice channel...")
        voice_channel = ctx.message.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)
            
    
    @commands.command()
    async def disconnect(self,ctx):
        await ctx.voice_client.disconnect()
    
    @commands.command()
    async def play(self,ctx,url):
        ctx.voice_client.stop()
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 
        'options': '-vn'}
        YDL_OPTIONS = {'format':"bestaudio"}
        vc = ctx.voice_client

        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
            vc.play(source)

    @commands.command()
    async def pause(self,ctx):
        await ctx.voice_client.pause()  
        await("Paused")   

    @commands.command()
    async def resume(self,ctx):
        await ctx.voice_client.resume()  
        await("Resumed") 

    @commands.command()
    async def assistance(self,ctx):
        await ctx.send("General commands:\n"+
        "?assistance - displays all the available commands\n"+
        "?join - places bot into channel\n?"+
        "play <keywords> - finds the song on youtube and plays it in your current channel. Will resume playing the current song if it was paused\n"+
        "?pause - pauses the current song being played or resumes if already paused\n"+
        "?resume - resumes playing the current song\n"+
        "?disconnect - disconnects bot from server")

        
def setup(client):
    client.add_cog(music(client))


        
