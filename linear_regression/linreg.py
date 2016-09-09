'''
Created on 9 Sep 2016

@author: matt

linear regression by gradient descent.
'''

#hypothesis
def h(t0,t1,x):
    return t0+t1*x

#square cost function
def J(t0,t1,data):
    j=(1./(2.*len(data))) * sum([ (h(t0,t1,x)-y)**2 for x,y in data])
    return  j

#square cost gradient descent
def grad_desc(t0,t1,alpha,data):
    m=len(data)
    t0_=t0- alpha*(1./m)* sum([ (h(t0,t1,x)-y)     for x,y in data] )
    t1_=t1- alpha*(1./m)* sum([ (h(t0,t1,x)-y)*x   for x,y in data] )
    return t0_,t1_

def linear_regression(data,t0,t1,alpha,lim):
    '''data = [(Xi,Yi),...]'''
    j=J(t0,t1,data)
    iteration=0
    print "iteration %s t0=%s t1=%s j=%s" % (iteration,t0,t1,j)
    while True:
        iteration+=1
        
        t0,t1=grad_desc(t0,t1,alpha,data)
        j_=J(t0,t1,data)

        #TODO: Change from a step_mag<limit to number of significant digits?
        step_mag=abs(j-j_)      
        print "iteration %s t0=%s t1=%s step_mag=%s" % (iteration,t0,t1,step_mag)
        
        if step_mag<lim:
            return t0,t1
        
        j=j_
        
if __name__=='__main__':
    #should give us t0=3 t1=2  y=3+2x
    data=[(1.,5.),(2.,7.),(3.,9.)]
    
    t0,t1=linear_regression(data,2.,3.,0.05,1e-9)
    
    print "linear fit to data is y=%s+%sx" % (t0,t1)
    
    
    
    
    
