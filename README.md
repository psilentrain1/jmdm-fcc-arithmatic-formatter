### Arithmatic Formatter

This project takes groups of math problems and rearranges them like they would be on paper. There's an optional flag to calculate the result.

#### Using the Arithmatic Formatter

Add any function calls you would llike as `arithmatic_arranger([list_of_problems])`.

#### Test Cases

Function call:
`arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])`
Expected output:

```
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
```

Function call:
`arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)`
Expected output:

```
  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474
```

#### freeCodeCamp Disclaimer

This project was completed as part of [freeCodeCamp.org](https://www.freecodecamp.org)'s _Scientific Computing with Python_ course. This was a Certification Project, meaning [freeCodeCamp](https://www.freecodecamp.org) provided specifications and limited guidance and I was expected to code to meet certain test cases. The code presented here is my own.
