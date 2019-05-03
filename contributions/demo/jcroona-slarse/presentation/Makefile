.PHONY: clean

%.pdf:
	pandoc meta.yaml $(basename $@).md -t beamer --toc -o $@

clean:
	rm -f presentation.pdf *.tex
