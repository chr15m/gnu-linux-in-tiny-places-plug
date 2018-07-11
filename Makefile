index.html: README.md res/* res res/fonts/fonts.css
	markdown-to-slides --include-remark -s res/style.css $< > $@

res/fonts/fonts.css:
	cd res && goofoffline "http://fonts.googleapis.com/css?family=Cutive+Mono|Alegreya"
	touch res/fonts/fonts.css

.PHONY: watch serve

watch:
	while [ 1 ]; do $(MAKE) -q || $(MAKE); sleep 1; done

serve:
	python -m SimpleHTTPServer

