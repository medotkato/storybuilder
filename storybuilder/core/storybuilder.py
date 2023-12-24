import os
import re
import sys

from tqdm import tqdm
from datetime import datetime

from storybuilder.utils.arguments import get_args
from storybuilder.utils.md_handler import get_md_file_content, md_to_yaml
from storybuilder.common.constants import DEFAULT_IN_FILE, DEFAULT_OUT_FILE
from storybuilder.utils.scene_handler import write_scene_to_file, get_raw_scene_text, get_polished_scene_text

def main () -> int:

    start_datetime = datetime.now().strftime("%y%m%d_%H-%M-%S")

    arguments = get_args(sys.argv[1:]) # all except the script's name

    in_file = arguments.in_file if arguments.in_file else DEFAULT_IN_FILE
    out_file = arguments.out_file if arguments.out_file else DEFAULT_OUT_FILE
    debug_mode_on = arguments.debug

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
            # comment_match = re.search("^\s*//\s*(.*)", line)

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
                scene_file_content_yaml = md_to_yaml(scene_file_content)
                scene_text_raw = get_raw_scene_text(scene_file_content_yaml)
                scene_text_polished = get_polished_scene_text(scene_text_raw)
                write_scene_to_file(out_file, scene_text_polished)

            # названия незавершенных сцен выводим как есть (без дефиса в начале)
            elif not_finished_scene_match:
                    out_file.write(f"=== {not_finished_scene_match.group(1)}\n\n")

            # все остальное нам не нужно (комментарии, например)
            else:
                pass
    if_debug = "Run again with -d flag (debug mode) if scenes are missing or you see unexpected things inside the compiled story" if not debug_mode_on else ""
    print (f"Done. Story was built and written to {out_file_abs}.\n" + if_debug)
    return 0

if __name__ == "__main__":
    main()
