#include "rational.h"


struct Rational build(const int a, const int b) {
    struct Rational result;
    result.numerator = a;
    result.denominator = b;
    return result;
}

struct Rational add(const struct Rational a, const struct Rational b) {
    int result_numerator = 0;
    int result_denominator = 0;

    if (a.denominator != b.denominator) {
        result_numerator = a.numerator * b.denominator + b.numerator * a.denominator;
        result_denominator = a.denominator * b.denominator;
    }
    else {
        result_numerator = a.numerator + b.numerator;
        result_denominator = a.denominator;
    }

    return build(result_numerator, result_denominator);
}

struct Rational subtract(const struct Rational a, const struct Rational b) {
    int result_numerator = 0;
    int result_denominator = 0;

    if (a.denominator != b.denominator) {
        result_numerator = a.numerator * b.denominator - b.numerator * a.denominator;
        result_denominator = a.denominator * b.denominator;
    }
    else {
        result_numerator = a.numerator + b.numerator;
        result_denominator = a.denominator;
    }
    
    return build(result_numerator, result_denominator);
}

struct Rational multiply(const struct Rational a, const struct Rational b) {
    struct Rational result;

    result.numerator = a.numerator * b.numerator;
    result.denominator = a.denominator * b.denominator;

    return result;
}

struct Rational divide(const struct Rational a, const struct Rational b) {
    struct Rational result;

    result.numerator = a.numerator * b.denominator;
    result.denominator = a.denominator * b.numerator;

    return result;
}