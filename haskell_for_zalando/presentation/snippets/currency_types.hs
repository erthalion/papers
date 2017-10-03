data USD
data EUR

newtype Currency a = Currency Double deriving Show

add :: Currency a -> Currency a -> Currency a
add (Currency a) (Currency b) = Currency $ a + b
