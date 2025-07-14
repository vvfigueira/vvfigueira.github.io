from numpy import arange, float32

def g(t,y,z):

    g = float32(12*t**2 + 4*t**3 - t**4 + y - z)

    return g

def RK4(t,y,z,h):

    k1y = float32(h*z)
    k1z = float32(h*g(t,y,z))
    k2y = float32(h*(z+0.5*k1z))
    k2z = float32(h*g(t+0.5*h,y+0.5*k1y,z+0.5*k1z))
    k3y = float32(h*(z+0.5*k2z))
    k3z = float32(h*g(t+0.5*h,y+0.5*k2y,z+0.5*k2z))
    k4y = float32(h*(z+k3z))
    k4z = float32(h*g(t+h,y+k3y,z+k3z))

    passo_y = float32((k1y+2*(k2y+k3y)+k4y)/6)
    passo_z = float32((k1z+2*(k2z+k3z)+k4z)/6)

    return passo_y, passo_z

h = float32(0.01)

y0 = 0
z0 = 0

y = y0
z = z0

for t in float32(arange(0,5,h)):

    #t = float32(t)

    passo_y, passo_z = float32(RK4(t,y,z,h))

    y = float32(y + passo_y)
    z = float32(z + passo_z)

    if t >= 4.98:

        print("y(5) = %f, z(5) = %f, t = %f" %(y,z,t))
