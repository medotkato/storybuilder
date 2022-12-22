import argparse

def get_args (args):

    my_parser = argparse.ArgumentParser(description='Storybuilder')
    my_parser.add_argument('-i', '--in_file',
                        metavar='/path/to/in_file',
                        type=str,
                        help='path to the outline.md file')
    my_parser.add_argument('-o', '--out_file',
                        metavar='/path/to/out_file',
                        type=str,
                        help='path to the output story file')
    my_parser.add_argument('-d', '--debug',
                        action="store_true",
                        help='debug mode on/off')
    return my_parser.parse_args(args)
