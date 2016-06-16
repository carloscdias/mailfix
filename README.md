# mailfix
Ferramenta para correção de erros ortográficos em listas de email

## uso

```python3 mailfix.py 'users.csv' 'teste.txt'```

## exemplo de saída

```
Terminada leitura do arquivo
23165 linhas processadas, 23162 possíveis e-mails, 3 linhas removidas
-- Removidos
xxxxhttp//www.youtube.com/watch?v=http//www.youtube.com/watch?v=http//www.you
xxx!xxx@gmail.com
xxxxxxxxx/@hotmail.com

Ordenando 542 domínios distintos pelo número de usuários inscritos e selecionando os top's 10 como corretos
Primeiros 10 domínios com maior número de usuários inscritos
hotmail.com          -   11687 usuários
gmail.com            -    6573 usuários
yahoo.com.br         -    1515 usuários
outlook.com          -     742 usuários
bol.com.br           -     524 usuários
live.com             -     352 usuários
ig.com.br            -     240 usuários
hotmail.com.br       -     189 usuários
yahoo.com            -     132 usuários
outlook.com.br       -      78 usuários
22032 correspondendo a 95.12% de emails considerados como certos
Processando semelhança entre 1130 (4.88%) emails restantes...
oi.com.br            -> ig.com.br           
uol.com.br           -> bol.com.br          
ymail.com            -> gmail.com           
hotmai.com           -> hotmail.com         
hotmal.com           -> hotmail.com         
gmai.com             -> gmail.com           
homail.com           -> hotmail.com         
gamil.com            -> gmail.com           
hotmail.co           -> hotmail.com         
outllok.com          -> outlook.com         
mail.com             -> gmail.com           
hotnail.com          -> hotmail.com         
hotamil.com          -> hotmail.com         
hitmail.com          -> hotmail.com         
gamail.com           -> gmail.com           
hormail.com          -> hotmail.com         
gmail.co             -> gmail.com           
hotmsil.com          -> hotmail.com         
gnail.com            -> gmail.com           
gmil.com             -> gmail.com           
hotmial.com          -> hotmail.com         
outlook.om           -> outlook.com         
hotmil.com           -> hotmail.com         
otmail.com           -> hotmail.com         
hotmaill.com         -> hotmail.com         
yaho.com.br          -> yahoo.com.br        
gotmail.com          -> hotmail.com         
yaoo.com.br          -> yahoo.com.br        
hotmail.comm         -> hotmail.com         
gmaio.com            -> gmail.com           
hotmail.cm           -> hotmail.com         
hotamail.com         -> hotmail.com         
gmqil.com            -> gmail.com           
gmail.con            -> gmail.com           
hotmail.con          -> hotmail.com         
gmal.com             -> gmail.com           
hotimail.com.br      -> hotmail.com.br      
outlok.com           -> outlook.com         
hotmail.cim          -> hotmail.com         
email.com            -> gmail.com           
hotma.com            -> hotmail.com         
autlook.com          -> outlook.com         
yhaoo.com.br         -> yahoo.com.br        
gmail.cim            -> gmail.com           
yahoo.com.brr        -> yahoo.com.br        
gmail.om             -> gmail.com           
gmais.com            -> gmail.com           
gmsil.com            -> gmail.com           
hotmailo.com         -> hotmail.com         
gmail.c0m            -> gmail.com           
yahoo.co.br          -> yahoo.com.br        
gmailc.com           -> gmail.com           
outlookl.com         -> outlook.com         
gmaol.com            -> gmail.com           
hotmail.colm         -> hotmail.com         
ayhoo.com.br         -> yahoo.com.br        
jotmail.com          -> hotmail.com         
cpgmail.com          -> gmail.com           
hltmail.com          -> hotmail.com         
hotmail.comw         -> hotmail.com         
61gmail.com          -> gmail.com           
hotmail.coma         -> hotmail.com         
hotmal.com.br        -> hotmail.com.br      
hotmail.vom          -> hotmail.com         
gmai.coml            -> gmail.com           
hot6mail.com         -> hotmail.com         
yahool.com           -> yahoo.com           
outlock.com          -> outlook.com         
gmail.c              -> gmail.com           
xgmail.com           -> gmail.com           
yahoo.com.be         -> yahoo.com.br        
outlook.con          -> outlook.com         
outlookl.com.br      -> outlook.com.br      
yahoor.com.br        -> yahoo.com.br        
homail.com.br        -> hotmail.com.br      
outoook.com          -> outlook.com         
hotmaail.com         -> hotmail.com         
gmeil.com            -> gmail.com           
gtmail.com           -> gmail.com           
homtmail.com         -> hotmail.com         
h0tmail.com          -> hotmail.com         
hotemail.com         -> hotmail.com         
bil.com.br           -> bol.com.br          
htmail.com.br        -> hotmail.com.br      
yaool.com.br         -> yahoo.com.br        
outlook.com.ar       -> outlook.com.br      
outlook.c0m          -> outlook.com         
gmail.vom            -> gmail.com           
hotmail.coom         -> hotmail.com         
gmael.com            -> gmail.com           
hotmaol.com          -> hotmail.com         
outlook.coms         -> outlook.com         
hotmaim.com          -> hotmail.com         
hotail.com           -> hotmail.com         
hotmail.cpm.br       -> hotmail.com.br      
hotmaiol.com         -> hotmail.com         
gmail.com14          -> gmail.com           
hotmai.com.br        -> hotmail.com.br      
yahoo.coom.br        -> yahoo.com.br        
yahaoo.com.br        -> yahoo.com.br        
g.mail.com           -> gmail.com           
outlook.combr        -> outlook.com.br      
35gmail.com          -> gmail.com           
hotlook.com          -> outlook.com         
gmaiil.com           -> gmail.com           
1outlook.com         -> outlook.com         
rotmail.com          -> hotmail.com         
uahoo.com.br         -> yahoo.com.br        
hotmail.com81        -> hotmail.com         
bol.com.ber          -> bol.com.br          
71yahoo.com.br       -> yahoo.com.br        
yahooo.com.br        -> yahoo.com.br        
outloo.com           -> outlook.com         
ohtlook.com          -> outlook.com         
hotrmail.com         -> hotmail.com         
hotmail.como         -> hotmail.com         
htmail.com           -> hotmail.com         
hotmeil.com          -> hotmail.com         
hotmail.xom          -> hotmail.com         
hptmail.com          -> hotmail.com         
hotmail.om           -> hotmail.com         
gmail.comp           -> gmail.com           
hotimal.com.br       -> hotmail.com.br      
hoitmail.com         -> hotmail.com         
outloook.com         -> outlook.com         
gmaul.com            -> gmail.com           
rotmail.com.br       -> hotmail.com.br      
hitmail.com.br       -> hotmail.com.br      
gimail.com           -> gmail.com           
outook.com.br        -> outlook.com.br      
hotimail.com         -> hotmail.com         
oultook.com          -> outlook.com         
442 emails recuperados
400 domínios adicionados totalizando 688 emails
Escrevendo arquivo...
Operação concluída

```
