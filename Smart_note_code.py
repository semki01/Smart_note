from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QPushButton, QTextEdit, QLineEdit, QLabel, QVBoxLayout, QHBoxLayout

app = QApplication([])
notes_win = QWidget()
notes_win.setWindowTitle("Умные заметки")
notes_win.resize(900, 600)
list_notes = QListWidget()

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
col_2.addWidget(list_tags)

col_2.addWidget(list_tags_label)
row_1.addWidget(button_note_create)
row_2.addWidget(button_note_save)
col_2.addWidget(field_tag)
col_2.addWidget(list_tags)
row_3.addWidget(button_tag_create)
row_3.addWidget(button_tag_del)
row_4.addWidget(button_tag_search)

col_2.addLayout(row_1)
col_2.addLayout(row_2)
col_2.addLayout(row_3)
col_2.addLayout(row_4)

layout_notes.addLayout(col_1, stretch = 2)
layout_notes.addLayout(col_2, stretch = 1)
notes_win.setLayout(layout_notes)
notes_win.show()
app.exec_()