# 开发者：_Iamsleepingnow
# 开发时间：2026-02-03 0:17
# 开发功能：Terraria 1.4.5 种子合成器 Seed Synth
# encoding = utf-8
# -----------------------------------------
import sys, random
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QFontDatabase, QCursor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QPlainTextEdit, QCheckBox, QRadioButton, QButtonGroup, QSpacerItem, QGroupBox,
    QScrollArea, QScrollBar, QSizePolicy
)

# 定义全局变量
font_path = ".\\UI\\unifont.ttf"  # 全局字体路径
title_text = 'Terraria 1.4.5 种子合成器 Seed Synth'  # 标题文本
scrollbar_stylesheet = '''
QScrollBar:vertical{ margin:0px 0px 0px 0px; background-color:#888888; border:1px #000000; width:18px; }
QScrollBar::handle:vertical{ background-color:#000000; border:1px #000000; border-radius:1px; width:18px; }
QScrollBar::handle:vertical:hover{ background-color:#ffffff; }
QScrollBar::sub-line:vertical, 
QScrollBar::add-line:vertical{ border: none; background: none; height: 0px; }
QScrollBar::up-arrow:vertical, 
QScrollBar::down-arrow:vertical{ border: none; width: 0px; height: 0px; background: none; }
QScrollBar::sub-page:vertical,
QScrollBar::add-page:vertical{ background-color:#888888; border: 5px solid; }
'''  # 滑动条样式表
data_world_size = {  # 世界大小
    1: {"NAME": "小　", "ID": "1"},
    2: {"NAME": "中　", "ID": "2"},
    3: {"NAME": "大　", "ID": "3"},
}
data_difficult = {  # 世界难度
    1: {"NAME": "经典", "ID": "1"},
    2: {"NAME": "专家", "ID": "2"},
    3: {"NAME": "大师", "ID": "3"},
    4: {"NAME": "旅行", "ID": "4"},
}
data_evil_type = {  # 邪恶类型
    1: {"NAME": "腐化", "ID": "1"},
    2: {"NAME": "猩红", "ID": "2"},
}
data_special_seeds = {  # 特殊世界种子
    1: {"NAME": "醉酒世界", "EN": "05162020", "MASK": 1},
    2: {"NAME": "蜜蜂世界", "EN": "not the bees", "MASK": 2},
    3: {"NAME": "传奇", "EN": "for the worthy", "MASK": 4},
    4: {"NAME": "十周年", "EN": "celebrationmk10", "MASK": 8},
    5: {"NAME": "永恒领域", "EN": "constant", "MASK": 16},
    6: {"NAME": "没有陷阱", "EN": "no traps", "MASK": 32},
    7: {"NAME": "颠倒世界", "EN": "dont dig up", "MASK": 64},
    8: {"NAME": "天顶世界", "EN": "get fixed boi", "MASK": 128},
    9: {"NAME": "空岛", "EN": "skyblock", "MASK": 256},
}
data_secret_seeds = {  # 秘密世界种子
    1: {"NAME": "灰色世界", "EN": "paint Everything Gray", "SEED": "monochrome", "ENABLE": True},
    2: {"NAME": "反色世界", "EN": "paint Everything Negative", "SEED": "negative infinity", "ENABLE": True},
    3: {"NAME": "隐形世界", "EN": "coat Everything Echo", "SEED": "invisible plane", "ENABLE": True},
    4: {"NAME": "点亮世界", "EN": "coat Everything Illuminant", "SEED": "xray vision", "ENABLE": True},
    5: {"NAME": "无地表", "EN": "no Surface", "SEED": "mole people", "ENABLE": True},
    6: {"NAME": "更多世界树", "EN": "extra Living Trees", "SEED": "save the rainforest", "ENABLE": True},
    7: {"NAME": "更多空岛", "EN": "extra Floating Islands", "SEED": "the carebears movie", "ENABLE": True},
    8: {"NAME": "错误世界", "EN": "error World", "SEED": "i am error", "ENABLE": True},
    9: {"NAME": "血月开局", "EN": "graveyard Bloodmoon Start", "SEED": "night of the living dead", "ENABLE": True},
    10: {"NAME": "地表太高", "EN": "surface Is In Space", "SEED": "such great heights", "ENABLE": True},
    11: {"NAME": "雨季", "EN": "rains For A Year", "SEED": "bring a towel", "ENABLE": True},
    12: {"NAME": "更大地下遗迹", "EN": "bigger Abandoned Houses", "SEED": "abandoned manors", "ENABLE": True},
    13: {"NAME": "随机出生点", "EN": "random Spawn", "SEED": "how did i get here", "ENABLE": True},
    14: {"NAME": "生成传送机", "EN": "add Teleporters", "SEED": "beam me up", "ENABLE": True},
    15: {"NAME": "肉后开局", "EN": "start In Hardmode", "SEED": "too easy", "ENABLE": True},
    16: {"NAME": "无邪恶感染", "EN": "no Infection", "SEED": "fishmox", "ENABLE": True},
    17: {"NAME": "地表神圣？", "EN": "hallow On The Surface", "SEED": "", "ENABLE": False},
    18: {"NAME": "全邪恶感染", "EN": "world Is Infected", "SEED": "purify this", "ENABLE": True},
    19: {"NAME": "发光蘑菇地表", "EN": "surface Is Mushrooms", "SEED": "toadstool", "ENABLE": True},
    20: {"NAME": "沙漠化", "EN": "surface Is Desert", "SEED": "sandy britches", "ENABLE": True},
    21: {"NAME": "便便", "EN": "poo Everywhere", "SEED": "truck stop", "ENABLE": True},
    22: {"NAME": "无蜘蛛洞穴", "EN": "no Spider Caves", "SEED": "arachnophobia", "ENABLE": True},
    23: {"NAME": "真没有陷阱", "EN": "actually No Traps", "SEED": "more traps please", "ENABLE": True},
    24: {"NAME": "彩虹世界", "EN": "rainbow Stuff", "SEED": "rainbow road", "ENABLE": True},
    25: {"NAME": "大裂谷", "EN": "dig Extra Holes", "SEED": "jagged rocks", "ENABLE": True},
    26: {"NAME": "小小星球", "EN": "round Landmasses", "SEED": "planetoids", "ENABLE": True},
    27: {"NAME": "水族馆", "EN": "extra Liquid", "SEED": "waterpark", "ENABLE": True},
    28: {"NAME": "传送枪？", "EN": "portal Gun In Chests", "SEED": "", "ENABLE": False},
    29: {"NAME": "冰雪世界", "EN": "world Is Frozen", "SEED": "winter is coming", "ENABLE": True},
    30: {"NAME": "南瓜季", "EN": "halloween Gen", "SEED": "pumpkin season", "ENABLE": True},
    31: {"NAME": "万圣节", "EN": "endless Halloween", "SEED": "hocus pocus", "ENABLE": True},
    32: {"NAME": "圣诞节", "EN": "endless Christmas", "SEED": "jingle all the way", "ENABLE": True},
    33: {"NAME": "吸血鬼", "EN": "vampirism", "SEED": "what a horrible night to have a curse", "ENABLE": True},
    34: {"NAME": "团队出生点", "EN": "team Based Spawns", "SEED": "royale with cheese", "ENABLE": True},
    35: {"NAME": "双地牢？", "EN": "dual Dungeons", "SEED": "dual dungeons", "ENABLE": False},
}


