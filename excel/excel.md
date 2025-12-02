# Excel Functions

## Round Functions
- round
- rounddown
- roundup
- int

## Mathematical Functions
- sign
- abs
- power
- log
- ln
- log10
- exp
- sqrt
- pi
- sin
- cos
- radians
- isnumber
- iseven
- isodd
- isblank
- base
- mod
- roman


## Statistical Functions
- min
- max
- var
- stddev
- sum
- product
- sumproduct
- average
- count
- median
- percentile
- quartile
- skew
- kurt
- correl
- forecast
- forecast.ets
- combin
- fact
- sumsq

## Logical Functions and Operations

- and
- or
- not
- xor
- if


## Random Numbers

- rand
- randbetween

## Date and Time Functions

- now
- year
- month
- day
- hour
- minute
- second


## String Functions

- CHAR
- CODE
- Unicode
- Unichar
- lower
- upper
- concatenate
- left
- right
- mid
- len
- istext
- ISNONTEXT
- Replace
- Search
- vlookup

## To be added

- FLOOR
- CEILING



## Visual Basic for Applications (VBA)

```vb
' This function returns the product of two numbers
Function times(a, b)
    times = a * b
End Function
```

```vb
Rem This function returns factorial of n
Function factorial(n)
    Dim result As Long
    Dim i As Long
    result = 1
    
    For i = 2 To n
        result = result * i
    Next

    factorial = result
End Function
```

```vb
Rem This functions returns delta of a given parabola
Function paraboladelta(a As Double, b As Double, c As Double) As Double
    paraboladelta = b * b - 4 * a * c
End Function
```

```vb
' This function returns
' -> 0, if delta < 0
' -> 1, if delta = 0
' -> 2, if delta > 0
Function numberofroots(a As Double, b As Double, c As Double) As Integer
    Dim delta As Double
    delta = b * b - 4 * a * c
    If delta < 0 Then
        numberofroots = 0
    ElseIf delta = 0 Then
        numberofroots = 1
    Else
        numberofroots = 2
    End If
End Function
```

```vb
' This function returns the minimum of a given range
Function findminimum(r As Range) As Double
    mymin = 9999999
    For i = 1 To r.Count
        If r.Cells(i, 1) < mymin Then
            mymin = r.Cells(i, 1)
        End If
    Next
    findminimum = mymin
End Function
```
