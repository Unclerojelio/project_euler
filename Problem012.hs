-- file: Project_Euler/Problem012.hs

triangleNum n = sum[x | x <- [1..n]]

triangleList m = [triangleNum x | x <- [1..m]]

triangleFactors m = [(x,length(factorList'' x)) | x <- (triangleList m)]

triangleTarget m = [(a,b) | (a,b) <- (triangleFactors m), b > 500]


isFactorOf :: Integral a => a -> a -> Bool
isFactorOf x n = n `mod` x == 0

factorList'' n = [ x | x <- [1 .. n], x `isFactorOf` n]