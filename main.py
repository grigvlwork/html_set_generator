from data import titles, background_colors_1, button_colors_1, button_texts, button_actions, colors, js_functions, \
    introductions
from random import sample
import flask
from flask import render_template
import json


def button_text_color(color):
    if color in ['Black', 'Gray', 'Fuchsia', 'Purple', 'Red', 'Maroon', 'Olive', 'Green', 'Blue', 'Navy',
                 'linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet)']:
        return 'White'
    else:
        return 'Black'


amount_intros = 4
amount_title = 5
amount_bg_color = 17
amount_button_color = 17
amount_button_text = 6
amount_actions = 4
# Простые действия
html_set = dict()
for intro in sample(introductions, amount_intros):
    for title in sample(titles, amount_title):
        bg_colors = sample(colors, amount_bg_color)
        for bg_color in bg_colors:
            bg_color_text = list(background_colors_1.keys())[list(background_colors_1.values()).index(bg_color)]
            button_colors = sample(list(set(colors) - {bg_color}), amount_button_color - 1)
            for button_color in button_colors:
                button_color_text = list(button_colors_1.keys())[list(button_colors_1.values()).index(button_color)]
                for button_text in sample(sorted(button_texts), amount_button_text):
                    for action_text in sample(sorted(button_actions.keys()), amount_actions):
                        prompt = f'{intro} с названием "{title}", ' + \
                                 f'на {bg_color_text} должна быть кнопка {button_color_text} с текстом ' + \
                                 f'"{button_text}", при нажатии на кнопку {action_text}.'
                        action_name = button_actions[action_text]
                        # print(prompt)
                        style = f'\n\t\t\tbody {{\n\t\t\t\tbackground: {bg_color};\n\t\t\t}}' + \
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
                        html_set[prompt] = answer

# Убегающая кнопка
for intro in sample(introductions, amount_intros):
    for title in sample(titles, amount_title):
        bg_colors = sample(colors, amount_bg_color)
        for bg_color in bg_colors:
            bg_color_text = list(background_colors_1.keys())[list(background_colors_1.values()).index(bg_color)]
            button_colors = sample(list(set(colors) - {bg_color}), amount_button_color - 1)
            for button_color in button_colors:
                button_color_text = list(button_colors_1.keys())[list(button_colors_1.values()).index(button_color)]
                for button_text in sample(sorted(button_texts), amount_button_text):
                    prompt = f'{intro} с названием "{title}", ' + \
                             f'на {bg_color_text} должна быть убегающая кнопка {button_color_text} с текстом ' + \
                             f'"{button_text}".'
                    # print(prompt)
                    style = f'\n\t\t\tbody {{\n\t\t\t\tmargin: 0;\n\t\t\t\tbackground: {bg_color};\n\t\t\t}}' + \
                            f'\n\t\t\t.stylebutton {{\n\t\t\t\tappearance: none;\n\t\t\t\tborder: 0;' + \
                            f'\n\t\t\t\tposition: absolute; \n\t\t\t\tleft: 50%;\n\t\t\t\ttop: 50%;\n\t\t\t\ttransition: 0.09s;' + \
                            f'\n\t\t\t\tborder-radius: 5px;\n\t\t\t\tbackground: {button_color};' + \
                            f'\n\t\t\t\tcolor: {button_text_color(button_color)};\n\t\t\t\tpadding: 8px 16px;' + \
                            f'\n\t\t\t\tfont-size: 16px;\n\t\t\t\tfont-weight:bold;\n\t\t\t}}' + \
                            f'\n\t\t\t.board{{\n\t\t\t\twidth: 100vw;\n\t\t\t\theight: 100vw;\n\t\t\t\tbackground-color: {bg_color};\n\t\t\t}}'

                    answer = f'\n<!doctype html>\n<html lang="ru">\n\t<head>\n\t\t<meta charset="utf-8">' + \
                             f'\n\t\t<title>{title}</title>\n\t\t<style type="text/css">{style}\n\t\t</style>' + \
                             f'\n\t</head>\n\t<body>\n\t<div class="board">\n\t\t<button id="Button" type="submit" class="stylebutton">' + \
                             f'\n\t\t\t{button_text}\n\t\t</button>\n\t<div>' + \
                             f'\n\t\t<script>\n\t\t\tconst random = (min, max) => {{\n\t\t\t\tconst rnd = min + Math.random() * (max - min + 1);' + \
                             f"\n\t\t\t\treturn Math.floor(rnd);\n\t\t\t}}\n\t\t\tconst btn = document.querySelector('#Button');" + \
                             f"\n\t\t\tbtn.addEventListener('mouseenter', () => {{\n\t\t\t\tbtn.style.left = `${{random(0, 90)}}%`;" + \
                             f"\n\t\t\t\tbtn.style.top = `${{random(0, 90)}}%`;\n\t\t\t}});\n\t\t\t\tbtn.addEventListener('click', () => {{" + \
                             f"\n\t\t\t\talert('Поздравляю! Ты нажал Кнопу! Давай ещё раз!:)');\n\t\t\t}});\n\t\t</script>" + \
                             f'\n\t</body>\n</html>'
                    html_set[prompt] = answer

