from math import gcd, lcm

class Fraction:
    def __init__(self, n, d) -> None:
        """
        A Fraction with basic functions
        """
        self.numerator = int(n)
        self.denominator = int(d)
    
    def __repr__(self) -> str:
        return f"{self.numerator}/{self.denominator}"

    def reciprocal(self):
        """Flips the numerator and denominator with each other"""
        return Fraction(self.denominator, self.numerator)

    def simplify(self):
        hcf = gcd(self.denominator, self.numerator)
        return Fraction(self.numerator/hcf, self.denominator/hcf)

    def mul(self, other):
        """Multiplies two fractional numbers"""
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def div(self, other):
        """Divides two fractional numbers"""
        return self.mul(other.reciprocal())

    def add(self, other):
        new_denominator = lcm(self.denominator, other.denominator)
        new_self_fraction = Fraction(self.numerator*(new_denominator/self.denominator), self.denominator)
        new_other_fraction = Fraction(other.numerator*(new_denominator/other.denominator), other.denominator)
        return Fraction(new_self_fraction.numerator+new_other_fraction.numerator, new_denominator)

    def subtract(self, other):
        new_denominator = lcm(self.denominator, other.denominator)
        new_self_fraction = Fraction(self.numerator*(new_denominator/self.denominator), self.denominator)
        new_other_fraction = Fraction(other.numerator*(new_denominator/other.denominator), other.denominator)
        return Fraction(new_self_fraction.numerator-new_other_fraction.numerator, new_denominator)


if __name__ == '__main__':
    f1 = Fraction(1,2)
    f2 = Fraction(3,4)
    print(f1.mul(f2))
    print(f1.div(f2))
    print(f2.simplify())
    print(f1.add(f2))