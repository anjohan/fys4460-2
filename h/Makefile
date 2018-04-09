all: data/v.dat data/vxcm.dat

data/v.dat: data/dump.flow velocity_distribution.py
	python velocity_distribution.py
data/dump.flow: in.script
	lmp_mpi -in in.script
data/vxcm.dat: data/dump.flow
	logplotter.py -i data/log.flow -l0 "Step v_mytime" -x v_mytime -y v_vcmx_moving --noplot --dump "data/vxcm.dat"
