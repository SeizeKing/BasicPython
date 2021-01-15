#!/usr/bin/env python
# coding: utf-8

# In[13]:


teori = int(input("Masukkan nilai teori : "))
praktek = int(input("Masukkan nilai praktek : "))
if (teori < 70 and praktek < 70):
    print("Anda harus mengulang ujian teori dan praktek")
elif (teori >= 70 and praktek < 70):
    print("Anda harus mengulang ujian praktek")
elif (teori < 70 and praktek >= 70):
    print("Anda harus mengulang ujian teori")
else:
    print("Selamat, anda lulus!")


# In[ ]:





# In[ ]:




