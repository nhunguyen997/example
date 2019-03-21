def sapxep():
    print("nhap vao mot chuoi:")
    s = input()
    print("ban da nhap vao: \n", s)
    s = s.split()
    s = list(set(s))
    s.sort()
    print("sau khi sap xep:")
    print(s)


sapxep()
