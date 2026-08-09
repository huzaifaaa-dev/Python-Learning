# Experiment 1- Match-Case Confusion

## Tried using the match-case loop on extensions.py, didn't work out, figuring out why.
## This code is NOT meant to be run, hence nothing is declared or any input is taken.

## I initially tried:
```python
match filename:
    case filename.endswith("gif"):
        print("image/gif")
```
## This didn't work.

## I did some research on my own and found:
```python
match filename:
    case _ if filename.endswith("gif"):
        print("image/gif")
```
## I came across (case _ if):

``` "case _" ``` is used like an else statement WHEN it is used at the bottom  of match-case. Everything else above it has already been checked.

``` "case _ if" ``` is slightly different. The _ still means the same, but the if adds another condition that has to be true.

For example:
```python
match filename:
    case _ if filename.endswith("jpeg"):
        print("image/jpeg")
```