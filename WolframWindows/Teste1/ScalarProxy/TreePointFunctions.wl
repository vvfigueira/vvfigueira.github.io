Tree3Point[momenta1_, momenta2_, momenta3_] := 
    I*g*(m^2 - mp[momenta1, momenta1] - mp[momenta2, momenta2] - 
      mp[momenta3, momenta3])
 
m[___] := m
 
Tree4Point[momenta1_, momenta2_, momenta3_, momenta4_] := 
    (-I)*g^2*(3 - (-m^2 + 2*mp[momenta2, momenta2] + 
        2*mp[momenta2, momenta3] + 2*mp[momenta3, momenta3])*
       ((-m^2 + mp[momenta1, momenta1] + mp[momenta2, momenta2] + 
         2*mp[momenta2, momenta3] + mp[momenta3, momenta3] + 
         mp[momenta4, momenta4])/((mp[momenta2, momenta2] + 
          2*mp[momenta2, momenta3] + mp[momenta3, momenta3])*
         (-m^2 + mp[momenta2, momenta2] + 2*mp[momenta2, momenta3] + 
          mp[momenta3, momenta3]))) - (-m^2 + mp[momenta1, momenta1] + 
        mp[momenta2, momenta2] + 2*mp[momenta2, momenta4] + 
        mp[momenta3, momenta3] + mp[momenta4, momenta4])*
       ((-m^2 + 2*mp[momenta2, momenta2] + 2*mp[momenta2, momenta4] + 
         2*mp[momenta4, momenta4])/((mp[momenta2, momenta2] + 
          2*mp[momenta2, momenta4] + mp[momenta4, momenta4])*
         (-m^2 + mp[momenta2, momenta2] + 2*mp[momenta2, momenta4] + 
          mp[momenta4, momenta4]))) - (-m^2 + mp[momenta1, momenta1] + 
        mp[momenta2, momenta2] + mp[momenta3, momenta3] + 
        2*mp[momenta3, momenta4] + mp[momenta4, momenta4])*
       ((-m^2 + 2*mp[momenta3, momenta3] + 2*mp[momenta3, momenta4] + 
         2*mp[momenta4, momenta4])/((mp[momenta3, momenta3] + 
          2*mp[momenta3, momenta4] + mp[momenta4, momenta4])*
         (-m^2 + mp[momenta3, momenta3] + 2*mp[momenta3, momenta4] + 
          mp[momenta4, momenta4]))))
 
