import sys

def operate(filename,outfile = 'output.bf',m = '1'):
  f = open(filename,'r')
  if m == '1': o = beguile(f.read())
  else: o = normalize(f.read())
  f.close()
  wf = open(outfile,'w')
  wf.write(o)
  wf.close()

def beguile(code):
    code = cleanup(code)
    lib = ['>','<','+','-','[',']','.',',']
    octc = ''
    beguiled = ''
    for i in range(len(code)): octc = octc + str(lib.index(code[i]))
    for i in range(len(octc)):
        if i%2 == 0:
            for j in range(3): lib[j], lib[7-j] = lib[7-j], lib[j]
        else: lib.insert(0, lib.pop())
        beguiled = beguiled + lib[int(octc[i])]
    return beguiled

def normalize(code):
    origlib = ['>','<','+','-','[',']','.',',']
    lib = ['>','<','+','-','[',']','.',',']
    octc = ''
    normalized = ''
    for i in range(len(code)):
        if i%2 == 0:
            for j in range(3): lib[j], lib[7-j] = lib[7-j], lib[j]
        else: lib.insert(0, lib.pop())
        octc = octc + str(lib.index(code[i]))
    for i in range(len(octc)): normalized = normalized + origlib[int(octc[i])]
    return normalized

def cleanup(code):
  return ''.join(filter(lambda x: x in ['.', ',', '[', ']', '<', '>', '+', '-'], code))

def main():
  if len(sys.argv) == 2: operate(sys.argv[1])
  elif len(sys.argv) == 3: operate(sys.argv[1],sys.argv[2])
  elif len(sys.argv) == 4: operate(sys.argv[1],sys.argv[2],sys.argv[3])
  else: print("Usage:", sys.argv[0], "filename")

if __name__ == "__main__": main()
