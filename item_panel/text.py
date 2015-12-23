cheatsheet = r'''
Python Regular Expressions Cheatsheet


Non-special chars match themselves. Exceptions are special characters:

  \             Escape special char or start a sequence.

  .             Match any char except newline, see re.DOTALL

  ^             Match start of the string, see re.MULTILINE

  $             Match end of the string, see re.MULTILINE

  []            Enclose a set of matchable chars

  R|S           Match either regex R or regex S.

  ()            Create capture group, & indicate precedence


After '[', enclose a set, the only special chars are:

  ]             End the set, if not the 1st char

  -             A range, eg. a-c matches a, b or c

  ^             Negate the set only if it is the 1st char


Quantifiers (append '?' for non-greedy):

  {m}           Exactly m repetitions

  {m,n}         From m (default 0) to n (default infinity)

  *             0 or more. Same as {,}

  +             1 or more. Same as {1,}

  ?             0 or 1. Same as {,1}


Special sequences:

  \A            Start of string

  \b            Match empty string at word (\w+) boundary

  \B            Match empty string not at word boundary

  \d            Digit

  \D            Non-digit

  \s            Whitespace [ \t\n\r\f\v], see LOCALE,UNICODE

  \S            Non-whitespace

  \w            Alphanumeric: [0-9a-zA-Z_], see LOCALE

  \W            Non-alphanumeric

  \Z            End of string

  \g<id>        Match prev named or numbered group,
                  '<' & '>' are literal, e.g. \g<0>
                  or \g<name> (not \g0 or \gname)


Special character escapes are much like those already escaped in Python string
  literals. Hence regex '\n' is same as regex '\\n':

  \a            ASCII Bell (BEL)

  \f            ASCII Formfeed

  \n            ASCII Linefeed

  \r            ASCII Carriage return

  \t            ASCII Tab

  \v            ASCII Vertical tab

  \\            A single backslash

  \xHH          Two digit hexadecimal character goes here

  \OOO          Three digit octal char (or just use an
                  initial zero, e.g. \0, \09)

  \DD           Decimal number 1 to 99, match
                  previous numbered group


Extensions. Do not cause grouping, except 'P<name>':

  (?iLmsux)     Match empty string, sets re.X flags

  (?:...)       Non-capturing version of regular parens

  (?P<name>...) Create a named capturing group.

  (?P=name)     Match whatever matched prev named group

  (?#...)       A comment; ignored.

  (?=...)       Lookahead assertion, match without consuming

  (?!...)       Negative lookahead assertion

  (?<=...)      Lookbehind assertion, match if preceded

  (?<!...)      Negative lookbehind assertion

  (?(id)y|n)    Match 'y' if group 'id' matched, else 'n'


  For a more complete documentation of python regular expressions;

    https://docs.python.org/3.5/library/re.html
'''
