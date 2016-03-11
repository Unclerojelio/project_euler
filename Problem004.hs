-- file: Project_Euler/Problem004.hs

palindrome = maximum[ x*y | x <- [100..999], y <- [100..999], reverse (show (x*y)) == show (x*y)]