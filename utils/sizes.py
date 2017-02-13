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

speach_margin = 20
speach_height = 150
speach_width = 200
speach_pos = (width_right_game - speach_width - speach_margin, height - speach_height - speach_margin)

# static UI
table_pos = (width_left_margin + 400, height_ref + 585)

# dynamic UI
human_size = (142, 177)
human_pos = (width_left_margin + 798 - 51, height_ref + 386 - 11)

tree_size = (274,245)
tree_pos = (width_left_margin + 350, height_ref + 175)

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

def event(pos, size):
    return (pos[0] + size[0] / 2, pos[1] + size[1] / 2)
# waters
size_c1 = (308,179)
pos_c1 = (width_left_margin + 191, 415)
event_c1 = event(pos_c1, size_c1)

#bushes
size_c2 = (175,175)
pos_c2 = (width_left_margin + 0, 0)
event_c2 = event(pos_c2, size_c2)

#walls
size_c3 = (593,306)
pos_c3 = (width_left_margin + 0, 463)
event_c3 = (width_left_margin + 239, 604)
event_c3alt = (width_left_margin + 239 - 58, 604)
event_c3alt2 = (width_left_margin + 239 - 58, 604 - 55)

#floor
size_c4 = (562,273)
pos_c4 = (width_left_margin + 463, 360)
event_c4 = event(pos_c4, size_c4)

#flowers (garden)
size_c5 = (144,109) #todo: check with tree
pos_c5 = (width_left_margin + 63, 271)
event_c5 = event(pos_c5, size_c5)

#animals
size_c6 = (121,75) #todo: check with goats
pos_c6 = (width_left_margin + 760, 164)
event_c6 = event(pos_c6, size_c6)

#flowers (balcony)
size_c7 = (58,65)
pos_c7 = (width_left_margin + 656, 646)
event_c7 = event(pos_c7, size_c7)

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
