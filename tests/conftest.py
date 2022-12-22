import pytest

@pytest.fixture
def outline_md_sample():
    return ['# Outline', '## Section 1', '- Scene 1', '- Scene 2', '## Section 2', '### Subssection 2.1', '- Subscene 2.1.1']

@pytest.fixture
def outline_md_parsed():
    return [
        {'H1_1': {'label': 'Outline', 'content': [
            {'H2_1': {'label': 'Section 1', 'content': [
                '- Scene 1', '- Scene 2']
                }
            },
            {'H2_2': {'label': 'Section 2', 'content': [
                {'H3_1': {'label': 'Subssection 2.1', 'content': [
                    '- Subscene 2.1.1']
                    }
                }]
                }
            }]
            }
        }]
