-- This is a working solution
{-
 - sumOfSquare :: [Integer] -> Integer
 - sumOfSquare xs = sum (map (^ 2) xs)
 - 
 - squareOfSum :: [Integer] -> Integer
 - squareOfSum xs =  ( sum xs ) ^ 2
 - 
 - diff :: [Integer] -> Integer
 - diff xs = squareOfSum xs - sumOfSquare xs
 - 
 - getResult :: Integer
 - getResult = diff [1..100]
 - 
 - main = do
 -     print (getResult)
 -}

-- This is the same as a one liner
getResult :: Integer
getResult = (sum [1..100])^2 - sum (map (^2) [1..100])

