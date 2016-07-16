#itamcojson2012.json
import ijson
parser = ijson.parse(open("dataprocessed.json"))
for prefix, event, value in parser:
    print prefix, event, value

