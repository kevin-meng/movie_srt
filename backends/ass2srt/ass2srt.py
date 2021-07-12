import argparse
import cchardet
import os
import sys
from ass2srt.ass2srt_functions import *

# COPY from
# https://github.com/locobastos/ass2srt-python/blob/master/ass2srt.py
# _____ FUNCTiONS ______________________________________________________________________________________________________


def convert_ass_to_srt(ass_filename):

    fonts_name_list = []
    style_list = []

    output_srt_file = ass_filename[:-4] + ".srt"
    if ass_filename.lower().endswith('.ass'):
        try:
            with open(ass_filename, 'rb') as ass_opened_file:
                char_enc = cchardet.detect(ass_opened_file.read()).get('encoding')
            with open(ass_filename, 'r', encoding=char_enc) as infile, open(output_srt_file, 'w', encoding=char_enc) as outfile:
                # I'm doing a loop over each lines, event_line is used to know if we have reach the [Events] section
                event_line = False
                dialogue_number = 1  # the number indicating which subtitle it is in the sequence.
                for line in infile:
                    if not event_line:
                        """
                        Removes the [Script Info] and [V4+ Styles] headers
                        + The Format line on the [Events] section
                        """
                        if line.startswith("Style: "):
                            split_line = line.split(",")
                            style_name = split_line[0]
                            if style_name not in style_list:
                                style_list.append(style_name)
                            font_name = split_line[1]
                            if font_name not in fonts_name_list:
                                fonts_name_list.append(font_name)
                        if line.startswith("Format: Layer"):
                            event_line = True
                    else:
                        """
                        We are now on the Dialogue lines
                        """
                        if line not in ['\n', '\r\n'] or len(line.strip()) != 0:
                            outfile.write(str(dialogue_number) + '\n')
                            tmp_line = line.split(",", 9)
                            outfile.write(tmp_line[1].replace(".", ",") + " --> " + tmp_line[2].replace(".", ",") + '\n')
                            outfile.write(remove_ass_tags(tmp_line[9]))
                            dialogue_number += 1
            outfile.close()
            infile.close()
        except EnvironmentError:
            print("The file " + ass_filename + " does not exist")
            exit(10)


def remove_ass_tags(str_input):
    fonts_name_list = []
    style_list = []
    # Remove current \n
    str_temp = str_input.replace('\n', '')
    str_temp = replace_ass_n_by_system_n(str_temp)

    # Source of all ASS Tags: http://docs.aegisub.org/3.2/ASS_Tags/
    str_temp = replace_italic_tags(str_temp)
    str_temp = replace_bold_tags(str_temp)
    str_temp = remove_b100_to_b900_explicit_bold_weight(str_temp)
    str_temp = replace_underline_tags(str_temp)
    str_temp = remove_strikeout_tags(str_temp)
    str_temp = remove_border_tags_and_extended(str_temp)
    str_temp = remove_shadow_distance_and_extended(str_temp)
    str_temp = remove_blur_edge_gaussian_kernel(str_temp)
    str_temp = remove_font_name(str_temp, fonts_name_list)
    str_temp = remove_font_size(str_temp)
    str_temp = remove_font_scale(str_temp)
    str_temp = remove_letter_spacing(str_temp)
    str_temp = remove_text_rotation(str_temp)
    str_temp = remove_text_shearing(str_temp)
    str_temp = remove_font_encoding(str_temp)
    str_temp = replace_text_color(str_temp)
    str_temp = remove_transparency_text_alpha(str_temp)
    str_temp = remove_line_alignment(str_temp)
    str_temp = remove_karaoke_effect(str_temp)
    str_temp = remove_wrap_style(str_temp)
    str_temp = remove_reset_style(str_temp, style_list)
    str_temp = remove_text_position(str_temp)
    str_temp = remove_movement(str_temp)
    str_temp = remove_rotation(str_temp)
    str_temp = remove_fade(str_temp)
    str_temp = remove_clip_rectangle(str_temp)

    # Add \n at the end of the line
    str_temp += '\n\n'
    return str_temp

# _____ MAiN ___________________________________________________________________________________________________________


# _____ ARGUMENTS PARSER _______________________________________________________________________________________________
if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        prog='ass2srt',
        description='Convert SubStationAlpha v4.00+ (.ass) into SubRip (.srt)',
        epilog='GitHub Page: https://github.com/locobastos/ass2srt-python'
    )

    parser.add_argument('-id', '--input-directory',
                        type=str,
                        action='append',
                        nargs='+',
                        help='the path to the directory containing all .ass files')
    parser.add_argument('-if', '--input-file',
                        type=str,
                        action='append',
                        nargs='+',
                        help='the path to the input file.')
    args = parser.parse_args()


    # _____ SHARED VARiABLES _______________________________________________________________________________________________




    if not len(sys.argv) == 1:
        if args.input_file is not None:
            for ass_file in range(len(args.input_file)):
                convert_ass_to_srt(args.input_file[ass_file][0])

        if args.input_directory is not None:
            for ass_dir in args.input_directory:
                for ass_file in os.listdir(ass_dir[0]):
                    convert_ass_to_srt(ass_dir[0] + ass_file)
    else:
        parser.print_help()
