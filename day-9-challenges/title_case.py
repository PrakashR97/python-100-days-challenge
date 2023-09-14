def  format_name(_name):

 t_c=""
 for i in range(0,len(_name)):
   if i==0 or _name[i-1]==' ':
       t_c+=_name[i].upper()
   else:
       t_c+=_name[i]
 return t_c


title_case=format_name("emma watson")
print(title_case)



print("they're bill's friends from the UK".title())
