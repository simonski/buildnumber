# buildnumber

## Introduction

`buildnumber` is a terminal tool that maintains build numbers.

The yaml file `Buildfile` is created in the current directory.  You can choose either `integer` or [`semantic` versioning](https://semver.org).

The `Buildfile` can contain an arbitrary number of build numbers; you refer to each one by its `name`.

## Installation

	pip install buildnumber

## Usage

Please read the [USER GUIDE](USER_GUIDE.md)

## Developing

Open source - fork and pull requests welcome!

	git clone github.com/simonski/buildnumber
	cd buildnumber/python
	mkvirtualenv buildnumber
	make 
	make build

## Future Plans

- Build history (when it was incremented)
- Document the yaml as a specification
- snapshotting/release mode?
- API for talking back to the Buildfile
- `brew install buildnumber`
- go implementation
- **DONE v1.0.1** Semantic versioning.

