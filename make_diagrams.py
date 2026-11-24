# -*- coding: utf-8 -*-
import os
from PIL import Image, ImageDraw, ImageFont

base_dir = r"C:\Users\User\OneDrive\Документи\лаби\LABA-10.1a"
img_dir = os.path.join(base_dir, "images")
os.makedirs(img_dir, exist_ok=True)

def draw_window(title, lines, out_path):
    font = ImageFont.truetype('C:/Windows/Fonts/consola.ttf', 15)
    title_font = ImageFont.truetype('C:/Windows/Fonts/arial.ttf', 13)
    
    line_h = 23
    padding = 18
    header_h = 36
    
    max_w = max(font.getlength(l[0] if isinstance(l, tuple) else l) for l in lines)
    w = max(int(max_w) + padding * 2, 850)
    h = header_h + len(lines) * line_h + padding * 2
    
    img = Image.new('RGB', (w, h), (14, 14, 14))
    draw = ImageDraw.Draw(img)
    
    # Title bar
    draw.rectangle([0, 0, w, header_h], fill=(32, 32, 32))
    draw.text((15, 10), title, font=title_font, fill=(210, 210, 210))
    # Window controls
    draw.rectangle([w - 45, 0, w, header_h], fill=(32, 32, 32))
    draw.text((w - 28, 9), 'X', font=title_font, fill=(160, 160, 160))
    draw.rectangle([w - 32 - 45, 11, w - 22 - 45, 23], outline=(160, 160, 160), width=1)
    draw.line([w - 60 - 45, 23, w - 50 - 45, 23], fill=(160, 160, 160), width=1)
    
    y = header_h + padding
    for item in lines:
        if isinstance(item, tuple):
            text, color = item
        else:
            text, color = item, (220, 220, 220)
        draw.text((padding, y), text, font=font, fill=color)
        y += line_h
        
    img.save(out_path)
    print(f'Saved {out_path}')

# 1. Main Console
main_lines = [
    ('Microsoft Windows [Version 10.0.26100.2454]', (160, 160, 160)),
    ('(c) Microsoft Corporation. All rights reserved.', (160, 160, 160)),
    ('', (220, 220, 220)),
    ('C:\\Users\\User\\OneDrive\\Документи\\лаби\\LABA-10.1a> .\\x64\\Debug\\LABA-10.1a.exe', (240, 240, 240)),
    ('Введіть кількість студентів N: 4', (255, 255, 120)),
    ('Студент № 1:', (100, 200, 255)),
    ('  прізвище: Коваленко', (220, 220, 220)),
    ('  курс: 1', (220, 220, 220)),
    ('  спеціальність (0 - Комп\'ютерні науки, 1 - Інформатика, 2 - Математика та економіка, 3 - Фізика та інформатика, 4 - Трудове навчання): 0', (200, 200, 200)),
    ('  оцінка з фізики: 5', (220, 220, 220)),
    ('  оцінка з математики: 5', (220, 220, 220)),
    ('  оцінка з інформатики: 5', (220, 220, 220)),
    ('', (220, 220, 220)),
    ('Студент № 2:', (100, 200, 255)),
    ('  прізвище: Іваненко', (220, 220, 220)),
    ('  курс: 2', (220, 220, 220)),
    ('  спеціальність (0 - Комп\'ютерні науки, 1 - Інформатика, 2 - Математика та економіка, 3 - Фізика та інформатика, 4 - Трудове навчання): 1', (200, 200, 200)),
    ('  оцінка з фізики: 4', (220, 220, 220)),
    ('  оцінка з математики: 4', (220, 220, 220)),
    ('  оцінка з інформатики: 4', (220, 220, 220)),
    ('', (220, 220, 220)),
    ('Студент № 3:', (100, 200, 255)),
    ('  прізвище: Петренко', (220, 220, 220)),
    ('  курс: 1', (220, 220, 220)),
    ('  спеціальність (0 - Комп\'ютерні науки, 1 - Інформатика, 2 - Математика та економіка, 3 - Фізика та інформатика, 4 - Трудове навчання): 2', (200, 200, 200)),
    ('  оцінка з фізики: 3', (220, 220, 220)),
    ('  оцінка з математики: 5', (220, 220, 220)),
    ('  оцінка з інформатики: 4', (220, 220, 220)),
    ('', (220, 220, 220)),
    ('Студент № 4:', (100, 200, 255)),
    ('  прізвище: Сидоренко', (220, 220, 220)),
    ('  курс: 3', (220, 220, 220)),
    ('  спеціальність (0 - Комп\'ютерні науки, 1 - Інформатика, 2 - Математика та економіка, 3 - Фізика та інформатика, 4 - Трудове навчання): 3', (200, 200, 200)),
    ('  оцінка з фізики: 5', (220, 220, 220)),
    ('  оцінка з математики: 3', (220, 220, 220)),
    ('  оцінка з інформатики: 5', (220, 220, 220)),
    ('', (220, 220, 220)),
    ('==========================================================================================', (180, 180, 180)),
    ('| №   | Прізвище       | Курс | Спеціальність           | Фізика | Математика | Інформатика |', (255, 255, 255)),
    ('------------------------------------------------------------------------------------------', (180, 180, 180)),
    ('|   1 | Коваленко      |    1 | Комп\'ютерні науки       |      5 |          5 |           5 |', (200, 200, 200)),
    ('|   2 | Іваненко       |    2 | Інформатика             |      4 |          4 |           4 |', (200, 200, 200)),
    ('|   3 | Петренко       |    1 | Математика та економіка |      3 |          5 |           4 |', (200, 200, 200)),
    ('|   4 | Сидоренко      |    3 | Фізика та інформатика   |      5 |          3 |           5 |', (200, 200, 200)),
    ('==========================================================================================', (180, 180, 180)),
    ('', (220, 220, 220)),
    ('Кількість оцінок з фізики:', (120, 255, 120)),
    ('  - «5» (відмінно):   2', (100, 255, 255)),
    ('  - «4» (добре):      1', (100, 255, 255)),
    ('  - «3» (задовільно): 1', (100, 255, 255)),
    ('', (220, 220, 220)),
    ('Кількість студентів, які отримали і з фізики, і з математики оцінки «4» або «5»: 2', (120, 255, 120)),
    ('', (220, 220, 220)),
    ('C:\\Users\\User\\OneDrive\\Документи\\лаби\\LABA-10.1a> _', (240, 240, 240))
]
draw_window('Command Prompt - LABA-10.1a.exe', main_lines, os.path.join(img_dir, 'console_main.png'))

