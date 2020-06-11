test: light.mdl main.py matrix.py mdl.py display.py draw.py gmath.py
	python main.py light.mdl
	magick convert simple_20020.ppm image.png
clean:
	rm *pyc *out parsetab.py

clear:
	rm *pyc *out parsetab.py *ppm
