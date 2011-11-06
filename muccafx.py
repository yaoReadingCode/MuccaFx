import win32gui
import win32con
import win32ui

class FxLine:
    text = ''
    
    def __init__(self, data = {}):
        if 'text' in data:
            self.text = str(data['text']
        pass

    def __str__(self):
        return str(self.text)

class MuccaFxEffect:
    ass = None
    nlines = []
    
    def __init__(self, ass):
        self.ass = ass
        pass

    def appendLine(self, line):
        self.nlines.append(line)

    def _getNewLines(self):
        return self.nlines

class TextToy:
    def __init__(self, text = '', style = {}):
        self.style = {
            'fontname':'Arial',
            'fontsize':20,
            'alpha1':'&H00',
            'color1':'&H00FFFFFF',
            'alpha2':'&H00',
            'color2':'&H000000FF',
            'alpha3':'&H00',
            'color3':'&H00000000',
            'alpha4':'&H00',
            'color4':'&H00000000',
            'bold':0,
            'italic':0,
            'underline':0,
            'strikeout':0,
            'scale_x':100,
            'scale_y':100,
            'spacing':0,
            'angle':0,
            'borderstyle':1,
            'outline':2,
            'shadow':2,
            'alignment':2,
            'margin_l':10,
            'margin_r':10,
            'margin_v':10,
            'encoding':1
        }
        self.text = text
        self.style.update(style)
        pass

    def selectFont(self, dc, style = None, scale = 64):
        if style == None:
            style = self.style
        font = win32gui.LOGFONT()
        font.lfHeight = style['fontsize'] * scale
        if style['bold']:
            font.lfWeight = win32con.FW_BOLD
        else:
            font.lfWeight = win32con.FW_NORMAL
        font.lfItalic = style['italic']
        font.lfUnderline = style['underline']
        font.lfStrikeOut = style['strikeout']
        font.lfCharSet = style['encoding']
        font.lfOutPrecision = win32con.OUT_TT_PRECIS;
        font.lfClipPrecision = win32con.CLIP_DEFAULT_PRECIS;
        font.lfQuality = win32con.ANTIALIASED_QUALITY;
        font.lfPitchAndFamily = win32con.DEFAULT_PITCH | win32con.FF_DONTCARE;
        font.lfFaceName = style['fontname'][:32]
        font = win32gui.CreateFontIndirect(font)
        win32gui.SelectObject(dc, font)
        pass

    def getExtents(self, text = None, style = None):
        if text == None:
            text = self.text
        if style == None:
            style = self.style
        txtext = {}
        dc = win32gui.CreateCompatibleDC(0)
        win32gui.SetMapMode(dc, win32con.MM_TEXT)
        font = self.selectFont(dc, style, 64)

        if style['spacing']:
            for char in text:
                cx, cy = win32gui.GetTextExtentPoint32(dc, char)
                txtext['width'] += cx + (style['spacing'] * 64)
                txtext['height'] = cy
        else:
            cx, cy = win32gui.GetTextExtentPoint32(dc, text)
            txtext['width'] = cx
            txtext['height'] = cy
        
        tm = win32gui.GetTextMetrics(dc);
        txtext['ascent'] = tm['Ascent'];
        txtext['descent'] = tm['Descent'];
        txtext['internal_lead'] = tm['InternalLeading'];
        txtext['external_lead'] = tm['ExternalLeading'];

        txtext['width'] = txtext['width'] * (style['scale_x'] / float(100)) / float(64);
        txtext['height'] = txtext['height'] * (style['scale_y'] / float(100)) / float(64);
        txtext['ascent'] = txtext['ascent'] * (style['scale_y'] / float(100)) / float(64);
        txtext['descent'] = txtext['descent'] * (style['scale_y'] / float(100)) / float(64);
        txtext['internal_lead'] = txtext['internal_lead'] * (style['scale_y'] / float(100)) / float(64);
        txtext['external_lead'] = txtext['external_lead'] * (style['scale_y'] / float(100)) / float(64);
        return txtext
        

if __name__ == "__main__":
    print TextToy("T",{'italic':True}).getExtents()
