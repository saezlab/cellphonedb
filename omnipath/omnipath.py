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

from pypath import omnipath
from pypath import cellphonedb
from pypath import settings


class OmnipathCellphonedb(omnipath.OmniPath):
    
    
    def __init__(
        self,
        output_dir = None,
        network_pickle = None,
        annotation_pickle = None,
        intercell_pickle = None,
        complex_pickle = None,
    ):
        
        settings.setup(network_expand_complexes = False)
        
        self.output_dir = (
            output_dir or
            os.path.join(
                '..',
                'cellphonedb',
                'src',
                'core',
                'data',
            )
        )
        
        self.network_pickle = (
            network_pickle or 'omnipath_for_cellphonedb.pickle'
        )
        self.intercell_pickle = (
            intercell_pickle or 'omnipath_intercell.pickle'
        )
        self.annotation_pickle = (
            annotation_pickle or 'omnipath_annot.pickle'
        )
        self.complex_pickle = (
            complex_pickle or 'omnipath_complexes.pickle'
        )
        
        omnipath.OmniPath.__init__(self)
    
    
    def main(self):
        
        omnipath.OmniPath.main(self)
        self.build()
    
    
    def build(self):
        
        self.cellphonedb = cellphonedb.CellPhoneDB(
            network = self.network,
            annotation = self.intercell,
            output_dir = output_dir,
        )
        self.cellphonedb.main()
