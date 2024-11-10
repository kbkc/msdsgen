from pathlib import Path
import pandas as pd
from pyhtml2pdf import converter
import os
#from openpyxl import  load_workbook
# import python_calamine as calamine

# 942256 - ok with footer. Not overlapped. 942245 - not

# --------------------------------------
# !!! run app: python -X utf8 main.py
# SRC: https://stackoverflow.com/questions/50933194/how-do-i-set-the-pythonutf8-environment-variable-to-enable-utf-8-encoding-by-def
# print(sys.flags.utf8_mode)
# --------------------------------------


def ing_proc(dir):
    dirs = {'data' : str(dir)+ '\\data\\',
            'tmpl' : str(dir)+ '\\data\\tmpl\\',
            'ing' : str(dir)+ '\\data\\ing\\',
            'out' : str(dir)+ '\\data\\out\\'}    
    fn_task = 'task-ing02.xlsx'
    fn_vars = 'vars.xlsx'
    dftask = pd.read_excel(dirs['data']+fn_task, keep_default_na=False, engine='openpyxl')
    dfvars = pd.read_excel(dirs['data']+fn_vars, keep_default_na=False, engine='openpyxl')

    # change data in task to data in vars
    update_df1(dftask, dfvars)
    write_msds(dftask,dirs)



def msds_proc(dir):
    
    dirs = {'data' : str(dir)+ '\\data\\',
            'tmpl' : str(dir)+ '\\data\\tmpl\\',
            'ing' : str(dir)+ '\\data\\ing\\',
            'out' : str(dir)+ '\\data\\out\\'
            #'out' : str(dir)+ '\\data\\task-2024-06-03\\'
            }
    #fn_task = 'prod.xlsx' # main. all prod
    fn_task = 'task-2024-06-03-01.xlsx'

    fn_vars = 'vars.xlsx'
    #files = dir.glob('*.*')
    #print(dirs)


    # wbtask = load_workbook(dirs['data']+fn_task)
    # sheet_t = wbtask[1]
    # wbvars = load_workbook(dirs['data']+fn_vars)
    # sheet_v = wbvars[1]
    # dftask = pd.DataFrame(sheet_t.values)
    # dfvars = pd.DataFrame(sheet_t.values)

    # dftask = pd.read_excel(dirs['data']+fn_task)
    # dfvars = pd.read_excel(dirs['data']+fn_vars)
    print(dirs['data']+fn_task)

    dftask = pd.read_excel(dirs['data']+fn_task, keep_default_na=False, engine='openpyxl')
    dfvars = pd.read_excel(dirs['data']+fn_vars, keep_default_na=False, engine='openpyxl')

    # change data in task to data in vars
    update_df1(dftask, dfvars)

    write_msds(dftask,dirs)



# Define a function to update values in df1 with matched colunms values in df2, mapping 
# by column value in df1 and value in 'id' in df2
def update_df1(df1, df2):
    for col in df1.columns:
        # Check if the column is present in df2 and 'id' matches the values in df1
        if col in df2.columns and 'id' in df2.columns:
            df1[col] = df1[col].map(df2.set_index('id')[col])
    #print(df1)


def  write_msds(df,dirs):
    for i in range(len(df)):
        row_proc(df.iloc[i], dirs)
        #return
    return

def row_proc(rrow, dirs):
    ffn_tmpl = dirs['tmpl'] + rrow['tmpl']
    ffn_ing = str(dirs['ing']) + str(rrow['ing'])
    try:
        ing1 = Path(ffn_ing).read_text()
    except Exception as e:
        print(f"Ingredients file : An error occurred: {e}")
    try:
        tmpl1 = Path(ffn_tmpl).read_text()
    except Exception as e:
        print(f"Template file : An error occurred: {e}")
    tmpl1 = tmpl1.split('{{ing}}')
    tmpl1.insert(1,ing1)  
    tmpl1 = ''.join(tmpl1)  

    drow = rrow.to_dict()
    for k,v in drow.items():
        #print(str('{{'+k+'}}'),'<<<>>>',v)
        tmpl1 = tmpl1.replace(str('{{'+k+'}}'),str(v))

    
    ffn_html = str(dirs['out'])+str(rrow['art'])+'.html'
    ffn_pdf = str(dirs['out'])+str(rrow['art'])+'.pdf'
    
    my_path = Path(ffn_html)
    my_path.write_text(tmpl1)
    print('written : ',ffn_html)

    pth = os.path.abspath(ffn_html)
    converter.convert(f'file:///{pth}', ffn_pdf)
    print('written : ',ffn_pdf)





# 1   >>>   art :  942965
# 2   >>>   pname :  interstellar
# 3   >>>   pfamily :  uv gel
# 4   >>>   puse :  nail gel
# 5   >>>   manuf :  5
# 6   >>>   addr :  6
# 7   >>>   ing :  35.html
# 8   >>>   tmpl :  tmpl01.html