import sys
from buildnumber import objects, utils, constants


def do_help():
    print("buildnumber, usage:")
    print("")
    print(
        "buildnumber COMMAND OPTIONS   (-name <app name>) (-file <override filename>)"
    )
    print("")
    print("  init       -type integer|semantic   - initialise a Buildfile entry")
    print(
        "  increment (major|minor|revision)    - increment by 1 (-dry_run - no increment)"
    )
    print("  get                                 - print current version")
    print("  help                                - show this help")
    print("  version                             - print the version of buildnumber")
    print("")


def main():
    cli = utils.CLI()
    command = cli.get_command()
    if cli.contains("-f"):
        filename = cli.get("-f")
    else:
        filename = "Buildfile"

    name = cli.get_or_default("-name", "default")

    if command == "init":
        bf = objects.Buildfile(filename)
        init_type = cli.get_or_die("-type")
        if init_type not in ["integer", "semantic"]:
            print("Error -type must be 'integer' or 'semantic'")
            sys.exit(1)

        bf.init(name, init_type)
        bf.increment(name)
        if not cli.contains("-dry_run"):
            bf.save()
        print(bf.get(name))

    elif command == "increment":
        bf = objects.Buildfile(filename)
        increment_type = cli.get_or_default("increment", "revision")
        if increment_type not in ["major", "minor", "revision"]:
            print("Error, increment type must be 'major', 'minor' or 'revision'")
            sys.exit(1)

        bf.increment(name, increment_type)
        if not cli.contains("-dry_run"):
            bf.save()
        print(bf.get(name))

    elif command == "version":
        print(str(constants.VERSION))

    elif command == "help":
        do_help()

    elif command == "get":
        bf = objects.Buildfile(filename)
        print(bf.get(name))

    else:
        do_help()
