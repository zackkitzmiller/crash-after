from crash_after import crash_after


@crash_after(date="09/07/2023")
def ok():
    print("ok")


@crash_after(date="09/07/1985")
def crash():
    print("oh no")


if __name__ == "__main__":
    ok()
    crash()
    ok()
    ok()
    crash()
