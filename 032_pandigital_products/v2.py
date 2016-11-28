# 5796 4396 7632 6952 5346 7254 7852 
# Answer 45228

# Solves problem 32, better than v1 but still not the best
# ~300000 useless operations

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

def main():
    # Generate the permutations
    print "Generating the permutations of 123456789"
    permutations = permute("123456789")
    print str(len(permutations)) + " permutations found"

    # for each permutations test if it can create a pandigital
    print "Testing permutations for pandigital products"

    productsPandigital = []

    for p in permutations:
        if (permutations.index(p) % 1000 == 0):
            print "permutation " + str(permutations.index(p)) + " on " + str(len(permutations))
        for i in range(1, len(p)-1):
            for j in range(i+1, len(p)):
                # print p[:i] + "*" + p[i:j] + "=" +p[j:]

                if (int(p[:i]) * int(p[i:j]) == int(p[j:]) and not p[j:] in productsPandigital):

                    productsPandigital.append([p[:i], p[i:j], p[j:]])
                    print productsPandigital
               
    print productsPandigital

    # Get the interesting result
    print "Sum of products:"
    print sum(productsPandigital)

main()
