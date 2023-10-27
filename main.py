from data import titles, background_colors_1, button_colors_1, button_texts, button_actions
from random import sample

amount_title = 5
amount_bg_color = 7
amount_button_color = 7
amount_button_text = 6
amount_actions = 8
# всего 5 * 7 * 7 * 6 * 8 = 11760

html_set = dict()

for title in sample(titles, amount_title):
    for bg_color in sample(background_colors_1.values(), amount_bg_color):
        for button_color in sample(list(set(button_colors_1.values()) - {bg_color}), amount_button_color):
            for button_text in sample(button_texts, amount_button_text):
                for action in sample(button_actions.keys(), amount_actions):
                    prompt = f'Напиши мне код HTML страницы с названием {title} ' + \
                        f'на {bg_color} должна быть кнопка {button_color} с текстом ' + \
                        f'{button_text}, при нажатии на кнопку {action}'
                    print(prompt)



for text_color in ['"White"', '"Black"']:
    for button_color in ['"White"', '"Black"']:
        button_style = f'''
        .c-button {{
          appearance: none;
          border: 0;
          border-radius: 5px;
          background: {button_color};
          color: {text_color};
          padding: 8px 16px;
          font-size: 16px;
        }}
        '''
        print(button_style)

