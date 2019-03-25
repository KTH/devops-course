.PHONY: clean

%.pdf:
	pandoc --filter=pandoc-citeproc meta.yaml $(basename $@).md -t beamer --toc -o $@

clean:
	rm -f *.pdf *.tex
