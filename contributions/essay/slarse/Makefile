.PHONY: clean

%.pdf:
	pandoc --filter=pandoc-tablenos --filter=pandoc-fignos --filter=pandoc-citeproc meta.yaml $(basename $@).md -o $@

%.html:
	pandoc --number-sections --from markdown --css pandoc.css -s --highlight-style pygments --filter=pandoc-tablenos --filter=pandoc-fignos  --filter=pandoc-citeproc meta.yaml $(basename $@).md -o $@

clean:
	rm -f *.pdf *.tex *.html
