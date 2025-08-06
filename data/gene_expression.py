import synapseclient 
import synapseutils
from dotenv import load_dotenv
import os

load_dotenv()

syn = synapseclient.Synapse() 
syn.login(authToken=os.getenv("SYNAPSE_API_KEY")) 

# loading in datasets
gene_expression = synapseutils.syncFromSynapse(syn, 'syn23650894') 
rosmap_metadata = synapseutils.syncFromSynapse(syn, '21073536')
rosmap_clinical = synapseutils.syncFromSynapse(syn, '3191087')
imaging_immunofluorescense = synapseutils.syncFromSynapse(syn, '5477198')
rosmap_rna_mapping = synapseutils.syncFromSynapse(syn, '34572333')