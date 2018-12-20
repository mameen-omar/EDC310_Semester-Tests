import numpy as np

L = 2
n = 4
c = [0.75, -0.24]
# Generate Source Symbols
S = np.array([1, -1, -1, 1])
print("S:")
print(S)

def dftmtx(n):
    return np.fft.fft(np.identity(n))


F = dftmtx(n)/n #normalize the kaka
print("DFT, F:")
print(F)

iF = np.conjugate(F)
iF = np.transpose(iF)
print("Complex Conjugate Transpose Matrix, iF:")
print(iF)



# IFFT of Source Symbols
s = np.matmul(iF,S)
print("IFFT of Source Symbols, s:")

print("s :")
print(s)

# Add cyclic prefix
s_ = np.append(s[-(L-1):], s)
print("s_ :")
print(s_) # triangle

# Create channel matrix

C_ = np.array([[0.75,   0,      0,      0,      0],  # Circulant Matrix - SAME DIMERNSIONS AS S_ THE SHIT WE MULTIPLY BY
              [ -0.24,  0.75,   0,      0,      0],
              [ 0,      -0.24,  0.75,   0,      0],
              [ 0,      0,      -0.24,  0.75,   0],
              [ 0,      0,      0,      -0.24,  0.75]])


# Receive Symbol Vector
r_ = np.matmul(C_,s_)


# Remove Cyclic Prefix
r_ = r_[L-1:]
print("r_ :")
print(r_)

# FFT of Received Symbol Vector
R_ = np.matmul(F,r_)

print("R_ :")
print(R_)

# Calculate Dell (Eigenvalues of CIR)
D = np.matmul(F,np.append(c,np.zeros(n-L)))
#D = D.A1
print("D :")
print(D)

# Determine estimate of S
S_Est = R_/D   
#S_Est = S_Est.A1
print("S_Est :")
print(S_Est)



