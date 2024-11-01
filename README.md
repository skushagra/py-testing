# Veritas

Veritas is a in-development lightweight testing library written in Python. Currently it supports basic function testing, one level of verbose outputs. However basic in the current state it should support testing any kind of function.

## Sample Usage
Here is a simple usage of the testing library. The function `do_crazy_stuff` returns the wrong output `(a-b)` is mearly an operation which simulates a wrong answer.

```python
from veritas import Veritas

def add(a, b):
    return a + b

def do_crazy_stuff(a, b):
  return (a - b) # does crazy stuff but gives the wrong output

veritas = Veritas()
veritas.on(add, 3, a=1, b=2)
veritas.on(do_crazy_stuff, 2, a=2, b=1)
success_percentage = veritas.runAll(descriptive=True)
```

This code will give the following output
![image](https://github.com/user-attachments/assets/99216075-30e7-462a-a702-b5ef5655d3cf)
