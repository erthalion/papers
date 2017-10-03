#! /usr/bin/env stack
-- stack runghc

calculation1 :: Int -> Maybe Int
calculation1 arg = Just (arg + 1)

calculation2 :: Int -> Maybe Int
calculation2 arg = Nothing

calculation3 :: Int -> Maybe Int
calculation3 arg = Just (arg + 2)

main = do
    print $ return 1 >>= calculation1 >>= calculation2
    print $ return 1 >>= calculation1 >>= calculation3
