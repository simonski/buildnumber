# buildnumber

## Introduction

`buildnumber` is a terminal tool that maintains a yaml `Buildfile` in the current directory with an ascending integer.  A future version will support semantic.


## Installation

	pip install buildnumber
	
## Usage

In your current directory, a file `Buildfile` will be created and maintained by `buildnumber`.  I use a single `Buildfile` per project.

To see the current buildnumber 

`buildnumber get`

To increment it

`buildnumber increment`

To see what the next number is without incrementing

`buildnumber increment -dry_run`

To force set a number

`buildnumber set N`

To see help

`buildnumber help`

To get the version of buildnumber itself

`buildnumber version`

## Options

|option|description|
|------|------------
`-name` |By default, the namespace `default` will be used as the application name.  If you want to maintain multiple buildnumbers, use `-name xxx` for each different thing you maintain.
`-file`|The file `Buildfile` will be read/written to in the current directory.  If you want to use a different file, use `-file`|

## Developing

Pull requests welcome!

	git clone github.com/simonski/buildnumber
	cd buildnumber
	mkvirtualenv buildnumber
	pip install -e .

## Future Plans

- Semantic versioning.
- Build history (when it was incremented)
