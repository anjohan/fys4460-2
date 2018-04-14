#/snippetstart/#
data/porosity_%.dat: in.script make_spheres.py delete_half_of_moving.py
	lmp_mpi -var num_spheres $* -in in.script
#/snippetend/#

data/permeability.dat: everything.py in.script make_spheres.py delete_half_of_moving.py
	python everything.py
