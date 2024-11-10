from def_menu import *
from def_proc import *
from pathlib import Path
# --------------------------------------
# !!! run app: python -X utf8 main.py
# SRC: https://stackoverflow.com/questions/50933194/how-do-i-set-the-pythonutf8-environment-variable-to-enable-utf-8-encoding-by-def
# print(sys.flags.utf8_mode)
# --------------------------------------
# !!! run app: python -X utf8 main.py
def main():
    choice=run_menu()
    print('you pressed ',choice)

    if choice == "1":
        msds_proc(Path.cwd())
      #nosta_proc(ffn_order,True)

    elif choice=="2":
        ing_proc(Path.cwd())
      #notes_proc()



    print('\nThe job is done, choice = ',choice)



if __name__ == "__main__":
    main()
