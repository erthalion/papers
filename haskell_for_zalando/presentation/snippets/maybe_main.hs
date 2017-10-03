main = do
    print $ return 1 >>= calculation1 >>= calculation2
    print $ return 1 >>= calculation1 >>= calculation3
