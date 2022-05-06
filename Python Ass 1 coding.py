dolocount=float(input("Enter number of dolomite cores:"))
shalecount=float(input("Enter number of shale cores:"))

dololoc=float(input("Enter number for dolomite mean:"))
doloscale=float(input("Enter number for dodomite standard deviation:"))

shaleloc=float(input("Enter number for shale mean:"))
shalescale=float(input("Enter number for shale standard deviation:"))

doloshalecount=dolocount + shalecount

p_dolo=dolocount/doloshalecount

p_shale=shalecount/doloshalecount

#
import scipy.stats
p_gamma_d=1-scipy.stats.norm(loc=dololoc,scale=doloscale).cdf(60)
p_gamma_s=1-scipy.stats.norm(loc=shaleloc,scale=shalescale).cdf(60)

p_gamma_d_60=((p_dolo)*(p_gamma_d))/((p_dolo*p_gamma_d)+(p_shale*p_gamma_s))

if p_gamma_d_60>0.5:
    print("This is a dolomite interval")
else:
    print("This interval is a Shale")
