account :: Currency USD
account = Currency 5.0

transaction1 :: Currency USD
transaction1 = Currency 5.0

transaction2 :: Currency EUR
transaction2 = Currency 5.0

main = do
    print $ add account transaction1 -- Currency 10.0
    print $ add account transaction2 -- won't compile
