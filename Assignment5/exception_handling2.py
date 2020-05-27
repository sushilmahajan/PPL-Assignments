def write_file():
    try:
        filename = input("Enter a file name:")
        f = open(filename, 'w')
        f.write("Wrote this using a python script")
    except OSError:
        print("You don't have write permission for this file")
    else:
        print("Written to the file successfully")
    finally:
        print("This will always get executed")

write_file()
