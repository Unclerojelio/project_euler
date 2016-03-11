-- file: Project_Euler/Problem039.hs

import Data.List
import Data.Function

triangles = [(x+y+z,(x,y,z)) | x <- [1..258], y <- [x..344], z <- [y..430], x^2 + y^2 == z^2]

sorted = sortBy (compare `on` fst) triangles
