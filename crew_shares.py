# pb crew shares project period 2
import random

pirate_amount = float(input("how many pirates are on your ship (including yondu and peter): "))
units = random.randint(500,5000)

#13%=0.13
units_share = units - (pirate_amount-2)* 3 
yondu_share = round(0.13 * units_share, 2)
remainder = units - yondu_share
peter_share = round(0.11 * remainder,2)
remainder = remainder - peter_share
crews_share = round(remainder / pirate_amount,2)

print(f"units found: {units:.2f}")
print(f"yondu's share: {yondu_share + crews_share:.2f}")
print(f"peter's share: {peter_share + crews_share:.2f}")
print(f"crews share: {crews_share:.2f}") 