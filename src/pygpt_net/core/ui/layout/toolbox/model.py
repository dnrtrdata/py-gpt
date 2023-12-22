#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ================================================== #
# This file is a part of PYGPT package               #
# Website: https://pygpt.net                         #
# GitHub:  https://github.com/szczyglis-dev/py-gpt   #
# MIT License                                        #
# Created By  : Marcin Szczygliński                  #
# Updated Date: 2023.12.22 19:00:00                  #
# ================================================== #

from PySide6.QtGui import QStandardItemModel
from PySide6.QtWidgets import QVBoxLayout, QLabel, QSplitter, QWidget

from ...widget.lists.base import BaseList
from ....utils import trans


class Model:
    def __init__(self, window=None):
        """
        Toolbox UI

        :param window: Window instance
        """
        self.window = window
        self.id = 'prompt.model'

    def setup(self):
        """
        Setup models

        :return: QWidget
        :rtype: QWidget
        """
        widget = QWidget()
        widget.setLayout(self.setup_list())

        return widget

    def setup_list(self):
        """
        Setup list

        :return: QVBoxLayout
        :rtype: QVBoxLayout
        """
        label_key = self.id + '.label'

        self.window.ui.nodes[label_key] = QLabel(trans("toolbox.model.label"))
        self.window.ui.nodes[label_key].setStyleSheet(self.window.controller.theme.get_style('text_bold'))
        self.window.ui.nodes[self.id] = BaseList(self.window, self.id)
        self.window.ui.nodes[self.id].selection_locked = self.window.controller.model.model_change_locked

        layout = QVBoxLayout()
        layout.addWidget(self.window.ui.nodes[label_key])
        layout.addWidget(self.window.ui.nodes[self.id])

        self.window.ui.models[self.id] = self.create_model(self.window)
        self.window.ui.nodes[self.id].setModel(self.window.ui.models[self.id])

        # prevent focus out selection leave
        self.window.ui.nodes[self.id].selectionModel().selectionChanged.connect(
            self.window.ui.nodes[self.id].lockSelection)

        return layout

    def create_model(self, parent):
        """
        Create list model

        :param parent: parent widget
        :return: QStandardItemModel
        :rtype: QStandardItemModel
        """
        return QStandardItemModel(0, 1, parent)

    def update(self, data):
        """
        Update list

        :param data: Data to update
        """
        # store previous selection
        self.window.ui.nodes[self.id].backup_selection()

        self.window.ui.models[self.id].removeRows(0, self.window.ui.models[self.id].rowCount())
        i = 0
        for n in data:
            if 'name' in data[n]:
                self.window.ui.models[self.id].insertRow(i)
                name = data[n]['name']
                self.window.ui.models[self.id].setData(self.window.ui.models[self.id].index(i, 0), name)
                i += 1

        # restore previous selection
        self.window.ui.nodes[self.id].restore_selection()
