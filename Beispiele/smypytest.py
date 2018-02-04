%matplotlib notebook

import numpy as np
import matplotlib
from matplotlib import pyplot as plt
import sympy


class PrimeTime:
    def __init__(self, anzahl):
        self.primes = self.createPrimeList(anzahl)

    def createPrimeList(self, n):
        sieve = sympy.ntheory.generate.sieve
        sieve.extend_to_no(n)
        return sieve._list

    def createData(self):
        allPrimes = np.flipud(self.primes)
        primes = allPrimes
        primes = primes[:-1]

        sum = 1 / primes[0]
        dataNormal = [sum]

        for i, prime in enumerate(primes):
            sum = (1 - sum) / allPrimes[i + 1] + sum
            dataNormal.append(sum)

        return dataNormal


myPrimeTime = PrimeTime(6)
print(myPrimeTime.primes)
myData = myPrimeTime.createData()
print(myData)
plt.plot(myData)
