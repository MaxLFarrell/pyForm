# pyForm
Python3 generator written in Python3

Very basic, pure python, requires no 3rd party libraries

Just import the base writer and the loop writer and instantiate a writer object
```
from pyForm import writer, inner
w = writer()
```
Then you can write!
```
w.asis("print('Hello world!')")
```
To write loops just do so with the with keyword
```
with inner("for",["x","y","z"], "avar"):
  w.asis("print(avar)")
```
The above writes:
```
for avar in ["x", "y", "z"]:
  print(avar)
```
to the doc variable

To get your document's value
```
w.getvalue()
```

For some examples look at [form_test.py](https://github.com/MaxLFarrell/pyForm/blob/master/form_test.py)

I took my inspiration from yattag so check it out [here](http://www.yattag.org/)!
