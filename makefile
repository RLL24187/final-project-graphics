test: cylinder.mdl main.py matrix.py mdl.py display.py draw.py gmath.py
	python main.py cylinder.mdl
	magick convert pic.ppm image.png
	imdisplay image.png

clean:
	rm *pyc *out parsetab.py

clear:
	rm *pyc *out parsetab.py *ppm
