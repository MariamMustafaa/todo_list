import PyQt5.QtWidgets as qtw
from PyQt5 import QtCore
import Todolist2
tasks = [" "]
class MainWindow(qtw.QMainWindow,Todolist2):
    def __init__(self):
        super().__init__()
        self.setup.ui()
        self.setupUi(self)
        self.pushButton6.clicked.connect(self.add_tasks)
        self.pushButton_7.clicked.connect(self.search_tasks)
        self.pushButton_9.clicked.connect(self.delete_task)
        self.pushButton_11.clicked.connect(self.delete_all)
        self.pushButton_10.clicked.connect(self.sort_tasksbyname)
        self.pushButton_8.clicked.connect(self.sort_tasksbydeadline)    

    def add_tasks(self):
            item = qtw.QListWidgetItem(self.lineEdit.text())
            tasks.append(self.lineEdit.text())
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
            item.setCheckState(QtCore.Qt.Unchecked)
            self.listWidget.addItem(item)

            item2=qtw.QListWidgetItem(self.lineEdit_2.text())
            item2.setFlags(item2.flags() | QtCore.Qt.ItemIsUserCheckable)
            item2.setCheckState(QtCore.Qt.Unchecked)
            self.listWidget_2.addItem(item2)

    def search_tasks(self):
        item = self.lineEdit.text()
        self.item = qtw.QListWidgetItem(item)
        self.item.setFlags(self.item.flags() | QtCore.Qt.ItemIsUserCheckable)
        self.item.setCheckState(QtCore.Qt.Unchecked)
        for i in range(len(tasks)):
            if tasks[i] == item:
                self.listWidget.clear()
                self.listWidget.addItem(self.item)


    def sort_tasks(self):
         self.listWidget.sortItems()

    def delete_task(self):
        sel_row = self.listWidget.currentRow()
        if sel_row >= 0:
            item = self.listWidget.takeItem(sel_row)
            del item
    def sort_tasksbydeadline(self):
        self.listWidget.sortItems(keys=lambda x:x.text())


    def delete_all(self):
        self.listWidget.clear()



app = qtw.QApplication([])
window = MainWindow()
window.show()
app.exec()

