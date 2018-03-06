import os, csv
from WaniKaniTools.dir import DATABASE


def chars2ids(chars):
    with open(os.path.join(DATABASE, 'id.txt')) as id_file:
        id_table = csv.reader(id_file, delimiter='\t')
        for row in id_table:
            if row[2] in chars:
                yield row[0]
