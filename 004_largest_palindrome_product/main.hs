import Data.List

-- Script to be compiled with
--      ghc -o main main.hs
--
-- Result of
--      time ./main 
-- 1,35s

-- palindrome and reversal both come from https://stackoverflow.com/a/26316718/4194289
palindrome :: Integer -> Bool
palindrome x = reversal x == x

reversal :: Integral a => a -> a
reversal = go 0
  where go a 0 = a
        go a b = let (q,r) = b `quotRem` 10 in go (a*10 + r) q

-- Given two lists get the product of each item of the first list
-- with all items of the second one (terribly inefficient)
getProducts :: [Integer] -> [Integer] -> [Integer]
getProducts [] a = []
getProducts a [] = []
getProducts (x:xs) b = map (* x) b ++ getProducts xs b

-- Given a list of integer only get the ones which are palindroms
getPalindroms :: [Integer] -> [Integer]
getPalindroms a = filter (palindrome) a

-- Given a list of integers get the largest one
getBiggestItem :: [Integer] -> Integer
getBiggestItem a = last (sort a)

-- Put all together to get a result
-- The function takes the list of all three digits numbers
getResult :: [Integer] -> Integer
getResult a = getBiggestItem (getPalindroms (getProducts a a ) )

-- Actual call
main = do
    print (getResult [100..999])
