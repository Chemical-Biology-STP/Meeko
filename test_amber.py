import meeko


mk_prep = meeko.MoleculePreparation(load_atom_params="amber")
templates = meeko.ResidueChemTemplates.create_from_defaults()
with open("/data/phd/waterkit/example/1uyg_no_ligand.pdb") as fi:
         pdbstring = fi.read()
polymer = meeko.Polymer.from_pdb_string(pdb_string=pdbstring,
                                        chem_templates=templates,
                                        mk_prep=mk_prep,
                                        allow_bad_res=True,
                                        default_altloc="A",blunt_ends = [("A:1", 0)])
