#!/usr/bin/env python
"""Script to compare several variant calling csv file 
in the frame of Performance testing of plant virus 
(followong COST-DIVAS action)."""

import argparse
import os
import pandas as pd
import statistics

def open_file(out_dir, file_name_data, file_name_control, col_name, col_name_control):
    """
    """
    try:
        virus_data = pd.read_csv(os.path.join(out_dir, file_name_data),
                                sep=";", header=0, names=col_name,
                                index_col=False)
    except pd.errors.ParserError:
        virus_data = pd.read_csv(os.path.join(out_dir, file_name_data),
                                sep=",", header=0, names=col_name,
                                index_col=False)        
    try:
        control_data = pd.read_csv(os.path.join(out_dir, file_name_control),
                        sep=";", header=0, names=col_name_control,
                        index_col=False)
    except pd.errors.ParserError:
        control_data = pd.read_csv(os.path.join(out_dir, file_name_control),
                        sep=",", header=0, names=col_name_control,
                        index_col=False)

    return virus_data, control_data


# def write_result(out_dir, file_name_data, virus_data, t1_threshold, 
# t2_threshold, t3_threshold, nb_read_limit_conta, mapping_highest_ratio, count):
#     """
#     """
#     path = file_name_data.split("/")
#     result_name = file_name_data.split(".")
#     result_folder_name = os.path.join(out_dir, "result_" + str(result_name[0]))
#     if len(path)>1: # control/Input_file_control_batch6.csv
#         file_name = "Result_" + "_threshold_case_" + str(count+1) + "_" + str(path[1] )
#     else: #Input_file_control_batch6.csv
#         file_name = "Result_" + "_threshold_case_" + str(count+1) + "_" + str(path[0])
#     try:
#         os.mkdir(result_folder_name)
#     except FileExistsError:
#         pass

#     virus_data.to_csv(os.path.join(result_folder_name, file_name), index=False, sep=';', encoding='utf-8')
    

#     current_case = threshold_case[count]
#     current_divider = current_case.split(":")
#     with open(os.path.join(result_folder_name, file_name), 'a') as out_file:
#         out_file.write("\n")
#         if t1_threshold == 1 :
#             out_file.write("mapping ratio threshold (step1 t1); ((avg+3*std)/" \
#                 + current_divider[0] + "; WARNING this threshold was ineffective as you don't have enough contamination in your control ; " + str(t1_threshold) + "\n")
#         else:
#             out_file.write("mapping ratio threshold (step1 t1); ((avg+3*std)/" \
#                 + current_divider[0] + ";" + str(t1_threshold) + "\n")
#         out_file.write("reads_nb_mapped threshold (step1 t2); Hihgest Reads Nr. \
#              Per sample in the same run/" + current_divider[1] + ";" + str(t2_threshold) + "\n")
#         out_file.write("deduplication threshold (step2 t3); ((avg(deduplication_ratio))/"\
#              + current_divider[2] + ";" + str(t3_threshold) + "\n")
#         out_file.write("nb_read_limit_conta (step3 t4_1); read_number ;" + str(nb_read_limit_conta) + "\n")
#         out_file.write("mapping_highest_ratio (step3 t4_2); highest mapping ratio ;" + str(mapping_highest_ratio) + "\n")

if __name__ == "__main__":

    #TODO argparse use argument ?
    col_name = ["File name","Type","Reference","Allele", "Coverage", "Average quality", \
    "Variant Frequency", "Personal validation", "Comment"] 

    out_dir = "/mnt/c/Users/johan/OneDrive/Bureau/bioinfo/PT3/Result/variant_calling/"
    
    file_name_control = "Input_file_control_3_20012021.csv"
    file_name_data = "Tested_virus_file_3_20012021.csv"
    
    for lab_dir in os.listdir(out_dir):
        print(lab_dir)
        filename_list = os.listdir(os.path.join(out_dir, lab_dir))
        for filename in filename_list:
            if filename.startswith("PT3_snp_template"):
                print(filename)
                #virus_data = open_file(out_dir, file_name_data, file_name_control, col_name, col_name_control)

        #  and ext == '.py':
        #     print filename

    #filename.startswith("")
    
    
    # open input file
    #virus_data, control_data = open_file(out_dir, file_name_data, file_name_control, col_name, col_name_control)
