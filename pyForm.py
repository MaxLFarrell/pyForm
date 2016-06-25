doc = ""
indent = ""
class writer:
    def getvalue(self):
        return doc
    def setIndent(self, string):
        print("Only use this if you know what you're doing")
        print("If you mess up call defaultIndent and it will reset the indent")
        global indent
        indent = string
    def defaultIndent(self):
        global indent
        indent = ""
    def asis(self, string):
        global doc
        doc += indent + string + "\n"
    def importer(self, importl):
        global doc
        for importn in importl:
            if type(importn) == tuple:
                tmpv = "from " + importn[0] + " import "
                for it, val in enumerate(importn[1]):
                    if it == len(importn[1]) - 1:
                        tmpv += val
                    else:
                        tmpv += val + ", "
                doc += indent + tmpv + "\n"
            else:
                doc += indent + "import " + importn + "\n"
class inner:
    def __init__(self, lt, ioc, itn=""):
        self.lt = lt
        self.ioc = ioc
        self.itn = itn 
    def __enter__(self):
        global doc, indent
        if self.lt == "for":
            iter = self.ioc
            if self.itn == "":
                itn = "it"
            else:
                itn = self.itn
            doc += indent + "for " + itn + " in " + str(iter) + ":\n"
        elif self.lt == "while":
            condition = self.ioc
            doc += indent + "while " + condition + ":\n"
        elif self.lt == "if" or self.lt == "elif":
            doc += indent + self.lt + " " + self.ioc + ":\n"
        elif self.lt == "else":
            doc += indent + "else:\n"
        indent += "   "
    def __exit__(self, type, value, traceback):
        global indent
        indent = ""