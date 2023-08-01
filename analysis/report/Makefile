report.pdf: $(wildcard ../out/*) report.tex
	pdflatex -halt-on-error report.tex
	pdflatex -halt-on-error report.tex

clean:
	rm -rf *.aux *.log *.out *.pdf *.bbl *.blg