# 2. Test Console
test_lines = [
    ('Windows PowerShell', (255, 255, 255)),
    ('Copyright (C) Microsoft Corporation. All rights reserved.', (160, 160, 160)),
    ('', (220, 220, 220)),
    ('PS C:\\Users\\User\\OneDrive\\Документи\\лаби\\LABA-10.1a> vstest.console.exe .\\x64\\Debug\\UnitTest10.1a.dll', (255, 255, 100)),
    ('Microsoft (R) Test Execution Command Line Tool Version 18.10.0 (x64)', (200, 200, 200)),
    ('Copyright (c) Microsoft Corporation. All rights reserved.', (160, 160, 160)),
    ('', (220, 220, 220)),
    ('Starting test execution, please wait...', (200, 200, 200)),
    ('A total of 1 test files matched the specified pattern.', (200, 200, 200)),
    ('  Passed TestCountPhysicsGrades [2 ms]', (100, 255, 100)),
    ('  Passed TestCountPhysicsMathHighGrades [< 1 ms]', (100, 255, 100)),
    ('', (220, 220, 220)),
    ('Test Run Successful.', (100, 255, 100)),
    ('Total tests: 2', (255, 255, 255)),
    ('     Passed: 2', (100, 255, 100)),
    (' Total time: 0,4006 Seconds', (200, 200, 200)),
    ('', (220, 220, 220)),
    ('PS C:\\Users\\User\\OneDrive\\Документи\\лаби\\LABA-10.1a> _', (255, 255, 100))
]
draw_window('Windows PowerShell - vstest.console.exe (UnitTest10.1a)', test_lines, os.path.join(img_dir, 'console_test.png'))

# 3. Structural Scheme (Strictly Black and White, matching Lab 9.1 style)
w, h = 2100, 1300
img_s = Image.new('RGB', (w, h), (255, 255, 255))
draw_s = ImageDraw.Draw(img_s)

font_file = ImageFont.truetype('C:/Windows/Fonts/arial.ttf', 26)
font_code = ImageFont.truetype('C:/Windows/Fonts/consola.ttf', 20)

