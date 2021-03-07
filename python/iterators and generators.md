Sources:
https://docs.python.org/3/whatsnew/2.4.html#pep-289-generator-expressions
https://www.freecodecamp.org/news/how-and-why-you-should-use-python-generators-f6fb56650888/
https://stackoverflow.com/a/2776865

# Iterators
An `iterator` is a more general concept: any object whose class has a `__next__` method (`next` in Python 2) and an `__iter__` method that does return self.

Every generator is an iterator, but not vice versa. A generator is built by calling a function that has one or more `yield` expressions (`yield statements`, in Python 2.5 and earlier), and is an object that meets the previous paragraph's definition of an iterator.

You may want to use a custom iterator, rather than a generator, when you need a class with somewhat complex state-maintaining behavior, or want to expose other methods besides `__next__` (and `__iter__` and `__init__`). Most often, a generator (sometimes, for sufficiently simple needs, a generator expression) is sufficient, and it's simpler to code because state maintenance (within reasonable limits) is basically "done for you" by the frame getting suspended and resumed.

For example, a generator such as:

```
def squares(start, stop):
    for i in range(start, stop):
        yield i * i

generator = squares(a, b)
```

or the equivalent generator expression (genexp)

```
generator = (i*i for i in range(a, b))
```

would take more code to build as a custom iterator:

```
class Squares(object):
    def __init__(self, start, stop):
       self.start = start
       self.stop = stop
    def __iter__(self): return self
    def __next__(self): # next in Python 2
       if self.start >= self.stop:
           raise StopIteration
       current = self.start * self.start
       self.start += 1
       return current

iterator = Squares(a, b)
```

But, of course, with class Squares you could easily offer extra methods, i.e.

```
    def current(self):
       return self.start
```

if you have any actual need for such extra functionality in your application.

# Generators
Generator functions allow you to declare a function that behaves like an iterator.
Generator expressions work similarly to list comprehensions but don’t materialize the entire list; instead they create a generator that will return elements one by one.

Key facts: 
- Iterators allow lazy evaluation, only generating the next element of an iterable object when requested. This is useful for very large data sets.
- Iterators and generators can only be iterated over once.
