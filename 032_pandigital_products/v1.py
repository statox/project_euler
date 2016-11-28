# Answer 45228 
# 5796 4396 7632 6952 5346 7254 7852

# Solves problem 32 but it is pretty long
# I should be able to do better

import re

# Recursively find permutations
def permute(n):
    if (len(n) == 2):
        return [str(n), str(n[1]+n[0])]
    else:
        list = []
        for i in n:
            sub = permute(re.sub(i, '', n))

            for s in sub:
                list.append(i + s)
                if (len(list) % 1000000 == 0):
                    print "1000000th permutations: " + i+s

        return list

# Takes a permutation of 123456789 and
# create the different possible products by putting * and =
# in all the possible places
def createOperation(n):
    productsToKeep = []

    for i in range(1, len(n)-1):
        multiplicand = n[:i]
        for j in range(i+1, len(n)):
                multiplier = n[i:j]
                product = n[j:]

                # print multiplicand + "*" + multiplier + "=" + product
                if ( int(multiplicand) * int(multiplier) == int(product) ):
                    productsToKeep.append(int(product))

    return productsToKeep

def main():
    # Generate the permutations
    print "Generating the permutations of 123456789"
    permutations = permute("123456789")
    print str(len(permutations)) + " permutations found"

    # for each permutations test if it can create a pandigital
    print "Testing permutations for pandigital products"

    products = []
    for p in permutations:
        results = createOperation(p)

        if len(results) > 0:
            products += results

        # I don't like to stare at an empty screen let's follow the process
        if (permutations.index(p) % 10000 == 0):
            print "permutation " + str(permutations.index(p)) + " on " + str(len(permutations))
            print "current permutation: " + p
            print "current products: " + str(products)

    print "End of loop. Final products:"
    print products

    # Remove duplicates in products
    products = list(set(products))
    print "Products without duplicates:"
    print products

    # Get the interesting result
    print "Sum of products:"
    print sum(products)

main()