# 种子合成器类
class SeedSynthManager(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.connect_signals()

    def init_ui(self):
        # 设置窗口属性
        self.setWindowTitle(title_text + '  BY _Iamsleepingnow')
        self.resize(690, 820)
        self.setMinimumSize(690, 820)

        # 设置主窗口
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        self.layout = QVBoxLayout(main_widget)  # 全局纵向布局器

        # 获取全局字体
        fontId = QFontDatabase.addApplicationFont(font_path)
        fontFamily = QFontDatabase.applicationFontFamilies(fontId)
        self.font_name = ''
        if fontFamily:
            self.font_name = fontFamily[0]

        # 标题
        self.title_label = self.add_label(title_text, f'margin: 10px;', 18, Qt.AlignCenter, -1, 70)
        self.layout.addWidget(self.title_label)  # 加入布局器

        # 生成执行行
        self.layout_execute = QHBoxLayout()
        self.layout.addLayout(self.layout_execute)
        self.tedit_seed_executed = self.add_textedit('', f'border: 5px solid; margin: 0px;', 10, -1, 50)
        self.tedit_seed_executed.setReadOnly(True)  # 设置为只读
        self.layout_execute.addWidget(self.tedit_seed_executed)
        self.btn_gen_seed = self.add_pushbutton(' 生成 ', f'border: 5px solid; margin: 0px;', 14, -1, 50)
        self.layout_execute.addWidget(self.btn_gen_seed)
        self.btn_copy = self.add_pushbutton(' 复制到剪贴板 ', f'border: 5px solid; margin: 0px;', 14, -1, 50)
        self.layout_execute.addWidget(self.btn_copy)

        # 世界大小设置
        self.group_world_size = self.add_groupbox('世界大小', f'border: 5px solid; margin: 0px;', 10)
        self.layout.addWidget(self.group_world_size)
        self.layout_world_size = QHBoxLayout()
        self.layout_world_size.setContentsMargins(5, 20, 5, 5)
        self.group_world_size.setLayout(self.layout_world_size)
        self.btnGroup_world_size = QButtonGroup()  # 按钮组
        self.btnGroup_world_size.setExclusive(True)  # 互斥按钮
        self.radio_world_size_buttons = []
        for i in range(len(data_world_size)):
            world_size = data_world_size[i + 1]
            is_first = world_size['ID'] == "1"
            radio_world_size = self.add_radiobutton(' ' + world_size['NAME'] + ' ', is_first,
                                                    f'border: 0px; margin: 0px 10px -5px 10px;', 12, -1, 25)
            self.btnGroup_world_size.addButton(radio_world_size)
            self.radio_world_size_buttons.append(radio_world_size)
            self.layout_world_size.addWidget(radio_world_size)
        self.layout_world_size.addSpacerItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))

        # 世界难度设置
        self.group_difficult = self.add_groupbox('世界难度', f'border: 5px solid; margin: 0px;', 10)
        self.layout.addWidget(self.group_difficult)
        self.layout_difficult = QHBoxLayout()
        self.layout_difficult.setContentsMargins(5, 20, 5, 5)
        self.group_difficult.setLayout(self.layout_difficult)
        self.btnGroup_difficult = QButtonGroup()  # 按钮组
        self.btnGroup_difficult.setExclusive(True)  # 互斥按钮
        self.radio_difficult_buttons = []
        for i in range(len(data_difficult)):
            difficult = data_difficult[i + 1]
            is_first = difficult['ID'] == "1"
            radio_difficult = self.add_radiobutton(' ' + difficult['NAME'] + ' ', is_first,
                                                   f'border: 0px; margin: 0px 10px -5px 10px;', 12, -1, 25)
            self.btnGroup_difficult.addButton(radio_difficult)
            self.radio_difficult_buttons.append(radio_difficult)
            self.layout_difficult.addWidget(radio_difficult)
        self.layout_difficult.addSpacerItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))

        # 世界邪恶类型设置
        self.group_evil_type = self.add_groupbox('邪恶类型', f'border: 5px solid; margin: 0px;', 10)
        self.layout.addWidget(self.group_evil_type)
        self.layout_evil_type = QHBoxLayout()
        self.layout_evil_type.setContentsMargins(5, 20, 5, 5)
        self.group_evil_type.setLayout(self.layout_evil_type)
        self.btnGroup_evil_type = QButtonGroup()  # 按钮组
        self.btnGroup_evil_type.setExclusive(True)  # 互斥按钮
        self.radio_evil_type_buttons = []
        for i in range(len(data_evil_type)):
            evil_type = data_evil_type[i + 1]
            is_first = evil_type['ID'] == "1"
            radio_evil_type = self.add_radiobutton(' ' + evil_type['NAME'] + ' ', is_first,
                                                   f'border: 0px; margin: 0px 10px -5px 10px;', 12, -1, 25)
            self.btnGroup_evil_type.addButton(radio_evil_type)
            self.radio_evil_type_buttons.append(radio_evil_type)
            self.layout_evil_type.addWidget(radio_evil_type)
        self.layout_evil_type.addSpacerItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))

        # 随机种设置
        self.group_random_seed = self.add_groupbox('随机种', f'border: 5px solid; margin: 0px;', 10)
        self.layout.addWidget(self.group_random_seed)
        self.layout_random_seed = QHBoxLayout()
        self.group_random_seed.setLayout(self.layout_random_seed)
        self.tedit_random_seed = self.add_textedit('留空则随机...', f'border: 5px solid #888888; margin: 10px 0px 0px 0px;', 14, -1, 60)
        self.tedit_random_seed.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.layout_random_seed.addWidget(self.tedit_random_seed)

        # 特殊世界种子设置
        self.group_special_seed = self.add_groupbox('特殊种子', f'border: 5px solid; margin: 5px 0px 0px 0px;', 10)
        self.group_special_seed.setMaximumHeight(350)
        self.group_special_seed.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.layout.addWidget(self.group_special_seed)
        self.scroll_special_seed, self.scroll_layout_special_seed = self.add_scrollerea()
        self.layout_special_seed = QVBoxLayout()
        self.layout_special_seed.setSpacing(0)
        self.group_special_seed.setLayout(self.layout_special_seed)
        self.layout_special_seed.addWidget(self.scroll_special_seed)
        self.checkbox_special_seed_buttons = []
        for i in range(len(data_special_seeds)):
            special_seed = data_special_seeds[i + 1]
            checkbox_special_seed = self.add_checkbox(' ' + special_seed['NAME'] + ' ' + special_seed['EN'], False,
                                                      f'border: 0px; margin: -5px 10px -5px 10px;', 14, -1, 25)
            self.checkbox_special_seed_buttons.append(checkbox_special_seed)
            self.scroll_layout_special_seed.addWidget(checkbox_special_seed)

        # 秘密世界种子设置
        self.group_secret_seed = self.add_groupbox('秘密种子', f'border: 5px solid; margin: 5px 0px 0px 0px;', 10)
        self.group_secret_seed.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.group_secret_seed.setMaximumHeight(1000)
        self.layout.addWidget(self.group_secret_seed)
        self.scroll_secret_seed, self.scroll_layout_secret_seed = self.add_scrollerea()
        self.scroll_layout_secret_seed.setSpacing(0)
        self.layout_secret_seed = QVBoxLayout()
        self.group_secret_seed.setLayout(self.layout_secret_seed)
        self.layout_secret_seed.addWidget(self.scroll_secret_seed)
        self.checkbox_secret_seed_buttons = []
        for i in range(len(data_secret_seeds)):
            secret_seed = data_secret_seeds[i + 1]
            checkbox_secret_seed = self.add_checkbox(' ' + secret_seed['NAME'] + ' ' + secret_seed['EN'], False,
                                                     f'border: 0px; margin: -5px 10px -5px 10px; padding: 0px;', 14, -1, 35)
            checkbox_secret_seed.setEnabled(secret_seed['ENABLE'])
            self.checkbox_secret_seed_buttons.append(checkbox_secret_seed)
            self.scroll_layout_secret_seed.addWidget(checkbox_secret_seed)

    def connect_signals(self):
        """连接信号和槽函数"""
        self.btn_gen_seed.clicked.connect(self.generate_seed)
        self.btn_copy.clicked.connect(self.copy_to_clipboard)

    def generate_seed(self):
        """生成种子"""
        try:
            # 1. 获取世界大小ID
            world_size_id = "1"
            for i, btn in enumerate(self.radio_world_size_buttons):
                if btn.isChecked():
                    world_size_id = data_world_size[i + 1]["ID"]
                    break

            # 2. 获取世界难度ID
            difficult_id = "1"
            for i, btn in enumerate(self.radio_difficult_buttons):
                if btn.isChecked():
                    difficult_id = data_difficult[i + 1]["ID"]
                    break

            # 3. 获取邪恶类型ID
            evil_type_id = "1"
            for i, btn in enumerate(self.radio_evil_type_buttons):
                if btn.isChecked():
                    evil_type_id = data_evil_type[i + 1]["ID"]
                    break

            # 4. 计算特殊世界种子掩码之和
            special_seed_mask = 0
            for i, checkbox in enumerate(self.checkbox_special_seed_buttons):
                if checkbox.isChecked():
                    special_seed_mask += data_special_seeds[i + 1]["MASK"]

            # 5. 获取秘密世界种子字符串
            secret_seeds_list = []
            for i, checkbox in enumerate(self.checkbox_secret_seed_buttons):
                if checkbox.isEnabled() and checkbox.isChecked():
                    seed_text = data_secret_seeds[i + 1]["SEED"]
                    if seed_text:  # 只添加非空的种子
                        secret_seeds_list.append(seed_text)

            # 6. 获取整数随机种
            random_seed_text = self.tedit_random_seed.toPlainText()
            if random_seed_text == "" or random_seed_text == "留空则随机...":
                # 生成0~(2^31)-1的随机整数
                random_seed = str(random.randint(0, (2 ** 31) - 1))
            else:
                # 使用用户输入的字符串
                random_seed = random_seed_text

            # 构建种子字符串
            seed_parts = []

            # 添加前4部分
            seed_parts.append(world_size_id)
            seed_parts.append(difficult_id)
            seed_parts.append(evil_type_id)
            seed_parts.append(str(special_seed_mask))

            # 构建第五部分（秘密种子和随机种）
            fifth_part_parts = []

            # 添加秘密种子
            if secret_seeds_list:
                fifth_part_parts.append("|".join(secret_seeds_list))

            # 添加随机种
            fifth_part_parts.append(random_seed)

            # 组合第五部分
            fifth_part = "|".join(fifth_part_parts)
            seed_parts.append(fifth_part)

            # 组合完整种子
            final_seed = ".".join(seed_parts)

            # 显示在文本框中
            self.tedit_seed_executed.setPlainText(final_seed)

        except Exception as e:
            self.tedit_seed_executed.setPlainText(f"生成种子时出错: {str(e)}")

    def copy_to_clipboard(self):
        """复制种子到剪贴板"""
        seed_text = self.tedit_seed_executed.toPlainText()
        if seed_text:
            clipboard = QApplication.clipboard()
            clipboard.setText(seed_text)
            self.btn_copy.setText(" 已复制! ")
            # 2秒后恢复按钮文本
            from PyQt5.QtCore import QTimer
            QTimer.singleShot(2000, lambda: self.btn_copy.setText(" 复制到剪贴板 "))
        else:
            self.tedit_seed_executed.setPlainText("请先生成种子!")

    # 实用功能
    def add_label(self, text, stylesheet, font_size, align, max_width, max_height):
        tlabel = QLabel(text)  # 创建QLabel实例
        tlabel.setStyleSheet(stylesheet)  # 设置样式表
        tlabel.setFont(QFont(self.font_name, font_size))  # 设置字体大小
        tlabel.setAlignment(align)  # 设置对齐方式
        if max_width != -1:
            tlabel.setMaximumWidth(max_width)
        if max_height != -1:
            tlabel.setMaximumHeight(max_height)
        return tlabel

    def add_textedit(self, placeholder, stylesheet, font_size, max_width, max_height):
        tedit = QPlainTextEdit()  # 创建QPlainTextEdit实例
        tedit.setStyleSheet(stylesheet)  # 设置样式表
        tedit.setFont(QFont(self.font_name, font_size))  # 设置字体大小
        tedit.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)  # 关闭滑动条
        tedit.setPlaceholderText(placeholder)
        if max_width != -1:
            tedit.setMaximumWidth(max_width)
        if max_height != -1:
            tedit.setMaximumHeight(max_height)
        return tedit

    def add_pushbutton(self, title, stylesheet, font_size, max_width, min_height):
        """ 创建QPushButton按钮 """
        btn = QPushButton(title)  # 创建QPushButton实例
        btn.setStyleSheet(stylesheet)  # 设置样式表
        btn.setFont(QFont(self.font_name, font_size))  # 设置字体大小
        btn.setCursor(QCursor(Qt.PointingHandCursor))  # 设置光标为指向手形状
        if max_width != -1:  # 设置最大宽度
            btn.setMaximumWidth(max_width)
            btn.setMinimumWidth(max_width)
        if min_height != -1:  # 设置最小高度
            btn.setMaximumHeight(min_height)
            btn.setMinimumHeight(min_height)
        return btn

    def add_groupbox(self, title, stylesheet, font_size):
        group = QGroupBox(title)
        group.setStyleSheet(stylesheet)  # 设置样式表
        group.setFont(QFont(self.font_name, font_size))  # 设置字体大小
        return group

    def add_radiobutton(self, title, checked, stylesheet, font_size, max_width, min_height):
        btn = QRadioButton(title)
        btn.setChecked(checked)
        btn.setStyleSheet(stylesheet)  # 设置样式表
        btn.setFont(QFont(self.font_name, font_size))  # 设置字体大小
        btn.setCursor(QCursor(Qt.PointingHandCursor))  # 设置光标为指向手形状
        if max_width != -1:  # 设置最大宽度
            btn.setMaximumWidth(max_width)
            btn.setMinimumWidth(max_width)
        if min_height != -1:  # 设置最小高度
            btn.setMaximumHeight(min_height)
            btn.setMinimumHeight(min_height)
        return btn

    def add_checkbox(self, title, checked, stylesheet, font_size, max_width, min_height):
        btn = QCheckBox(title)
        btn.setChecked(checked)
        btn.setStyleSheet(stylesheet)  # 设置样式表
        btn.setFont(QFont(self.font_name, font_size))  # 设置字体大小
        btn.setCursor(QCursor(Qt.PointingHandCursor))  # 设置光标为指向手形状
        if max_width != -1:  # 设置最大宽度
            btn.setMaximumWidth(max_width)
            btn.setMinimumWidth(max_width)
        if min_height != -1:  # 设置最小高度
            btn.setMaximumHeight(min_height)
            btn.setMinimumHeight(min_height)
        return btn

    def add_scrollerea(self):
        scrollbar = QScrollBar()  # 创建滚动条
        scrollbar.setStyleSheet(scrollbar_stylesheet)
        scroll = QScrollArea()
        scroll.setVerticalScrollBar(scrollbar)
        scroll.setWidgetResizable(True)
        scroll.setViewportMargins(0, 0, 0, 0)
        scroll.setStyleSheet(f'border: 0px;')
        scroll_content = QWidget()
        scroll_layout = QVBoxLayout(scroll_content)
        scroll_layout.setAlignment(Qt.AlignTop)
        scroll_layout.setContentsMargins(0, 0, 0, 0)
        scroll.setWidget(scroll_content)
        return scroll, scroll_layout


# 程序入口
if __name__ == "__main__":
    app = QApplication(sys.argv)
    manager = SeedSynthManager()
    manager.show()
    sys.exit(app.exec_())