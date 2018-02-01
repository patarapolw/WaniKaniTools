import os
from web import login
import csv


def char2id(char):
    global id_table
    for row in id_table:
        if row[2] == char:
            return row[0]

    return 'Not found'


to_resurrect = [] # Array of Radical / Kanji / Vocabulary you want to resurrect.

id_array = []
with open(os.path.join('database', 'id.txt')) as id_file:
    id_table = csv.reader(id_file, delimiter='\t')
    for char in to_resurrect:
        id_array += [ char2id(char) ]

with login.web() as w:
    for id in id_array:
        w.driver.execute_script(
            "$.ajax({url:'https://www.wanikani.com/assignments/"+id+"/resurrect', method:'PUT'})")