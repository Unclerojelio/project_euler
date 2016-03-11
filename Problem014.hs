-- file: /Project_Euler/Problem014.hs

import Data.List
import Data.Ord
import Data.Function

collatz a 1  = a
collatz a x
  | even x    = collatz (a + 1) (x `div` 2)
  | otherwise = collatz (a + 1) (3 * x + 1)
  
max' :: (Num a,Ord a) => [(a,a)] -> (a,a)
max' [] = (0,0)
max' [x] = x
max' (x:xs)
	| (fst x) > fst(max' xs) = x
	| otherwise = max' xs
  
--answer = max'[(collatz 1 x, x)| x <- [1..30]]

--answer = maximumBy (compare `on` fst) [(collatz 1 x, x)| x <- [1..100]]

main = print (maximumBy (compare `on` fst) [(collatz 1 x, x)| x <- [1..1000000]])