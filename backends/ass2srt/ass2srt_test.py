import unittest
from ass2srt_functions import *


class Ass2SrtTestCases(unittest.TestCase):
    def test_replace_ass_n_by_system_n(self):
        original_text = " Insert a forced line break, regardless of wrapping mode.\\NNote that this is an uppercase N."
        modified_text = replace_ass_n_by_system_n(original_text)
        target_text = " Insert a forced line break, regardless of wrapping mode.\nNote that this is an uppercase N."
        self.assertEqual(target_text, modified_text)

    def test_replace_italic_tags(self):
        original_text = "Switch italics text on or off. Use {\\i1} to enable italics for the following text and {\\i0} to disable italics again."
        modified_text = replace_italic_tags(original_text)
        target_text = "Switch italics text on or off. Use <i> to enable italics for the following text and </i> to disable italics again."
        self.assertEqual(target_text, modified_text)

    def test_replace_bold_tags(self):
        original_text = "Switch boldface text on or off. Use {\\b1} to enable boldface for the following text and {\\b0} to disable boldface again."
        modified_text = replace_bold_tags(original_text)
        target_text = "Switch boldface text on or off. Use <b> to enable boldface for the following text and </b> to disable boldface again."
        self.assertEqual(target_text, modified_text)

    def test_remove_b100_to_b900_explicit_bold_weight(self):
        original_text = "The \b<weight> form allows you to specify an explicit weight to use. Note that most fonts only support one or two weights so you rarely need to use this. Font weights are multiples of 100, such that {\\b100}100 is the lowest, {\\b400}400 is normal, {\\b700}700 is bold and {\\b900}900 is the heaviest."
        modified_text = remove_b100_to_b900_explicit_bold_weight(original_text)
        target_text = "The \b<weight> form allows you to specify an explicit weight to use. Note that most fonts only support one or two weights so you rarely need to use this. Font weights are multiples of 100, such that 100 is the lowest, 400 is normal, 700 is bold and 900 is the heaviest."
        self.assertEqual(target_text, modified_text)

    def test_replace_underline_tags(self):
        original_text = "Switch underlined text on or off. Use {\\u1} to enable underlining for the following text and {\\u0} to disable underlining again."
        modified_text = replace_underline_tags(original_text)
        target_text = "Switch underlined text on or off. Use <u> to enable underlining for the following text and </u> to disable underlining again."
        self.assertEqual(target_text, modified_text)

    def test_remove_strikeout_tags(self):
        original_text = "Switch striked out text on or off. Use {\\s1}\\s1 to enable strikeout for the following text and {\\s0}\\s0 to disable strikeout again."
        modified_text = remove_strikeout_tags(original_text)
        target_text = "Switch striked out text on or off. Use \\s1 to enable strikeout for the following text and \\s0 to disable strikeout again."
        self.assertEqual(target_text, modified_text)

    def test_remove_border_tags_and_extended(self):
        original_text = "{\\bord1}border1 {\\bord3.14159}border2 {\\xbord3.14}border3 {\\ybord9}border4 {\\bord10}border5 {\\bord123456789}border6{\\bord0}"
        modified_text = remove_border_tags_and_extended(original_text)
        target_text = "border1 border2 border3 border4 border5 border6"
        self.assertEqual(target_text, modified_text)

    def test_remove_shadow_distance_and_extended(self):
        original_text = "{\\shad1}shadow1 {\\shad3.14159}shadow2 {\\xshad3.14}shadow3 {\\yshad9}shadow4 {\\shad10}shadow5 {\\shad123456789}shadow6{\\shad0}"
        modified_text = remove_shadow_distance_and_extended(original_text)
        target_text = "shadow1 shadow2 shadow3 shadow4 shadow5 shadow6"
        self.assertEqual(target_text, modified_text)

    def test_remove_blur_edge(self):
        original_text = "{\\be1}This {\\be12}is {\\be154664}a blur edge text{\\be0}"
        modified_text = remove_blur_edge(original_text)
        target_text = "This is a blur edge text"
        self.assertEqual(target_text, modified_text)

    def test_remove_blur_edge_gaussian_kernel(self):
        original_text = "{\\blur1}This {\\blur1.2}is {\\blur154.664}a blur edge gaussian text{\\blur0.0}"
        modified_text = remove_blur_edge_gaussian_kernel(original_text)
        target_text = "This is a blur edge gaussian text"
        self.assertEqual(target_text, modified_text)

    def test_remove_font_name(self):
        test_fonts_name_list = ['Arial', 'Times New Roman', 'Adobe Text Pro Regular']
        original_text = "This is {\\fnArial}Arial, this is {\\fnTimes New Roman}Times New Roman and this is {\\fnAdobe Text Pro Regular}Adobe Text Pro Regular fonts."
        modified_text = remove_font_name(original_text, test_fonts_name_list)
        target_text = "This is Arial, this is Times New Roman and this is Adobe Text Pro Regular fonts."
        self.assertEqual(target_text, modified_text)

    def test_remove_font_size(self):
        original_text = "{\\fs10}The {\\fs18}text {\\fs26}is {\\fs34}bigger {\\fs42}and {\\fs50}bigger {\\fs58}and {\\fs66}bigger"
        modified_text = remove_font_size(original_text)
        target_text = "The text is bigger and bigger and bigger"
        self.assertEqual(target_text, modified_text)

    def test_remove_font_scale(self):
        original_text = "{\\fscx10}The {\\fscy18}text {\\fscx26}is {\\fscy34}weirder {\\fscx42}and {\\fscy50}weirder {\\fscx58}and {\\fscy66}weirder"
        modified_text = remove_font_scale(original_text)
        target_text = "The text is weirder and weirder and weirder"
        self.assertEqual(target_text, modified_text)

    def test_remove_letter_spacing(self):
        original_text = "Changes {\\fsp-0.9}the {\\fsp-.5}spacing {\\fsp9}between {\\fsp0.04546459}the individual {\\fsp1}letters in the text"
        modified_text = remove_letter_spacing(original_text)
        target_text = "Changes the spacing between the individual letters in the text"
        self.assertEqual(target_text, modified_text)

    def test_remove_text_rotation(self):
        original_text = "Rotates the text along the {\\frx565}X, {\\fry-058}Y or {\\frz720}Z axis. The \\fr {\\fr46}tag is a shortcut for \\frz."
        modified_text = remove_text_rotation(original_text)
        target_text = "Rotates the text along the X, Y or Z axis. The \\fr tag is a shortcut for \\frz."
        self.assertEqual(target_text, modified_text)

    def test_remove_text_shearing(self):
        original_text = "Perform a shearing ({\\fax.6}perspective distortion) {\\fay2}transformation of the {\\fax-5}text."
        modified_text = remove_text_shearing(original_text)
        target_text = "Perform a shearing (perspective distortion) transformation of the text."
        self.assertEqual(target_text, modified_text)

    def test_remove_font_encoding(self):
        original_text = "Set {\\fe136}the Windows {\\fe0}font {\\fe162}encoding {\\fe163}used to {\\fe1}select the font {\\fe2}mapping table {\\fe128}used to {\\fe177}translate {\\fe129}Unicode {\\fe130}code points {\\fe134}to glyph {\\fe178}indices in the font."
        modified_text = remove_font_encoding(original_text)
        target_text = "Set the Windows font encoding used to select the font mapping table used to translate Unicode code points to glyph indices in the font."
        self.assertEqual(target_text, modified_text)

    def test_replace_text_color(self):
        original_text = "{\\c&H000000&}Set {\\1c&H111111&}the {\\2c&H151985&}color {\\3c&Hfe58cd&}of {\\4c&Hff00ff&}the following text. The \\c tag is an abbreviation of \\1c."
        modified_text = replace_text_color(original_text)
        target_text = "Set the color of the following text. The \\c tag is an abbreviation of \\1c."
        self.assertEqual(target_text, modified_text)

    def test_remove_transparency_text_alpha(self):
        original_text = "{\\alpha&H00&}Set {\\1a&H80&}the {\\2a&H5F&}alpha ({\\3a&HFF&}transparency) {\\4a&HCD&}of the text."
        modified_text = remove_transparency_text_alpha(original_text)
        target_text = "Set the alpha (transparency) of the text."
        self.assertEqual(target_text, modified_text)

    def test_remove_line_alignment(self):
        original_text = "{\\an5}Specify the {\\a11}alignment of the line."
        modified_text = remove_line_alignment(original_text)
        target_text = "Specify the alignment of the line."
        self.assertEqual(target_text, modified_text)

    def test_remove_karaoke_effect(self):
        original_text = "{\\k100}Please {\\K150}note {\\kf200}that {\\ko250}these {\\kt300}tags alone only create some very specific effects"
        modified_text = remove_karaoke_effect(original_text)
        target_text = "Please note that these tags alone only create some very specific effects"
        self.assertEqual(target_text, modified_text)

    def test_remove_wrap_style(self):
        original_text = "Determine {\\q0}how line {\\q1}breaking is {\\q2}applied to {\\q3}the subtitle line."
        modified_text = remove_wrap_style(original_text)
        target_text = "Determine how line breaking is applied to the subtitle line."
        self.assertEqual(target_text, modified_text)

    def test_remove_reset_style(self):
        test_regex_style_names = ['Default', 'Alternate', 'Sign', 'Song', 'TITLE']
        original_text = "{\\r}Reset the style. This {\\rDefault}cancels all {\\rAlternate}style overrides {\\rSign}in effect, {\\rSong}including animations, for all {\\rTITLE}following text."
        modified_text = remove_reset_style(original_text, test_regex_style_names)
        target_text = "Reset the style. This cancels all style overrides in effect, including animations, for all following text."
        self.assertEqual(target_text, modified_text)

    def test_remove_text_position(self):
        original_text = "{\\pos(152, 758)}Set the position {\\pos(2,1)}of the line."
        modified_text = remove_text_position(original_text)
        target_text = "Set the position of the line."
        self.assertEqual(target_text, modified_text)

    def test_remove_movement(self):
        original_text = "The \\move {\\move(156,750, 48, 10)}tag works similar to \\pos in that it positions the subtitle line, the{\\move(574, 1088,931, 49,74, 54)} difference is that \\move makes the subtitle move."
        modified_text = remove_movement(original_text)
        target_text = "The \\move tag works similar to \\pos in that it positions the subtitle line, the difference is that \\move makes the subtitle move."
        self.assertEqual(target_text, modified_text)

    def test_remove_rotation(self):
        original_text = "Set {\\org(150, 898)}the origin point used for rotation. {\\org(150,898)}This affects all rotations of the line."
        modified_text = remove_rotation(original_text)
        target_text = "Set the origin point used for rotation. This affects all rotations of the line."
        self.assertEqual(target_text, modified_text)

    def test_remove_fade(self):
        original_text = "Produce a {\\fad(1500, 500)}fade-in and {\\fad(500,1500)}fade-out effect. {\\fad(5,10, 15, 20,7,5, 6)}The fadein and fadeout times are given in milliseconds."
        modified_text = remove_fade(original_text)
        target_text = "Produce a fade-in and fade-out effect. The fadein and fadeout times are given in milliseconds."
        self.assertEqual(target_text, modified_text)

    def test_remove_clip_rectangle(self):
        original_text = "Define {\\clip(0,0, 150, 254)}a rectangle to clip the line, only the part{\\iclip(5, 152,350, 569)} of the line that is inside the rectangle is visible."
        modified_text = remove_clip_rectangle(original_text)
        target_text = "Define a rectangle to clip the line, only the part of the line that is inside the rectangle is visible."
        self.assertEqual(target_text, modified_text)


if __name__ == '__main__':
    unittest.main()
