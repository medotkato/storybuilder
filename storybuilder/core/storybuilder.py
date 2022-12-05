import os
import re

from tqdm import tqdm

from storybuilder.utils.getArgs import getArgs
from storybuilder.utils.md_parser import get_md_file_content_stripped, get_md_file_content_as_is, parse_md_yaml

def scene_text_writer (file_TextIOWrapper, scene_text: list):
    file_TextIOWrapper.write("\n\n".join(scene_text) + "\n\n")
    # for scene_text_line in scene_text:
        # dialogue_line_match = re.search('^\s*[-—]\s*.+', scene_text_line)
        # line_ending = "\n" if dialogue_line_match else "\n"*2
        # out_file.write(line_begining + scene_text_line)
    return True

def main () -> int:
    in_folder, out_file = getArgs()
    in_folder_abs = os.path.abspath(in_folder)
    out_file_abs = os.path.abspath(out_file)
    outline_file = os.path.abspath(in_folder + "/outline.md")

    print (f"Reading data from {in_folder_abs}")
    print (f"Getting outline from {outline_file}")

    outline_content = get_md_file_content_stripped (outline_file)

    with open(out_file_abs,'w', encoding="utf-8") as out_file:
        for line in tqdm(outline_content):
            title_match = re.search('^\s*(#+)(.*)', line)
            if title_match:
                out_file.write(line + "\n\n")
            else:
                md_url_match = re.search('^\s*-\s*\[.+\]\((.+)\)', line)
                if md_url_match:
                    md_url = md_url_match.group(1)
                    scene_filename = os.path.abspath(f'{in_folder}/{md_url}')
                    scene_file_content = get_md_file_content_stripped(scene_filename)
                    scene_file_content_yaml = parse_md_yaml(scene_file_content)
                    scene_text = scene_file_content_yaml[0]["H1_1"]["content"][1]["H2_2"]["content"]
                    # print (scene_file_content_yaml)
                    scene_text_writer(out_file, scene_text)
                else:
                    comment_match = re.search("^\s*//\s*(.*)", line)
                    not_finished_scene_match = re.search("^\s*-\s*(.+)$", line)
                    if not comment_match and not_finished_scene_match:
                        out_file.write("--- " + not_finished_scene_match.group(1) + "\n\n")

    print (f"Done. Story was successfully built and written to {out_file_abs}")
    return 0

if __name__ == "__main__":
    main()
