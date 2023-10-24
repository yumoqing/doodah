import os
import sys

from appPublic.folderUtils import listFile
from appPublic.ExecFile import ExecFile

from kivy.logger import Logger

def load_plugins(p_dir):
	ef = ExecFile()
	pdir = os.path.join(p_dir, 'plugins')
	if not os.path.isdir(pdir):
		Logger.error('load_plugins:%s not exists', pdir)
		return
	sys.path.append(pdir)
	for py in listFile(pdir, suffixs=['py'], rescursive=False):
		ef.set('sys',sys)
		ef.run(py)

