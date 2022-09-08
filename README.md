
# Homology Modeling of nAChR a4a5b2

##### MODELLER
These restrains are on myModel.py. These restraints include:<br>

1. Include ligand to model the binding pocket.<br>
2. Make a restraint to insure the proline in the ECD-TMD interface is in cis conformation.<br>
3. Disulfide bonds.<br>
4. Impose end of MA helix in the open state to be an alpha-helix.<br>
5. Symmetry between alpha and beta subunits.<br>

Scores are: DOPE, GA341, zDOPE and procheck per chain.<br>

To run modeller in paraller with slurm run makemodels_slurm.sh