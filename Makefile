ifndef NOPAGER
PAGER ?= most
endif
ifdef PAGER
PAGED = | $(PAGER)
endif

.PHONY: test
test:
	nosetests --detailed-errors --with-doctest --verbose 2>&1 $(PAGED)

.PHONY: clean
clean:
	find . -name '*.py[co]' -exec rm -f {} ';'
