# Comparative modeling with multiple templates
from modeller import *              # Load standard Modeller classes
from modeller.automodel import *    # Load the automodel class
from modeller.parallel import *
from myModel import MyModel
import random
import sys


### add random negative number to make sure each model will be different
r = random.uniform(2,50000)
nr = round(r*-1)

sequence_file = sys.argv[1]
sequence_name = sys.argv[1].split(".")[0]

print(sequence_name)

ali_file = sys.argv[1]

#open
#template = ('7kox')

#closed
template = ('6uwz','7koo','MLA')

#desensitized
#template = ('5kxi','6pv7','7koq')

log.verbose()    # request verbose output
env = environ(rand_seed=nr)  # create a new MODELLER environment to build this model in

env.io.hetatm = False

# directories for input atom files
env.io.atom_files_directory = ['.', '/TEMPLATES']
# Read in HETATM records from template PDBs
env.io.hetatm = True

a = MyModel(env, sequence = sequence_name,
            # alignment file with template codes and target sequence
            alnfile = ali_file,
            # PDB codes of the templates
            knowns = template
            )

# index of the first model
# index of the last model
# (determines how many models to calculate)
# do the actual comparative modeling
a.starting_model= 1
a.ending_model  = 1

# Very thorough VTFM optimization:
a.library_schedule = autosched.slow

# Thorough MD optimization:
a.md_level = refine.slow

# Repeat the whole cycle 2 times and do not stop unless obj.func. > 1E6
#a.repeat_optimization = 2
#a.max_molpdf = 1e6

# Assesses the quality of models using
# the DOPE (Discrete Optimized Protein Energy) method (Shen & Sali 2006)
# and the GA341 method (Melo et al 2002, John & Sali 2003)
a.assess_methods = (assess.GA341, assess.DOPE,assess.normalized_dope)

a.make()