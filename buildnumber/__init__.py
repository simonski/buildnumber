from buildnumber import objects, utils, constants


def do_help():
    print("buildnumber, usage:")
    print("")
    print(
        "buildnumber COMMAND OPTIONS   (-name <app name>) (-file <override filename>)"
    )
    print("")
    print("  increment          - increment by 1   (-dry_run - no increment)")
    print("  get                - print current version")
    print("  set N              - force the version to a value")
    print("  help               - show this help")
    print("  version            - print the version of buildnumber")
    print("")


def main():
    cli = utils.CLI()
    command = cli.get_command()
    if cli.contains("-f"):
        filename = cli.get("-f")
    else:
        filename = "Buildfile"

    name = cli.get_or_default("-name", "default")

    if command == "increment":
        bf = objects.Buildfile(filename)
        bf.increment(name)
        if not cli.contains("-dry_run"):
            bf.save()
        print(bf.get(name))

    elif command == "version":
        print(str(constants.VERSION))

    elif command == "set":
        bf = objects.Buildfile(filename)
        value = cli.get_or_die("set")
        bf.set(name, value)
        if not cli.contains("-dry_run"):
            bf.save()
        print(bf.get(name))

    elif command == "help":
        do_help()

    elif command == "get":
        bf = objects.Buildfile(filename)
        print(bf.get(name))

    else:
        do_help()
