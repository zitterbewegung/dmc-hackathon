with open("data2012.json", "r") as f:
    with open("dataprocessed.json", 'w+') as p:
        p.write("[")
        for line in f:
            line = line + ','
            p.write(line)
            print "."
        p.write("]")
