-- file: Project_Euler/Problem005.hs

answer = [x | x <- [923780..], x `mod` 11 == 0 &&
                               x `mod` 12 == 0 &&
                               x `mod` 13 == 0 &&
                               x `mod` 14 == 0 &&
                               x `mod` 15 == 0 &&
                               x `mod` 16 == 0 &&
                               x `mod` 17 == 0 &&
                               x `mod` 18 == 0 &&
                               x `mod` 19 == 0 &&
                               x `mod` 20 == 0]
                          