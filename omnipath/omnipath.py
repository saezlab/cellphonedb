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

from pypath import main
from pypath import intercell
from pypath import cellphonedb

output_dir = os.path.join(
    '..',
    'cellphonedb',
    'src',
    'core',
    'data',
)

c = cellphonedb.CellPhoneDB(output_dir = output_dir)
c.main()
