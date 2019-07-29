-- This solution works with the example but it seems way too long for the actual problem
{-
 - isEvenlyDivisible :: Integer -> Bool
 - isEvenlyDivisible a = length (filter (/= 0) ( map (mod a) [1..20] )) == 0
 -
 - getResult :: Integer
 - getResult = head (filter (isEvenlyDivisible) [2520,1..])
 -}


-- This solution gets the right result in 111s
{-
 - _isEvenlyDivisible :: Integer -> [Integer] -> Bool
 - _isEvenlyDivisible a b =
 -     if length b > 1 then
 -         if mod a (head b) /= 0 then False
 -         else _isEvenlyDivisible a (drop 1 b)
 -     else
 -         True
 - 
 - isEvenlyDivisible :: Integer -> Bool
 - isEvenlyDivisible a = _isEvenlyDivisible a (reverse [1..20])
 - 
 - getResult :: Integer
 - getResult = head (filter (isEvenlyDivisible) [1..])
 -}

-- This solution gets the result in 29s
{-
 - _isEvenlyDivisible :: Integer -> Integer -> Bool
 - _isEvenlyDivisible a b =
 -     if b <= 20 then
 -         if mod a b /= 0 then False
 -         else _isEvenlyDivisible a (b + 1)
 -     else
 -         True
 - 
 - isEvenlyDivisible :: Integer -> Bool
 - isEvenlyDivisible a = _isEvenlyDivisible a 2
 - 
 - getResult :: Integer
 - getResult = head (filter (isEvenlyDivisible) [1..])
 -}

-- And this solution gets the result in 2.8s
_isEvenlyDivisible :: Integer -> Integer -> Bool
_isEvenlyDivisible a b =
    if b <= 20 then
        if mod a b /= 0 then False
        else _isEvenlyDivisible a (b + 1)
    else
        True

isEvenlyDivisible :: Integer -> Bool
isEvenlyDivisible a = _isEvenlyDivisible a 2

getResult :: Integer
getResult = head (filter (isEvenlyDivisible) (map (* 20) [1..] ))

main = do
    print (getResult)
