import pandas as pd
import openpyxl
import csv

csv_file_for_word = open('test.csv', encoding="utf8")
csv_word_file_reader = csv.reader(csv_file_for_word)

df = pd.read_excel('clean_dataset.xlsx')

data = df['Data'].tolist()

all_word_csv = []
all_moderate_word_csv = []
all_rural_word_csv = []
unchanged_word_dummy_list = []
unchanged_word_dummy_list_temp = []
unchanged_word_dummy_list_2 = []
unchanged_word_dummy_list_temp_2 = []
unchanged_word_final_list = []
expected_rural_text = ""
re_run_expected_rural_text = ""
test = ""
processed_moderate_data = ''
counter = 0
track = 0
test_2 = ''
test_3 = ''
tracker_1 = 0
tracker_2 = 0
tracker_3 = 0
tracker_4 = 0

def separete_csv_word_list():
    for info in csv_word_file_reader:
        all_word_csv.append(info)

    for a in range(len(all_word_csv)):
        all_moderate_word_csv.append(all_word_csv[a][0])
        all_rural_word_csv.append(all_word_csv[a][1])
    getting_dummy_modetare_data()




def getting_dummy_modetare_data():
    for x in data:
        dummy_moderate_text = str(x)
        processing(dummy_moderate_text)


def processing(dummy_moderate_text):
    temp = str(dummy_moderate_text)
    temp1 = temp.replace('।', " ")
    temp2 = temp1.replace(',', " ")
    temp3 = temp2.replace('\'', " ")
    temp4 = temp3.replace('\"', " ")
    temp5 = temp4.replace('-', " ")
    temp6 = temp5.replace('?', " ")
    processed_moderate_data = temp6

    print(processed_moderate_data)
    global test_2
    test_2 = processed_moderate_data
    build_word_list(processed_moderate_data)
    processed_moderate_data = ""


def build_word_list(processed_moderate_data):
    processed_moderate_data_word_list = list(processed_moderate_data.split(" "))

    matching_and_changing(processed_moderate_data_word_list)



def matching_and_changing(processed_moderate_data_word_list):
    for c in range(len(processed_moderate_data_word_list)):
        unchanged_word_dummy_list_temp_2.append(processed_moderate_data_word_list[c])
        for d in range(len(all_moderate_word_csv)):
            if processed_moderate_data_word_list[c] == all_moderate_word_csv[d]:
                unchanged_word_dummy_list_temp.append(processed_moderate_data_word_list[c])
                processed_moderate_data_word_list[c] = all_rural_word_csv[d]

    back_to_text(processed_moderate_data_word_list)
    processed_moderate_data_word_list.clear()


def back_to_text(processed_moderate_data_word_list):
    for i in processed_moderate_data_word_list:
        global expected_rural_text
        expected_rural_text = expected_rural_text + str(i) + " "


    print(expected_rural_text)
    global test,test_3
    test = expected_rural_text
    test_3 = expected_rural_text
    expected_rural_text = ""
    unchanged_word()

def unchanged_word():
    global counter
    accuracy = 0
    for ele in unchanged_word_dummy_list_temp:
        if ele.strip():
            unchanged_word_dummy_list.append(ele)

    for ele in unchanged_word_dummy_list_temp_2:
        if ele.strip():
            unchanged_word_dummy_list_2.append(ele)

    print("\n")
    accuracy = ((len(unchanged_word_dummy_list) / len(unchanged_word_dummy_list_2)) * 100)
    if accuracy >= 80:
        write_extra_pro_max_file()
    if accuracy >= 50 and accuracy <70 :
        write_pro_max_file()
    if accuracy >= 40 and accuracy <50 :
        write_max_file()
    if accuracy >= 70 and accuracy <80 :
        write_max_2_file()
    print("\t\t\t\t\t\t At sentence ",counter," Here we got ", int(accuracy), "% accuracy from this mapping")
    print("\n")
    unchanged_word_final_list = set(unchanged_word_dummy_list_2) - set(unchanged_word_dummy_list)
    print(unchanged_word_final_list)
    unchanged_word_dummy_list.clear()
    unchanged_word_dummy_list_2.clear()
    unchanged_word_dummy_list_temp.clear()
    unchanged_word_dummy_list_temp_2.clear()
    unchanged_word_final_list.clear()
    print("\n")


def write_extra_pro_max_file():
    global tracker_1
    tracker_1 = tracker_1 + 1
    global test_2,test_3
    print(test_2,"xxx")
    print(test_3,"yyy")

    with open('80_plus.txt', "a+", encoding="utf-8") as file_object:
        file_object.seek(0)
        data = file_object.read(100)
        if len(data) > 0:
            file_object.write("\n")
        file_object.write(str(tracker_1))
        file_object.write("\n")
        file_object.write(test_2)
        file_object.write("\n")
        file_object.write(test_3)
        file_object.write("\n")
        file_object.write("\n")
        file_object.write("\n")
        file_object.write("\n")



def write_pro_max_file():
    global tracker_2
    tracker_2 = tracker_2 + 1
    global test_2,test_3
    print(test_2,"xxx")
    print(test_3,"yyy")

    with open('between_50_to_80.txt', "a+", encoding="utf-8") as file_object:
        file_object.seek(0)
        data = file_object.read(100)
        if len(data) > 0:
            file_object.write("\n")
        file_object.write(str(tracker_2))
        file_object.write("\n")
        file_object.write(test_2)
        file_object.write("\n")
        file_object.write(test_3)
        file_object.write("\n")
        file_object.write("\n")
        file_object.write("\n")
        file_object.write("\n")



def write_max_file():
    global tracker_3
    tracker_3 = tracker_3 + 1
    global test_2,test_3
    print(test_2,"xxx")
    print(test_3,"yyy")

    with open('between_40_to_50.txt', "a+", encoding="utf-8") as file_object:
        file_object.seek(0)
        data = file_object.read(100)
        if len(data) > 0:
            file_object.write("\n")
        file_object.write(str(tracker_3))
        file_object.write("\n")
        file_object.write(test_2)
        file_object.write("\n")
        file_object.write(test_3)
        file_object.write("\n")
        file_object.write("\n")
        file_object.write("\n")
        file_object.write("\n")


def write_max_2_file():
    global tracker_4
    tracker_4 = tracker_4 + 1
    global test_2,test_3
    print(test_2,"xxx")
    print(test_3,"yyy")

    with open('between_70_to_80.txt', "a+", encoding="utf-8") as file_object:
        file_object.seek(0)
        data = file_object.read(100)
        if len(data) > 0:
            file_object.write("\n")
        file_object.write(str(tracker_4))
        file_object.write("\n")
        file_object.write(test_2)
        file_object.write("\n")
        file_object.write(test_3)
        file_object.write("\n")
        file_object.write("\n")
        file_object.write("\n")
        file_object.write("\n")


separete_csv_word_list()























