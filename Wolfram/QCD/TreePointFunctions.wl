Tree3Point[p1_, p2_, p3_, (pol_)[]] := 
    (-g)*(mp[p1, pol[p3]]*mp[pol[p1], pol[p2]] - mp[p2, pol[p3]]*
       mp[pol[p1], pol[p2]] - mp[p1, pol[p2]]*mp[pol[p1], pol[p3]] + 
      mp[p3, pol[p2]]*mp[pol[p1], pol[p3]] + mp[p2, pol[p1]]*
       mp[pol[p2], pol[p3]] - mp[p3, pol[p1]]*mp[pol[p2], pol[p3]])
 
Tree3Point[p1_, p2_, p3_, pol_] := 
    (-g)*(mp[p1, pol[p3]]*mp[pol[p1], pol[p2]] - mp[p2, pol[p3]]*
       mp[pol[p1], pol[p2]] - mp[p1, pol[p2]]*mp[pol[p1], pol[p3]] + 
      mp[p3, pol[p2]]*mp[pol[p1], pol[p3]] + mp[p2, pol[p1]]*
       mp[pol[p2], pol[p3]] - mp[p3, pol[p1]]*mp[pol[p2], pol[p3]])
