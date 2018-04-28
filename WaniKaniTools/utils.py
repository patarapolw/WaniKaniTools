import csv

from WaniKaniTools.dir import database_path


def chars2ids(chars):
    """

    :param list chars: list of radicals, kanji or vocabularies
    :return generator:
    >>> list(chars2ids(['ハ']))
    ['2']
    >>> list(chars2ids(['七']))  # 4: as radical; 443: as kanji; 2469: as vocabulary
    ['4', '443', '2469']
    >>> list(chars2ids(['ハ', '七']))
    ['2', '4', '443', '2469']
    """
    with open(database_path('id.txt')) as id_file:
        id_table = csv.reader(id_file, delimiter='\t')
        for row in id_table:
            if row[2] in chars:
                yield row[0]
