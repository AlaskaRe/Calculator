import wx
import wx.lib.masked as mked
import wx.lib.inspection
from manypanels import *

# global n, n_backward
# n = '放坡'


class MainFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title=title)
        # 1.先创建一个Sizer来接受各种panel
        self.main_sizer = wx.BoxSizer(wx.VERTICAL)

        # 2.设置状态栏
        """
        这个先略过
        """
        # 3.necessary panel
        capanel = CaptialPanel(self)
        self.main_sizer.Add(capanel, 1, wx.BOTTOM, 5)

        # 4.optional panel
        # global n, n_backward
        # OptPl = self.__option_panel(n)
        # optpanel = OptPl(self)
        optpanel = OptionalPanelSlope(self)
        self.main_sizer.Add(optpanel, 1, wx.TOP, 5)
        self.SetSizer(self.main_sizer)
    """
        global n, n_backward
        self.add_panel(n, n_backward)
        if n != n_backward:
            self.add_panel(n, n_backward)
        self.SetSizerAndFit(self.main_sizer)

        # 4.根据输入值来判断选择
    def __option_panel(self, value):

        optionalpanels = {'放坡': OptionalPanelSlope,
                          '土钉': OptionalPanelNailWall,
                          '排桩': OptionalPanelPipe}
        if value in ['放坡', '土钉', '排桩']:

            return optionalpanels[value]
        else:
            blankpanel = wx.Panel
            # blankpanel.SetBackgroundColour()
            return blankpanel

    def add_panel(self, value, value_backward):

        if value == value_backward:
            capanel = CaptialPanel(self)
            self.main_sizer.Add(capanel, 1, wx.ALL)
        else:
            OptPl = self.__option_panel(value)
            optpanel = OptPl(self)
            self.main_sizer.Add(optpanel, 1, wx.ALL)
    """


class MainApp(wx.App):

    def OnInit(self):

        frame = MainFrame(None, -1, 'Test')
        frame.Show()
        wx.lib.inspection.InspectionTool().Show()

        return True


if __name__ == "__main__":

    app = MainApp(False)
    app.MainLoop()