# Фейерверк
for intro in sample(introductions, amount_intros):
    for title in sample(titles, amount_title):
        bg_colors = sample(colors, amount_bg_color)
        for bg_color in bg_colors:
            bg_color_text = list(background_colors_1.keys())[list(background_colors_1.values()).index(bg_color)]
            button_colors = sample(list(set(colors) - {bg_color}), amount_button_color - 1)
            for button_color in button_colors:
                button_color_text = list(button_colors_1.keys())[list(button_colors_1.values()).index(button_color)]
                for button_text in sample(sorted(button_texts), amount_button_text):
                    prompt = f'{intro} с названием "{title}", ' + \
                             f'на {bg_color_text} должна быть кнопка {button_color_text} с текстом ' + \
                             f'"{button_text}", при нажатии на кнопку запускается фейерверк.'
                    # print(prompt)
                    style = f'\n\t\t\tbody {{\n\t\t\t\tbackground: {bg_color};\n\t\t\t\tmargin: 0;\n\t\t\t\tpadding: 0;' + \
                            f'\n\t\t\t\toverflow: hidden;\n\t\t\t}}' + \
                            f'\n\t\t\t.stylebutton {{\n\t\t\t\tappearance: none;\n\t\t\t\tborder: 0;' + \
                            f'\n\t\t\t\tborder-radius: 5px;\n\t\t\t\tbackground: {button_color};' + \
                            f'\n\t\t\t\tcolor: {button_text_color(button_color)};\n\t\t\t\tpadding: 8px 16px;' + \
                            f'\n\t\t\t\tfont-size: 16px;\n\t\t\t}}' + \
                            f'\n\t\t\t.divcanvas {{\n\t\t\t\tvisibility: hidden;\n\t\t\t}}' + \
                            f'\n\t\t\t.divcbtn {{\n\t\t\t\tvisibility: visible;\n\t\t\t}}'
                    answer = f'\n<!doctype html>\n<html lang="ru">\n\t<head>\n\t\t<meta charset="utf-8">' + \
                             f'\n\t\t<title>{title}</title>\n\t\t<style type="text/css">{style}\n\t\t</style>' + \
                             f'\n\t</head>\n\t<body>\n\t<div id="btndiv" class="divbtn">' + \
                             f'\n\t\t<button id="Button" onclick="submitButton()" type="submit" class="stylebutton">' + \
                             f'\n\t\t\t{button_text}\n\t\t</button>\n\t</div>\n\t<div id="div" align="center" class="divcanvas">' + \
                             f'\n\t\t<canvas id="canvas" style="border: 0px">\n\t\t</canvas>\n\t</div>' + \
                             f'\n\t<script>\n\t\tvar b = document.getElementById("div");' + \
                             f'\n\t\tvar c = document.getElementById("canvas");\n\t\tvar a = c.getContext("2d");' + \
                             f'\n\t\tvar W=c.width=document.body.clientWidth;\n\t\tvar H=c.height=screen.height;' + \
                             f'\n\t\tvar Objects=[];\n\t\tvar Colors="255,0,0;0,255,0;0,0,255;255,255,0;255,0,255;0,255,255;255,255,204;255,204,255;204,255,255".split(";");' + \
                             f'\n\t\tvar timeInterval=20;\n\t\tvar petardColor="rgb(0,128,0)";\n\t\tvar numRays=16;' + \
                             f'\n\t\tvar percentAlive=60;\n\t\tvar petardRadius=3;\n\t\tvar fireRadius=31;' + \
                             f'\n\t\tvar fireBallRadius=5;\n\n\t\tfunction submitButton(){{' + \
                             f'\n\t\t\tdocument.getElementById("div").style.visibility = "visible";\n\t\t}};' + \
                             f'\n\n\t\tDeleteObject=function (obj,t) {{\n\t\t\tif(t) delete Objects[obj];' + \
                             f'\n\t\t\telse Objects[Objects.length]=obj;\n\t\t}};\n\n\t\tDrawBack=function() {{' + \
                             f'\n\t\t\ta["globalCompositeOperation"]="source-over";\n\t\t\ta.fillStyle="rgba(0,0,0,.4)";' + \
                             f'\n\t\t\ta.fillRect(0,0,W,H);\n\t\t}};\n\t\tColorPath=function(x,y,r,f) {{' + \
                             f'\n\t\t\ta.beginPath();\n\t\t\ta.arc(x,y,r,0,Math.PI*2,0);\n\t\t\ta.fillStyle=f;' + \
                             f'\n\t\t\ta.fill();\n\t\t}};\n\n\t\tFinalDraw=function(k,x,y,g){{\n\t\t\tthis.k=k;' + \
                             f'\n\t\t\tthis.x=k?x:(Math.random()*(W-200))+100;\n\t\t\tthis.y=k?y:H;\n\t\t\tthis.t=0;' + \
                             f'\n\t\t\tthis.j=k ? 25 : 75;\n\t\t\tthis.a=k ? Math.random()*360 : 240+Math.random()*70;' + \
                             f'\n\t\t\tthis.s=Math.random()*3+2;\n\t\t\tthis.g=g;\n\t\t\tthis.thisDraw=function() {{' + \
                             f'\n\t\t\t\tthis.t++;\n\t\t\t\tif(this.k) {{\n\t\t\t\t\tf=(Math.PI/180)*this.a;' + \
                             f'\n\t\t\t\t\tthis.x+=Math.cos(f)*this.s;\n\t\t\t\t\tthis.y+=Math.sin(f)*this.s;' + \
                             f'\n\t\t\t\t\ta["globalCompositeOperation"]="lighter";' + \
                             f'\n\t\t\t\t\tg=a.createRadialGradient(this.x,this.y,1,this.x,this.y,fireBallRadius);' + \
                             f'\n\t\t\t\t\tg["addColorStop"](0,"rgba(255,255,255,.55)");\n\t\t\t\t\tg["addColorStop"](1,"rgba("+this.g+",.03)");' + \
                             f'\n\t\t\t\t\tColorPath(this.x,this.y,fireRadius,g);\n\t\t\t\t}}\n\t\t\t\telse {{' + \
                             f'\n\t\t\t\t\tf=(Math.PI/180)*this.a;\n\t\t\t\t\tthis.x+=Math.cos(f)*5;' + \
                             f'\n\t\t\t\t\tthis.y+=Math.sin(f)*7.5;\n\t\t\t\t\tColorPath(this.x,this.y,petardRadius,petardColor);' + \
                             f'\n\t\t\t\t}}\n\t\t\t}}\n\t\t\t}};\n\t\t\tsetInterval(\n\t\t\t\tfunction() {{' + \
                             f'\n\t\t\t\t\tDrawBack();\n\t\t\t\t\tfor (q in Objects) {{\n\t\t\t\t\t\tvar obj=Objects[q];' + \
                             f'\n\t\t\t\t\t\tobj.thisDraw();\n\t\t\t\t\t\tif(obj.t>obj.j) {{' + \
                             f'\n\t\t\t\t\t\t\tif(!obj.k) {{\n\t\t\t\t\t\t\t\th=Math.random()*Colors.length|0;' + \
                             f'\n\t\t\t\t\t\t\t\tfor (c=0;c<numRays;c++) DeleteObject(new FinalDraw(1,obj.x,obj.y,Colors[h]));' + \
                             f'\n\t\t\t\t\t\t\t}}\n\t\t\t\t\t\t\tDeleteObject(q,1);\n\t\t\t\t\t\t}}\n\t\t\t\t\t}}' + \
                             f'\n\t\t\t\t\tvar c=Math.random()*100;\n\t\t\t\t\tif(c>percentAlive) DeleteObject(new FinalDraw);' + \
                             f'\n\t\t\t\t}},timeInterval);' + \
                             f'\n\t</script>\n\t</body>\n</html>'
                    html_set[prompt] = answer

with open('dataset.json', 'w', encoding='utf-8') as fp:
    json.dump(html_set, fp, ensure_ascii=False)


