# encoding: utf-8

import os
# os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
from functools import partial
import codecs
from threading import Thread
import json
os.environ["KIVY_VIDEO"] = "ffpyplayer"
import sys
from traceback import print_exc
import requests

from functools import partial

import kivy
import kivyblocks
from kivy.config import Config
from kivy.resources import resource_add_path
resource_add_path(os.path.join(os.path.dirname(kivyblocks.__file__),'./ttf'))
Config.set('kivy', 'default_font', [
        'msgothic',
        'DroidSansFallback.ttf'])


from kivy.app import App
from kivy.utils import platform
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.logger import Logger
from kivy.uix.label import Label
from kivy.factory import Factory
from kivy.uix.boxlayout import BoxLayout

import plyer

from appPublic.folderUtils import ProgramPath
from appPublic.jsonConfig import getConfig
from appPublic.Singleton import GlobalEnv
from appPublic.uniqueID import getID
from appPublic.registerfunction import RegisterFunction

from kivyblocks.blocksapp import BlocksApp
from kivyblocks.blocks import registerWidget, Blocks
from kivyblocks.pagescontainer import PageContainer
from kivyblocks.utils import *
from kivyblocks.dg import DataGrid
from kivyblocks.baseWidget import *
from kivyblocks.threadcall import HttpClient
from appPublic.find_player import BroadcastServer, find_players
from appPublic.background import Background
from kivyblocks.player_osc import PlayerOSCServer
from kivyblocks.threadcall import Workers
from loadplugins import load_plugins

r = Factory.register

def changeDesktopFontSize():
	desktopOSs=[
		"win",
		"linux",
		"macosx"
	]
	if not platform in desktopOSs:
		return 
	config = getConfig()
	d = {k:v+3.0 for k,v in config.font_sizes.items()}
	config.font_sizes = d
	
class DoodahApp(BlocksApp):
	def build(self):
		load_plugins(ProgramPath())
		x = super().build()
		return x
	
if __name__ == '__main__':
	pp = workdir = ProgramPath()
	print('ProgramPath=',pp,'workdir=',workdir)
	config = getConfig(workdir,NS={'workdir':workdir,'ProgramPath':pp})
	changeDesktopFontSize()
	myapp = DoodahApp()
	ge = GlobalEnv()
	# Window.maximize()
	myapp.run()

