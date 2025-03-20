import sys
from generate_num import gen_aligned_nums_with_char
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QVBoxLayout,QPushButton,QHBoxLayout,QLineEdit,QLabel,QSpinBox
from PyQt5.QtGui import QFont,QIntValidator
from PyQt5.QtCore import Qt

class Example(QWidget):

    def __init__(self):
        super().__init__()
        
        
        #生成基準
        self.startNum = 1
        self.endNum = 100
        self.genNum = 0
        
        
        self.initUI()
        
        

    def initUI(self):

        #ボタンの作成
        randomize_button = QPushButton("生成")
        randomize_button.clicked.connect(self.on_button_clicked)
        operation_box = QVBoxLayout()
        
        #出題数ラベルテキストボックス
        self.gen_num_text_box = QSpinBox()
        gen_num_vbox = self.create_labeled_textbox("出題数",self.gen_num_text_box,1,0)
        
        #始まりラベルテキストボックス
        self.begin_num_text_box = QSpinBox()
        begin_num_vbox = self.create_labeled_textbox("始まりの数",self.begin_num_text_box,10,1)
        
        #終わりラベルテキストボックス
        self.end_num_text_box = QSpinBox()
        end_num_vbox = self.create_labeled_textbox("終わりの数",self.end_num_text_box,10,0)
        
        labeled_textbox_aggregate = QHBoxLayout()
        labeled_textbox_aggregate.addLayout(gen_num_vbox)
        labeled_textbox_aggregate.addLayout(begin_num_vbox)
        labeled_textbox_aggregate.addLayout(end_num_vbox)
        
        
        
        operation_box.addLayout(labeled_textbox_aggregate)
        operation_box.addWidget(randomize_button)
        
        

        
        # QListWidget の作成
        self.list_widget = QListWidget()
        self.update_list()
        # 文字の大きさの変更
        self.list_widget.setFont(QFont("Arial", 20))
        
        
        
        #最終的な左レイアウト
        main_layout = QVBoxLayout()
        main_layout.addLayout(operation_box)
        main_layout.addWidget(self.list_widget)
        
        
        
        
        
        
        
        
        
        
        
        
        check_button = QPushButton("わからなかった...")
        
        
        
        
        
        #最終的な右レイアウト
        sub_layout = QVBoxLayout()
        sub_layout.addWidget(check_button)
        
        
        
        
        
        #最終的な総合レイアウト
        layout = QHBoxLayout()
        layout.addLayout(main_layout)
        layout.addLayout(sub_layout)
        
        self.setLayout(layout)

        # ウィンドウの設定
        self.setGeometry(300, 300, 600, 600)
        self.setWindowTitle('consecutive nums generator')
        self.show()
    
    def on_button_clicked(self):
        gen_num_str = self.gen_num_text_box.text()
        begin_num_str = self.begin_num_text_box.text()
        end_num_str = self.end_num_text_box.text()
        
        if gen_num_str and begin_num_str and end_num_str:
            self.genNum = int(gen_num_str)
            self.beginNum = int(begin_num_str)
            self.endNum = int(end_num_str)
            self.update_list()
                
    def update_list(self):
        self.list_widget.clear()
        my_list = gen_aligned_nums_with_char(self.startNum, self.endNum, self.genNum)
        
        self.list_widget.addItems(my_list)
        
    #(self,テキストボックスに表示する文字,テキストボックスインスタンス,矢印の感度,初期値)
    def create_labeled_textbox(self,label,text_box,single_step,init_value):
        
        vbox = QVBoxLayout()
        qlabel = QLabel(label)
        qlabel.setAlignment(Qt.AlignCenter)
        qlabel.setFont(QFont("Arial", 15))
        vbox.addWidget(qlabel)
        
        #spin box setting
        text_box.setRange(0, 100000)
        text_box.setSingleStep(single_step)
        text_box.setFont(QFont("Arial",15))
        text_box.setValue(init_value)
        
        
        vbox.addWidget(text_box)
        
        return vbox
    


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # GuiApplicationの呼び出し
    ex = Example()
    sys.exit(app.exec_())