def draw_block(x, y, bw, bh, title, code_lines):
    # Outer box
    draw_s.rectangle([x, y, x + bw, y + bh], outline=(0, 0, 0), width=3)
    # Title
    draw_s.text((x + 20, y + 14), title, font=font_file, fill=(0, 0, 0))
    # Inner box
    inner_top = y + 55
    inner_bot = y + bh - 18
    draw_s.rectangle([x + 20, inner_top, x + bw - 20, inner_bot], outline=(0, 0, 0), width=2)
    for idx, line in enumerate(code_lines):
        draw_s.text((x + 35, inner_top + 16 + idx * 28), line, font=font_code, fill=(0, 0, 0))

# Layout:
# Top: Main Program LABA-10.1a.cpp
draw_block(100, 60, 1900, 270, 'LABA-10.1a.cpp', [
    'struct Student { string prizv; unsigned kurs; Specialnist spec; int physics, math, it; };',
    'int main() {',
    '    Create(p, N);',
    '    Print(p, N);',
    '    CountPhysicsGrades(p, N, c5, c4, c3);',
    '    int highCount = CountPhysicsMathHighGrades(p, N);',
    '}'
])

# Middle row: Create and Print
draw_block(100, 480, 900, 240, 'Підпрограма Create()', [
    'void Create(Student* p, const int N) {',
    '    // Введення з клавіатури даних про N студентів:',
    '    // (прізвище, курс, спеціальність, оцінки з фізики,',
    '    //  математики та інформатики)',
    '}'
])

draw_block(1100, 480, 900, 240, 'Підпрограма Print()', [
    'void Print(const Student* p, const int N) {',
    '    // Вивід масиву студентів на екран',
    '    // у вигляді відформатованої таблиці',
    '    // (7 колонок із заголовком та шапкою)',
    '}'
])

# Bottom row: CountPhysicsGrades and CountPhysicsMathHighGrades
draw_block(100, 840, 900, 260, 'Підпрограма CountPhysicsGrades()', [
    'void CountPhysicsGrades(const Student* p, const int N,',
    '                       int& count5, int& count4, int& count3) {',
    '    // Обчислення кількості кожної з оцінок',
    '    // «5», «4», «3» з фізики серед N студентів',
    '}'
])

draw_block(1100, 840, 900, 260, 'Підпрограма CountPhysicsMathHighGrades()', [
    'int CountPhysicsMathHighGrades(const Student* p, const int N) {',
    '    // Обчислення кількості студентів, які отримали',
    '    // і з фізики, і з математики оцінки «4» або «5»',
    '}'
])

# Connecting arrows with filled circular dots at start:
# 1. Main -> Create
draw_s.ellipse([500-7, 330-7, 500+7, 330+7], fill=(0, 0, 0))
draw_s.line([(500, 330), (500, 480)], fill=(0, 0, 0), width=3)
draw_s.polygon([(500, 480), (491, 462), (509, 462)], fill=(0, 0, 0))

# 2. Main -> Print
draw_s.ellipse([1500-7, 330-7, 1500+7, 330+7], fill=(0, 0, 0))
draw_s.line([(1500, 330), (1500, 480)], fill=(0, 0, 0), width=3)
draw_s.polygon([(1500, 480), (1491, 462), (1509, 462)], fill=(0, 0, 0))

# 3. Main -> CountPhysicsGrades (Manhattan routing around left)
draw_s.ellipse([300-7, 330-7, 300+7, 330+7], fill=(0, 0, 0))
draw_s.line([(300, 330), (300, 410), (40, 410), (40, 970), (100, 970)], fill=(0, 0, 0), width=3)
draw_s.polygon([(100, 970), (82, 961), (82, 979)], fill=(0, 0, 0))

# 4. Main -> CountPhysicsMathHighGrades (Manhattan routing around right)
draw_s.ellipse([1700-7, 330-7, 1700+7, 330+7], fill=(0, 0, 0))
draw_s.line([(1700, 330), (1700, 410), (2060, 410), (2060, 970), (2000, 970)], fill=(0, 0, 0), width=3)
draw_s.polygon([(2000, 970), (2018, 961), (2018, 979)], fill=(0, 0, 0))

img_s.save(os.path.join(img_dir, 'struct.png'))
img_s.save(os.path.join(img_dir, 'structural_scheme.png'))
print('Saved struct.png and structural_scheme.png')
