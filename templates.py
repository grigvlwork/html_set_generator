base_html = f'''
<!doctype html>
<html lang="ru">
<head>
  <meta charset="utf-8" />
  <title>{title}</title>
  <link rel="stylesheet" href="style.css" />
</head>
<body>
 {body}    
</body>
</html>
'''

html_with_style = f'''
<!doctype html>
<html lang="ru">
<head>
  <meta charset="utf-8" />
  <title>{title}</title>
  <style type="text/css">
  {style}
  </style>
  <link rel="stylesheet" href="style.css" />
</head>
<body>
 {body}    
</body>
</html>
'''

html_with_button = f'''
<!doctype html>
<html lang="ru">
<head>
  <meta charset="utf-8" />
  <title>{title}</title>
  <style type="text/css">
  {style}
  </style>
  <link rel="stylesheet" href="style.css" />
</head>
<body>
    <button id="Button" onclick="submitButton()" type="submit" class="stylebutton"> 
    {button_text} </button> 
    <script>
    {js_function}
    </script>   
</body>
</html>
'''

base_prompt = f'Сделай страницу с кнопкой {color} на {bgcolor} с текстом {button_text}, при нажатии на кнопку {button_action}'
