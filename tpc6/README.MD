Gramatica com prioridade  


A -> Num B 
   | ( A ) B
   | - Num B  



B -> * A
   | / A
   | C  



C -> + A
   | - A
   | ε  

