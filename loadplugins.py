import os

from kivy.logger import Logger
from kivy.app import App
from kivy.factory import Factory

from appPublic.folderUtils import ProgramPath, listFile
from appPublic.ExecFile import ExecFile

def register_widget(name, klass):
	try:
		Factory.regiter(name, klass)
	except:
		Logger.Error(f'Plugin : register_widget():{name} register error')

def register_registerfunction(name, func):
	rf = RegisterFunction()
	try:
		rf.add(name, function)
	except:
		Logger.Error(f'Plugin :register_registerfunction():{name} register error')

def register_blocks(name, value):
	b = Factory.Blocks()
	try:
		b.register_widget(name, value)
	except:
		Logger.Error(f'plugin : register_blocks():{name} register error')

def load_plugins(p_dir):
	ef = ExecFile()
	ef.set('register_blocks', register_blocks)
	ef.set('register_registerfunction', register_registerfunction)
	ef.set('register_widget', register_widget)
	ef.set('Factory', Factory)
	ef.set('Blocks', Blocks)

	pdir = os.path.join(p_dir, 'plugins')
	
	for py in listFile(pdir, subfixes=['py'], rescusive=True):
		ef.run(py)

