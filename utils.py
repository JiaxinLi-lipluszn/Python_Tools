def readGeneList(file):
  ls = []
  import re # to recognize file discription line
  with open(file, 'r') as f:
    flag = 0
    line = f.readline()
    while line :
      if re.search('>', line):
          flag = 1
          line = f.readline()
          continue
      else:
        if flag == 0 :
            line = f.readline()
            continue
        gene = line.split('\n')
        gene = gene[0]
        ls.append(gene)
      line = f.readline()
  f.close()
  return ls

def writeGeneList(geneList, file, description, list_name):
  with open(file, 'w') as f:
    print(description, file = f)
    print(f'> {list_name}', file = f)
    for i in geneList:
        print(i, file = f)
  f.close()