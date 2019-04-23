.PHONY: clean

%.pdf:
	pandoc --filter=pandoc-citeproc meta.yaml $(basename $@).md -o $@

%.html:
	pandoc --filter=pandoc-citeproc meta.yaml $(basename $@).md -o $@

clean:
	rm -f *.pdf *.tex
