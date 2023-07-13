d={"tv":1000,"mobile":10000,"refrigerator":30000,"oven":4000}
for  key,value in d.items():
    print(key,value)
    print("enter the required name. enter completed to exist")
rate=0
while True:
    key=input("enter the name:")
    if key=="completed":
        break
rate+=d[key]    
if "rate">45000:
    final_rate=rate-((10/100)*rate)
    print(f"actual rate:{rate}")
    print(f"final rate after 10% discount:{final_rate}")
else:
    print(f"final rate:{rate}")