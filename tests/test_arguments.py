import storybuilder.utils.arguments as arg

def test_args_parser ():
    arguments_parsed = arg.get_args(['-i','/path/to/in_file','-o','/path/to/out_file','-d'])
    assert arguments_parsed.in_file == '/path/to/in_file'
    assert arguments_parsed.out_file == '/path/to/out_file'
    assert arguments_parsed.debug
