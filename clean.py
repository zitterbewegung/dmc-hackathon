with open("test-subset.json", "r") as f:
    with open("dataprocessed_subset.json", 'w+') as p:
        p.write("""{"root": {""")
        for line in f:
            line = line + ','
            p.write(line)
            print "."
        p.write("}")
