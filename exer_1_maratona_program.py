import math

class num_min_pg():
   
    def num_palav(self, num1):
 

        self.texto = str (input(''))
        self.tamanho = len(self.texto)
        self.texto = self.texto.split(' ')
        for x in self.texto:
            if len(x) >= 1 and len(x) <= 70:
                self.texto_1 = []
                if num1 < len(self.texto):
                    for x in range(0 , num1):
                        self.texto_1.append(self.texto[x])
                elif num1 > len(self.texto):
                    for x in range(0 , len(self.texto)):
                        self.texto_1.append(self.texto[x])

            elif len(x) < 1 or  len(x) > 70:
                self.texto_1 = []
                y = 'default value'
                self.texto_1.append(y)
                print('erro palavra grande!!')
                continue
               
                        
            
                
    
    def caract_linha(self, num2, num3):
        self.tam = self.tamanho / num3
        self.num_pg = self.tam / num2
       

        if (self.num_pg % 2) != 0:
            self.num_pg = int(self.num_pg + 1)
            

        

    def printer(self):
        print(self.num_pg)
        
        
    
   
     
            

        

list_num = []
num1,num2,num3 = 0,0,0

nums = str(input(''))

list_num = nums.split(' ')

if  len(list_num) == 3:
    for x in range(0,3):
        if x == 0:
            num1 = int (list_num[x])
        elif x == 1:
            num2 = int (list_num[x])
        elif x == 2:
            num3 = int(list_num[x])

if num1 >= 2 and num1 <= 1000:
    if num2 >= 1 and num2 <= 30:
        if num3 >= 1 and num3 <= 70:
            x = num_min_pg()
            x.num_palav(num1)
            x.caract_linha(num2, num3)
            x.printer()
        else:
            print('Condição inválida!!! C')
    else:
        print('Condição inválida!!! L')
else:
     print('Condição inválida!!! N')

    
