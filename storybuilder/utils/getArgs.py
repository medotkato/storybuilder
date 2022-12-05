import argparse
import os
from datetime import datetime
from storybuilder.common.constants import default_in_folder

def getArgs ():

    started_datetime = datetime.now().strftime("%y%m%d_%H-%M") # время начала обработки

    my_parser = argparse.ArgumentParser(description='Storybuilder')
    my_parser.add_argument('-i', '--in_folder',
                        metavar='/path/to/in_folder',
                        type=str,
                        help='path to the story source folder')
    my_parser.add_argument('-o', '--out_file',
                        metavar='/path/to/out_file',
                        type=str,
                        help='path to the output story file')
    args = my_parser.parse_args()

    in_folder = args.in_folder if args.in_folder else default_in_folder
    out_file = args.out_file if args.out_file else f"{in_folder}/story_{started_datetime}.md"

    return in_folder, out_file
