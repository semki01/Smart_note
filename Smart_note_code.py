from os import terminal_size
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QPushButton, QTextEdit, QLineEdit, QLabel, QVBoxLayout, QHBoxLayout, QInputDialog

import json

notes = {"Добро пожаловать!" : {
    'текст' : 'Это самое лучшее приложение в мире!',
    'теги' : ['Добро', "инструкция"]
    }
}

#with open('notes_data.json', 'w') as file:
#    json.dump(notes, file)


app = QApplication([])
notes_win = QWidget()
notes_win.setWindowTitle("Умные заметки")
notes_win.resize(900, 600)
list_notes = QListWidget()
list_notes_label = QLabel('Список заметок')

button_note_create = QPushButton('Создать заметку')
button_note_del = QPushButton('Удалить заметку')
button_note_save = QPushButton('Сохранить заметку')

list_tags = QListWidget()
list_tags_label = QLabel('Список тегов')

button_tag_create = QPushButton ('Добавить тег')
button_tag_del = QPushButton('Удалить тег')
button_tag_search = QPushButton('Поиск по тегу')

field_text = QTextEdit()
field_tag = QLineEdit()
field_tag.setPlaceholderText('Введите тег...')

layout_notes = QHBoxLayout()
col_1 = QVBoxLayout()
col_2 = QVBoxLayout()
row_1 = QHBoxLayout()
row_2 = QHBoxLayout()
row_3 = QHBoxLayout()
row_4 = QHBoxLayout()
col_1.addWidget(field_text)
col_2.addWidget(list_notes_label)
col_2.addWidget(list_notes)

row_1.addWidget(button_note_create)
row_1.addWidget(button_note_del)
row_2.addWidget(button_note_save)
col_2.addLayout(row_1)
col_2.addLayout(row_2)
col_2.addWidget(list_tags_label)
col_2.addWidget(list_tags)
col_2.addWidget(field_tag)
row_3.addWidget(button_tag_create)
row_3.addWidget(button_tag_del)
row_4.addWidget(button_tag_search)

col_2.addLayout(row_3)
col_2.addLayout(row_4)

layout_notes.addLayout(col_1, stretch = 2)
layout_notes.addLayout(col_2, stretch = 1)
notes_win.setLayout(layout_notes)

def show_note():
    key = list_notes.selectedItems()[0].text()
    field_text.setText(notes[key]['текст'])
    list_tags.clear()
    list_tags.addItems(notes[key]['теги'])
list_notes.itemClicked.connect(show_note)

def add_note():
    note_name, ok = QInputDialog.getText(notes_win, 'Добавить заметку', 'Название заметки:')
    if ok and note_name:
        notes[note_name] = {'текст' : '', "теги": []}
        list_notes.addItem(note_name)

def save_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        notes[key]['текст'] = field_text.toPlainText()
        with open('notes_data.json', 'w') as file:
            json.dump(notes, file, sort_keys = True)

def del_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        del notes[key]
        list_notes.clear()
        list_tags.clear()
        field_text.clear()
        list_notes.addItems(notes)
        with open('notes_data.json', 'w') as file:
            json.dump(notes, file, sort_keys = True)

def add_tag():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        tag = field_tag.text()
        if not tag in notes[key]['теги']:
            notes[key]['теги'].append(tag)
            list_tags.addItem(tag)
            field_tag.clear()
        with open('notes_data.json', 'w') as file:
            json.dump(notes, file, sort_keys = True)

button_tag_create.clicked.connect(add_tag)
button_note_del.clicked.connect(del_note)
button_note_save.clicked.connect(save_note)
button_note_create.clicked.connect(add_note)
list_notes.itemClicked.connect(show_note)

with open('notes_data.json', 'r') as file:
    notes = json.load(file)
list_notes.addItems(notes)
notes_win.show()
app.exec_()
