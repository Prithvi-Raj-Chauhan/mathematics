class Fraction:
    def __init__(self, n, d) -> None:
        """
        A Fraction with basic functions
        """
        self.numerator = n
        self.denominator = d
    
    def __repr__(self) -> str:
        return f"{self.numerator}/{self.denominator}"

if __name__ == '__main__':
    f1 = Fraction(1,2)
    print(f1)