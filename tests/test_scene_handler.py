from storybuilder.utils.scene_handler import get_polished_scene_text, get_raw_scene_text

def test_get_polished_scene_text ():
    as_is: list = ["- Иван родил", "\"Марью\" - дочь-человека"]
    to_be: list = ["— Иван родил", "«Марью» — дочь-человека"]
    assert get_polished_scene_text(as_is) == to_be

def test_get_raw_scene_text ():

    scene_md_parsed_ok: list = [
            {'H1_1': {'label': 'Normal Scene', 'content': [
                {'H2_1': {'label': 'Sketch', 'content': [
                    'Bla-bla-bla']}
                },
                {'H2_2': {'label': 'Text', 'content': [
                    "Scene text"]}
                }]}
            }]

    scene_md_parsed_not_ok_1: list = [
            "Text",
                {'H2_2': {'label': 'Text', 'content': [
                    "Scene text"]}
                }]

    scene_md_parsed_not_ok_2: list = [
            {'H1_1': {'label': 'Scene with error', 'content': [
                {'H2_2': {'label': 'Text', 'content': [
                    "Scene text"]}
                }]}
            }]

    assert get_raw_scene_text (scene_md_parsed_ok) == ["Scene text"]
    assert get_raw_scene_text (scene_md_parsed_not_ok_1) == \
        ["Oops, 1st level header (# Scene name) not found.\n" + \
         "Check for # at the beginning of the first line"]
    assert get_raw_scene_text (scene_md_parsed_not_ok_2) == \
        ["Oops, 2nd level header '## Text' section not found on the 2nd position"]
