from modeller import *
from modeller.automodel import *
from modeller.scripts import cispeptide

class MyModel(automodel):
    def special_restraints(self, aln):

        # Impose alpha secondary structure a the end of MX

        #a4
        self.restraints.add(secondary_structure.alpha(self.residue_range('308:A', '323:A')))
        #b2
        self.restraints.add(secondary_structure.alpha(self.residue_range('307:C','322:C')))
        #a5
        self.restraints.add(secondary_structure.alpha(self.residue_range('309:E', '323:E')))
        #a4
        self.restraints.add(secondary_structure.alpha(self.residue_range('308:G', '323:G')))
        #b2
        self.restraints.add(secondary_structure.alpha(self.residue_range('307:I','322:I')))

        # Impose alpha secondary structure a the end of M4
        #a4
        self.restraints.add(secondary_structure.alpha(self.residue_range('53:B', '59:B')))
        #a4
        self.restraints.add(secondary_structure.alpha(self.residue_range('53:H', '59:H')))

        # Impose alpha secondary structure on helix at the beginning of a5
        #a5
        self.restraints.add(secondary_structure.alpha(self.residue_range('1:E', '3:E')))

        ## make As and Bs symetric
        #A4
        s1 = selection(self.chains['A']).only_atom_types('CA')
        s2 = selection(self.chains['G']).only_atom_types('CA')
        s3 = selection(self.chains['B']).only_atom_types('CA')
        s4 = selection(self.chains['H']).only_atom_types('CA')

        # B2
    # B2

    s5 = selection(self.chains['C']).only_atom_types('CA')
    s6 = selection(self.chains['I']).only_atom_types('CA')
    s7 = selection(self.chains['D']).only_atom_types('CA')
    s8 = selection(self.chains['J']).only_atom_types('CA')

    self.restraints.symmetry.append(symmetry(s1, s2, 1.0))
    self.restraints.symmetry.append(symmetry(s3, s4, 1.0))
    self.restraints.symmetry.append(symmetry(s5, s6, 1.0))
    self.restraints.symmetry.append(symmetry(s7, s8, 1.0))

    # Report on symmetry violations
    # self.restraints.symmetry.report(1)

    # force cis conf for Pro in c-loop
    a = self.atoms

    c='A' #a4 pro 136
    cispeptide(self.restraints,
               atom_ids1=(a['O:136:'+c], a['C:136:'+c], a['N:135:'+c], a['CA:135:'+c]),
               atom_ids2=(a['CA:136:'+c], a['C:136:'+c], a['N:135:'+c], a['CA:135:'+c]))

    c='G' #a4
    cispeptide(self.restraints,
               atom_ids1=(a['O:136:'+c], a['C:136:'+c], a['N:135:'+c], a['CA:135:'+c]),
               atom_ids2=(a['CA:136:'+c], a['C:136:'+c], a['N:135:'+c], a['CA:135:'+c]))

    c='E' # a5 137
    cispeptide(self.restraints,
               atom_ids1=(a['O:137:'+c], a['C:137:'+c], a['N:136:'+c], a['CA:136:'+c]),
               atom_ids2=(a['CA:137:'+c], a['C:137:'+c], a['N:136:'+c], a['CA:136:'+c]))

    c='C' # b2 138
    cispeptide(self.restraints,
               atom_ids1=(a['O:138:'+c], a['C:138:'+c], a['N:137:'+c], a['CA:137:'+c]),
               atom_ids2=(a['CA:138:'+c], a['C:138:'+c], a['N:137:'+c], a['CA:137:'+c]))


    c='I' # b2
    cispeptide(self.restraints,
               atom_ids1=(a['O:138:'+c], a['C:138:'+c], a['N:137:'+c], a['CA:137:'+c]),
               atom_ids2=(a['CA:138:'+c], a['C:138:'+c], a['N:137:'+c], a['CA:137:'+c]))


def special_patches(self, aln):

    # Rename both chains and renumber the residues in each
    self.rename_segments(segment_ids=['A', 'B','C','D','E','F','G','H','I','J'],
                         renumber_residues=[1,1,1,1,1,1,1,1,1,1])

    # Force disulfide bond

    #A4
    self.patch(residue_type='DISU', residues=(self.residues['192:A'], self.residues['193:A']))
    self.patch(residue_type='DISU', residues=(self.residues['128:A'], self.residues['142:A']))
    self.patch(residue_type='DISU', residues=(self.residues['192:G'], self.residues['193:G']))
    self.patch(residue_type='DISU', residues=(self.residues['128:G'], self.residues['142:G']))

    #A5
    self.patch(residue_type='DISU', residues=(self.residues['193:E'], self.residues['194:E']))
    self.patch(residue_type='DISU', residues=(self.residues['129:E'], self.residues['143:E']))

    #B2
    self.patch(residue_type='DISU', residues=(self.residues['130:C'], self.residues['144:C']))
    self.patch(residue_type='DISU', residues=(self.residues['130:I'], self.residues['144:I']))

    pass
