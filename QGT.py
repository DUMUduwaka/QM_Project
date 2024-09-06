import  numpy as np 
import matplotlib.pyplot as plt 

alpha_R = 5
B0 = 25


def N_function(x):
    return 1 / np.sqrt(2 * (1 + x**2 - x * np.sqrt(1 + x**2)))

def delta_function(x):
    return x * (x - np.sqrt(1 + x**2))

def g_kxkx(kx, ky):
    k = np.sqrt(kx**2 + ky**2)
    x = B0 / (alpha_R * k)
    delta = delta_function(x)
    N = N_function(x)
    return (4 * alpha_R**2 * N**4) / (k**2 * (alpha_R**2 * k**2 + B0**2)) * (ky**2 + 2 * ky**2 * delta + k**2 * delta**2)

def g_kyky(kx, ky):
    k = np.sqrt(kx**2 + ky**2)
    x = B0 / (alpha_R * k)
    delta = delta_function(x)
    N = N_function(x)
    return (4 * alpha_R**2 * N**4) / (k**2 * (alpha_R**2 * k**2 + B0**2)) * (kx**2 + 2 * kx**2 * delta + k**2 * delta**2)

def g_kxky(kx, ky):
    k = np.sqrt(kx**2 + ky**2)
    x = B0 / (alpha_R * k)
    delta = delta_function(x)
    N = N_function(x)
    return (-4 * alpha_R**2 * N**4) / (k**2 * (alpha_R**2 * k**2 + B0**2)) * (ky * kx * (1 + 2 * delta))

def O_kxky(kx, ky):
    k = np.sqrt(kx**2 + ky**2)
    x = B0 / (alpha_R * k)
    delta = delta_function(x)
    N = N_function(x)
    return (8 * alpha_R**2 * N**4 * (delta**2 + delta))/ (alpha_R**2 * k**2 + B0**2)

#)



a = 10
# Create a grid of kx and ky values
kx = np.linspace(-a, a, 100)
ky = np.linspace(-a, a, 100)
kx, ky = np.meshgrid(kx, ky)

# Calculate the values of g(k_x, k_x), g(k_y, k_y), and g(k_x, k_y)
g_kxkx_values = g_kxkx(kx, ky)
g_kyky_values = g_kyky(kx, ky)
g_kykx_values = g_kxky(kx, ky)
O_kxky_values = O_kxky(kx, ky)

# Plot g(k_x, k_x)
plt.figure(figsize=(8, 6))
#plt.subplot(1, 3, 1)
plt.contourf(kx, ky, g_kxkx_values, cmap='viridis')
plt.colorbar()
plt.title(r'$g_{k_xk_x}$',fontsize = 18)
plt.xlabel(r'$k_x$',fontsize = 18)
plt.ylabel(r'$k_y$',fontsize = 18)
plt.show()

# Plot g(k_y, k_y)
#plt.subplot(1, 3, 2)
plt.figure(figsize=(8, 6))
plt.contourf(kx, ky, g_kyky_values, cmap='viridis')
plt.colorbar()
plt.title(r'$g_{k_yk_y}$',fontsize = 18)
plt.xlabel(r'$k_x$',fontsize = 18)
plt.ylabel(r'$k_y$',fontsize = 18)
plt.show()
# Plot g(k_x, k_y)
#plt.subplot(1, 3, 3)
plt.figure(figsize=(8, 6))
plt.contourf(kx, ky, g_kykx_values, cmap='viridis')
plt.colorbar()
plt.title(r'$g_{k_xk_y}$',fontsize = 18)
plt.xlabel(r'$k_x$',fontsize = 18)
plt.ylabel(r'$k_y$',fontsize = 18)
plt.show()

plt.figure(figsize=(8, 6))
plt.contourf(kx, ky, O_kxky_values, cmap='viridis')
plt.colorbar()
plt.title(r'${\Omega}_{k_xk_y}$',fontsize = 18)
plt.xlabel(r'$k_x$',fontsize = 18)
plt.ylabel(r'$k_y$',fontsize = 18)
plt.show()


# Create separate 3D surface plots for each function
fig1 = plt.figure(figsize=(10, 6))
ax1 = fig1.add_subplot(111, projection='3d')
ax1.plot_surface(kx, ky, g_kxkx_values, cmap='viridis')
ax1.set_title(r'$g_{k_xk_x}$',fontsize = 18)
ax1.set_xlabel(r'$k_x$',fontsize = 18)
ax1.set_ylabel(r'$k_y$',fontsize = 18)
ax1.set_zlabel(r'$g_{k_xk_x}$',fontsize = 18)
plt.show()

fig2 = plt.figure(figsize=(8, 6))
ax2 = fig2.add_subplot(111, projection='3d')
ax2.plot_surface(kx, ky, g_kyky_values, cmap='viridis')
ax2.set_title(r'$g_{k_yk_y}$',fontsize = 18)
ax2.set_xlabel(r'$k_x$',fontsize = 18)
ax2.set_ylabel(r'$k_y$',fontsize = 18)
ax2.set_zlabel(r'$g_{k_yk_y}$',fontsize = 18)
plt.show()

fig3 = plt.figure(figsize=(8, 6))
ax3 = fig3.add_subplot(111, projection='3d')
ax3.plot_surface(kx, ky, g_kykx_values, cmap='viridis')
ax3.set_title(r'$g_{k_xk_y}$',fontsize = 18)
ax3.set_xlabel(r'$k_x$',fontsize = 18)
ax3.set_ylabel(r'$k_y$',fontsize = 18)
ax3.set_zlabel(r'$g_{k_xk_y}$',fontsize = 18)
plt.show()

fig4 = plt.figure(figsize=(8, 6))
ax4 = fig4.add_subplot(111, projection='3d')
ax4.plot_surface(kx, ky,O_kxky_values , cmap='viridis')
ax4.set_title(r'${\Omega}_{k_xk_y}$',fontsize = 18)
ax4.set_xlabel(r'$k_x$',fontsize = 18)
ax4.set_ylabel(r'$k_y$',fontsize = 18)
ax4.set_zlabel(r'${\Omega}_{k_xk_y}$',fontsize = 18)
plt.show()