# -*- coding: utf-8 -*-
import os
from docx import Document
from docx.shared import Pt, Inches, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

BASE_DIR = r"C:\Users\User\OneDrive\Документи\лаби\LABA-10.1a"
IMG_DIR = os.path.join(BASE_DIR, "images")
OUT_DOCX = os.path.join(BASE_DIR, "АП_РІ-13_Шах_ЛР-10.1а.docx")

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._element.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('w:top', top), ('w:bottom', bottom), ('w:left', left), ('w:right', right)]:
        node = OxmlElement(m)
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def set_cell_shading(cell, color_hex="F8F9FA"):
    shading_elm = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>')
    cell._element.get_or_add_tcPr().append(shading_elm)

def add_p(doc, text="", bold=False, italic=False, size=12, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=6, space_before=0):
    p = doc.add_paragraph()
    p.alignment = align
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.line_spacing = 1.15
    if text:
        r = p.add_run(text)
        r.bold = bold
        r.italic = italic
        r.font.name = 'Times New Roman'
        r.font.size = Pt(size)
        r.font.color.rgb = RGBColor(0, 0, 0)
    return p

def add_h(doc, text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.keep_with_next = True
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(6)
    r = p.add_run(text)
    r.bold = True
    r.font.name = 'Times New Roman'
    r.font.size = Pt(14)
    r.font.color.rgb = RGBColor(0, 0, 0)
    return p

def add_code_block(doc, code_text):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    cell.width = Inches(6.5)
    set_cell_shading(cell, "F8F9FA")
    set_cell_margins(cell, top=100, bottom=100, left=140, right=140)
    tcPr = cell._element.get_or_add_tcPr()
    tcBorders = parse_xml(
        f'<w:tcBorders {nsdecls("w")}>\n'
        f'  <w:left w:val="single" w:sz="12" w:space="0" w:color="333333"/>\n'
        f'  <w:top w:val="single" w:sz="4" w:space="0" w:color="CCCCCC"/>\n'
        f'  <w:right w:val="single" w:sz="4" w:space="0" w:color="CCCCCC"/>\n'
        f'  <w:bottom w:val="single" w:sz="4" w:space="0" w:color="CCCCCC"/>\n'
        f'</w:tcBorders>'
    )
    tcPr.append(tcBorders)
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.line_spacing = 1.05
    r = p.add_run(code_text)
    r.font.name = 'Courier New'
    r.font.size = Pt(10)
    r.font.color.rgb = RGBColor(0, 0, 0)
    add_p(doc, "", space_after=4)

def add_img(doc, path, caption):
    if os.path.exists(path):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(6)
        p.paragraph_format.space_after = Pt(2)
        p.add_run().add_picture(path, width=Inches(5.5))
        add_p(doc, caption, italic=True, size=11, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=8)

def read_txt(rel_path):
    with open(os.path.join(BASE_DIR, rel_path), "r", encoding="utf-8") as f:
        return f.read().rstrip()

def generate_report():
    doc = Document()
    for section in doc.sections:
        section.top_margin = Cm(2)
        section.bottom_margin = Cm(2)
        section.left_margin = Cm(2)
        section.right_margin = Cm(2)

    # Титульна сторінка
    add_p(doc, "", space_after=60)
    title_text = (
        "ЗВІТ\n"
        "про виконання лабораторної роботи № 10.1a\n"
        "«Масиви структур та об'єднань»\n"
        "з дисципліни\n"
        "«Алгоритмізація та програмування»\n\n"
        "студента групи РІ-13\n"
        "Шаха Владислава Ігоровича"
    )
    add_p(doc, title_text, bold=True, size=14, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12)
    add_p(doc, "", space_after=60)
    add_p(doc, "Варіант № 32", bold=True, size=12, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12)
    doc.add_page_break()

    # 1. Мета роботи
    add_h(doc, "1. Мета роботи")
    add_p(doc, "Метою лабораторної роботи є набуття практичних навичок визначення і використання структур даних (struct), переліків (enum) та об'єднань (union) у мові програмування С++. Вивчення способів оголошення масивів структур, звернення до полів структур, а також реалізації підпрограм обробки масивів структур.")

    # 2. Завдання
    add_h(doc, "2. Завдання")
    add_img(doc, os.path.join(IMG_DIR, "task.png"), "Рис. 1. Умова лабораторної роботи № 10.1а (Варіант 32)")

    # 3. Алгоритм розв'язання
    add_h(doc, "3. Алгоритм розв'язання")
    add_p(doc, "1. Оголошено перелік enum Specialnist (KOMP_NAUKY, INFORMATYKA, MAT_EKON, FIZ_INF, TRUD_NAVCH) та масив рядків specialnistStr для текстового відображення спеціальності.")
    add_p(doc, "2. Описано структуру Student рівня А, що містить поля: prizv (прізвище студента, std::string), kurs (номер курсу, unsigned), spec (спеціальність, Specialnist), physics, math, it (цілочисельні оцінки з фізики, математики та інформатики).")
    add_p(doc, "3. У функції main() користувач вводить кількість студентів N, після чого динамічно виділяється пам'ять під масив структур Student* p = new Student[N].")
    add_p(doc, "4. Підпрограма Create(p, N) заповнює поля кожного елемента масиву з клавіатури; Print(p, N) виводить дані у вигляді відформатованої таблиці із 7 стовпців.")
    add_p(doc, "5. Підпрограма CountPhysicsGrades(p, N, count5, count4, count3) у циклі підраховує кількість оцінок «5», «4» та «3» з фізики та повертає результати через параметри-посилання.")
    add_p(doc, "6. Підпрограма CountPhysicsMathHighGrades(p, N) підраховує та повертає кількість студентів, у яких одночасно оцінка з фізики належить множині {4, 5} і оцінка з математики належить множині {4, 5}. Після виведення результатів пам'ять звільняється оператором delete[].")

    # 4. Лістинг програми
    add_h(doc, "4. Лістинг програми")
    add_p(doc, "Головний файл програми LABA-10.1a.cpp:", bold=True, space_after=4)
    add_code_block(doc, read_txt(r"LABA-10.1a\LABA-10.1a.cpp"))
    add_p(doc, "Заголовний файл student.h:", bold=True, space_after=4)
    add_code_block(doc, read_txt(r"LABA-10.1a\student.h"))
    add_p(doc, "Файл реалізації student.cpp:", bold=True, space_after=4)
    add_code_block(doc, read_txt(r"LABA-10.1a\student.cpp"))

    # 5. Схема програми
    add_h(doc, "5. Схема програми")
    add_img(doc, os.path.join(IMG_DIR, "struct.png"), "Рис. 2. Структурна схема програми LABA-10.1a")

    # 6. Результати виконання програми
    add_h(doc, "6. Результати виконання програми")
    add_img(doc, os.path.join(IMG_DIR, "console_main.png"), "Рис. 3. Результат роботи основної програми у консолі")
    add_img(doc, os.path.join(IMG_DIR, "console_test.png"), "Рис. 4. Результат виконання модульних тестів (vstest.console.exe)")

    # 7. Контрольні запитання
    add_h(doc, "7. Контрольні запитання")
    qa = [
        ("1. Що таке структура (struct) у C++ та для чого вона використовується?",
         "Структура (struct) — це складений тип даних, що об'єднує під одним іменем логічно пов'язані поля різних типів. Вона використовується для опису комплексних об'єктів, наприклад запису про студента."),
        ("2. Чим відрізняється перелік (enum) від звичайних цілочисельних констант?",
         "Перелік enum створює новий іменований тип даних із обмеженим набором символічних констант, що підвищує читабельність коду та забезпечує суворішу типізацію порівняно з розрізненими числовими константами."),
        ("3. Що таке об'єднання (union) і як воно зберігається в пам'яті?",
         "Об'єднання (union) — це тип даних, усі поля якого розміщуються в одній і тій самій області пам'яті, тому розмір union визначається розміром його найбільшого поля, і в кожен момент часу коректно зберігається лише одне активне поле."),
        ("4. Як виконується динамічне виділення та звільнення пам'яті для масиву структур?",
         "Динамічний масив створюється оператором new Student[N], який повертає вказівник на перший елемент, а після завершення використання обов'язково звільняється оператором delete[]."),
        ("5. Якими способами можна передавати масив структур у функцію та повертати кілька значень?",
         "Масив структур передається у функцію через вказівник Student* або константний вказівник const Student* разом із розміром N. Кілька обчислених значень зручно повертати через параметри-посилання (наприклад, int& count5).")
    ]
    for q, a in qa:
        add_p(doc, q, bold=True, size=12, space_before=4, space_after=2)
        add_p(doc, a, bold=False, size=12, space_before=0, space_after=6)

    # 8. Висновки
    add_h(doc, "8. Висновки")
    add_p(doc, "Під час виконання лабораторної роботи № 10.1a було закріплено навички роботи зі структурами (struct), переліками (enum) та динамічними масивами структур у мові C++. Реалізовано окремі підпрограми введення, табличного виведення, підрахунку оцінок з фізики та аналізу успішності з фізики і математики. Коректність роботи функцій підтверджено проходженням модульних тестів у UnitTest10.1a.")

    doc.save(OUT_DOCX)
    print("Saved:", OUT_DOCX)

if __name__ == "__main__":
    generate_report()
