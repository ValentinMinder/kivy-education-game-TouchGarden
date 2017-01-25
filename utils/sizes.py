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

border_margin = 20
height_left_margin = 300
height_left_elements = 250
height_button_small = 78

border = 26


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
