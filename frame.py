import tkinter
import tkinter.filedialog
from tkinter.filedialog import askdirectory
from dealer import verticalCut

class Frame:
    def __init__(self):
        self.filename = ''
        self.top = tkinter.Tk()
        self.top.title("PDF DEALER V1.0")

        select_file = tkinter.Button(self.top, text="SELECT A PDF", 
        command = self.addfile)
        select_file.pack(fill=tkinter.X)

        cut = tkinter.Button(self.top, text="START TO CUT", 
        command = lambda: verticalCut(self.filename))
        cut.pack(fill=tkinter.X)

    def addfile(self):
        self.filename = tkinter.filedialog.askopenfilename()
        tip = tkinter.Label(self.top, text='INPUT FILE: '+self.filename)
        tip.pack()
    
    def center_window(self, w, h):
        # 获取屏幕 宽、高
        ws = self.top.winfo_screenwidth()
        hs = self.top.winfo_screenheight()
        # 计算 x, y 位置
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.top.geometry('%dx%d+%d+%d' % (w, h, x, y))

if __name__ == "__main__":
    frame = Frame()
    frame.center_window(400, 100)
    tkinter.mainloop()
