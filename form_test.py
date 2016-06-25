from pyForm import writer, inner

w = writer()
w.importer(["random","os", ("datetime",("datetime", "timedelta"))])
with inner("for", ["x", "y", "z"]):
    w.asis("print(it)")
    with inner("while","True"):
        w.asis("print('im in the loop')")
        w.asis("break")
w.asis("print('im out of the loop')")
w.setIndent("")
w.defaultIndent()
print(w.getvalue())
f = open("test.py", "w")
f.write(w.getvalue())
f.close()