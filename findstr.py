#!/usr/bin/python3

import sys
from os import listdir
from os.path import isfile, join


def searchStr(path, keywords, varname=False):
    # varname=True to print names of function/keyword
    with open(path, encoding="utf-8") as f:
        try:
            for line_number, line in enumerate(f):
                for keyword in keywords:
                    if keyword in line:
                        if varname:
                            try:
                                equal_sign = line.index('=')
                                space = line.index(' ')
                                print("%s" % line[space+1:equal_sign].strip())
                            except ValueError:
                                pass
                        else:
                            line = line.strip()
                            print("Path -> %s" % (path))
                            print("%d: %s" % (line_number, line))
                            print("")
        except UnicodeDecodeError:
            pass

# list paths in a directory
def list_paths(path):
    paths = []
    try:
        for i in listdir(path):
            entity_path = join(path, i)
            if isfile(entity_path):
                paths.append(entity_path)
            else:
                paths.extend(list_paths(entity_path))
    except FileNotFoundError:
        print("[-] File not found")
    except PermissionError:
        pass
    finally:
        return paths
def main():
    if(len(sys.argv)<=2):
        print("\033[32m")
        print("Usage: python %s <FOLDER> <KEYWORD1 KEYWORD2 etc..>\n" % (sys.argv[0]))
        print("OPTIONAL")
        print("-v - print name of variables assign to certain funcions")
        print("example: malloc( -v will print variable names assign to mallocs\n")
        print("use \\-v to search for -v as keyword")
        print("Reminder: <> is just a placeholder, don't type it in idiot :)")
        print("\033[0m")
        exit(-1)


    path = sys.argv[1]
    paths = list_paths(path)
    
    keywords = sys.argv[2:]
    varname = False

    if "-v" in keywords:
        keywords.remove("-v")
        varname = True
    elif "\\-v" in keywords:
        keywords[keywords.index("\\-v")] = "-v"
        
    print("keywords: ", end=' ')
    for index, key in enumerate(keywords):
        if index == len(keywords) - 1:
            print(key, end=' ')
        else:
            print(key, end=", ")
    print()

   
    if len(paths) > 0:
        try:
            for p in paths:
                if not varname:
                    searchStr(p, keywords)
                else:
                    searchStr(p, keywords, varname)
        except KeyboardInterrupt:
            print("[-] Program stopped")
    else:
        print("[-] No paths")
        exit(-1)

if(__name__ == "__main__"):
    main()
