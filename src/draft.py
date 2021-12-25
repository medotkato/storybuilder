import re
import yaml_handler

def md_read (md_file: str) -> list:
    with open(f'{md_file}','r', encoding="utf-8") as md_file:
        # md = list(md_file) # это если пофиг на \n, но нам надо убрать
        # убираем \n в конце строк и пустые строки из файла
        md = [x.rstrip() for x in md_file]
        md_strip = [x for x in md if x != '']
    return md_strip

def md_parse (md_list: list) -> list:

    out_list = list()
    rownum = 0
    level_index = 1

    while rownum < len(md_list):

        # ищем заголовки
        match = re.search('(#+)(.*)', md_list[rownum])
        if match:
            level = len(match.group(1))
            section_key = f'H{level}_{level_index}'
            section_label = match.group(2).strip()

            rownum = rownum + 1
            start_rownum = rownum

            below = md_list [start_rownum:]

            for x in range(len(below)):

                # ищем диапазон строк с содержимым секции
                match_below = re.search('(#+)(.*)', below[x])
                if match_below:
                    level_below = len(match_below.group(1).strip())
                    if level_below <= level:
                        break
                    else:
                        rownum = rownum + 1
                else:
                    rownum = rownum + 1
            end_rownum = rownum
            # нашли номер строки, где заканчивается секция (либо дошли до конца)

            section_content = md_parse (md_list[start_rownum:end_rownum])
            out_list.append ({section_key: {'label': section_label, 'content': section_content}})
            level_index = level_index + 1

        else:
            out_list.append (md_list[rownum])
            rownum = rownum + 1

    return out_list

def scenes_outline_builder (md_list: list) -> list:

    # выбрасываем комменты
    # match_comment = re.search('(//)(.*)', md_list[rownum])
    # if not match_comment:
    #     ...

    return md_list


def get_scenes(content: list) -> list:
    scenes = []
    scenes_src = [x for x in content] # dicts (each is heading and below)
    for item in scenes_src:
        print (item)
        # scenes.append()

    scenes=scenes_src
    return scenes

def main():

    # md2 = ['## Scene 1','Scene 1 Text','Scene 1 More Text', '## Scene 2','Scene 2 Text', '### Subscene 1' ,'Subscene 1 Text', '## Scene 3', 'Scene 3 Text']
    # md_in = md2

    md_file = 'src/story.md'
    md_in = md_read (md_file)

    # print ('in:')
    # print (md_in)

    md_parsed = md_parse (md_in)

    # yaml_handler.yaml_write('meta/story.yaml',md_parsed)

    content=md_parsed[0]['H1_1']['content']
    for item in content:
        val = [x for x in item.values()][0]
        if val['label'] == 'Scenes':
            scenes = get_scenes(val['content'])
            # for scene in scenes:
            #     print (scene)

if __name__ == '__main__':
    main()
