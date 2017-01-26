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
border_text_min = 10
width_text_max = width_left_margin - 2 * border_text_min
height_button_small = 78 - border_small

width_left_images = width_left_elements - 2 * border_small

width_border_left = (width_left_margin - width_left_elements) / 2
height_left_margin = width_border_left
height_left_category = 682
height_left_category_desc = height_left_category - height_button_small
height_left_first = height_left_category_desc - width_left_elements - height_left_margin
height_left_first_desc = height_left_first - height_button_small
height_left_second = height_left_first_desc - width_left_elements - height_left_margin
height_left_second_desc = height_left_second - height_button_small


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
category_width = 186
category_number = 6.0

def category_width_progress (step):
    return step * category_width / category_number
