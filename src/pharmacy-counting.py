import sys
import re

inputfile=sys.argv[1]
outputfile=sys.argv[2]

#f = open('./input/itcont.txt') 
#f = open('./input/de_cc_data.txt') 
f = open(inputfile) 
line = f.readline()
line = f.readline()
dict_cost={}
dict_unique={}


def updata_dict(line, dict_cost, dict_unique):
    line=line.strip()
    line = re.sub('^,', ' ,', line)
    line = re.sub(',,', ', ,', line)
    line = re.sub(',$', ', ', line)
    templine=line.split(',')
    if len(templine)!=5:
        templine=re.findall(r'(?:[^,"]|"(?:\\.|[^"])*")+', line)
    line=templine
    if (line[0]!=' ')&(line[4]!=' ')&(float(line[4])>=0)&(len(line)==5):
        if line[3] in dict_cost.keys():
            dict_cost[line[3]]=dict_cost[line[3]]+float(line[4])
            dict_unique[line[3]].append(line[0])
        else:
            dict_cost[line[3]]=float(line[4])
            dict_unique[line[3]]=[line[0]]
    else:
        print ('Bad format!')
    return (dict_cost,dict_unique)

count=0
while line:
    try:
        dict_cost,dict_unique=updata_dict(line, dict_cost, dict_unique)
    except:
        print ('Warning!')
    line = f.readline()   
    count+=1
    if (count%1000000)==0:
        print (count)
f.close()

lines=[]
for key, value in sorted(dict_cost.items(), key=lambda x: (x[1], x[0]),reverse=True):
    if key==' ':
        drug='other'
    else:
        drug=key    
    line=drug+','+str(len(set(dict_unique[key])))+','+str(round(value,2))+'\n'
    #print (line)
    lines.append(line)

#f = open("./output/top_cost_drug.txt", "w")
f = open(outputfile, "w")
f.writelines('drug_name,num_prescriber,total_cost\n')
f.writelines(lines)
f.close()
