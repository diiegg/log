# log.py Is script which parses /var/log/messages

[![Build Status](https://travis-ci.org/diiegg/log.svg?branch=master)](https://travis-ci.org/diiegg/log)

# Parses /var/log/messages

# Introduction!
     
Pyparsing module - Classes and methods to define and execute parsing grammars.

The pyparsing module is an alternative approach to creating and executing simple grammars, vs. the traditional lex/yacc approach, or the use of regular expressions. With pyparsing, you don’t need to learn a new syntax for defining grammars or matching expressions - the parsing module provides a library of classes that you use to construct the grammar directly in Python.

Here is a program to parse “Hello, World!” (or any greeting of the form "<salutation>, <addressee>!"), built up using Word, Literal, and And elements (the '+' operators create And expressions, and the strings are auto-converted to Literal expressions):

```sh
from pyparsing import Word, alphas

# define grammar of a greeting
greet = Word(alphas) + "," + Word(alphas) + "!"

hello = "Hello, World!"
print(hello, "->", greet.parseString(hello))
```

The program outputs the following: .....
```sh
Hello, World! -> ['Hello', ',', 'World', '!']
```

The Python representation of the grammar is quite readable, owing to the self-explanatory class names, and the use of '+', '|', '^' and '&' operators.

The ParseResults object returned from ParserElement.parseString can be accessed as a nested list, a dictionary, or an object with named attributes.

The pyparsing module handles some of the problems that are typically vexing when writing text parsers:

        extra or missing whitespace (the above program will also handle “Hello,World!”, “Hello , World !”, etc.)
        quoted strings
        embedded comments


### Getting Started

Visit the classes ParserElement and ParseResults to see the base classes that most other pyparsing classes inherit from. Use the docstrings for examples of how to:

     -  construct literal match expressions from Literal and CaselessLiteral classes
     -  construct character word-group expressions using the Word class
     -  see how to create repetitive expressions using ZeroOrMore and OneOrMore classes
     -  use '+', '|', '^', and '&' operators to combine simple expressions into more complex ones
     -  associate names with your parsed results using ParserElement.setResultsName
     -  access the parsed data, which is returned as a ParseResults object
     -  find some helpful expression short-cuts like delimitedList and oneOf
     -  find more useful common expressions in the pyparsing_common namespace class

 class pyparsing.And(exprs, savelist=True)
    Bases: pyparsing.core.ParseExpression
    Requires all given ParseExpression s to be found in the given order. Expressions may be separated by whitespace. May be constructed using the '+' operator. May also be constructed using the '-' operator, which will suppress backtracking.

### Module

```sh
pyparsing
```

### Installation

to Run  a test :

```sh
pyton log.py
```

Output :

```sh
May 26 11:40:38 HomeOne org.freedesktop.portal.IBus[11095]: Not connected to the ibus bus

May 26 13:13:28 HomeOne 50-motd-news[36452]:  * MicroK8s passes 9 million downloads. Thank you to all our contributors!

May 26 13:13:28 HomeOne 50-motd-news[36452]:      https://microk8s.io/

May 26 14:08:25 HomeOne io.snapcraft.Settings[59044]: userd.go:98: Starting snap userd

```
### How to setup cron

Tu Run the script every 5 min, we need to set up a cron
```sh
# run script every 5 minutes
*/5 * * * *   myuser  python /path/to/script.py

# run script after system (re)boot
@reboot       myuser  python /path/to/script.py
```

License
----

MIT


**Free Software, Hell Yeah!**

