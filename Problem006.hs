-- file: Project_Euler/Problem006.hs

sumSquares n = sum[x^2|x <-[1..n]]

squareSum n = x^2 where x = sum[x|x <- [1..n]]

diffSquares n = squareSum n - sumSquares n