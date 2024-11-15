# MSDS generator
## Description:

The program generates documents in .html and .pdf formats on the basis of templates, which are located in the data/tmpl/ folder.

The unit composition files are located in the data/ing/ folder.

The file tmpl/prod.xlsx is a product list with text sections taken from the manufacturer's MSDS.

The generated documents are located in the folder data/out/

##  How to work:
1. Create task by filling variables values in data/prod.xlxs and in data/vars.xlsx
2. Run main.py and select menu option
3. Your generated documents in data/out/

##     How program works:
1. open xls and read data with colname
2. cycle with data
- read template
  - cycle with var line
  - find var and replace
  - write data/out/.html file
  - create data/out/.pdf
- end cycle with var line
- end cycle with data
3. exit
