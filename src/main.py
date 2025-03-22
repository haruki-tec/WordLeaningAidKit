import sys
from generate_num import gen_aligned_nums_with_char
from miss_word import appdate_missed_words_dict,create_texts_about_keys_and_values_from_dict,delete_miss_words
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QVBoxLayout,QPushButton,QHBoxLayout,QLineEdit,QLabel,QSpinBox,QAbstractItemView
from PyQt5.QtGui import QFont,QIntValidator,QColor
from PyQt5.QtCore import Qt

class Example(QWidget):

    def __init__(self):
        super().__init__()
        
        
        #生成基準
        self.start_num = 1
        self.end_num = 100
        self.gen_num = 0
        
        self.missed_words_dict = {}
        
        self.gen_list = []        
        
        self.initUI()
        
        

    def initUI(self):
        
        #左レイアウト

        #ボタンの作成
        randomize_button = QPushButton("生成")
        randomize_button.clicked.connect(self.on_gen_num_button_clicked)
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
        self.generated_num_list_widget = QListWidget()
        #複数の単語をまとめて選択可能化
        self.generated_num_list_widget.setSelectionMode(QAbstractItemView.MultiSelection)
        self.update_generated_num_list()
        # 文字の大きさの変更
        self.generated_num_list_widget.setFont(QFont("Arial", 20))
        
        
        
        
        #わからなかったボタン
        miss_word_button = QPushButton("わからなかった...")
        miss_word_button.clicked.connect(self.on_miss_word_button_clicked)
        
        
        
        #最終的な左レイアウト
        main_layout = QVBoxLayout()
        main_layout.addLayout(operation_box)
        main_layout.addWidget(self.generated_num_list_widget)
        main_layout.addWidget(miss_word_button)
        
        
        
        
        
        
        
        
        #右レイアウト
        
        
        
        self.miss_word_list_widget = QListWidget()
        #複数選択できるようにする
        self.miss_word_list_widget.setSelectionMode(QAbstractItemView.MultiSelection)
        self.miss_word_list_widget.setFont(QFont("Arial", 20))
        
        
        
        
        #最終的な右レイアウト
        
        #わかるようになったボタン
        understand_button = QPushButton("わかるようになった")
        understand_button.clicked.connect(self.on_understand_button_clicked)

        
        
        sub_layout = QVBoxLayout()
        sub_layout.addWidget(understand_button)
        sub_layout.addWidget(self.miss_word_list_widget)
        
        
        
        
        
        #最終的な総合レイアウト
        layout = QHBoxLayout()
        layout.addLayout(main_layout)
        layout.addLayout(sub_layout)
        
        self.setLayout(layout)

        # ウィンドウの設定
        self.setGeometry(300, 300, 600, 600)
        self.setWindowTitle('consecutive nums generator')
        self.show()
    
    def on_gen_num_button_clicked(self):
        gen_num_str = self.gen_num_text_box.text()
        begin_num_str = self.begin_num_text_box.text()
        end_num_str = self.end_num_text_box.text()
        
        if gen_num_str and begin_num_str and end_num_str:
            self.gen_num = int(gen_num_str)
            self.beginNum = int(begin_num_str)
            self.end_num = int(end_num_str)
            self.update_generated_num_list()
                
    #ランダム生成された整数郡をリストに表示する
    def update_generated_num_list(self):
        self.generated_num_list_widget.clear()
        
        self.gen_list.clear()
        self.gen_list = gen_aligned_nums_with_char(self.start_num, self.end_num, self.gen_num)
        
        self.generated_num_list_widget.addItems(self.gen_list)
        
        self.add_color_to_QList_from_list()
        
    def clear_color_to_QList(self):
        for nops in range(self.generated_num_list_widget.count()):
            item = self.generated_num_list_widget.item(nops)
            item.setBackground(QColor("#ffffff"))
        
    def add_color_to_QList_from_list(self):
        for nops in range(len(self.gen_list)):
            self.add_color_to_QList_from_num(nops)
            
    def add_color_to_QList_from_num(self,nops):
        if int(self.gen_list[nops]) in self.missed_words_dict:
            item = self.generated_num_list_widget.item(nops)
            item.setBackground(QColor("#ffc0cb"))
            
    def clear_selection_of_QList(self,list_widget):
        list_widget.clearSelection()
             
        
    def update_miss_word_list(self):
        
        self.miss_word_list_widget.clear()
        missed_words = create_texts_about_keys_and_values_from_dict(self.missed_words_dict)
        
        self.miss_word_list_widget.addItems(missed_words)
        
        #generated_numに色付けする
        self.add_color_to_QList_from_list()
    
    def on_miss_word_button_clicked(self):
        items = self.generated_num_list_widget.selectedItems()
        
        if items:
            selected_texts = [item.text() for item in items]
            
            appdate_missed_words_dict(self.missed_words_dict,selected_texts)
            
            self.update_miss_word_list()
            
            self.clear_selection_of_QList(self.generated_num_list_widget)
            

        
        
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
    
    def on_understand_button_clicked(self):
        items = self.miss_word_list_widget.selectedItems()
        
        if items:
            items_text = [item.text() for item in items]
            delete_miss_words(self.missed_words_dict,items_text)
            
            self.update_miss_word_list()
            
            #generated_num_QListに色付けする
            self.clear_color_to_QList()
            self.add_color_to_QList_from_list()
            
    


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # GuiApplicationの呼び出し
    ex = Example()
    sys.exit(app.exec_())