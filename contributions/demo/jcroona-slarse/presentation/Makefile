.PHONY: clean

%.pdf:
	pandoc meta.yaml $(basename $@).md -t beamer -o $@

clean:
	rm -f presentation.pdf *.tex
