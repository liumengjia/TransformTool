# -*- coding: utf-8 -*-
 
###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################
 
import wx
import wx.xrc
 
 
###########################################################################
## Class Frame
###########################################################################
 
class Frame(wx.Frame):
 
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"ThreeToOneTools", pos=wx.DefaultPosition, size=wx.Size(500, 700),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
 
        self.icon = wx.Icon('logo.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)
 
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
 
        wxBoxSizer = wx.BoxSizer(wx.VERTICAL)
 
        self.staticTexttitle = wx.StaticText(self, wx.ID_ANY, u"请在第一个输入框输入字符", wx.DefaultPosition, wx.DefaultSize, 0)
        self.staticTexttitle.Wrap(-1)
        wxBoxSizer.Add(self.staticTexttitle, 0, wx.ALL, 5)
 
        self.CommonInput = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(500,200), wx.TE_MULTILINE|wx.TE_RICH|wx.TE_PROCESS_ENTER)
        wxBoxSizer.Add(self.CommonInput, 0, wx.ALL, 5)
 
        self.staticTexttitleView = wx.StaticText(self, wx.ID_ANY,u"感谢您使用此软件", wx.DefaultPosition, wx.DefaultSize, 0)
        self.staticTexttitleView.Wrap(-1)
        wxBoxSizer.Add(self.staticTexttitleView, 0, wx.ALL, 5)
 
        self.ResultInput = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(500,200), wx.TE_MULTILINE|wx.TE_RICH|wx.TE_PROCESS_ENTER)
        wxBoxSizer.Add(self.ResultInput, 0, wx.ALL, 5)
 
        self.BtnTranwords = wx.Button(self, wx.ID_ANY, u"点击此处进行转化", wx.Point(100, 100), wx.DefaultSize, 0)
        wxBoxSizer.Add(self.BtnTranwords, 0, wx.ALL, 5)
 
        self.staticTexttitle = wx.StaticText(self, wx.ID_ANY, u"软件使用说明：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.staticTexttitle.Wrap(-1)
        wxBoxSizer.Add(self.staticTexttitle, 0, wx.ALL, 5)
 
        self.staticTexttitle = wx.StaticText(self, wx.ID_ANY,u"1、输入key1=value1&&key2=value2&&key3=value3格式字符将会转化成Dict", wx.DefaultPosition, wx.DefaultSize, 0)
        self.staticTexttitle.Wrap(-1)
        wxBoxSizer.Add(self.staticTexttitle, 0, wx.ALL, 5)
 
        self.staticTexttitle = wx.StaticText(self, wx.ID_ANY, u"2、输入key1=value1;key2=value2;key3=value3格式字符将会转化成Dict", wx.DefaultPosition, wx.DefaultSize, 0)
        self.staticTexttitle.Wrap(-1)
        wxBoxSizer.Add(self.staticTexttitle, 0, wx.ALL, 5)
 
        self.staticTexttitle = wx.StaticText(self, wx.ID_ANY, u"3、如不符合上述格式，将进行联网在线翻译，支持多国语言翻译。", wx.DefaultPosition, wx.DefaultSize, 0)
        self.staticTexttitle.Wrap(-1)
        wxBoxSizer.Add(self.staticTexttitle, 0, wx.ALL, 5)
 
        self.SetSizer(wxBoxSizer)
        self.Layout()
 
        self.Centre(wx.BOTH)
 
        # Connect Events
        self.BtnTranwords.Bind(wx.EVT_BUTTON, self.BtnTranWord)
 
    def __del__(self):
        pass
 
    # Virtual event handlers, overide them in your derived class
    def BtnTranWord(self, event):
        event.Skip()
 
 
