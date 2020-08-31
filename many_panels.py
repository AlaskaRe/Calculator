# -*- coding: utf-8 -*-
# 思路
# 1.首先创建一个panel, 每次都先有一个打头的Panel——CaptialPanel
# 2.根据输入的值来确定下一个panel是啥——OptionalPanel

import wx
import wx.lib.masked as mked
import wx.lib.inspection

slope_grade = 1


class CaptialPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        # 创建horizontal Sizer
        # 设置首行ctrl
        self.staticText_supportUnit = wx.StaticText(
            self, style=wx.ALIGN_CENTRE_HORIZONTAL, label="支护单元")

        self.textCtrl_supportUnit = wx.TextCtrl(
            self, style=wx.TE_LEFT)
        self.staticText_supportType = wx.StaticText(
            self, style=wx.ALIGN_CENTRE_HORIZONTAL, label="支护形式")
        self.combList = ['放坡', '土钉', '排桩']
        self.combox_supportList = wx.ComboBox(self, size=(100, -1),
                                              choices=self.combList, style=wx.TE_PROCESS_ENTER)
        self.Bind(wx.EVT_COMBOBOX_CLOSEUP, self.GetOptionalPanelValue,
                  self.combox_supportList)

        # self.button_Insure = wx.button
        # 设置排布
        self.__do_layout()

    def GetOptionalPanelValue(self, event):

        global n
        n = self.combox_supportList.GetStringSelection()

    def __do_layout(self):
        cap_row_sizer = wx.BoxSizer(wx.HORIZONTAL)
        cap_row_sizer.Add(self.staticText_supportUnit, 1, wx.ALL, 5)
        cap_row_sizer.Add(self.textCtrl_supportUnit, 1, wx.ALL, 5)
        cap_row_sizer.Add(self.staticText_supportType, 1, wx.ALL, 5)
        cap_row_sizer.Add(self.combox_supportList, 1, wx.ALL, 5)
        self.SetSizer(cap_row_sizer)


class OptionalPanelSlope(wx.Panel):

    """slope类"""

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.staticText_supportLength = wx.StaticText(
            self, label='支护长度', style=wx.ALIGN_CENTER_HORIZONTAL)
        self.textCtrl_supportLength = mked.NumCtrl(
            self, style=wx.ALIGN_CENTER_HORIZONTAL, value=0.0, fractionWidth=2, allowNegative=False, min=0.0, max=5000)
        self.staticText_slopeRate = wx.StaticText(
            self, label='放坡级数', style=wx.ALIGN_CENTER_HORIZONTAL)
        self.NumCtrl_slopeRate = mked.NumCtrl(
            self, value=1, allowNegative=False, min=1, max=10, limited=True, invalidBackgroundColor="RED")
        # 创建按钮
        self.button_slope = wx.Button(self, label="确定")
        self.Bind(wx.EVT_BUTTON, self.On_return_slope_value(),
                  self.button_slope)
        # 接收用户输入值来确定有多少级放坡

        self.__do_layout()

        """
        self.textCtrl_slopeRate = wx.TextCtrl(
            self, value=1, style=wx.ALIGN_CENTER_HORIZONTAL, validator=Validator)
        """

    def On_return_slope_value(self):

        global slope_grade

        slope_grade = self.NumCtrl_slopeRate.GetValue()

    def __do_layout(self):
        opt_row_sizer = wx.BoxSizer(wx.HORIZONTAL)
        opt_row_sizer.Add(self.staticText_supportLength, 1, wx.ALL, 5)
        opt_row_sizer.Add(self.textCtrl_supportLength, 1, wx.ALL, 5)
        opt_row_sizer.Add(self.staticText_slopeRate, 1, wx.ALL, 5)
        opt_row_sizer.Add(self.NumCtrl_slopeRate, 1, wx.ALL, 5)
        opt_row_sizer.Add(self.button_slope, 1, wx.ALL, 5)
        self.SetSizer(opt_row_sizer)


class OptionalPanelNailWall(wx.Panel):

    pass


class OptionalPanelPipe(wx.Panel):

    pass


class InputTypeValidator(wx.PyValidator):
    """检测整型、浮点、字符串"""

    def __init__(self, flag):
        """
        标准构造方法
        """
        wx.PyValidator.__init__(self)
        self.flag = flag
        self.Bind(wx.EVT_CHAR, self.Validate)

    def Clone(self):
        """
        Standard cloner.
        注意每个validator都必须implement方法
        """
        return InputTypeValidator()

    def Validate(self, win):
        TextCtrl = self.GetWindow()
        text = TextCtrl.GetValue()

        if text.isdigit():
            wx.MessageBox("只允许数字")


class MyFrame(wx.Frame):

    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, title=title)

        # 1.先创建一个Sizer来接受各种panel
        self.main_sizer = wx.BoxSizer(wx.VERTICAL)

        # 2.设置状态栏
        """
        这个先略过
        """
        # 3.necessary panel
        CapPanel = CaptialPanel(self)

        # 4.optional panel
        n = CapPanel.support_value
        # OptPanel = self.__optional_panel(n)

        # 设置布局
        self.main_sizer.Add(CapPanel, 1, wx.ALL, 5)
        self.__optional_panel(n)
        self.SetSizerAndFit(self.main_sizer)

        # self.Show()
        # 4.根据输入值来判断选择

    def __optional_panel(self, value):

        # 根据值返回相应的类
        optionalpanels = {'放坡': OptionalPanelSlope,
                          '土钉': OptionalPanelNailWall,
                          '排桩': OptionalPanelPipe}
        if value in ['放坡', '土钉', '排桩']:

            OptPanel = optionalpanels[value]
            self.main_sizer.Add(OptPanel, 1, wx.ALL, 5)
            self.SetSizerAndFit(self.main_sizer)


class SlopeGrid(wx.grid.Grid):
    # 添加新的属性，让其可用。
