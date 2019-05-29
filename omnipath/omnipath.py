#!/usr/bin/env python
#-*- coding: utf-8 -*-

# Copyright (c) 2019
# Dénes Türei
# turei.denes@gmail.com
# SysBioMed Group (Saez-Rodriguez Group)
# http://saezlab.org/
# BioQant Center, Faculty of Medicine, Heidelberg University
# JRC-COMBINE, Uniklinik RWTH Aachen
#
# Free to use according to the MIT License terms:
# https://directory.fsf.org/wiki/License:Expat

import os
import copy

from pypath import main
from pypath import data_formats
from pypath import intercell
from pypath import cellphonedb
from pypath import settings

settings.setup(network_expand_complexes = False)

output_dir = os.path.join(
    '..',
    'cellphonedb',
    'src',
    'core',
    'data',
)

network_pickle_path = 'omnipath_for_cellphonedb.pickle'

network = main.PyPath()

if os.path.exists(network_pickle_path):
    
    network.load_network(pfile = network_pickle_path)
    
else:
    
    network_input = copy.deepcopy(data_formats.omnipath)
    network_input.update(data_formats.ligand_receptor)
    network_input.update(data_formats.ptm_misc)
    network.load_omnipath(omnipath = network_input, remove_htp = False)

c = cellphonedb.CellPhoneDB(
    network = network,
    output_dir = output_dir,
)
c.main()
