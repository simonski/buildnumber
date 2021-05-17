# buildnumber

## Installation

	pip install buildnumber
	
## Usage

In your current directory, a file `Buildfile` will be created and maintained by `buildnumber`.  I use a single `Buildfile` per project.

## Initial setup

	buildnumber init

### To see the current buildnumber

	buildnumber get

### To increment it

`buildnumber increment` or `buildnumber inc` will increment by 1 the build, either by `major`, `minor`, or `revision`

So, to incrment the revision, specify

	buildnumber inc revision

> By default you can omit `revision` and your version will increase.

`buildnumber inc minor` increases the major version (e.g. 1.2.3 > 2.0.0)

`buildnumber inc major` increases the munor version (e.g. 1.2.3 > 1.3.0)

> **Note**: incrementing the verison will set to 0 the "relavtive minor" versions.

## Force a version

`buildnumber set 1.2.3` will **force** the version to 1.2.3

## To see what the next number is without incrementing

`buildnumber inc revision -dry_run`

Will print to STDOUT what the version will be without actually changing it.

### To see help

`buildnumber help`

### To get the version of buildnumber itself

`buildnumber version`

## Options

|option|description|
|------|------------
`-name` |By default, the name `default` will be used. If you want to maintain multiple buildnumbers in the same file, use `-name xxx` for each different thing you maintain.
`-file`|The file `Buildfile` will be read/written to in the current directory.  If you want to use a different file, use `-file`|

