import win32gui
import win32con
import win32ui
import re

class assStyle:
    fontname = 'Arial'
    fontsize = 20
    alpha1 = '&H00'
    color1 = '&H00FFFFFF'
    alpha2 = '&H00'
    color2 = '&H000000FF'
    alpha3 = '&H00'
    color3 = '&H00000000'
    alpha4 = '&H00'
    color4 = '&H00000000'
    bold = 0
    italic = 0
    underline = 0
    strikeout = 0
    scale_x = 100
    scale_y = 100
    spacing = 0
    angle = 0
    borderstyle = 1
    outline = 2
    shadow = 2
    alignment = 2
    margin_l = 10
    margin_r = 10
    margin_v = 10
    encoding = 1
    
    def __init__(self, data = {}, from_ass = None):
        if 'fontname' in data:
            self.fontname = str(data['fontname'])
        if 'fontsize' in data:
            self.fontsize = int(data['fontsize'])
        if 'alpha1' in data:
            self.alpha1 = str(data['alpha1'])
        if 'color1' in data:
            self.color1 = str(data['color1'])
        if 'alpha2' in data:
            self.alpha2 = str(data['alpha2'])
        if 'color2' in data:
            self.color2 = str(data['color2'])
        if 'alpha3' in data:
            self.alpha3 = str(data['alpha3'])
        if 'color3' in data:
            self.color3 = str(data['color3'])
        if 'alpha4' in data:
            self.alpha4 = str(data['alpha4'])
        if 'color4' in data:
            self.color4 = str(data['color4'])
        if 'bold' in data:
            self.bold = int(data['bold'])
        if 'italic' in data:
            self.italic = int(data['italic'])
        if 'underline' in data:
            self.underline = int(data['underline'])
        if 'strikeout' in data:
            self.strikeout = int(data['strikeout'])
        if 'scale_x' in data:
            self.scale_x = float(data['scale_x'])
        if 'scale_y' in data:
            self.scale_y = float(data['scale_y'])
        if 'spacing' in data:
            self.spacing = float(data['spacing'])
        if 'angle' in data:
            self.angle = float(data['angle'])
        if 'borderstyle' in data:
            self.borderstyle = int(data['borderstyle'])
        if 'outline' in data:
            self.outline = float(data['outline'])
        if 'shadow' in data:
            self.shadow = float(data['shadow'])
        if 'alignment' in data:
            self.alignment = int(data['alignment'])
        if 'margin_l' in data:
            self.margin_l = int(data['margin_l'])
        if 'margin_r' in data:
            self.margin_r = int(data['margin_r'])
        if 'margin_v' in data:
            self.margin_v = int(data['margin_v'])
        if 'encoding' in data:
            self.encoding = int(data['encoding'])
        pass

class assLine:
    text = ''
    start_time = 0
    end_time = 0
    effect = ''
    syls = []
    
    def __init__(self, data = {}, from_ass = None):
        if 'text' in data:
            self.text = str(data['text'])
        if 'effect' in data:
            self.effect = str(data['effect'])
        if 'start_time' in data:
            self.start_time = int(data['start_time'])
        if 'end_time' in data:
            self.end_time = int(data['end_time'])
        pass
        

    def __str__(self):
        if len(self.syls) > 0:
            self.text = ''
            for syl in self.syls:
                self.text += str(syl)
        return re.sub('(\\{.*?\\})','',str(self.text))

class assMeta:
    name = ''
    value = ''

    def __init__(self, data = {}, from_ass = None):
        if 'name' in data:
            self.name = data['name']
        if 'value' in data:
            self.value = data['value']
        pass

    def __str__(self):
        return self.value

