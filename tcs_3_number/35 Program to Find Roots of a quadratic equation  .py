
import cmath

def roots(a, b, c):
    d = b * b - 4 * a * c
    sqrt_val = cmath.sqrt(abs(d))

    if d > 0:
        print("Roots are real and different")
        root1 = (-b + sqrt_val) / (2 * a)
        root2 = (-b - sqrt_val) / (2 * a)
        print(root1)
        print(root2)
    elif d == 0:
        print("Roots are real and same")
        root1 = -b / (2 * a)
        root2 = -b / (2 * a)
        print(root1)
        print(root2)
    else:  # d < 0
        print("Roots are complex")
        root1 = -b / (2 * a) + sqrt_val * 1j
        root2 = -b / (2 * a) - sqrt_val * 1j
        print(root1)
        print(root2)

if __name__ == "__main__":
    a, b, c = 1, -3, -10
    roots(a, b, c)


