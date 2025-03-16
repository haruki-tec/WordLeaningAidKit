import sys
from generate_num import gen_aligned_nums_with_char
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QVBoxLayout
from PyQt5.QtGui import QFont

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        # リストデータ
        my_list = gen_aligned_nums_with_char(1,100,20)

        # QListWidget の作成
        list_widget = QListWidget()

        # リストアイテムを追加
        for item in my_list:
            list_widget.addItem(item)
            
        # 文字の大きさの変更
        
        list_widget.setFont(QFont("Arial", 20))

        # レイアウトの設定
        vbox = QVBoxLayout()
        vbox.addWidget(list_widget)
        self.setLayout(vbox)

        # ウィンドウの設定
        self.setGeometry(300, 300, 1250, 600)
        self.setWindowTitle('consecutive nums generator')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())