test: light.mdl main.py matrix.py mdl.py display.py draw.py gmath.py
	python main.py light.mdl

clean:
	rm *pyc *out parsetab.py parser.out

clear:
	rm *pyc *out parsetab.py *ppm
