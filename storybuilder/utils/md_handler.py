import re

def get_md_file_content (md_file: str) -> list:
    """
    Возвращает содержимое .md файла в виде списка строк.
    Пустые строки и пробелы с конца строк удаляются.
    """
    with open(f'{md_file}','r', encoding="utf-8") as md_file:
        md = [x.rstrip() for x in md_file]
        md_strip = [x for x in md if x != '']
    return md_strip

def md_to_yaml(file_content: list) -> list:
    """ Парсит .md файл и собирает список dict-ов, где каждый раздел (по уровню заголовка) - свой dict внутри списка, а текстовые строки содержатся списком в элементе content соответствующего раздела """
    parsed_md = list()
    rownum = 0
    level_index = 1

    while rownum < len(file_content):

        # ищем заголовки
        match = re.search('(#+)(.*)', file_content[rownum])
        if match:
            level = len(match.group(1))
            section_key = f'H{level}_{level_index}'
            section_label = match.group(2).strip()

            rownum += 1
            start_rownum = rownum

            below = file_content [start_rownum:]

            for x in range(len(below)):

                # ищем диапазон строк с содержимым секции
                match_below = re.search('(#+)(.*)', below[x])
                if match_below:
                    level_below = len(match_below.group(1).strip())
                    if level_below <= level:
                        break
                    else:
                        rownum += 1
                else:
                    rownum += 1
            end_rownum = rownum
            # нашли номер строки, где заканчивается секция (либо дошли до конца)

            section_content = md_to_yaml (file_content[start_rownum:end_rownum])
            parsed_md.append ({section_key: {'label': section_label, 'content': section_content}})
            level_index += 1

        else:
            parsed_md.append (file_content[rownum])
            rownum += 1

    return parsed_md
