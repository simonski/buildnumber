# buildnumber

## Introduction

`buildnumber` is a terminal tool that maintains build numbers.

The yaml file `Buildfile` is created in the current directory.  You can choose either `integer` or [`semantic` versioning](https://semver.org).

The `Buildfile` can contain an arbitrary number of build numbers; you refer to each one by its `name`.


## Installation

	pip install buildnumber
	
## Usage

In your current directory, a file `Buildfile` will be created and maintained by `buildnumber`.  I use a single `Buildfile` per project.

### To see the current buildnumber 

`buildnumber get`

### To increment it

`buildnumber increment` or `buildnumber increment revision` to increment the revision number.
`buildnumber increment minor`
`buildnumber increment major`

### To see what the next number is without incrementing

`buildnumber increment -dry_run`

### To see help

`buildnumber help`

### To get the version of buildnumber itself

`buildnumber version`

## Options

|option|description|
|------|------------
`-name` |By default, the name `default` will be used. If you want to maintain multiple buildnumbers in the same file, use `-name xxx` for each different thing you maintain.
`-file`|The file `Buildfile` will be read/written to in the current directory.  If you want to use a different file, use `-file`|

## Developing

Pull requests welcome!

	git clone github.com/simonski/buildnumber
	cd buildnumber/python
	mkvirtualenv buildnumber
	make

## Future Plans

- Build history (when it was incremented)
- Document the yaml as a specification
- snapshotting/release mode?
- API for talking back to the Buildfile 
- `brew install buildnumber`
- go implementation
- **DONE v1.0.1** Semantic versioning.
