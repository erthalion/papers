main = do
    print $ pure 1 >>= calculation1 >>= calculation2
    print $ pure 1 >>= calculation1 >>= calculation3
