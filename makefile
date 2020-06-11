test: light.mdl main.py matrix.py mdl.py display.py draw.py gmath.py
	python main.py light.mdl
	magick convert simple_20000.ppm beg.png
	magick convert simple_20010.ppm mid.png
	magick convert simple_20019.ppm end.png
clean:
	rm *pyc *out parsetab.py

clear:
	rm *pyc *out parsetab.py *ppm
