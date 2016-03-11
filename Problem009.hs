-- file: Project_Euler/Problem009.hs

pythTriplet = [x*y*z | x <- [1..500], y <- [x..500], z <- [y..500], x^2+y^2 == z^2 && x+y+z == 1000]