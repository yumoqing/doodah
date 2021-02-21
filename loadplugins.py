import os
import sys

from appPublic.folderUtils import listFile
from appPublic.ExecFile import ExecFile

def load_plugins(p_dir):
	ef = ExecFile()
	pdir = os.path.join(p_dir, 'plugins')
	sys.path.append(pdir)
	for py in listFile(pdir, suffixs=['py'], rescursive=False):
		ef.set('sys',sys)
		ef.run(py)

