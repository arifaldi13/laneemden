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

#xin0  = laneemden(xi0,phi0,theta0,dxi,ximax,0)[0]
#xin1  = laneemden(xi0,phi0,theta0,dxi,ximax,1)[0]
#xin2  = laneemden(xi0,phi0,theta0,dxi,ximax,2)[0]
#xin3  = laneemden(xi0,phi0,theta0,dxi,ximax,3)[0]
#xin4  = laneemden(xi0,phi0,theta0,dxi,ximax,4)[0]
#xin5  = laneemden(xi0,phi0,theta0,dxi,ximax,5)[0]
#then0 = laneemden(xi0,phi0,theta0,dxi,ximax,0)[1]
#then1 = laneemden(xi0,phi0,theta0,dxi,ximax,1)[1]
#then2 = laneemden(xi0,phi0,theta0,dxi,ximax,2)[1]
#then3 = laneemden(xi0,phi0,theta0,dxi,ximax,3)[1]
#then4 = laneemden(xi0,phi0,theta0,dxi,ximax,4)[1]
#then5 = laneemden(xi0,phi0,theta0,dxi,ximax,5)[1]
xin  = laneemden(xi0,phi0,theta0,dxi,ximax,n)[0]
then = laneemden(xi0,phi0,theta0,dxi,ximax,n)[1]

plt.figure(figsize=(7,7))
#plt.plot(xin0,then0,"r-",lw=0.7,label="n = 0")
#plt.plot(xin1,then1,"g-",lw=0.7,label="n = 1")
#plt.plot(xin2,then2,"b-",lw=0.7,label="n = 2")
#plt.plot(xin3,then3,"c-",lw=0.7,label="n = 3")
#plt.plot(xin4,then4,"m-",lw=0.7,label="n = 4")
#plt.plot(xin5,then5,"y-",lw=0.7,label="n = 5")
plt.plot(xin,then,"k-",lw=0.7)
plt.legend()
plt.xlim(0,10)
plt.ylim(-0.5,1)
plt.xlabel(r"$\xi$",size=15)
plt.ylabel(r"$\theta$",size=15)
plt.xticks(ticks=[2,4,6,8],size=12)
plt.yticks(ticks=[-0.5,0,0.5,1],size=12)
#plt.savefig("plot",dpi=300)
plt.show()