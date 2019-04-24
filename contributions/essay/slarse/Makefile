.PHONY: clean all build

IMAGE_SRC = $(wildcard images/*.svg)
IMAGE_OUT = $(patsubst images/%.svg, images/%.png, $(IMAGE_SRC))

all: clean build

build: $(IMAGE_OUT) graph_introduction.pdf
	
images/%.pdf: images/%.svg
	inkscape -D -z --file=$< --export-pdf $@

images/%.png: images/%.svg
	inkscape -D -z --file=$< --export-dpi 300 --export-png $@

%.pdf:
	pandoc --filter=pandoc-tablenos --filter=pandoc-fignos --filter=pandoc-citeproc meta.yaml $(basename $@).md -o $@

%.html:
	pandoc --number-sections --from markdown --css pandoc.css -s --highlight-style pygments --filter=pandoc-tablenos --filter=pandoc-fignos  --filter=pandoc-citeproc meta.yaml $(basename $@).md -o $@

clean:
	rm -f *.pdf *.tex *.html
