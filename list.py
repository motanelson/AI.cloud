var1="Display.ShowMessageDialog.ShowMessage"

values=[ "Title:", "Message:","Icon:","Buttons:","DefaultButton:","IsTopMost:"]
valuesv=[ "","","Display.Icon.None","Display.Buttons.OK","Display.DefaultButton.Button1","False"]
c="ButtonPressed=> ButtonPressed"
list1=[]
a="list"
print("\033c\033[40;37m\n give me list item empty to exit? ")
while 1:
    z=input().strip()
    if z=="":
        break
    else:
        list1=list1+[z]

var2=var1+" "+values[0]+" $'''"+a+"''' "+values[1]+" list1 "+values[2]+" "+valuesv[2]+" "+values[3]+" "+valuesv[3]+" "+values[4]+" "+valuesv[4]+" "+values[5]+" "+valuesv[5]+" "+c
print("\n"+"-"*80 +"\n")
print("Variables.CreateNewList List=> list1")
for l in list1:
    print("Variables.AddItemToList Item: $'''$hello''' List: list1".replace("$hello",l))
print(var2)