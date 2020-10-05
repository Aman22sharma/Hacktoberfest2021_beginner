// AUTHOR: PPraneetha Chebolu
//Python3 Concept: Math Modules
// GITHUB: https://github.com/praneethacl

# This module provides access to the mathematical functions defined by the C standard.
# These functions cannot be used with complex numbers

# To use mathematical functions under this module, you have to import the module using import math.
import math


#Constants

print(math.pi)   # prints the mathematical constant π = 3.141592…, to available precision.

print(math.e)    # prints the mathematical constant e = 2.718281…, to available precision.

print(math.tau)  # prints the mathematical constant τ = 6.283185…, to available precision.

print(math.inf)  # prints a floating-point positive infinity.

print(math.nan)  # prints a floating-point “not a number” (NaN) value.



#Number-theoretic functions

# math.ceil(x):	returns the smallest integer greater than or equal to x.
print(math.ceil(5.4))         # prints 6

# math.copysign(x, y): returns a float with the magnitude (absolute value) of x with the sign of y
print(math.copysign(1.0, -1)) # prints -1.0

# math.fabs(x): return the absolute value of x.
print(math.fabs(-12.3))       # prints 12.3

# math.factorial(x): return x factorial as an integer.
print(math.factorial(5))      # prints 120

# math.floor(x): return the largest integer less than or equal to x.
print(math.ceil(5.4))         # prints 5

# math.fmod(x, y): returns x % y, but is generally used for floats instead of integers.
print(math.fmod(-15.7, 4.9))  # prints -0.9982 but -15.7 % 4.9 gives 3.9002

# math.frexp(x): return the mantissa and exponent of x as the pair (m, e), such that x == m * 2**e.
print(math.frexp(3))          # prints(0.75, 2)

# math.fsum(iterable): return an accurate floating point sum of values in the iterable.
print(math.fsum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1])) # prints 1.0

# math.gcd(a, b): return the greatest common divisor of the integers a and b.
print(math.gcd(147, 21))      # prints 21

# math.isfinite(x): return True if x is neither an infinity nor a NaN, and False otherwise.
print(math.isfinite(1))       # print True

# math.isinf(x): return True if x is a positive or negative infinity, and False otherwise.
print(math.isinf(-math.inf))  # prints True

# math.isnan(x): return True if x is a NaN (not a number), and False otherwise.
print(math.isnan(math.nan))   # prints True

# math.ldexp(x, i): return x * (2**i). This is essentially the inverse of function frexp().
print(math.ldexp(2, 2))       # prints 8.0

# math.modf(x): return the fractional and integer parts of x.
print(math.modf(-11.44))      # prints (-0.4399999999999995, -11.0)

# math.trunc(x): returns the truncated integer value of x
print(math.trunc(134.33))     # prints 134



#Power and logarithmic functions

# math.log(x): return the natural logarithm of x (to base e).
print(math.log(2))            # prints 0.6931471805599453

# math.log(x, base): return the logarithm of x to the given base.
print(math.log(4, 2))         # prints 2.0

# math.log1p(x): return the natural logarithm of 1+x (base e). 
print(math.log1p(1))          # prints 0.6931471805599453

# math.log2(x): return the base-2 logarithm of x.
print(math.log2(2))           # prints 1.0

# math.log10(x): return the base-10 logarithm of x.
print(math.log10(2))          # prints 0.3010299956639812

# math.pow(x, y): return x raised to the power y.
print(math.pow(2, 3))         # prints 8.0

# math.sqrt(x): return the square root of x.
print(math.sqrt(9))           # prints 3.0



#Trigonometric functions

# math.acos(x): return the arc cosine of x, in radians.
print(math.acos(0.1))         # prints 1.4706289056333368

# math.asin(x): return the arc sine of x, in radians.
print(math.asin(0.1))         # prints 0.1001674211615598

# math.atan(x): return the arc tangent of x, in radians.
print(math.atan(0.1))         # prints 0.09966865249116204

# math.atan2(y, x): returns atan(y / x)
print(math.atan2(1, 10))      # prints 0.09966865249116202

# math.cos(x): return the cosine of x.
print(math.cos(0.1))          # prints 0.9950041652780258

# math.sin(x): returns the sine of x.
print(math.sin(0.1))          # prints 0.09983341664682815

# math.tan(x): returns the tangent of x.
print(math.tan(0.1))          # prints 0.10033467208545055

# math.hypot(x, y): returns the Euclidean norm, sqrt(x*x + y*y)
print(math.hypot(3,4))        # prints 5.0

# math.degrees(x): converts angle x from radians to degrees
print(math.degrees(1.57079))  # prints 89.99963750135457 

# math.radians(x): converts angle x from degrees to radians
print(math.radians(90))       # prints 1.5707963267948966



# Hyperbolic functions

# math.acosh(x): return the inverse hyperbolic cosine of x.
print(math.acosh(90))         # prints 5.192925985263684

# math.asinh(x): return the inverse hyperbolic sine of x.
print(math.asinh(90))         # prints 5.192987713658941

# math.atanh(x): return the inverse hyperbolic tangent of x.
print(math.atanh(0.5))        # prints 0.5493061443340549

# math.cosh(x): return the hyperbolic cosine of x.
print(math.cosh(0.5))         # prints 1.1276259652063807

# math.sinh(x): return the hyperbolic sine of x.
print(math.sinh(0.5))         # prints 0.5210953054937474

# math.tanh(x): return the hyperbolic tangent of x.
print(math.tanh(0.5))         # prints 0.46211715726000974


