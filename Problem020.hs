-- file: Project_Euler/Problem020.hs

fact 0 = 1
fact n = n * fact (n-1)

sumDigits n | n < 10    = n
            | otherwise = (n `mod` 10) + sumDigits (n `div` 10)
            
answer n = sumDigits(fact n) 