def rombusz(rmeret):
    rsorok = rmeret * 2 - 1
    i = 0;
    while(i<rmeret):
        i+=1
        szokoz = rmeret - i
        print(" "*szokoz+"*"*(i+(i-1))+" "*szokoz)
    while(i>0):
        i-=1
        szokoz = rmeret - i
        print(" "*szokoz+"*"*(i+(i-1))+" "*szokoz)

def ures_rombusz(rmeret):
    rsorok = rmeret * 2 - 1
    i = 0;
    while(i<rmeret):
        i+=1
        if(i==1):
            csillag = 0
        else:
            csillag = 1
        szokoz = rmeret - i
        print(" "*szokoz+"*"+" "*(i+(i-1)-2)+"*"*csillag+" "*szokoz)
    while(i>1):
        i-=1
        if(i==1):
            csillag = 0
        else:
            csillag = 1
        szokoz = rmeret - i
        print(" "*szokoz+"*"+" "*(i+(i-1)-2)+"*"*csillag+" "*szokoz)

print("Kitöltött rombusz")
rombusz(5)
print("Üreges rombusz")
ures_rombusz(5)

"""
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *    
    
    *
   * *
  *   *
 *     *
*       *
 *     *
  *   *
   * *
    *
"""