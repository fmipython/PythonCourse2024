#ifndef EXAMPLE_2_RATIONAL_H
#define EXAMPLE_2_RATIONAL_H

struct Rational{
    int numerator;
    int denominator;
};

extern struct Rational add(const struct Rational a, const struct Rational b);
extern struct Rational subtract(const struct Rational a, const struct Rational b);
extern struct Rational multiply(const struct Rational a, const struct Rational b);
extern struct Rational divide(const struct Rational a, const struct Rational b);

extern struct Rational build(const int a, const int b);

#endif
