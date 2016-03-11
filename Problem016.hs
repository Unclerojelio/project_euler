-- file: Project_Euler/Problem016.hs

import Data.Char

sumNum = sum[ord x - ord '0'| x<- (show $ 2^1000)]
