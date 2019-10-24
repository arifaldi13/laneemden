import matplotlib.pyplot as plt

n = 1

phi0   = 0
theta0 = 1
xi0    = 0
dxi    = 0.1
ximax  = 10

def dtheta_dxi(phi,xi):
    if xi != 0:
        y = -phi/(xi**2)
    else:
        y = 0
    return(y)

def dphi_dxi(theta,xi,n):
    y = (theta**n)*(xi**2)
    return(y)

def laneemden(xi0,phi0,theta0,dxi,ximax,n):
    xix    = xi0
    thetax = theta0
    phix   = phi0
    xi     = [xi0]
    theta  = [theta0]
    phi    = [phi0]
    i      = 0
    while xix <= ximax:
        dtheta = dtheta_dxi(phi[i],xi[i]  )*dxi
        dphi   = dphi_dxi(theta[i],xi[i],n)*dxi
        xix  += dxi
        thetax+= dtheta
        phix  += dphi
        i     += 1
        xi   .append(xix)
        theta.append(thetax)
        phi  .append(phix)
    return(xi,theta)

xin  = laneemden(xi0,phi0,theta0,dxi,ximax,n)[0]
then = laneemden(xi0,phi0,theta0,dxi,ximax,n)[1]

plt.figure(figsize=(7,7))
plt.plot(xin,then,"k-",lw=0.7)
plt.legend()
plt.xlim(0,10)
plt.ylim(-0.5,1)
plt.xlabel(r"$\xi$",size=15)
plt.ylabel(r"$\theta$",size=15)
plt.xticks(ticks=[2,4,6,8],size=12)
plt.yticks(ticks=[-0.5,0,0.5,1],size=12)
plt.show()
