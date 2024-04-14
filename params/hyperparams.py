import os

dict_featureType = {1: 'onehot', 2: 'protTrans', 3: 'msa_transformer'}
dict_n_features = {'onehot': 21, 'protTrans':1024, 'msa_transformer':768}
dict_max_length = {'onehot': 40000, 'protTrans':40000, 'msa_transformer':1022}

# netName = 'model_many2one.cnnV3'
netNames = ['model.cnn2_L11', 'model.cnn2_L3_50']

# mdoel paramethers
padding = True

lr = 0.0001
dropout = 0

label_threshold = 0.07