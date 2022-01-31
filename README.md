# C++ Calculator

## Usage
I Used Visual Studio Code on 64bit macOS (intel)

Use the following to compile the program:
using gcc: 
`gcc -o out calculator-main.cpp -std=c++17`

To run the program:
`./out`


## Explination

To add division I refactored existing code to accept the division operator and added division as a Type. 

If the divisor is 0 then the result will be `inf` (positive inf as negative numbers are not parsed in this calculator) or NaN if the dividend is also 0.

In either case I added a quick check using `isinf()` and `isnan()` to print out a warning to the user.

To add pi to the calculator, I simply added a check in `findAndExtractLHS()` and `findAndExtractRHS()` where if `substr()` yields `"pi"` then the functions returns the const variable `PI`

To avoid errors regarding whitespace I used regex to remove any whitespace from the input expression inside of `tokenize()`.

Furthermore to ensure that the output is formatted to 5 decimal places, I used `std::fixed` to set the IO to a fixed-point format and `std::setprecision()` to set the precision to 5.

Finally I added a couple of assertions in the `test()` functions to test division and pi.


# API Parsing

## Usage
install requests (if necessary):
`python3 -m pip install requests`

## 
Personally I would've chosen TypeScript to do this task, however since that wasn't an explicit option I chose to use Python 3. 

First the program grabs the json data from `https://api.ampifymusic.com/packs` using the requests module, then the data is sorted by genre using a nested for loop, where the resulting dictionary is formatted as such: `parsed : {[genre: string]: pack[]}`.

Finally I print out the keys of the parsed dictionary to get the list of genres and then print out the packs in the `hip-hop` genre using `json.dump()` for better formatting.