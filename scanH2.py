from diffiqult.Basis import basis_set_3G_STO as basis
#from diffiqult.Basis import basis_set_6G_STO_uncontracted as basis
from diffiqult.Molecule import System_mol
from diffiqult.Task import Tasks
import diffiqult.Energy
import diffiqult.Task
from algopy import UTPM
import numpy as np

# set up meta data
d = -1.64601435
mol = [(1,(0.0,0.0,0.20165898)),(1,(0.0,0.0,d))]
ne = 2
system = System_mol(mol,basis,ne,shifted=False,mol_name='agua')
manager = Tasks(system, name='h2_sto_3g',verbose=True)

# calculate SCF energy
print 'EnergyH2', diffiqult.Energy.rhfenergy(*manager._energy_args())

# calculate derivatives
args = list(manager._energy_args())

for lval in np.linspace(-1, 1, 200):
	cfdargs = list(manager._energy_args())
	cfdargs[4] = [1+lval, 1-lval]
	cfd = diffiqult.Energy.rhfenergy(*cfdargs)
	print lval, cfd
