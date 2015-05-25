#!/usr/bin/python
# -*- coding: utf-8 -*-
# -*- coding: cp-1252 -*-

import wx
import os
import Image
 
class MyApp(wx.App):
   def OnInit(self):
       frame = MyFrame("Konwerterek", (50, 60), (550, 350))
       frame.Show()
       self.SetTopWindow(frame)
       return True
 
class MyFrame(wx.Frame):
   def __init__(self, title, pos, size):
       wx.Frame.__init__(self, None, -1, title, pos, size,
                         style=wx.DEFAULT_FRAME_STYLE)
 
       self.createMenuBar()
       self.panel = p = wx.Panel(self)
       self.popupmenu = wx.Menu()
       self.CreateStatusBar()
 
       pMdata = (
           ("&New", "New file", self.OnNew),
           ("&Open", "Open file", self.OnOpen),
           ("&Save", "Save file", self.OnSave),
       )
 
       self.popupmenu = self.createMenu(pMdata)                    
       p.Bind(wx.EVT_CONTEXT_MENU, self.OnShowPopup)
 
   def menuData(self):
       return [("&File", (
               #("&New", "New file", self.OnNew),
               ("&Open", "Open file", self.OnOpen),
               ("&Save", "Save file", self.OnSave),
               ("&Quit", "Quit", self.OnCloseWindow)))]
              
 
   def createMenuBar(self):
       menuBar = wx.MenuBar()
       for eachMenuData in self.menuData():
           menuLabel = eachMenuData[0]
           menuItems = eachMenuData[1]
           menuBar.Append(self.createMenu(menuItems), menuLabel)
       self.SetMenuBar(menuBar)
 
   def createMenu(self, menuData):
       menu = wx.Menu()
       for eachItem in menuData:
           if len(eachItem) == 2:
               label = eachItem[0]
               subMenu = self.createMenu(eachItem[1])
               menu.AppendMenu(wx.NewId(), label, subMenu)
           else:
               self.createMenuItem(menu, *eachItem)
       return menu
 
   def createMenuItem(self, menu, label, status, handler,
               kind=wx.ITEM_NORMAL):
       if not label:
           menu.AppendSeparator()
           return
       menuItem = menu.Append(-1, label, status, kind)
       self.Bind(wx.EVT_MENU, handler, menuItem)
 
   def OnShowPopup(self, event):
       pos = event.GetPosition()
       pos = self.panel.ScreenToClient(pos)
       self.panel.PopupMenu(self.popupmenu, pos)
 
   def OnContext(self, event):
       item = self.popupmenu.FindItemById(event.GetId())
       text = item.GetText()
       wx.MessageBox("You selected item '%s'" % text)
       print item
 
   def OnNew(self,event):
       wildcard = "Digital (*.dat)" \
                   "All files (*.*)|*.*"
       dialog = wx.FileDialog(None, "Nowy", os.getcwd(),
                   "", wildcard, wx.SAVE)
       if dialog.ShowModal() == wx.ID_OK:
           path = dialog.GetPath()
           open(path, 'w')
       dialog.Destroy()
 
   def OnOpen(self, event):
       wildcard = "All files (*.*)|*.*"
       dialog = wx.FileDialog(None, "Wybierz plik", os.getcwd(),
                   "", wildcard, wx.OPEN)
       if dialog.ShowModal() == wx.ID_OK:
           path = dialog.GetPath()
       print path
       dialog.Destroy()
 
   def OnSave(self, event):
       wildcard = "Digital (*.dat)" \
                   "All files (*.*)|*.*"
       dialog = wx.FileDialog(None, "Gdzie zapisac?", os.getcwd(),
                   "", wildcard, wx.SAVE)
       if dialog.ShowModal() == wx.ID_OK:
           path = dialog.GetPath()
           open(path, 'w')
       dialog.Destroy()
 

   def OnCloseWindow(self, event):
       dlg = wx.MessageDialog(None, 'Wyjście ?',
                   'Potwierdz!', wx.YES_NO | wx.ICON_QUESTION)
       result = dlg.ShowModal()
       if result == 5103:
           self.Destroy()
       elif result == 5104:
           print 'not ok'
       dlg.Destroy()
       
    
 
 
if __name__ == "__main__":
   app = MyApp(False)
   app.MainLoop()