import re

def write_scene_to_file (file_TextIOWrapper, scene_text: list):
    file_TextIOWrapper.write("\n\n".join(scene_text) + "\n\n")
    # особое форматирование для реплик в диалогах (убрал, ибо так себе выглядит)
    # for scene_text_line in scene_text:
        # dialogue_line_match = re.search('^\s*[-—]\s*.+', scene_text_line)
        # line_ending = "\n" if dialogue_line_match else "\n"*2
        # out_file.write(line_begining + scene_text_line)
    return True

def get_raw_scene_text (scene_file_content_yaml: list) -> list:
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

def get_polished_scene_text (scene_text_raw: list) -> list:
    """ типографика: замена кавычек на елочки, дефисов на тире и пр.
    """
    def multi_replace (string, replace_dict):
        result = string
        for as_is, to_be in replace_dict.items():
            result = result.replace(as_is, to_be)
        return result

    replace_dict = {"- " : "— ", " -" : " —"}
    polished_scene_text = [multi_replace(row, replace_dict) for row in scene_text_raw]
    # типографим открывающую кавычку
    polished_scene_text = [re.sub(r"\"(\w)",r"«\1",row) for row in polished_scene_text]
    # типографим закрывающую кавычку
    polished_scene_text = [re.sub(r"(\w|[?!.])\"",r"\1»",row) for row in polished_scene_text]

    return polished_scene_text
