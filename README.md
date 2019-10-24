# Lane-Emden Equation Plotter
### 1. Simplification of Equations
The Lane-Emden equation can be written as\
\
<a href="https://www.codecogs.com/eqnedit.php?latex=\frac{1}{\xi^{2}}&space;\frac{d}{d\xi}&space;\left&space;(&space;\xi^{2}\frac{d\theta}{d\xi}&space;\right&space;)&space;&plus;&space;\theta^{n}&space;=&space;0" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\frac{1}{\xi^{2}}&space;\frac{d}{d\xi}&space;\left&space;(&space;\xi^{2}\frac{d\theta}{d\xi}&space;\right&space;)&space;&plus;&space;\theta^{n}&space;=&space;0" title="\frac{1}{\xi^{2}} \frac{d}{d\xi} \left ( \xi^{2}\frac{d\theta}{d\xi} \right ) + \theta^{n} = 0" /></a>
\
where <a href="https://www.codecogs.com/eqnedit.php?latex=\xi" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\xi" title="\xi" /></a> is the radius without dimensions and <a href="https://www.codecogs.com/eqnedit.php?latex=\theta" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\theta" title="\theta" /></a> is related to density.
\
The equation above can be simplified into two equations
\
<a href="https://www.codecogs.com/eqnedit.php?latex=\frac{d\theta}{d\xi}=-\frac{\varphi}{\xi^{2}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\frac{d\theta}{d\xi}=-\frac{\varphi}{\xi^{2}}" title="\frac{d\theta}{d\xi}=-\frac{\varphi}{\xi^{2}}" /></a>
\
<a href="https://www.codecogs.com/eqnedit.php?latex=\frac{d\varphi}{d\xi}=\theta^{n}\xi^{2}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\frac{d\varphi}{d\xi}=\theta^{n}\xi^{2}" title="\frac{d\varphi}{d\xi}=\theta^{n}\xi^{2}" /></a>
\
where <a href="https://www.codecogs.com/eqnedit.php?latex=\varphi" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\varphi" title="\varphi" /></a> is defined as <a href="https://www.codecogs.com/eqnedit.php?latex=-\xi^{2}\frac{d\theta}{d\xi}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?-\xi^{2}\frac{d\theta}{d\xi}" title="-\xi^{2}\frac{d\theta}{d\xi}" /></a>.
This simplification can be used to get the value of <a href="https://www.codecogs.com/eqnedit.php?latex=\theta" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\theta" title="\theta" /></a> on every <a href="https://www.codecogs.com/eqnedit.php?latex=\xi" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\xi" title="\xi" /></a> for a certain value of <a href="https://www.codecogs.com/eqnedit.php?latex=n" target="_blank"><img src="https://latex.codecogs.com/gif.latex?n" title="n" /></a>.
The boundary conditions used for the upper equation are <a href="https://www.codecogs.com/eqnedit.php?latex=\theta&space;\left&space;(&space;0&space;\right&space;)&space;=1" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\theta&space;\left&space;(&space;0&space;\right&space;)&space;=1" title="\theta \left ( 0 \right ) =1" /></a> and for the lower equation is <a href="https://www.codecogs.com/eqnedit.php?latex=\varphi&space;\left&space;(&space;0&space;\right&space;)&space;=0" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\varphi&space;\left&space;(&space;0&space;\right&space;)&space;=0" title="\varphi \left ( 0 \right ) =0" /></a>.

### 2. Equation Solution Approach
The range of steps taken on <a href="https://www.codecogs.com/eqnedit.php?latex=\xi" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\xi" title="\xi" /></a> to solve the differential equation.
The narrower range, the better resolution of the equation's solution. For the current case, take a range of 0.1 for the value of <a href="https://www.codecogs.com/eqnedit.php?latex=\xi" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\xi" title="\xi" /></a> from 0 to 10.
This value is an approach to the infinitesimal form of <a href="https://www.codecogs.com/eqnedit.php?latex=d\xi" target="_blank"><img src="https://latex.codecogs.com/gif.latex?d\xi" title="d\xi" /></a>.
Thus from the two simple equations in part 1, <a href="https://www.codecogs.com/eqnedit.php?latex=\theta" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\theta" title="\theta" /></a> can be obtained.
To get every value of <a href="https://www.codecogs.com/eqnedit.php?latex=\theta" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\theta" title="\theta" /></a> for every value of <a href="https://www.codecogs.com/eqnedit.php?latex=\xi" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\xi" title="\xi" /></a>, iterates two simple equations. Thus, the solution of <a href="https://www.codecogs.com/eqnedit.php?latex=\theta" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\theta" title="\theta" /></a> can be obtained.

### 3. Implemented on Python 3
At this time Python 3 is used to do iterations, as mentioned in section 2, and make plot <a href="https://www.codecogs.com/eqnedit.php?latex=\xi" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\xi" title="\xi" /></a> against <a href="https://www.codecogs.com/eqnedit.php?latex=\theta" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\theta" title="\theta" /></a>.
