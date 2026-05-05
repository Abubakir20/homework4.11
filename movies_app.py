import json
from PyQt5.QtWidgets import *

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Yangi film qo'shish ilovasi")
        self.setGeometry(650, 300, 450, 300)

        self.v_main_lay = QVBoxLayout()
        self.h_title_lay = QHBoxLayout()
        self.h_director_lay = QHBoxLayout()
        self.h_year_lay = QHBoxLayout()
        self.h_genre_lay = QHBoxLayout()

        self.lbl_title = QLabel("Film nomi: ")
        self.lbl_director = QLabel("Rejissor: ")
        self.lbl_year = QLabel("Yili: ")
        self.lbl_genre = QLabel("Janr: ")

        self.title_input = QLineEdit()
        self.director_input = QLineEdit()
        self.year_input = QLineEdit()
        self.genre_input = QLineEdit()

        self.lbl_title.setFixedWidth(75)
        self.lbl_director.setFixedWidth(75)
        self.lbl_year.setFixedWidth(75)
        self.lbl_genre.setFixedWidth(75)

        self.lbl_title.setStyleSheet("border: 1px solid #3f3f3f; border-radius: 5px; font-size: 15px")
        self.lbl_director.setStyleSheet("border: 1px solid #3f3f3f; border-radius: 5px; font-size: 15px")
        self.lbl_year.setStyleSheet("border: 1px solid #3f3f3f; border-radius: 5px; font-size: 15px")
        self.lbl_genre.setStyleSheet("border: 1px solid #3f3f3f; border-radius: 5px; font-size: 15px")

        self.btn_add = QPushButton("Qo'shish")
        
        self.btn_add.setStyleSheet("padding: 10px; border: 2px solid #3f3f3f; border-radius: 5px; background-color: lightgreen; font-size: 15px")
        
        self.btn_add.clicked.connect(self.Add)
        
        self.h_title_lay.addWidget(self.lbl_title)
        self.h_title_lay.addWidget(self.title_input)

        self.h_director_lay.addWidget(self.lbl_director)
        self.h_director_lay.addWidget(self.director_input)

        self.h_year_lay.addWidget(self.lbl_year)
        self.h_year_lay.addWidget(self.year_input)

        self.h_genre_lay.addWidget(self.lbl_genre)
        self.h_genre_lay.addWidget(self.genre_input)

        self.v_main_lay.addLayout(self.h_title_lay)
        self.v_main_lay.addLayout(self.h_director_lay)
        self.v_main_lay.addLayout(self.h_year_lay)
        self.v_main_lay.addLayout(self.h_genre_lay)

        self.v_main_lay.addStretch()
        self.v_main_lay.addWidget(self.btn_add)

        self.setLayout(self.v_main_lay)

    def Add(self):
        name = self.title_input.text()
        director = self.director_input.text()
        year = self.year_input.text()
        genre = self.genre_input.text()

        if name and director and year and genre:
            if year.isdigit():
                new_movie = {
                "Title": name,
                "Director": director,
                "Year": year,
                "Genre": genre
                }

                try:
                    with open("movies.json", "r") as f:
                        movies = json.load(f)
                except:
                    movies = []

                movies.append(new_movie)

                with open("movies.json", "w") as f:
                    json.dump(movies, f, indent = 4)

                QMessageBox.information(self, "Ma'lumot", "Kino muvofaqiyatli qo'shildi!")
                self.title_input.clear()
                self.director_input.clear()
                self.year_input.clear()
                self.genre_input.clear()
            else:
                QMessageBox.warning(self, "Muammo", "<Yil> Bo'limidagi ma'lumot raqam bo'lishi shart!")
                self.year_input.clear()
        else:
            QMessageBox.warning(self, "Muammo!", "Barcha to'rt maydom to'ldirilishi shart!")


app = QApplication([])
win = MyWindow()
win.show()
app.exec_()