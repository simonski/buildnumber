default_target: build
.PHONY : default_target upload

# VERSION := $(shell $(PYTHON) setup.py --version)

clean:
	rm -rf build

test:
	#go test

build: clean test
	mkdir -p build
	go build src/lib/*.go
	go build -o build/buildnumber src/main/*.go

