index.html: README.md res/* res res/fonts/fonts.css
	markdown-to-slides -s res/style.css $< > $@

res/fonts/fonts.css:
	cd res && goofoffline "http://fonts.googleapis.com/css?family=Cutive+Mono|Alegreya"
	touch res/fonts/fonts.css

.PHONY: watch

watch:
	while [ 1 ]; do make -q || make; sleep 1; done

