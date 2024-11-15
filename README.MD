The program generates documents in .html and .pdf formats on the basis of templates, which are located in the data/tmpl/ folder.
The unit composition files are located in the data/ing/ folder.
The file tmpl/prod.xlsx is a product list with text sections taken from the manufacturer's MSDS.
The generated documents are located in the folder data/out/

how to work:
create task from prod.xlxs 


open xls and read data with colname

cycle with data
	read template
		cycle with var line
			find var and replace
		write .html file
		create pdf
,