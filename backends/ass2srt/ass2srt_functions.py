import re


def replace_ass_n_by_system_n(str_temp):
    return str_temp.replace(r'\N', '\n')


def replace_italic_tags(str_temp):
    return str_temp.replace(r'{\i1}', '<i>').replace(r'{\i0}', '</i>')


def replace_bold_tags(str_temp):
    return str_temp.replace(r'{\b1}', '<b>').replace(r'{\b0}', '</b>')


def remove_b100_to_b900_explicit_bold_weight(str_temp):
    return re.sub(r'{\\b[1-9]00}', '', str_temp)


def replace_underline_tags(str_temp):
    return str_temp.replace(r'{\u1}', '<u>').replace(r'{\u0}', '</u>')


def remove_strikeout_tags(str_temp):
    return re.sub(r'{\\s[0-1]\}', '', str_temp)


def remove_border_tags_and_extended(str_temp):
    return re.sub(r'{\\[x-y]?bord[0-9]*\.?[0-9]*\}', '', str_temp)


def remove_shadow_distance_and_extended(str_temp):
    return re.sub(r'{\\[x-y]?shad[0-9]*\.?[0-9]*\}', '', str_temp)


def remove_blur_edge(str_temp):
    return re.sub(r'{\\be[0-9]*\}', '', str_temp)


def remove_blur_edge_gaussian_kernel(str_temp):
    return re.sub(r'{\\blur[0-9]*\.?[0-9]*\}', '', str_temp)


def remove_font_name(str_temp, fonts_name_list):
    regex_fonts_name = "|".join(fonts_name_list)
    return re.sub(r'{\\fn(' + regex_fonts_name + ')}', '', str_temp)


def remove_font_size(str_temp):
    return re.sub(r'{\\fs[0-9]*\}', '', str_temp)


def remove_font_scale(str_temp):
    return re.sub(r'{\\fsc[x-y]?[0-9]*\}', '', str_temp)


def remove_letter_spacing(str_temp):
    return re.sub(r'{\\fsp-?[0-9]*\.?[0-9]*\}', '', str_temp)


def remove_text_rotation(str_temp):
    return re.sub(r'{\\fr[x-z]?-?[0-9]*\}', '', str_temp)


def remove_text_shearing(str_temp):
    return re.sub(r'{\\fa[x-y]+-?[0-9]*\.?[0-9]*\}', '', str_temp)


def remove_font_encoding(str_temp):
    return re.sub(r'{\\fe[0-9]*\}', '', str_temp)


def replace_text_color(str_temp):
    return re.sub(r'{\\[1-4]?c&H[0-9a-fA-F]{6}&\}', '', str_temp)


def remove_transparency_text_alpha(str_temp):
    return re.sub(r'{\\[1-4]?a(?:lpha)?&H[0-9a-fA-F]{2}&\}', '', str_temp)


def remove_line_alignment(str_temp):
    return re.sub(r'{\\a[n]?[0-9]+\}', '', str_temp)


def remove_karaoke_effect(str_temp):
    return re.sub(r'{\\[k,K][fot]?[0-9]*\}', '', str_temp)


def remove_wrap_style(str_temp):
    return re.sub(r'{\\q[0-3]*\}', '', str_temp)


def remove_reset_style(str_temp, style_list):
    regex_style_names = "|".join(style_list)
    return re.sub(r'{\\r(' + regex_style_names + ')?}', '', str_temp)


def remove_text_position(str_temp):
    return re.sub(r'{\\pos\([0-9]*, ?[0-9]*\)\}', '', str_temp)


def remove_movement(str_temp):
    return re.sub(r'{\\move\([0-9]*, ?[0-9]*, ?[0-9]*, ?[0-9]*,? ?[0-9]*,? ?[0-9]*\)\}', '', str_temp)


def remove_rotation(str_temp):
    return re.sub(r'{\\org\([0-9]*, ?[0-9]*\)\}', '', str_temp)


def remove_fade(str_temp):
    return re.sub(r'{\\fad\([0-9]*, ?[0-9]*,? ?[0-9]*,? ?[0-9]*,? ?[0-9]*,? ?[0-9]*,? ?[0-9]*\)\}', '', str_temp)


def remove_clip_rectangle(str_temp):
    return re.sub(r'{\\[i]?clip\([0-9]*, ?[0-9]*, ?[0-9]*, ?[0-9]*\)\}', '', str_temp)
