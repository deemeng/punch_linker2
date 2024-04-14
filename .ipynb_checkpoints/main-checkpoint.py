# https://www.docker.com/blog/how-to-dockerize-your-python-applications/

import os

import numpy as np
import pandas as pd
import torch
from Bio import SeqIO

import json
import datetime
import time
import argparse
import shutil

from utils.common import dump_list2json, read_json2list
import params.filePath as paramF
import params.hyperparams as paramH

from model.utils import load_model
from utils.ensemble import generate_models, ensemble_predict

from utils.prediction import get_pred_label, save_prediction, save_timing
from params.utils import create_folder

if __name__ == "__main__":
    
    comment = f'Running PUNCH_Linker, started {str(datetime.datetime.now())}'
    print(comment)
    '''
    1. JSON file
    '''
    # get FASTA file
    fasta_sequences = SeqIO.parse(open(paramF.path_input),'fasta')
    list_entity = []
    for entity in fasta_sequences:
        dict_e = {}
        dict_e['id'], dict_e['sequence'] = entity.id, str(entity.seq)
        list_entity.append(dict_e)

    # save JSON file
    dump_list2json(list_entity, paramF.path_input_json)

    '''
    2. Predictor
    '''
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print('Using device:', device)
    
    # model_pth = os.path.join(path_output, f'trained_model/{featureType}/{model_name}.pth')
    list_modelInfo_protTrans = [{'model_name':f'{paramH.netNames[1][6:]}_protTrans.pth_f{i}', 'net_name': paramH.netNames[1], 'lr':paramH.lr, 'dropout':paramH.dropout, 'featureType': paramH.dict_featureType[2]}  for i in range(1, 6)]
    list_modelInfo_msaTrans = [{'model_name':f'{paramH.netNames[1][6:]}_msa_transformer.pth_f{i}', 'net_name': paramH.netNames[1], 'lr':paramH.lr, 'dropout':paramH.dropout, 'featureType': paramH.dict_featureType[3]}  for i in range(1, 6)]
    list_modelInfo_msaTrans_len10 = [{'model_name':f'len10_{paramH.netNames[1][6:]}_msa_transformer.pth_f{i}', 'net_name': paramH.netNames[1], 'lr':paramH.lr, 'dropout':paramH.dropout, 'featureType': paramH.dict_featureType[3]}  for i in range(1, 6)]


    list_modelInfo = list_modelInfo_msaTrans + list_modelInfo_protTrans + list_modelInfo_msaTrans_len10
    models = generate_models(list_modelInfo)

    '''
    3. Prediction & saving results
    '''
    list_entity = read_json2list(paramF.path_input_json)
    
    list_seq_id = []
    list_timing = []

    for entity in list_entity:
        t_start = round(time.time() * 1000)
        entity_id = entity['id']
        entity_seq = entity['sequence']
        entity_length = len(entity_seq)
        msaTrans = True
        if entity_length>1022:
            msaTrans = False
        # get prediction
        avg_pred = ensemble_predict(models, list_modelInfo, entity_id, paramF.path_msaTrans, paramF.path_protTrans, msaTrans)
        pred_label = get_pred_label(avg_pred, threshold=paramH.label_threshold)
        predInfo = {'id': entity_id, 'sequence': entity_seq, 'pred': avg_pred.tolist(), 'label': pred_label}
        
        t_end = round(time.time() * 1000)
        timing = t_end - t_start
        
        list_seq_id.append(entity_id)
        list_timing.append(timing)
        # saving
        save_prediction(paramF.path_prediction, predInfo)
    
    '''
    4. Addictional output: timing
    '''
    # saving timings
    save_timing(paramF.path_time, list_seq_id, list_timing, comment='')

    print(f'Output (prediction): {paramF.path_prediction}')
    print(f'Additional Output (timings): {paramF.path_time}')
    
    os.remove(paramF.path_input_json)
    shutil.rmtree(paramF.path_seq)