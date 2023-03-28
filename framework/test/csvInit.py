import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys
import getopt
pd.options.mode.chained_assignment = None

def myfunc(argv):
    arg_value = ""
    arg_file = ""
    arg_c = ""
    arg_r = ""
    arg_p = ""
    arg_b = ""
    arg_help = "{0} -f <path to file> -c <column name> -v <value> -r <row (criterion)> -p <project name> -b <bug name>".format(argv[0])

    try:
        opts, args = getopt.getopt(argv[1:], "hf:c:v:r:p:b:", ["help", "f=",
                                                         "c=", "v=","r=","b=","p="])
    except:
        print(arg_help)
        print("failed to get opt")
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(arg_help)  # print the help message
            sys.exit(2)
        elif opt in ("-f", "--file"):
            arg_file= arg
        elif opt in ("-c", "--column"):
            arg_c = arg
        elif opt in ("-v", "--value"):
            arg_value = arg
        elif opt in ("-r", "--row", "--criterion"):
            arg_r = arg
        elif opt in ("-p"):
            arg_p = arg
        elif opt in ("-b"):
            arg_b = arg




    if str(arg_file)=="":
        print("A file path is needed.")
        print(arg_help)
        sys.exit(2)

    df = pd.read_csv(arg_file)
    if str(arg_p)!="":
        df.Project[0] = arg_p
        df.Project[1] = arg_p
        df.Project[2] = arg_p
        df.Project[3] = arg_p
        df.Project[4] = arg_p
        df.to_csv(arg_file)
    if str(arg_b)!="":
        df.Bug[0] = arg_b
        df.Bug[1] = arg_b
        df.Bug[2] = arg_b
        df.Bug[3] = arg_b
        df.Bug[4] = arg_b
        df.to_csv(arg_file)


    row = 99
    if arg_c=="BRANCH":
        row=0
    elif arg_c=="PRIVATEMETHOD":
        row=1
    elif arg_c=="EXCEPTION":
        row=2
    elif arg_c=="BRANCH:PRIVATEMETHOD":
        row=3
    elif arg_c=="BRANCH:EXCEPTION":
        row=4
    #if row>4:
        #print("Unspecified Criterion, -r .")
        #sys.exit(2)
    if row<5:
        if arg_r=="Bug_Detection":
            df.Bug_Detection[row] = arg_value
            df.to_csv(arg_file)
            print(df)
        if arg_r=="Total_Banches":
            df.Total_Banches[row] = arg_value
            df.to_csv(arg_file)
        if arg_r=="Covered_Banches":
            df.Covered_Banches[row] = arg_value
            df.to_csv(arg_file)
        if arg_r=="Total_Methods":
            df.Total_Methods[row] = arg_value
            df.to_csv(arg_file)
        if arg_r=="Covered_Methods":
            df.Covered_Methods[row] = arg_value
            df.to_csv(arg_file)
        if arg_r=="CoverageBitString":
            df.CoverageBitString[row] = arg_value
            df.to_csv(arg_file)

    #df.to_csv(arg_file)  # Save the file
    #try:
        #df = pd.read_csv(arg_file)
        #df[2][2] = 10  # Write the value 10 to column A, row 5 (zero-indexed)
        #df.to_csv(arg_file)  # Save the file
    #except:
        #print("Could not read the specified CSV file.")
        #sys.exit(2)

if __name__ == "__main__":
    myfunc(sys.argv)