class assFile:
    lines = []
    styles = {}
    metas = {}
    path = None

    def __init__(self, path = None):
        self.path = path

    def open(self, path = None):
        if path == None:
            path = self.path
        if path == None:
            return None
        try:
            fp = open(self.path, 'rb+')
        except:
            return None
        meta_start = ['[Script Info]']
        style_start = ['[V4+ Styles]','[V4 Styles]']
        line_start = ['[Events]']
        style_index_change = {'primarycolour':'color1','secondarycolour':'color2','outlinecolour':'color3','backcolour':'color4','scalex':'scale_x','scaley':'scale_y','marginl':'margin_l','marginr':'margin_r','marginv':'margin_v'}
        line_index_change = {'marginl':'margin_l','marginr':'margin_r','marginv':'margin_v','text':'raw_text'}
        in_location = None
        style_format = None
        line_format = None
        for line in iter(fp):
            line = str(str(line).strip())
            if not line == '':
                start_tag_line = None
                for meta_tag in meta_start:
                    if line.lower().find(meta_tag.lower()) >= 0 and line.lower().find(meta_tag.lower()) < 5:
                        in_location = 'meta'
                        start_tag_line = True
                        print "===> Entred in meta."
                        continue
                for style_tag in style_start:
                    if line.lower().find(style_tag.lower()) >= 0 and line.lower().find(style_tag.lower()) < 5:
                        in_location = 'style'
                        start_tag_line = True
                        print "===> Entred in style."
                        continue
                for line_tag in line_start:
                    if line.lower().find(line_tag.lower()) >= 0 and line.lower().find(line_tag.lower()) < 5:
                        in_location = 'line'
                        start_tag_line = True
                        print "===> Entred in line."
                        continue
                if not start_tag_line:
                    if in_location == 'meta':
                        p = line.find(':')
                        if p >= 1:
                            self.appendMeta(line[:][0:p].strip(), assMeta({'name':line[:][0:p].strip(),'value':line[:][p+1:].strip()}))
                        continue
                    if in_location == 'style':
                        p = line.find(':')
                        if line[:][0:p].lower() == 'format':
                            print "======> Format Style."
                            form = line[:][p+1:]
                            k = 0
                            p = {}
                            for param_ass_name in form.split(','):
                                param_ass_name = param_ass_name.strip().lower()
                                if param_ass_name in style_index_change:
                                    p[k] = style_index_change[param_ass_name]
                                    k = k + 1
                                else:
                                    p[k] = param_ass_name
                                    k = k + 1

                            style_format = p
                            print p
                            continue
                        if line[:][0:p].lower() == 'style':
                            print "======> Recognized Style."
                            if not style_format:
                                continue
                            else:
                                s = {}
                                k = 0
                                style = line[:][p+1:]
                                for param in style.split(','):
                                    s[style_format[k]] = param.strip()
                                    k = k + 1
                                if 'name' in s:
                                    self.styles[s['name']] = assStyle(s, True)
                        continue
                                
                    if in_location == 'line':
                        p = line.find(':')
                        if line[:][0:p].lower() == 'format':
                            print "======> Format Line."
                            form = line[:][p+1:]
                            k = 0
                            p = {}
                            for param_ass_name in form.split(','):
                                param_ass_name = param_ass_name.strip().lower()
                                if param_ass_name in line_index_change:
                                    p[k] = line_index_change[param_ass_name]
                                    k = k + 1
                                else:
                                    p[k] = param_ass_name
                                    k = k + 1

                            line_format = p
                            print p
                            continue
                        if line[:][0:p].lower() == 'dialogue' or line[:][0:p].lower() == 'comment':
                            print "======> Recognized Line."
                            if not line_format:
                                continue
                            else:
                                s = {}
                                k = 0
                                l = line[:][p+1:]
                                for param in l.split(','):
                                    s[line_format[k]] = param.strip()
                                    k = k + 1
                                if line[:][0:p].lower() == 'dialogue':
                                    s['comment'] = 0
                                else:
                                    s['comment'] = 1
                                self.lines.append(assLine(s, True))
                                continue
                    print "=> {0}".format(line)
        fp.close()
        

    def appendLine(self, line):
        self.lines.append(line)

    def appendStyle(self, name, style):
        self.styles[name] = style

    def appendMeta(self, name, value):
        self.metas[name] = value
    

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
    def __init__(self, text = '', style = None):
        if style == None:
            style = assStyle()
        self.text = str(text)
        self.style = style
        pass

    def selectFont(self, dc, style = None, scale = 64):
        if style == None:
            style = self.style
        font = win32gui.LOGFONT()
        font.lfHeight = style.fontsize * scale
        if style.bold:
            font.lfWeight = win32con.FW_BOLD
        else:
            font.lfWeight = win32con.FW_NORMAL
        font.lfItalic = style.italic
        font.lfUnderline = style.underline
        font.lfStrikeOut = style.strikeout
        font.lfCharSet = style.encoding
        font.lfOutPrecision = win32con.OUT_TT_PRECIS;
        font.lfClipPrecision = win32con.CLIP_DEFAULT_PRECIS;
        font.lfQuality = win32con.ANTIALIASED_QUALITY;
        font.lfPitchAndFamily = win32con.DEFAULT_PITCH | win32con.FF_DONTCARE;
        font.lfFaceName = style.fontname[:32]
        font = win32gui.CreateFontIndirect(font)
        win32gui.SelectObject(dc, font)
        pass

    def getExtents(self, text = None, style = None):
        if text == None:
            text = str(self.text)
        if style == None:
            style = self.style
        txtext = {}
        dc = win32gui.CreateCompatibleDC(0)
        win32gui.SetMapMode(dc, win32con.MM_TEXT)
        font = self.selectFont(dc, style, 64)

        if style.spacing:
            for char in text:
                cx, cy = win32gui.GetTextExtentPoint32(dc, char)
                txtext['width'] += cx + (style.spacing * 64)
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

        txtext['width'] = txtext['width'] * (style.scale_x / float(100)) / float(64);
        txtext['height'] = txtext['height'] * (style.scale_y / float(100)) / float(64);
        txtext['ascent'] = txtext['ascent'] * (style.scale_y / float(100)) / float(64);
        txtext['descent'] = txtext['descent'] * (style.scale_y / float(100)) / float(64);
        txtext['internal_lead'] = txtext['internal_lead'] * (style.scale_y / float(100)) / float(64);
        txtext['external_lead'] = txtext['external_lead'] * (style.scale_y / float(100)) / float(64);
        return txtext
        

if __name__ == "__main__":
    print TextToy("T").getExtents()
    line = assLine({'text':'{\b1}LOL{\b0}'})
    print line
    f = assFile("preview.ass")
    f.open()
