#!/usr/bin/env python
"""Script to compare several variant calling csv file 
in the frame of Performance testing of plant virus 
(followong COST-DIVAS action)."""

import argparse
import os
import pandas as pd
import statistics
def clean_data(new_df, clean_virus_data):
    """
    """
    col_name = ["Lab", "File_name", "Input_file", "Org_ref", "Position", \
        "Type", "Reference","Allele", "Coverage", "Average_quality", \
        "Variant_frequency", "Personal_validation", "Comment"]
    clean_virus_tmp = pd.DataFrame(columns=col_name)
    clean_virus_list = []
    
    # print(new_df.loc[new_df.index[pd.isna(new_df["File name"])]])
    dumb_list1 = []
    dumb_list2 = []
    dumb_list3 = []

    # remove row when "File name" is null
    update_df = new_df.drop(new_df.index[pd.isna(new_df["File name"])])

    for index, row in update_df.iterrows():
        el = row["File name"]
        data = el.split("_")
        input_file_data = str(data[0] + "_" + data[1])
        org_ref_data = data[2]
        if "." in org_ref_data:
            org_ref_data = org_ref_data.split(".")[0]
        file_name = str(input_file_data + "_" + org_ref_data )
        update_df.loc[index,"Input_file"] = input_file_data
        update_df.loc[index,"Org_ref"] = org_ref_data
        update_df.loc[index,"File_name"] = file_name
        dumb_list1.append(el)
        dumb_list2.append(input_file_data)
        dumb_list3.append(org_ref_data)
    
    update_df = update_df.drop(["File name"], axis=1)
    # print("File name")
    # print(set(dumb_list1))  
    # print("input_file_data")
    # print(set(dumb_list2))   
    # print("org_ref_data")
    # print(set(dumb_list3))    
    clean_virus_data = clean_virus_data.append(update_df, ignore_index=True)
    # print(clean_virus_data)

    return clean_virus_data

def open_file(full_path, col_name, lab_dir, clean_virus_data):
    """
    """
    # print(full_path)
    xls = pd.ExcelFile(full_path, engine='openpyxl')
    sheet_list = xls.sheet_names
    for sheet in sheet_list:
        # print(sheet)
        virus_data = pd.read_excel(full_path, engine='openpyxl', sheet_name=sheet)
        virus_data.insert(0,"Lab", lab_dir)
        selected_columns = virus_data[col_name]
        new_df = selected_columns.copy()
        clean_virus_data = clean_data(new_df, clean_virus_data)
    return clean_virus_data


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
    col_name = ["Lab", "File name", "Position", \
        "Type", "Reference","Allele", "Coverage", "Average quality", \
        "Variant Frequency", "Personal validation", "Comment"]

    out_dir = "/mnt/c/Users/johan/OneDrive/Bureau/bioinfo/PT3/Result/variant_calling/"
    clean_virus_data = pd.DataFrame(columns=col_name)
    
    for lab_dir in os.listdir(out_dir):
        #print(lab_dir)
        filename_list = os.listdir(os.path.join(out_dir, lab_dir))
        for filename in filename_list:
            if filename.startswith("PT3_snp_template"):
                #print(filename)
                full_path = os.path.join(os.path.join(out_dir, lab_dir),filename)
                clean_virus_data = open_file(full_path, col_name, lab_dir, clean_virus_data)
    print('toto')
    print(clean_virus_data)
    #filename.startswith("")
    
    print(clean_virus_data.File_name.unique())
    print(clean_virus_data.Org_ref.unique())
    print(clean_virus_data.Input_file.unique())
    # open input file
    #virus_data, control_data = open_file(out_dir, file_name_data, file_name_control, col_name, col_name_control)
