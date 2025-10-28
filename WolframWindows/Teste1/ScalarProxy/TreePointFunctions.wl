Tree3Point[momenta1_, momenta2_, momenta3_] := 
    I*g*(m^2 - mp[momenta1, momenta1] - mp[momenta2, momenta2] - 
      mp[momenta3, momenta3])
 
m[___] := m
 
Tree4Point[momenta1_, momenta2_, momenta3_, momenta4_] := 
    (-I)*g^2*(3 - ((-m^2 + 2*mp[momenta2, momenta2] + 
         2*mp[momenta2, momenta3] + 2*mp[momenta3, momenta3])*
        (-m^2 + mp[momenta1, momenta1] + mp[momenta2, momenta2] + 
         2*mp[momenta2, momenta3] + mp[momenta3, momenta3] + 
         mp[momenta4, momenta4]))/((mp[momenta2, momenta2] + 
         2*mp[momenta2, momenta3] + mp[momenta3, momenta3])*
        (-m^2 + mp[momenta2, momenta2] + 2*mp[momenta2, momenta3] + 
         mp[momenta3, momenta3])) - 
      ((-m^2 + mp[momenta1, momenta1] + mp[momenta2, momenta2] + 
         2*mp[momenta2, momenta4] + mp[momenta3, momenta3] + 
         mp[momenta4, momenta4])*(-m^2 + 2*mp[momenta2, momenta2] + 
         2*mp[momenta2, momenta4] + 2*mp[momenta4, momenta4]))/
       ((mp[momenta2, momenta2] + 2*mp[momenta2, momenta4] + 
         mp[momenta4, momenta4])*(-m^2 + mp[momenta2, momenta2] + 
         2*mp[momenta2, momenta4] + mp[momenta4, momenta4])) - 
      ((-m^2 + mp[momenta1, momenta1] + mp[momenta2, momenta2] + 
         mp[momenta3, momenta3] + 2*mp[momenta3, momenta4] + 
         mp[momenta4, momenta4])*(-m^2 + 2*mp[momenta3, momenta3] + 
         2*mp[momenta3, momenta4] + 2*mp[momenta4, momenta4]))/
       ((mp[momenta3, momenta3] + 2*mp[momenta3, momenta4] + 
         mp[momenta4, momenta4])*(-m^2 + mp[momenta3, momenta3] + 
         2*mp[momenta3, momenta4] + mp[momenta4, momenta4])))
