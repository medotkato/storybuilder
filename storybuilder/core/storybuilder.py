import os
import re

from tqdm import tqdm
from datetime import datetime

from storybuilder.utils.arguments import get_args
from storybuilder.utils.md_parser import get_md_file_content, parse_md_yaml

def scene_text_writer (file_TextIOWrapper, scene_text: list):
    file_TextIOWrapper.write("\n\n".join(scene_text) + "\n\n")
    # особое форматирование для реплик в диалогах (убрал, ибо так себе выглядит)
    # for scene_text_line in scene_text:
        # dialogue_line_match = re.search('^\s*[-—]\s*.+', scene_text_line)
        # line_ending = "\n" if dialogue_line_match else "\n"*2
        # out_file.write(line_begining + scene_text_line)
    return True

def get_scene_text (scene_file_content_yaml):
    first_item = scene_file_content_yaml[0]
    if isinstance(first_item, dict):
        scene_content = scene_file_content_yaml[0].get \
                        ("H1_1", "Oops, 1st level header (# bla-bla) not found")["content"]
        f = lambda list, i, default: list[i:i+1] and list[i] or default
        scene_text_dict = f(scene_content, 1, "ERROR")
        scene_text = scene_text_dict["H2_2"]["content"] \
                    if (scene_text_dict != "ERROR" and scene_text_dict["H2_2"]["label"].lower() == "text") \
                    else ["Oops, 2nd level header '## Text' section not found on the 2nd position"]
    else:
        scene_text = ["Oops, 1st level header (# Scene name) not found.\n" + \
                      "Check for # at the beginning of the first line"]

    # scene_text = scene_file_content_yaml[0]["H1_1"]["content"]\
                                        # [1]["H2_2"]["content"]

    return scene_text

def main () -> int:

    start_datetime = datetime.now().strftime("%y%m%d_%H-%M-%S")

    in_file, out_file, debug_mode_on = get_args()
    if debug_mode_on:
        print ("DEBUG MODE ON")
    debug_flag = "_debug" if debug_mode_on else ""
    in_folder = os.path.dirname(in_file)
    outline_file_abs = os.path.abspath(in_file)
    out_file_abs = os.path.abspath(\
                    out_file if out_file else \
                    f"{in_folder}/story_{start_datetime}{debug_flag}.md"
                    )

    print (f"Parsing outline from {outline_file_abs}")

    outline_content = get_md_file_content(outline_file_abs)

    with open(out_file_abs,'w', encoding="utf-8") as out_file:
        for line in tqdm(outline_content):
            title_match = re.search('^\s*(#+)(.*)', line)
            md_url_match = re.search("\[.+\]\((.+)\)", line)
            not_finished_scene_match = re.search("^\s*-\s*(.+)$", line)
            comment_match = re.search("^\s*//\s*(.*)", line)

            # пишем заголовки as is, только для режима отладки
            # добавим пометку в начало файла
            if title_match:
                debug_title = " // DEBUG_MODE" if title_match.group(1) == "#" \
                                                 and debug_mode_on else ""
                out_file.write(f"{line}{debug_title}\n\n")

            # сцены забираем из файлов по ссылке, парсим
            # и выводим второй блок (Text) с текстом сцены
            elif md_url_match:
                if debug_mode_on:
                    out_file.write(f"=== {md_url_match.group(0)} ===\n\n")
                md_url = md_url_match.group(1)
                scene_filename = os.path.abspath(f'{in_folder}/{md_url}')
                scene_file_content = get_md_file_content(scene_filename)
                scene_file_content_yaml = parse_md_yaml(scene_file_content)
                scene_text = get_scene_text(scene_file_content_yaml)
                scene_text_writer(out_file, scene_text)

            # названия незавершенных сцен выводим как есть (без - в начале)
            elif not_finished_scene_match:
                    out_file.write(f"=== {not_finished_scene_match.group(1)}\n\n")

            # все остальное нам не нужно (комментарии, например)
            else:
                pass

    print (f"Done. Story was built and written to {out_file_abs}.\n" + \
            "Run again with -d flag (debug mode) if some scenes are missing")
    return 0

if __name__ == "__main__":
    main()
