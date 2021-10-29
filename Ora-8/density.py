olom_suruseg = 11.34
rez_suruseg = 8.69
v_rez = 23
v_olom = 18
m_rez = v_rez * rez_suruseg
m_olom = v_olom * olom_suruseg

if(m_rez > m_olom):
    print("Nehezebb",v_rez,"cm^3 réz mint",v_olom,"cm^3 ólom.")
    print("A réz tömege",m_rez,"és az ólom tömege",m_olom)
elif(m_rez == m_olom):
    print("Megegyezik a tömege",v_rez,"cm^3 réznek és",v_olom,"cm^3 ólomnak.")
    print("A tömegük",m_olom)
else:
    print("Nem nehezebb",v_rez,"cm^3 réz mint",v_olom,"cm^3 ólom.")
    print("A réz tömege",m_rez,"és az ólom tömege",m_olom)