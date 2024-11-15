# MSDS generator
Program for generating MSDS according to REACH Regulation (EC) No. 1907/2006 requirements
 ( Can generate all other documents, with variables templates)
## Description:
There are program 3 files, ant rules/templates files in data/
- program files:
  - main.py - startind file
  - def_menu.py - menu file
  - def_proc.py - contains settings and procedures
- rules/variable files:
  - data/prod.xlxs - list of products with records from original MSDS
  - data/vars.xlxs - list of contacts
- templates/data files
  - /tmpl/*.html *.css - contains template.
  - /img/*.html - files for inserting data (ingredients tables) in document

The program generates documents in .html and .pdf formats on the basis of templates, which are located in the data/tmpl/ folder.

The unit composition files are located in the data/ing/ folder.

The file tmpl/prod.xlsx is a product list with text sections taken from the manufacturer's MSDS.

The generated documents are located in the folder data/out/

##  How to work:
1. Create task by filling variables values in data/prod.xlxs and in data/vars.xlsx
2. Run main.py and select menu option
3. Your generated documents in data/out/

##     How program works:
- Open xls and read data with colname
- cycle with data
- read template
  - cycle with var line
  - find var and replace
  - write data/out/.html file
  - create data/out/.pdf
- end cycle with var line
- end cycle with data
- exit
