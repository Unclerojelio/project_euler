-- file: Project_Euler/Problem002.hs

fibs = 0 : 1 : zipWith (+) fibs (tail fibs)

showFibs n = take n fibs

sumEvenFibs :: Int -> Int
sumEvenFibs n = sum[x | x <- take n fibs, x `mod` 2 == 0]

main = putStrLn(show(sumEvenFibs 10))