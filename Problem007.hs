-- file: Project_Euler/Problem007.hs

import Data.List.minus

primesTo m = eratos [2..m]  where        -- bounded, up to m
   eratos []     = []
   eratos (p:xs) = p : eratos (xs `minus` [p,p+p..])