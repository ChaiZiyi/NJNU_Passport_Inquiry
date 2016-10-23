# -*- coding: utf-8 -*-
import wx
import requests
from cStringIO import StringIO

url = 'http://223.2.10.123/jwgl/photos/rx20'

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit\
/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'}


class Frame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, -1, u'南师大证件照查看器',
                          size=(300, 360))
        self.Centre()
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        panel1 = wx.Panel(self, -1)
        sizer = wx.FlexGridSizer(1, 2, 10, 10)
        basicLabel = wx.StaticText(panel1, -1, u'请输入要查询的学号：')
        basicText = wx.TextCtrl(panel1, -1, size=(100, 18))
        basicText.SetInsertionPoint(0)

        self.Bind(wx.EVT_TEXT, self.showImage, basicText)

        sizer.AddMany([basicLabel, basicText])
        hbox.Add(sizer, proportion=2, flag=wx.ALL | wx.EXPAND, border=15)
        panel1.SetSizer(hbox)

    def showImage(self, text):
        panel2 = wx.Panel(self, -1, (70, 50), (150, 210))
        panel2.Refresh()
        id = text.GetString()
        year = id[2:4]
        name = id + '.jpg'
        turl = url + year + '/' + name
        req = requests.get(turl, headers=header)
        if req.headers.get('content-length') != '1163':
            image = wx.ImageFromStream(
                StringIO(req.content), wx.BITMAP_TYPE_ANY)
            temp = image.ConvertToBitmap()
            wx.StaticBitmap(parent=panel2, bitmap=temp)

if __name__ == '__main__':
    app = wx.App()
    frame = Frame()
    frame.Show()
    app.MainLoop()
