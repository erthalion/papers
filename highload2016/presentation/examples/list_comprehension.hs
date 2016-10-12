-- list comprehension in haskell
[getAttr v | v <- source, condition v]

-- function chain in haskell
reverse . take 5 $ [0..]
