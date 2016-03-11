-- file: Project_Euler/Problem025.hs

fib 0 = 0
fib 1 = 1
fib 2 = 1
fib n = fib (n-1) + fib (n-2)

fibs = 0 : 1 : zipWith (+) fibs (tail fibs)

fibs2n n = [x| x <- fibs, x <= n]

countDigits n | n < 10 = 1
              | otherwise = 1 + countDigits(n `div` 10)
              
countFibs = [countDigits x | x <- fibs]
              
answer = zip countFibs [0..]