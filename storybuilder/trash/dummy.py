def get_items(outline_item: list) -> list:
    for item in outline_item:
        if type(item) == 'str':
            return item
        else:
            vals = item.values()
            return vals[0]['label'] + "\n" + get_items(vals[0]['content'])


outline = [
    {'H1_1':
        {'label': 'Story outline', 'content':
            [{'H2_1':
                {'label': 'Section 1', 'content':
                    ['- Scene 1', '- Scene 2']
                }
             },
             {'H2_2':
                {'label': 'Section 2', 'content':
                    ['- Scene 3',
                        {'H3_1': {'label': 'Subssection 2.1', 'content': ['- Subscene 2.1.1']}}]}}]}}]

formatted_story = get_items(outline)

print (formatted_story)
