import os
from params.utils import create_folder

# !!! IMPORTANT
# Change this to True if you want to manually provide these paths.
user = False
'''
1. Data-Input

an example:
---------------------
path_input = '/home/dimeng/caid3/linker_long.fasta'
path_msaTrans = '/home/dimeng/project/domain_linker/data/caid/features/msaTrans'
path_protTrans = '/home/dimeng/project/domain_linker/data/caid/features/protTrans'
'''
path_input = ''
path_msaTrans = ''
path_protTrans = ''

'''
2.Output folder
    All the outputs will be stored in this folder, including
    a. timings.csv
    b. disorder folder, where will keep all the prediction resulds.
an example:
---------------------
path_output = '/home/dimeng/caid3/punch_linker_output'
'''
path_output = ''