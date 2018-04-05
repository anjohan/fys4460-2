all:
	$(MAKE) report.pdf

report.pdf: report.tex sources.bib cd/in.script cd/make_spheres.py e/in.script e/make_spheres.py e/data/temp.dat
	mkdir -p data
	latexmk -pdflua -shell-escape report

e/data/temp.dat: e/data/log.simulation
	logplotter.py -i e/data/log.simulation -l0 "Step v_mytime" -x "v_mytime" -y "c_mytemp" --noplot --dump e/data/temp.dat
e/data/log.simulation: e/in.script e/make_spheres.py e/delete_half_of_moving.py
	cd e; lmp_mpi -in in.script

clean:
	latexmk -c
	rm -rf __pycache__ pythontex-files-report *.pytxcode *.auxlock *.run.xml data *.bbl report.pdf
