age=40+10
age=age-10
age=age/50

#文字だからダブルクオーテーション
for i in range(3): 
    print(i,"人目")
    name=input("名前を入れてください")
    waist=float(input("胸囲は？"))
    age=int(input("年齢は？"))
    print(name, "さんは腹囲", waist, "cmで年齢は",age, "才ですね。")



    if waist>=85 and age>=40:#この部分が変更されました
        print(name,"さん、内臓脂肪蓄積注意です")
    else:
        print(name,"さん、腹囲は問題ありません")

    



