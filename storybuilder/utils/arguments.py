import argparse
from storybuilder.common.constants import DEFAULT_IN_FILE

def get_args ():

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
    args = my_parser.parse_args()

    in_file = args.in_file if args.in_file else DEFAULT_IN_FILE
    out_file = args.out_file if args.out_file else ""
    debug_mode_on = args.debug

    return in_file, out_file, debug_mode_on
