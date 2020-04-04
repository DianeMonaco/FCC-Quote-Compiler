quotesFile = open('raw quotes.txt', 'r')
rawLines = quotesFile.readlines()
lines = []

for line in rawLines:
    lines.append(line.strip())

quotesFile = quotesFile.close()

quotesDB = open('quotes.json', 'w')
quotesDB.write('{ "quotes": [\n')

for i in range(0, len(lines) - 2, 2):
    quotesDB.write('    { "quote": "' + lines[i] + '", "author": "' + lines[i+1] + '" },\n' )

quotesDB.write('    { "quote": "' + lines[-2] + '", "author": "' + lines[-1] + '" }\n  ]\n}')
