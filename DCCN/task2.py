import numpy as np
import PS2_tests

def mod2(A):
    for i in range(2):
        A[A%2==i] = i
    return A

def equal(a, b):
    if (a == b).all():
        return True
    return False

def syndrome_decode(codeword, n, k, G):
    A = G[:, k:n]
    I = np.identity(n-k, dtype=int)
    H = np.concatenate((A.T, I), axis = 1)
    
    c_decoded = mod2(np.dot(H, codeword.T))
    zeros = not np.any(c_decoded)
    if zeros:
        return codeword[:k]
    for i in range(k):
        P = np.zeros((n,), dtype=int)
        P[i] = 1
        syndrome = np.dot(H, P.T)
        if equal(syndrome, c_decoded):
            codeword[i] = int(not codeword[i])
            break

    return codeword[:k]

# if __name__ == '__main__':
#     # (7,4,3) Hamming code
#     G1 = np.array([[1, 0, 0, 0, 1, 1, 0], [0, 1, 0, 0, 1, 0, 1], [0, 0, 1, 0, 0, 1, 1], [0, 0, 0, 1, 1, 1, 1]], 
#                 dtype=int)
#     PS2_tests.test_linear_sec(syndrome_decode, 7, 4, G1)

#     # (8,4,3) rectangular parity code
#     G2 = np.array([[1, 0, 0, 0, 1, 0, 1, 0], [0, 1, 0, 0, 1, 0, 0, 1], [0, 0, 1, 0, 0, 1, 1, 0], [0, 0, 0, 1, 0, 1, 0, 1]], dtype=int)
#     PS2_tests.test_linear_sec(syndrome_decode, 8, 4, G2)

#      # (6,3,3) pairwise parity code
#     G3 = np.array([[1, 0, 0, 1, 1, 0],[0, 1, 0, 0, 1, 1], [0, 0, 1, 1, 0, 1]], dtype=int)
#     PS2_tests.test_linear_sec(syndrome_decode, 6, 3, G3)
    
#     # (15,11,3) Hamming code
#     # G4 = np.array([[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0 0 1 0 1 1; 0 0 1 0 0 0 0 0 0 0 0 1 1 0 1; 0 0 0 1 0 0 0 0 0 0 0 1 1 1 0; 0 0 0 0 1 0 0 0 0 0 0 1 1 1 1; 0 0 0 0 0 1 0 0 0 0 0 1 1 0 0; 0 0 0 0 0 0 1 0 0 0 0 1 0 1 0; 0 0 0 0 0 0 0 1 0 0 0 1 0 0 1; 0 0 0 0 0 0 0 0 1 0 0 0 1 1 0; 0 0 0 0 0 0 0 0 0 1 0 0 1 0 1; 0 0 0 0 0 0 0 0 0 0 1 0 0 1 1')
#     # PS2_tests.test_linear_sec(syndrome_decode, 15, 11, G4)

if __name__ == "__main__":
    n=7
    k=4
    G = np.array([1,0,0,0,1,1,0,
                  0,1,0,0,1,0,1,
                  0,0,1,0,0,1,1,
                  0,0,0,1,1,1,1
                 ]).reshape(k,n)
    print("Generator Matrix:")
    print(G)
    codeword = np.array([1,1,1,0,1,0,1])
    print("Received message:")
    print(codeword[:k].tolist())
    message = syndrome_decode(codeword, n, k, G)
    print("Corrected message:")  
    print(message.tolist())