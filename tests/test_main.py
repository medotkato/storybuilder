import pytest
from context import storybuilder


@pytest.fixture
def md_sample():
    return ['# Story outline', '## Section 1', '- Scene 1', '- Scene 2', '## Section 2', '- Scene 3', '### Subssection 2.1', '- Subscene 2.1.1']


def test_md_parse(md_simple):
    assert storybuilder.parse_outline(md_sample) == [{'H1_1': {'label': 'Story outline', 'content': [{'H2_1': {'label': 'Section 1', 'content': [
        '- Scene 1', '- Scene 2']}}, {'H2_2': {'label': 'Section 2', 'content': ['- Scene 3', {'H3_1': {'label': 'Subssection 2.1', 'content': ['- Subscene 2.1.1']}}]}}]}}]


def test_get_md_content():
    assert storybuilder.get_md_file_content(
        'tests/test.md') == ['# header', '- some string', '- other string']
