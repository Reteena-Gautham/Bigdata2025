import synapseclient 
import synapseutils
from dotenv import load_dotenv
import os

load_dotenv()

syn = synapseclient.Synapse() 
syn.login(authToken=os.getenv("SYNAPSE_API_KEY")) 
files = synapseutils.syncFromSynapse(syn, 'syn23650894') 
