import json
import pathlib
from importlib.resources import files

data_path = files("meeko") / "data"

def load_amber_params():
    '''
    atom_params is a dictionary with kesys residue names and values
    a dictionary with the keys smiles, containing the resdiue smiles, atom_names,
    containing atom_names for each atom in the residue and amber_params which 
    contains amber parameters for epsilon (kcal/mol) and r_min_half for each atom_name.
    The order of the amber_params is the same as atom_names.
    '''
    atom_params = dict()
    p = pathlib.Path("residue_chem_templates")
    if (data_path / (p.name + ".json")).exists():
        filename = str(data_path / (p.name + ".json"))
        with open(filename) as fi:
            residue_chem_templates = json.load(fi)
        for residue, data in residue_chem_templates["residue_templates"].items():
            if "amber_params" in data:
                atom_params["residue"] = {"smiles": data["smiles"], 
                                        "atom_name": data["atom_name"],
                                        "amber_params": data["amber_params"]}
    return atom_params
        
    