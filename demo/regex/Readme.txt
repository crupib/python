r”\(([\d\-+]+)\)”
“r” here stands for the raw string
Python RegEx use a backslash(\)to indicate a special sequence or as an escape character. This collides with Python’s usage of the backslash(\) for the same purpose in string lateral. Thus, the raw string here is used to avoid confusion between the two.
\d  matches a single digit character [0-9]
\w  matches any alphabet, digit, or underscore
\s  matches a white space character (space, tab, enter)
\D  matches a single non-digit character
.   matches any character(except for newline character)
^   the string starts with a character
$   the string ends with a character
*   zero or more occurrences 
+   one or more occurrences
?   one or no occurrence 
{}  exactly the specified number of occurrences
|   either or

"c.t"            will match anything like "cat", "c*t", "c1t", etc
"^a"             will match "a" from "a cat" but not "eat a cake"
"cat$"           will match "a cat" but not "cat party"
"a*b"            will match "b", "ab", "aab", "aaab", ...
"a+b"            will match "ab", "aab", "aaab", ...
"a?b"            will match "b" or "ab"
"a{1}b"          will match "ab"
"a{1,3}b"        will match "ab", "aab", or "aaab"
"cat|dog"        will match "cat" or "dog"

[abcd]           matches either a, b, c or d
[a-z0-9]         matches one of the characters from a-z or 0-9
[\w]             matches an alphabet, digit, or underscore
The caret character(^) stands for except.
[^\d]            matches a character that is not a digit [0-9]

RegEx Functions

findall()        Returns a list that contains all matches       
search()         Returns a 'match object' if there is a match in          the string
split()          Returns a list of string that has been split at each match
sub()            Replaces the matches with a string            

RegEx Capturing Group

