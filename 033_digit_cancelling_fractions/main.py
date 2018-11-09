#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fractions import Fraction
from operator import mul

def main():
    answers = [];

    # Our numerators are between 10 and 99
    for numerator in range(10, 99):
        nfirst, nsecond = int(numerator.__str__()[0]), int(numerator.__str__()[1]);

        # The possible denominators are two digits and composed of the second digit
        # of the numerator followed by another digit
        denominators = [int(nsecond.__str__() + i.__str__()) for i in range(0, 10)];

        for denominator in denominators:
            try:
                # We need to get the second digit of the denominator to create the simplyfied fraction
                dsecond = int(denominator.__str__()[1]);
                fracComplete = Fraction(numerator, denominator);
                fracSimplify = Fraction(nfirst, dsecond)

                if (fracComplete < 1 and fracComplete == fracSimplify):
                    answers.append(fracComplete);
            except:
                pass;

    # Multiply all the answers so we can get the final denominator which is the answer
    total = reduce(mul, answers, 1);

    print("answers:", answers);
    print("total:", total);
    print("result:", total.denominator);

main();
