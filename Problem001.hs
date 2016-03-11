-- file: Project_Euler/Problem001.hs

sumMults35 :: (Enum a, Eq a, Num a, Integral a) => a -> a
sumMults35 n = sum[x | x <- [1..n-1], x `mod` 3 == 0 || x `mod` 5 == 0]