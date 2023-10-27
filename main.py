from data import titles, background_colors_1, button_colors_1, button_texts, button_actions, colors, js_functions, \
    introductions
from random import sample
import flask
from flask import render_template
import json


def button_text_color(color):
    if color in ['Black', 'Gray', 'Fuchsia', 'Purple', 'Red', 'Maroon', 'Olive', 'Green', 'Blue', 'Navy']:
        return 'White'
    else:
        return 'Black'


amount_intros = 4
amount_title = 5
amount_bg_color = 7
amount_button_color = 7
amount_button_text = 6
amount_actions = 4
# всего 4 * 5 * 7 * 7 * 6 * 4 = 23520

html_set = dict()
for intro in sample(introductions, amount_intros):
    for title in sample(titles, amount_title):
        bg_colors = sample(colors, amount_bg_color)
        for bg_color in bg_colors:
            bg_color_text = list(background_colors_1.keys())[list(background_colors_1.values()).index(bg_color)]
            button_colors = sample(list(set(colors) - {bg_color}), amount_button_color)
            for button_color in button_colors:
                button_color_text = list(button_colors_1.keys())[list(button_colors_1.values()).index(button_color)]
                for button_text in sample(sorted(button_texts), amount_button_text):
                    for action_text in sample(sorted(button_actions.keys()), amount_actions):
                        prompt = f'{intro} с названием "{title}", ' + \
                                 f'на {bg_color_text} должна быть кнопка {button_color_text} с текстом ' + \
                                 f'"{button_text}", при нажатии на кнопку {action_text}.'
                        action_name = button_actions[action_text]
                        # print(prompt)
                        style = f'\n\t\t\tbody {{\n\t\t\t\tbackground-color: {bg_color};\n\t\t\t}}'+ \
                                f'\n\t\t\t.stylebutton {{\n\t\t\t\tappearance: none;\n\t\t\t\tborder: 0;' + \
                                f'\n\t\t\t\tborder-radius: 5px;\n\t\t\t\tbackground: {button_color};' + \
                                f'\n\t\t\t\tcolor: {button_text_color(button_color)};\n\t\t\t\tpadding: 8px 16px;' + \
                                f'\n\t\t\t\tfont-size: 16px;\n\t\t\t}}'

                        answer = f'\n<!doctype html>\n<html lang="ru">\n\t<head>\n\t\t<meta charset="utf-8">' + \
                                 f'\n\t\t<title>{title}</title>\n\t\t<style type="text/css">{style}\n\t\t</style>' + \
                                 f'\n\t</head>\n\t<body>' + \
                                 f'\n\t\t<button id="Button" onclick="submitButton()" type="submit" class="stylebutton">' + \
                                 f'\n\t\t\t{button_text}\n\t\t</button>\n\t\t<script>\n\t\t\t{js_functions[action_name]}' + \
                                 f'\n\t\t</script>\n\t</body>\n</html>'

                        #
                        # answer = render_template('html_with_button.html',
                        #                          title='title',
                        #                          style=style,
                        #                          button_text=button_text,
                        #                          js_function=js_functions[action_name]
                        #                          )
                        html_set[prompt] = answer
with open('dataset.json', 'w', encoding='utf-8') as fp:
    json.dump(html_set, fp, ensure_ascii=False)
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
