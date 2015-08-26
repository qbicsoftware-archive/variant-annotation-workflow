from CTDopts.CTDopts import _InFile, CTDModel, args_from_file
import sys
import os
import subprocess

wf_dir = sys.argv[1]
ctd_files = args_from_file(wf_dir + '/IN-FILESTOSTAGE')


command = './annotateVariants.sh '

data_path = '%s/data/' % wf_dir
result_path = '%s/result/' % wf_dir

files = []

for f in ctd_files["input"]:
	fileName = f.split('/')[-1]
        command += ('%s' % (data_path, fileName))

command += '%s ' % wf_dir 
command += '%s ' fileName

subprocess.call(command.split())
