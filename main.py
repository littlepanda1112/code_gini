import os
import sys
import subprocess
import xlrd
from xlwt import *
from xlrd import *
from xlutils.copy import copy
import pandas as pd
import re

approach = sys.argv[1]

PDDLFolder =sys.argv[2]

File =sys.argv[3]

gameType = sys.argv[4]

choice_way = sys.argv[5]
if choice_way == "ID3" or choice_way == "Incre":
    algorithm_way_type = sys.argv[6]

# For example
# the first method: python main.py Enum.py "domain\1.Sub\1.3 S, D-MarkGame" "result.xls" "normal" "in"  

# the second method: python main.py SynDT.py "domain\1.Sub\1.3 S, D-MarkGame" "result.xls" "normal" "ID3" "InfoGain"       

# the third method: python main.py SynDT.py "domain\1.Sub\1.3 S, D-MarkGame" "result.xls" "normal" "Incre"

# the fourth method: python main.py SynDT.py "domain\1.Sub\1.3 S, D-MarkGame" "result.xls" "normal" "DT1"

PDDLlist = os.listdir(PDDLFolder)
PDDLlist = sorted(PDDLlist,key=None)

def needJump(pddl) :
    name = pddl[:-5]
    oldwb = xlrd.open_workbook(resultFile, encoding_override='utf-8')
    sheet1 = oldwb.sheet_by_index(0)
    row = sheet1.nrows - 1                          
    # print(row)
    if row == -1:
        return False  
    df = pd.read_excel(resultFile, header=None)
    if name in df.iloc[:,0].values:
        return True
    timeString = "" if len(sheet1.row_values(row)) <= 2 else sheet1.row_values(row)[2]
    if re.match(r'^-?\d+\.?\d*$', str(timeString)) and 0 < float(timeString)  < 1200:
        return False
    else:
        fail_game_name = sheet1.row_values(row)[0]
       
        if  is_one_char_diff(fail_game_name, pddl[:-5]) and "Sub" not in pddl[:-5]:
            
            newwb = copy(oldwb)
            sheet1 = newwb.get_sheet(0)
            sheet1.write(row + 1, 0, pddl[:-5])
            sheet1.write(row + 1, 6, "J-C")
            newwb.save(resultFile)
            
            return True
        else:
            
            return False

def is_one_char_diff(str1, str2):
    if len(str1) == len(str2) - 1:
       
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                return str1 == str2[:i] + str2[i+1:]  
        return True
    elif len(str2) == len(str1) - 1:
        
        for i in range(len(str2)):
            if str2[i] != str1[i]:
                return str2 == str1[:i] + str1[i+1:]  
        return True
    elif len(str1) == len(str2):
       
        count_diff = 0  
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                count_diff += 1
                if count_diff > 1:
                    return False 
        return count_diff == 1  
    else:
        return False

for pddl in PDDLlist:
    print(pddl)
    try:
        if 'pddl' not in pddl:    
            continue
        print("test case：", pddl)
        if needJump(pddl) == False:
            pddl = PDDLFolder+'\\'+pddl
            if choice_way == "ID3" or choice_way == "Incre":
                subprocess.call("python \"%s\" \"%s\" \"%s\" \"%s\" \"%s\" \"%s\" "%(approach, pddl, resultFile, gameType, choice_way, algorithm_way_type), timeout = 2400)
            else:
                subprocess.call("python \"%s\" \"%s\" \"%s\" \"%s\" \"%s\" "%(approach, pddl, resultFile, gameType, choice_way), timeout = 2400)
    except subprocess.TimeoutExpired as e:
        print('Error: Subprocess execution timed out:', e)
        continue
    except subprocess.CalledProcessError as e:
        print("Error executing subprocess:", e)
        continue
    except:
        print("other error")
        continue

