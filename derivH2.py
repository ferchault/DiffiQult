from diffiqult.Basis import basis_set_3G_STO as basis
#from diffiqult.Basis import basis_set_6G_STO_uncontracted as basis
#from diffiqult.Basis import def2TZVP as basis
from diffiqult.Molecule import System_mol
from diffiqult.Task import Tasks
import diffiqult.Energy
import diffiqult.Task
from algopy import UTPM
import numpy as np

# set up meta data
d = -1.64601435
mol = [(6,(0.0,0.0,0.20165898)),(8,(0.0,0.0,d))]
ne = 14
system = System_mol(mol,basis,ne,shifted=False,mol_name='agua')
manager = Tasks(system, name='h2_sto_3g',verbose=True)

# calculate SCF energy
#print 'EnergyH2', diffiqult.Energy.rhfenergy(*manager._energy_args())

# calculate derivatives
args = list(manager._energy_args())

D = 20; P = 1
x = UTPM(np.zeros((D, P, 2, 1)))
x.data[0, 0] = 0
x.data[1, 0] = 1

args[4] = [1+x, 1-x]
args[-1]= x
args = tuple(args)

y = diffiqult.Energy.rhfenergy(*(args))
#print 'derivatives', y.data

# calculate target energy
heargs = list(manager._energy_args())
heargs[4] = [7, 7]
#print 'EnergyTarget', diffiqult.Energy.rhfenergy(*heargs)
