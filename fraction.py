class Fraction:
    def __init__(self, n, d) -> None:
        """
        A Fraction with basic functions
        """
        self.numerator = n
        self.denominator = d
    
    def __repr__(self) -> str:
        return f"{self.numerator}/{self.denominator}"

    def reciprocal(self):
        return Fraction(self.denominator, self.numerator)

    def mul(self, other):
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def div(self, other):
        return self.mul(other.reciprocal())


if __name__ == '__main__':
    f1 = Fraction(1,2)
    f2 = Fraction(3,4)
    print(f1.mul(f2))
    print(f1.div(f2))