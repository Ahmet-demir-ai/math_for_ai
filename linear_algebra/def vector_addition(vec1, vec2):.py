def vector_addition(vec1, vec2):
    """Vektörlerin toplamını döndürür"""
    return [vec1[i] + vec2[i] for i in range(len(vec1))]
def vector_substraction(vec1,vec2):
    return[vec1[i]-vec2[i] for i in range(len(vec1))]
def vector_scalerdupucition(value,vec1):
    return (value*vec1[i] for i in range(len(vec1)))
def dot_product(vec1, vec2):
    """Vektörlerin noktasal çarpımını döndürür"""
    return sum(vec1[i] * vec2[i] for i in range(len(vec1)))
over_calculate=True
while over_calculate:
    def vector_calculator():
         """Vektör hesap makinesi"""
    print("Vektör Hesap Makinesi")
    print("1. Vektör Toplama")
    print("2. Vektör Çıkarma")
    print("3. Skalar Çarpma")
    print("4. Noktasal Çarpma")
   
    choice = int(input("Bir işlem seçin (1/2/3/4): "))
    
 
    vec1 = list(map(int, input("Birinci vektörü girin (örneğin: 1 2 3): ").split()))
    vec2 = list(map(int, input("İkinci vektörü girin (örneğin: 4 5 6): ").split()))
    
    
    
    if choice == 1:
        result = vector_addition(vec1, vec2)
        print(f"Vektör Toplamı: {result}")
    elif choice == 2:
        result = vector_subtraction(vec1, vec2)
        print(f"Vektör Farkı: {result}")
    elif choice == 3:
        scalar = int(input("Skaları girin: "))
        result = scalar_multiply(scalar, vec1)
        print(f"Skalar Çarpma Sonucu: {result}")
    elif choice == 4:
        result = dot_product(vec1, vec2)
        print(f"Noktasal Çarpım Sonucu: {result}")
    else:
        print("Geçersiz işlem seçildi.")
    shoud_contiune=input("would you like contnue")
    if shoud_contiune=="no":
        over_calculate=False
    else:
        print("20*\n")
    


vector_calculator()


   