from data import titles, background_colors_1, button_colors_1, button_texts, button_actions, colors, js_functions
from random import sample
import flask
from flask import render_template


def button_text_color(color):
    if color in ['Black', 'Gray', 'Fuchsia', 'Purple', 'Red', 'Maroon', 'Olive', 'Green', 'Blue', 'Navy']:
        return 'White'
    else:
        return 'Black'


amount_title = 5
amount_bg_color = 7
amount_button_color = 7
amount_button_text = 6
amount_actions = 8
# всего 5 * 7 * 7 * 6 * 8 = 11760

html_set = dict()

for title in sample(titles, amount_title):
    bg_colors = sample(colors, amount_bg_color)
    for bg_color in bg_colors:
        bg_color_text = list(background_colors_1.keys())[list(background_colors_1.values()).index(bg_color)]
        button_colors = sample(list(set(colors) - {bg_color}), amount_button_color)
        for button_color in button_colors:
            button_color_text = list(button_colors_1.keys())[list(button_colors_1.values()).index(button_color)]
            for button_text in sample(sorted(button_texts), amount_button_text):
                for action_text in sample(sorted(button_actions.keys()), amount_actions):
                    prompt = f'Напиши мне код HTML страницы с названием "{title}" ' + \
                             f'на {bg_color_text} должна быть кнопка {button_color_text} с текстом ' + \
                             f'"{button_text}", при нажатии на кнопку {action_text}.'
                    action_name = button_actions[action_text]
                    # print(prompt)
                    style = f'''
                    body {{
                      background-color: {bg_color};
                    }}
                    .stylebutton {{
                      appearance: none;
                      border: 0;
                      border-radius: 5px;
                      background: {button_color};
                      color: {button_text_color(button_color)};
                      padding: 8px 16px;
                      font-size: 16px;
                    }}
                    '''
                    answer = render_template('html_with_button.html',
                                             title='title',
                                             style=style,
                                             button_text=button_text,
                                             js_function=js_functions[action_name]
                                             )
                    print(answer)

# for text_color in ['"White"', '"Black"']:
#     for button_color in ['"White"', '"Black"']:
#         button_style = f'''
#         .c-button {{
#           appearance: none;
#           border: 0;
#           border-radius: 5px;
#           background: {button_color};
#           color: {text_color};
#           padding: 8px 16px;
#           font-size: 16px;
#         }}
#         '''
#         print(button_style)
