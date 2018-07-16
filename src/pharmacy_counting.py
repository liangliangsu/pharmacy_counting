import sys
import re

#inputfile = './input/de_cc_data.txt'
#outputfile = './output/top_cost_drug.txt'
inputfile=sys.argv[1] 
outputfile=sys.argv[2]

def check_float(value):
    try:
        value=float(value)
        return (True,value)
    except ValueError:
        return (False,-1)

def updata_dict(line, dict_cost, dict_unique):
    line=line.strip()
    # fill NA with 'Missing'
    line = re.sub('^,', 'Missing,', line)
    line = re.sub(',,', ',Missing,', line)
    line = re.sub(',$', ',Missing', line)
    templine=line.split(',')
    
    # check if line is splited in right way, otherwise use Regular expression to split line 
    if len(templine)!=5:
        templine=re.findall(r'(?:[^,"]|"(?:\\.|[^"])*")+', line)
    line=templine
    
    # check if splited drug_cost value is float value
    flag,drug_cost=check_float(line[4]) 
    
    # check drug_cost is a float and nonegative
    # double check line is splited correctly
    # otherwise skip this function
    if flag&(len(line)==5)&(drug_cost>=0):
        # if drug_name isn't in dictonary key list, create one
        if line[3] in dict_cost.keys():
            dict_cost[line[3]]=dict_cost[line[3]]+drug_cost
            dict_unique[line[3]].append((line[1]+'---'+line[2]))
        else:
            dict_cost[line[3]]=drug_cost
            dict_unique[line[3]]=[((line[1]+'---'+line[2]))]
    else:        
        print ('This line is not splited correctly or invalid cost value, skip this line!')
        return (dict_cost,dict_unique)
    
    return (dict_cost,dict_unique)

dict_cost={}
dict_unique={}
f = open(inputfile) 
line = f.readline() # skip header line in input dataset
line = f.readline()

count=0
# updata drug_name dictionary line by line
while line:
    try:
        dict_cost,dict_unique=updata_dict(line, dict_cost, dict_unique)
    except:
        print ('Warning, can not updata dictionary!')
    line = f.readline()   
    count+=1
    if (count%2000000)==0:
        print (count)
f.close()

# calcualte the number of unique prescribers and sort results in descending order
lines=[]
for key, value in sorted(dict_cost.items(), key=lambda x: (x[1], x[0]),reverse=True):
    if key=='Missing':
        drug_name='Unknown'
    else:
        drug_name=key    
    line=drug_name+','+str(len(set(dict_unique[key])))+','+str('{0:.2f}'.format(value).rstrip('0').rstrip('.'))+'\n'
    lines.append(line)


# write results to desired folder
f = open(outputfile, "w")
f.writelines('drug_name,num_prescriber,total_cost\n')
f.writelines(lines)
f.close()