Tree5Point[momenta1_, momenta2_, momenta3_, momenta4_, momenta5_] := 
    -((3*g^2*(I*g*m^2 - I*g*mp[momenta2, momenta2] - 
         I*g*mp[momenta3, momenta3] - I*g*(mp[momenta2, momenta2] + 
           2*mp[momenta2, momenta3] + mp[momenta3, momenta3])))/
       ((mp[momenta2, momenta2] + 2*mp[momenta2, momenta3] + 
         mp[momenta3, momenta3])*(-m^2 + mp[momenta2, momenta2] + 
         2*mp[momenta2, momenta3] + mp[momenta3, momenta3]))) - 
     (3*g^2*(I*g*m^2 - I*g*mp[momenta2, momenta2] - 
        I*g*mp[momenta4, momenta4] - I*g*(mp[momenta2, momenta2] + 
          2*mp[momenta2, momenta4] + mp[momenta4, momenta4])))/
      ((mp[momenta2, momenta2] + 2*mp[momenta2, momenta4] + 
        mp[momenta4, momenta4])*(-m^2 + mp[momenta2, momenta2] + 
        2*mp[momenta2, momenta4] + mp[momenta4, momenta4])) - 
     (3*g^2*(I*g*m^2 - I*g*mp[momenta3, momenta3] - 
        I*g*mp[momenta4, momenta4] - I*g*(mp[momenta3, momenta3] + 
          2*mp[momenta3, momenta4] + mp[momenta4, momenta4])))/
      ((mp[momenta3, momenta3] + 2*mp[momenta3, momenta4] + 
        mp[momenta4, momenta4])*(-m^2 + mp[momenta3, momenta3] + 
        2*mp[momenta3, momenta4] + mp[momenta4, momenta4])) - 
     (3*g^2*(I*g*m^2 - I*g*mp[momenta1, momenta1] - 
        I*g*(mp[momenta2, momenta2] + 2*mp[momenta2, momenta3] + 
          2*mp[momenta2, momenta4] + mp[momenta3, momenta3] + 
          2*mp[momenta3, momenta4] + mp[momenta4, momenta4]) - 
        I*g*mp[momenta5, momenta5]))/((mp[momenta2, momenta2] + 
        2*mp[momenta2, momenta3] + 2*mp[momenta2, momenta4] + 
        mp[momenta3, momenta3] + 2*mp[momenta3, momenta4] + 
        mp[momenta4, momenta4])*(-m^2 + mp[momenta2, momenta2] + 
        2*mp[momenta2, momenta3] + 2*mp[momenta2, momenta4] + 
        mp[momenta3, momenta3] + 2*mp[momenta3, momenta4] + 
        mp[momenta4, momenta4])) - 
     ((I*g*m^2 - I*g*mp[momenta2, momenta2] - I*g*mp[momenta3, momenta3] - 
        I*g*(mp[momenta2, momenta2] + 2*mp[momenta2, momenta3] + 
          mp[momenta3, momenta3]))*(I*g*m^2 - I*g*(mp[momenta2, momenta2] + 
          2*mp[momenta2, momenta3] + mp[momenta3, momenta3]) - 
        I*g*mp[momenta4, momenta4] - I*g*(mp[momenta2, momenta2] + 
          2*mp[momenta2, momenta3] + 2*mp[momenta2, momenta4] + 
          mp[momenta3, momenta3] + 2*mp[momenta3, momenta4] + 
          mp[momenta4, momenta4]))*(I*g*m^2 - I*g*mp[momenta1, momenta1] - 
        I*g*(mp[momenta2, momenta2] + 2*mp[momenta2, momenta3] + 
          2*mp[momenta2, momenta4] + mp[momenta3, momenta3] + 
          2*mp[momenta3, momenta4] + mp[momenta4, momenta4]) - 
        I*g*mp[momenta5, momenta5]))/((mp[momenta2, momenta2] + 
        2*mp[momenta2, momenta3] + mp[momenta3, momenta3])*
       (-m^2 + mp[momenta2, momenta2] + 2*mp[momenta2, momenta3] + 
        mp[momenta3, momenta3])*(mp[momenta2, momenta2] + 
        2*mp[momenta2, momenta3] + 2*mp[momenta2, momenta4] + 
        mp[momenta3, momenta3] + 2*mp[momenta3, momenta4] + 
        mp[momenta4, momenta4])*(-m^2 + mp[momenta2, momenta2] + 
        2*mp[momenta2, momenta3] + 2*mp[momenta2, momenta4] + 
        mp[momenta3, momenta3] + 2*mp[momenta3, momenta4] + 
        mp[momenta4, momenta4])) - 
     ((I*g*m^2 - I*g*mp[momenta2, momenta2] - I*g*mp[momenta4, momenta4] - 
        I*g*(mp[momenta2, momenta2] + 2*mp[momenta2, momenta4] + 
          mp[momenta4, momenta4]))*(I*g*m^2 - I*g*mp[momenta3, momenta3] - 
        I*g*(mp[momenta2, momenta2] + 2*mp[momenta2, momenta4] + 
          mp[momenta4, momenta4]) - I*g*(mp[momenta2, momenta2] + 
          2*mp[momenta2, momenta3] + 2*mp[momenta2, momenta4] + 
          mp[momenta3, momenta3] + 2*mp[momenta3, momenta4] + 
          mp[momenta4, momenta4]))*(I*g*m^2 - I*g*mp[momenta1, momenta1] - 
        I*g*(mp[momenta2, momenta2] + 2*mp[momenta2, momenta3] + 
          2*mp[momenta2, momenta4] + mp[momenta3, momenta3] + 
          2*mp[momenta3, momenta4] + mp[momenta4, momenta4]) - 
        I*g*mp[momenta5, momenta5]))/((mp[momenta2, momenta2] + 
        2*mp[momenta2, momenta4] + mp[momenta4, momenta4])*
       (-m^2 + mp[momenta2, momenta2] + 2*mp[momenta2, momenta4] + 
        mp[momenta4, momenta4])*(mp[momenta2, momenta2] + 
        2*mp[momenta2, momenta3] + 2*mp[momenta2, momenta4] + 
        mp[momenta3, momenta3] + 2*mp[momenta3, momenta4] + 
        mp[momenta4, momenta4])*(-m^2 + mp[momenta2, momenta2] + 
        2*mp[momenta2, momenta3] + 2*mp[momenta2, momenta4] + 
        mp[momenta3, momenta3] + 2*mp[momenta3, momenta4] + 
        mp[momenta4, momenta4])) - 
     ((I*g*m^2 - I*g*mp[momenta3, momenta3] - I*g*mp[momenta4, momenta4] - 
        I*g*(mp[momenta3, momenta3] + 2*mp[momenta3, momenta4] + 
          mp[momenta4, momenta4]))*(I*g*m^2 - I*g*mp[momenta2, momenta2] - 
        I*g*(mp[momenta3, momenta3] + 2*mp[momenta3, momenta4] + 
          mp[momenta4, momenta4]) - I*g*(mp[momenta2, momenta2] + 
          2*mp[momenta2, momenta3] + 2*mp[momenta2, momenta4] + 
          mp[momenta3, momenta3] + 2*mp[momenta3, momenta4] + 
          mp[momenta4, momenta4]))*(I*g*m^2 - I*g*mp[momenta1, momenta1] - 
        I*g*(mp[momenta2, momenta2] + 2*mp[momenta2, momenta3] + 
          2*mp[momenta2, momenta4] + mp[momenta3, momenta3] + 
          2*mp[momenta3, momenta4] + mp[momenta4, momenta4]) - 
        I*g*mp[momenta5, momenta5]))/((mp[momenta3, momenta3] + 
        2*mp[momenta3, momenta4] + mp[momenta4, momenta4])*
       (-m^2 + mp[momenta3, momenta3] + 2*mp[momenta3, momenta4] + 
        mp[momenta4, momenta4])*(mp[momenta2, momenta2] + 
        2*mp[momenta2, momenta3] + 2*mp[momenta2, momenta4] + 
        mp[momenta3, momenta3] + 2*mp[momenta3, momenta4] + 
        mp[momenta4, momenta4])*(-m^2 + mp[momenta2, momenta2] + 
        2*mp[momenta2, momenta3] + 2*mp[momenta2, momenta4] + 
        mp[momenta3, momenta3] + 2*mp[momenta3, momenta4] + 
        mp[momenta4, momenta4])) - 
     (3*g^2*(I*g*m^2 - I*g*mp[momenta2, momenta2] - 
        I*g*mp[momenta5, momenta5] - I*g*(mp[momenta2, momenta2] + 
          2*mp[momenta2, momenta5] + mp[momenta5, momenta5])))/
      ((mp[momenta2, momenta2] + 2*mp[momenta2, momenta5] + 
        mp[momenta5, momenta5])*(-m^2 + mp[momenta2, momenta2] + 
        2*mp[momenta2, momenta5] + mp[momenta5, momenta5])) - 
     ((I*g*m^2 - I*g*mp[momenta3, momenta3] - I*g*mp[momenta4, momenta4] - 
        I*g*(mp[momenta3, momenta3] + 2*mp[momenta3, momenta4] + 
          mp[momenta4, momenta4]))*(I*g*m^2 - I*g*mp[momenta1, momenta1] - 
        I*g*(mp[momenta3, momenta3] + 2*mp[momenta3, momenta4] + 
          mp[momenta4, momenta4]) - I*g*(mp[momenta2, momenta2] + 
          2*mp[momenta2, momenta5] + mp[momenta5, momenta5]))*
       (I*g*m^2 - I*g*mp[momenta2, momenta2] - I*g*mp[momenta5, momenta5] - 
        I*g*(mp[momenta2, momenta2] + 2*mp[momenta2, momenta5] + 
          mp[momenta5, momenta5])))/((mp[momenta3, momenta3] + 
        2*mp[momenta3, momenta4] + mp[momenta4, momenta4])*
       (-m^2 + mp[momenta3, momenta3] + 2*mp[momenta3, momenta4] + 
        mp[momenta4, momenta4])*(mp[momenta2, momenta2] + 
        2*mp[momenta2, momenta5] + mp[momenta5, momenta5])*
       (-m^2 + mp[momenta2, momenta2] + 2*mp[momenta2, momenta5] + 
        mp[momenta5, momenta5])) - 
     (3*g^2*(I*g*m^2 - I*g*mp[momenta3, momenta3] - 
        I*g*mp[momenta5, momenta5] - I*g*(mp[momenta3, momenta3] + 
          2*mp[momenta3, momenta5] + mp[momenta5, momenta5])))/
      ((mp[momenta3, momenta3] + 2*mp[momenta3, momenta5] + 
        mp[momenta5, momenta5])*(-m^2 + mp[momenta3, momenta3] + 
        2*mp[momenta3, momenta5] + mp[momenta5, momenta5])) - 
     ((I*g*m^2 - I*g*mp[momenta2, momenta2] - I*g*mp[momenta4, momenta4] - 
        I*g*(mp[momenta2, momenta2] + 2*mp[momenta2, momenta4] + 
          mp[momenta4, momenta4]))*(I*g*m^2 - I*g*mp[momenta1, momenta1] - 
        I*g*(mp[momenta2, momenta2] + 2*mp[momenta2, momenta4] + 
          mp[momenta4, momenta4]) - I*g*(mp[momenta3, momenta3] + 
          2*mp[momenta3, momenta5] + mp[momenta5, momenta5]))*
       (I*g*m^2 - I*g*mp[momenta3, momenta3] - I*g*mp[momenta5, momenta5] - 
        I*g*(mp[momenta3, momenta3] + 2*mp[momenta3, momenta5] + 
          mp[momenta5, momenta5])))/((mp[momenta2, momenta2] + 
        2*mp[momenta2, momenta4] + mp[momenta4, momenta4])*
       (-m^2 + mp[momenta2, momenta2] + 2*mp[momenta2, momenta4] + 
        mp[momenta4, momenta4])*(mp[momenta3, momenta3] + 
        2*mp[momenta3, momenta5] + mp[momenta5, momenta5])*
       (-m^2 + mp[momenta3, momenta3] + 2*mp[momenta3, momenta5] + 
        mp[momenta5, momenta5])) - 
     (3*g^2*(I*g*m^2 - I*g*mp[momenta1, momenta1] - 
        I*g*mp[momenta4, momenta4] - I*g*(mp[momenta2, momenta2] + 
          2*mp[momenta2, momenta3] + 2*mp[momenta2, momenta5] + 
          mp[momenta3, momenta3] + 2*mp[momenta3, momenta5] + 
          mp[momenta5, momenta5])))/((mp[momenta2, momenta2] + 
        2*mp[momenta2, momenta3] + 2*mp[momenta2, momenta5] + 
        mp[momenta3, momenta3] + 2*mp[momenta3, momenta5] + 
        mp[momenta5, momenta5])*(-m^2 + mp[momenta2, momenta2] + 
        2*mp[momenta2, momenta3] + 2*mp[momenta2, momenta5] + 
        mp[momenta3, momenta3] + 2*mp[momenta3, momenta5] + 
        mp[momenta5, momenta5])) - 
     ((I*g*m^2 - I*g*mp[momenta2, momenta2] - I*g*mp[momenta3, momenta3] - 
        I*g*(mp[momenta2, momenta2] + 2*mp[momenta2, momenta3] + 
          mp[momenta3, momenta3]))*(I*g*m^2 - I*g*mp[momenta1, momenta1] - 
        I*g*mp[momenta4, momenta4] - I*g*(mp[momenta2, momenta2] + 
          2*mp[momenta2, momenta3] + 2*mp[momenta2, momenta5] + 
          mp[momenta3, momenta3] + 2*mp[momenta3, momenta5] + 
          mp[momenta5, momenta5]))*(I*g*m^2 - I*g*(mp[momenta2, momenta2] + 
          2*mp[momenta2, momenta3] + mp[momenta3, momenta3]) - 
        I*g*mp[momenta5, momenta5] - I*g*(mp[momenta2, momenta2] + 
          2*mp[momenta2, momenta3] + 2*mp[momenta2, momenta5] + 
          mp[momenta3, momenta3] + 2*mp[momenta3, momenta5] + 
          mp[momenta5, momenta5])))/((mp[momenta2, momenta2] + 
        2*mp[momenta2, momenta3] + mp[momenta3, momenta3])*
       (-m^2 + mp[momenta2, momenta2] + 2*mp[momenta2, momenta3] + 
        mp[momenta3, momenta3])*(mp[momenta2, momenta2] + 
        2*mp[momenta2, momenta3] + 2*mp[momenta2, momenta5] + 
        mp[momenta3, momenta3] + 2*mp[momenta3, momenta5] + 
        mp[momenta5, momenta5])*(-m^2 + mp[momenta2, momenta2] + 
        2*mp[momenta2, momenta3] + 2*mp[momenta2, momenta5] + 
        mp[momenta3, momenta3] + 2*mp[momenta3, momenta5] + 
        mp[momenta5, momenta5])) - 
     ((I*g*m^2 - I*g*mp[momenta2, momenta2] - I*g*mp[momenta5, momenta5] - 
        I*g*(mp[momenta2, momenta2] + 2*mp[momenta2, momenta5] + 
          mp[momenta5, momenta5]))*(I*g*m^2 - I*g*mp[momenta1, momenta1] - 
        I*g*mp[momenta4, momenta4] - I*g*(mp[momenta2, momenta2] + 
          2*mp[momenta2, momenta3] + 2*mp[momenta2, momenta5] + 
          mp[momenta3, momenta3] + 2*mp[momenta3, momenta5] + 
          mp[momenta5, momenta5]))*(I*g*m^2 - I*g*mp[momenta3, momenta3] - 
        I*g*(mp[momenta2, momenta2] + 2*mp[momenta2, momenta5] + 
          mp[momenta5, momenta5]) - I*g*(mp[momenta2, momenta2] + 
          2*mp[momenta2, momenta3] + 2*mp[momenta2, momenta5] + 
          mp[momenta3, momenta3] + 2*mp[momenta3, momenta5] + 
          mp[momenta5, momenta5])))/((mp[momenta2, momenta2] + 
        2*mp[momenta2, momenta5] + mp[momenta5, momenta5])*
       (-m^2 + mp[momenta2, momenta2] + 2*mp[momenta2, momenta5] + 
        mp[momenta5, momenta5])*(mp[momenta2, momenta2] + 
        2*mp[momenta2, momenta3] + 2*mp[momenta2, momenta5] + 
        mp[momenta3, momenta3] + 2*mp[momenta3, momenta5] + 
        mp[momenta5, momenta5])*(-m^2 + mp[momenta2, momenta2] + 
        2*mp[momenta2, momenta3] + 2*mp[momenta2, momenta5] + 
        mp[momenta3, momenta3] + 2*mp[momenta3, momenta5] + 
        mp[momenta5, momenta5])) - 
     ((I*g*m^2 - I*g*mp[momenta3, momenta3] - I*g*mp[momenta5, momenta5] - 
        I*g*(mp[momenta3, momenta3] + 2*mp[momenta3, momenta5] + 
          mp[momenta5, momenta5]))*(I*g*m^2 - I*g*mp[momenta1, momenta1] - 
        I*g*mp[momenta4, momenta4] - I*g*(mp[momenta2, momenta2] + 
          2*mp[momenta2, momenta3] + 2*mp[momenta2, momenta5] + 
          mp[momenta3, momenta3] + 2*mp[momenta3, momenta5] + 
          mp[momenta5, momenta5]))*(I*g*m^2 - I*g*mp[momenta2, momenta2] - 
        I*g*(mp[momenta3, momenta3] + 2*mp[momenta3, momenta5] + 
          mp[momenta5, momenta5]) - I*g*(mp[momenta2, momenta2] + 
          2*mp[momenta2, momenta3] + 2*mp[momenta2, momenta5] + 
          mp[momenta3, momenta3] + 2*mp[momenta3, momenta5] + 
          mp[momenta5, momenta5])))/((mp[momenta3, momenta3] + 
        2*mp[momenta3, momenta5] + mp[momenta5, momenta5])*
       (-m^2 + mp[momenta3, momenta3] + 2*mp[momenta3, momenta5] + 
        mp[momenta5, momenta5])*(mp[momenta2, momenta2] + 
        2*mp[momenta2, momenta3] + 2*mp[momenta2, momenta5] + 
        mp[momenta3, momenta3] + 2*mp[momenta3, momenta5] + 
        mp[momenta5, momenta5])*(-m^2 + mp[momenta2, momenta2] + 
        2*mp[momenta2, momenta3] + 2*mp[momenta2, momenta5] + 
        mp[momenta3, momenta3] + 2*mp[momenta3, momenta5] + 
        mp[momenta5, momenta5])) - 
     (3*g^2*(I*g*m^2 - I*g*mp[momenta4, momenta4] - 
        I*g*mp[momenta5, momenta5] - I*g*(mp[momenta4, momenta4] + 
          2*mp[momenta4, momenta5] + mp[momenta5, momenta5])))/
      ((mp[momenta4, momenta4] + 2*mp[momenta4, momenta5] + 
        mp[momenta5, momenta5])*(-m^2 + mp[momenta4, momenta4] + 
        2*mp[momenta4, momenta5] + mp[momenta5, momenta5])) - 
     ((I*g*m^2 - I*g*mp[momenta2, momenta2] - I*g*mp[momenta3, momenta3] - 
        I*g*(mp[momenta2, momenta2] + 2*mp[momenta2, momenta3] + 
          mp[momenta3, momenta3]))*(I*g*m^2 - I*g*mp[momenta1, momenta1] - 
        I*g*(mp[momenta2, momenta2] + 2*mp[momenta2, momenta3] + 
          mp[momenta3, momenta3]) - I*g*(mp[momenta4, momenta4] + 
          2*mp[momenta4, momenta5] + mp[momenta5, momenta5]))*
       (I*g*m^2 - I*g*mp[momenta4, momenta4] - I*g*mp[momenta5, momenta5] - 
        I*g*(mp[momenta4, momenta4] + 2*mp[momenta4, momenta5] + 
          mp[momenta5, momenta5])))/((mp[momenta2, momenta2] + 
        2*mp[momenta2, momenta3] + mp[momenta3, momenta3])*
       (-m^2 + mp[momenta2, momenta2] + 2*mp[momenta2, momenta3] + 
        mp[momenta3, momenta3])*(mp[momenta4, momenta4] + 
        2*mp[momenta4, momenta5] + mp[momenta5, momenta5])*
       (-m^2 + mp[momenta4, momenta4] + 2*mp[momenta4, momenta5] + 
        mp[momenta5, momenta5])) - 
     (3*g^2*(I*g*m^2 - I*g*mp[momenta1, momenta1] - 
        I*g*mp[momenta3, momenta3] - I*g*(mp[momenta2, momenta2] + 
          2*mp[momenta2, momenta4] + 2*mp[momenta2, momenta5] + 
          mp[momenta4, momenta4] + 2*mp[momenta4, momenta5] + 
          mp[momenta5, momenta5])))/((mp[momenta2, momenta2] + 
        2*mp[momenta2, momenta4] + 2*mp[momenta2, momenta5] + 
        mp[momenta4, momenta4] + 2*mp[momenta4, momenta5] + 
        mp[momenta5, momenta5])*(-m^2 + mp[momenta2, momenta2] + 
        2*mp[momenta2, momenta4] + 2*mp[momenta2, momenta5] + 
        mp[momenta4, momenta4] + 2*mp[momenta4, momenta5] + 
        mp[momenta5, momenta5])) - 
     ((I*g*m^2 - I*g*mp[momenta2, momenta2] - I*g*mp[momenta4, momenta4] - 
        I*g*(mp[momenta2, momenta2] + 2*mp[momenta2, momenta4] + 
          mp[momenta4, momenta4]))*(I*g*m^2 - I*g*mp[momenta1, momenta1] - 
        I*g*mp[momenta3, momenta3] - I*g*(mp[momenta2, momenta2] + 
          2*mp[momenta2, momenta4] + 2*mp[momenta2, momenta5] + 
          mp[momenta4, momenta4] + 2*mp[momenta4, momenta5] + 
          mp[momenta5, momenta5]))*(I*g*m^2 - I*g*(mp[momenta2, momenta2] + 
          2*mp[momenta2, momenta4] + mp[momenta4, momenta4]) - 
        I*g*mp[momenta5, momenta5] - I*g*(mp[momenta2, momenta2] + 
          2*mp[momenta2, momenta4] + 2*mp[momenta2, momenta5] + 
          mp[momenta4, momenta4] + 2*mp[momenta4, momenta5] + 
          mp[momenta5, momenta5])))/((mp[momenta2, momenta2] + 
        2*mp[momenta2, momenta4] + mp[momenta4, momenta4])*
       (-m^2 + mp[momenta2, momenta2] + 2*mp[momenta2, momenta4] + 
        mp[momenta4, momenta4])*(mp[momenta2, momenta2] + 
        2*mp[momenta2, momenta4] + 2*mp[momenta2, momenta5] + 
        mp[momenta4, momenta4] + 2*mp[momenta4, momenta5] + 
        mp[momenta5, momenta5])*(-m^2 + mp[momenta2, momenta2] + 
        2*mp[momenta2, momenta4] + 2*mp[momenta2, momenta5] + 
        mp[momenta4, momenta4] + 2*mp[momenta4, momenta5] + 
        mp[momenta5, momenta5])) - 
     ((I*g*m^2 - I*g*mp[momenta2, momenta2] - I*g*mp[momenta5, momenta5] - 
        I*g*(mp[momenta2, momenta2] + 2*mp[momenta2, momenta5] + 
          mp[momenta5, momenta5]))*(I*g*m^2 - I*g*mp[momenta1, momenta1] - 
        I*g*mp[momenta3, momenta3] - I*g*(mp[momenta2, momenta2] + 
          2*mp[momenta2, momenta4] + 2*mp[momenta2, momenta5] + 
          mp[momenta4, momenta4] + 2*mp[momenta4, momenta5] + 
          mp[momenta5, momenta5]))*(I*g*m^2 - I*g*mp[momenta4, momenta4] - 
        I*g*(mp[momenta2, momenta2] + 2*mp[momenta2, momenta5] + 
          mp[momenta5, momenta5]) - I*g*(mp[momenta2, momenta2] + 
          2*mp[momenta2, momenta4] + 2*mp[momenta2, momenta5] + 
          mp[momenta4, momenta4] + 2*mp[momenta4, momenta5] + 
          mp[momenta5, momenta5])))/((mp[momenta2, momenta2] + 
        2*mp[momenta2, momenta5] + mp[momenta5, momenta5])*
       (-m^2 + mp[momenta2, momenta2] + 2*mp[momenta2, momenta5] + 
        mp[momenta5, momenta5])*(mp[momenta2, momenta2] + 
        2*mp[momenta2, momenta4] + 2*mp[momenta2, momenta5] + 
        mp[momenta4, momenta4] + 2*mp[momenta4, momenta5] + 
        mp[momenta5, momenta5])*(-m^2 + mp[momenta2, momenta2] + 
        2*mp[momenta2, momenta4] + 2*mp[momenta2, momenta5] + 
        mp[momenta4, momenta4] + 2*mp[momenta4, momenta5] + 
        mp[momenta5, momenta5])) - 
     ((I*g*m^2 - I*g*mp[momenta4, momenta4] - I*g*mp[momenta5, momenta5] - 
        I*g*(mp[momenta4, momenta4] + 2*mp[momenta4, momenta5] + 
          mp[momenta5, momenta5]))*(I*g*m^2 - I*g*mp[momenta1, momenta1] - 
        I*g*mp[momenta3, momenta3] - I*g*(mp[momenta2, momenta2] + 
          2*mp[momenta2, momenta4] + 2*mp[momenta2, momenta5] + 
          mp[momenta4, momenta4] + 2*mp[momenta4, momenta5] + 
          mp[momenta5, momenta5]))*(I*g*m^2 - I*g*mp[momenta2, momenta2] - 
        I*g*(mp[momenta4, momenta4] + 2*mp[momenta4, momenta5] + 
          mp[momenta5, momenta5]) - I*g*(mp[momenta2, momenta2] + 
          2*mp[momenta2, momenta4] + 2*mp[momenta2, momenta5] + 
          mp[momenta4, momenta4] + 2*mp[momenta4, momenta5] + 
          mp[momenta5, momenta5])))/((mp[momenta4, momenta4] + 
        2*mp[momenta4, momenta5] + mp[momenta5, momenta5])*
       (-m^2 + mp[momenta4, momenta4] + 2*mp[momenta4, momenta5] + 
        mp[momenta5, momenta5])*(mp[momenta2, momenta2] + 
        2*mp[momenta2, momenta4] + 2*mp[momenta2, momenta5] + 
        mp[momenta4, momenta4] + 2*mp[momenta4, momenta5] + 
        mp[momenta5, momenta5])*(-m^2 + mp[momenta2, momenta2] + 
        2*mp[momenta2, momenta4] + 2*mp[momenta2, momenta5] + 
        mp[momenta4, momenta4] + 2*mp[momenta4, momenta5] + 
        mp[momenta5, momenta5])) - 
     (3*g^2*(I*g*m^2 - I*g*mp[momenta1, momenta1] - 
        I*g*mp[momenta2, momenta2] - I*g*(mp[momenta3, momenta3] + 
          2*mp[momenta3, momenta4] + 2*mp[momenta3, momenta5] + 
          mp[momenta4, momenta4] + 2*mp[momenta4, momenta5] + 
          mp[momenta5, momenta5])))/((mp[momenta3, momenta3] + 
        2*mp[momenta3, momenta4] + 2*mp[momenta3, momenta5] + 
        mp[momenta4, momenta4] + 2*mp[momenta4, momenta5] + 
        mp[momenta5, momenta5])*(-m^2 + mp[momenta3, momenta3] + 
        2*mp[momenta3, momenta4] + 2*mp[momenta3, momenta5] + 
        mp[momenta4, momenta4] + 2*mp[momenta4, momenta5] + 
        mp[momenta5, momenta5])) - 
     ((I*g*m^2 - I*g*mp[momenta3, momenta3] - I*g*mp[momenta4, momenta4] - 
        I*g*(mp[momenta3, momenta3] + 2*mp[momenta3, momenta4] + 
          mp[momenta4, momenta4]))*(I*g*m^2 - I*g*mp[momenta1, momenta1] - 
        I*g*mp[momenta2, momenta2] - I*g*(mp[momenta3, momenta3] + 
          2*mp[momenta3, momenta4] + 2*mp[momenta3, momenta5] + 
          mp[momenta4, momenta4] + 2*mp[momenta4, momenta5] + 
          mp[momenta5, momenta5]))*(I*g*m^2 - I*g*(mp[momenta3, momenta3] + 
          2*mp[momenta3, momenta4] + mp[momenta4, momenta4]) - 
        I*g*mp[momenta5, momenta5] - I*g*(mp[momenta3, momenta3] + 
          2*mp[momenta3, momenta4] + 2*mp[momenta3, momenta5] + 
          mp[momenta4, momenta4] + 2*mp[momenta4, momenta5] + 
          mp[momenta5, momenta5])))/((mp[momenta3, momenta3] + 
        2*mp[momenta3, momenta4] + mp[momenta4, momenta4])*
       (-m^2 + mp[momenta3, momenta3] + 2*mp[momenta3, momenta4] + 
        mp[momenta4, momenta4])*(mp[momenta3, momenta3] + 
        2*mp[momenta3, momenta4] + 2*mp[momenta3, momenta5] + 
        mp[momenta4, momenta4] + 2*mp[momenta4, momenta5] + 
        mp[momenta5, momenta5])*(-m^2 + mp[momenta3, momenta3] + 
        2*mp[momenta3, momenta4] + 2*mp[momenta3, momenta5] + 
        mp[momenta4, momenta4] + 2*mp[momenta4, momenta5] + 
        mp[momenta5, momenta5])) - 
     ((I*g*m^2 - I*g*mp[momenta3, momenta3] - I*g*mp[momenta5, momenta5] - 
        I*g*(mp[momenta3, momenta3] + 2*mp[momenta3, momenta5] + 
          mp[momenta5, momenta5]))*(I*g*m^2 - I*g*mp[momenta1, momenta1] - 
        I*g*mp[momenta2, momenta2] - I*g*(mp[momenta3, momenta3] + 
          2*mp[momenta3, momenta4] + 2*mp[momenta3, momenta5] + 
          mp[momenta4, momenta4] + 2*mp[momenta4, momenta5] + 
          mp[momenta5, momenta5]))*(I*g*m^2 - I*g*mp[momenta4, momenta4] - 
        I*g*(mp[momenta3, momenta3] + 2*mp[momenta3, momenta5] + 
          mp[momenta5, momenta5]) - I*g*(mp[momenta3, momenta3] + 
          2*mp[momenta3, momenta4] + 2*mp[momenta3, momenta5] + 
          mp[momenta4, momenta4] + 2*mp[momenta4, momenta5] + 
          mp[momenta5, momenta5])))/((mp[momenta3, momenta3] + 
        2*mp[momenta3, momenta5] + mp[momenta5, momenta5])*
       (-m^2 + mp[momenta3, momenta3] + 2*mp[momenta3, momenta5] + 
        mp[momenta5, momenta5])*(mp[momenta3, momenta3] + 
        2*mp[momenta3, momenta4] + 2*mp[momenta3, momenta5] + 
        mp[momenta4, momenta4] + 2*mp[momenta4, momenta5] + 
        mp[momenta5, momenta5])*(-m^2 + mp[momenta3, momenta3] + 
        2*mp[momenta3, momenta4] + 2*mp[momenta3, momenta5] + 
        mp[momenta4, momenta4] + 2*mp[momenta4, momenta5] + 
        mp[momenta5, momenta5])) - 
     ((I*g*m^2 - I*g*mp[momenta4, momenta4] - I*g*mp[momenta5, momenta5] - 
        I*g*(mp[momenta4, momenta4] + 2*mp[momenta4, momenta5] + 
          mp[momenta5, momenta5]))*(I*g*m^2 - I*g*mp[momenta1, momenta1] - 
        I*g*mp[momenta2, momenta2] - I*g*(mp[momenta3, momenta3] + 
          2*mp[momenta3, momenta4] + 2*mp[momenta3, momenta5] + 
          mp[momenta4, momenta4] + 2*mp[momenta4, momenta5] + 
          mp[momenta5, momenta5]))*(I*g*m^2 - I*g*mp[momenta3, momenta3] - 
        I*g*(mp[momenta4, momenta4] + 2*mp[momenta4, momenta5] + 
          mp[momenta5, momenta5]) - I*g*(mp[momenta3, momenta3] + 
          2*mp[momenta3, momenta4] + 2*mp[momenta3, momenta5] + 
          mp[momenta4, momenta4] + 2*mp[momenta4, momenta5] + 
          mp[momenta5, momenta5])))/((mp[momenta4, momenta4] + 
        2*mp[momenta4, momenta5] + mp[momenta5, momenta5])*
       (-m^2 + mp[momenta4, momenta4] + 2*mp[momenta4, momenta5] + 
        mp[momenta5, momenta5])*(mp[momenta3, momenta3] + 
        2*mp[momenta3, momenta4] + 2*mp[momenta3, momenta5] + 
        mp[momenta4, momenta4] + 2*mp[momenta4, momenta5] + 
        mp[momenta5, momenta5])*(-m^2 + mp[momenta3, momenta3] + 
        2*mp[momenta3, momenta4] + 2*mp[momenta3, momenta5] + 
        mp[momenta4, momenta4] + 2*mp[momenta4, momenta5] + 
        mp[momenta5, momenta5]))
