from storybuilder.utils.md_handler import md_to_yaml, get_md_file_content

def test_md_to_yaml(outline_md_sample, outline_md_parsed):
    assert md_to_yaml(outline_md_sample) == outline_md_parsed

def test_get_md_file_content():
    assert get_md_file_content('tests/test_sample_md.md') == \
        ['# header', '- some string', '- other string']
