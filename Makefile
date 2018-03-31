all:
	$(MAKE) report.pdf

report.pdf: report.tex sources.bib
	mkdir -p data
	latexmk -pdflua -shell-escape report

clean:
	latexmk -c
	rm -rf __pycache__ pythontex-files-report *.pytxcode *.auxlock *.run.xml data *.bbl report.pdf