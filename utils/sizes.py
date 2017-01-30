height_ref = 0
height_used = 768
height = height_ref + height_used
width_ref = 0
width_used = 1366
width = width_ref + width_used
width_game = 1024

width_left_margin = 200
width_right_game = width_left_margin + width_game
width_right_margin = width - width_game - width_left_margin
width_left_elements = 144

border_small = 6
border_text_min = border_small * 2
width_text_max = width_left_margin - 2 * border_text_min
height_button_small = 78 - border_small

height_title = 80
height_left_category_element = height_title - border_small

width_left_images = width_left_elements - 2 * border_small

width_border_left = (width_left_margin - width_left_elements) / 2
height_left_margin = width_border_left
height_left_category_title = height_used - height_title
height_left_category_desc = height_left_category_title - height_title
height_left_first = height_left_category_desc - width_left_elements - height_left_margin
height_left_first_desc = height_left_first - height_title


def gauge_height(step):
    return gauge_bottom_first + step * gauge_bottom_next


gauge_width = 24
gauge_left_margin = width_right_game + 22
gauge_left_start = gauge_left_margin + 47
gauge_bottom_margin = 150
gauge_bottom_start = gauge_bottom_margin + 9
gauge_bottom_first = 18
gauge_bottom_next = 34.3
gauge_number = 6

smiley_size = 29
gauge_smiley_left = gauge_left_start + (gauge_width - smiley_size) / 2.0
gauge_smiley_margin = 11
gauge_smiley_bottom = gauge_bottom_margin - gauge_smiley_margin - smiley_size
gauge_smiley_top = gauge_bottom_start + gauge_height(2 * gauge_number) + 27

cursor_height = 20
cursor_left = gauge_left_start + 15
def cursor_pos_y(step):
    return gauge_bottom_start + gauge_height(step) - cursor_height/2.0

category_height = 23
category_width = 188
category_number = 6.0

#remaining size is spread over the 2 elements
left_margin_elements = (height_left_first - 2 * height_title - width_left_elements - height_button_small - border_small - category_height) / 2
height_left_second = height_left_first_desc - width_left_elements - left_margin_elements
height_left_second_desc = height_left_second - height_title

def category_width_progress (step):
    return step * category_width / category_number

font_size_default= 18
font_size_large = 22
font_size_subtitle = 24
font_size_title = 34

#negative_window
win_dx = 262
win_dy = 82
win_width = 898
win_height = 600
win_header = 80
win_width_infos = 183
win_choice_width = 400
win_choice_height = 194
win_choice_header = 38
win_choice_margin = (win_width - 2 * win_choice_width) / 3
win_choice_left = win_choice_margin
win_choice_right = win_choice_width + 2 * win_choice_margin
win_choice_down = win_choice_margin
win_choice_up = win_choice_height + 2 * win_choice_margin
win_choice_img_size = width_left_images

win_choice_inner_margin = (win_choice_height - win_choice_header - win_choice_img_size) / 2
win_choice_inner_center = (win_choice_width - win_choice_img_size) / 2
win_choice_inner_left = win_choice_inner_center - win_choice_img_size * 0.75
win_choice_inner_right = win_choice_inner_center + win_choice_img_size * 0.75
