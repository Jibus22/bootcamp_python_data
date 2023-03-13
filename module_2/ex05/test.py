from TinyStatistician import TinyStatistician

tstat = TinyStatistician()
a = [1, 42, 300, 10, 59]
b = [1, 42, 400, 39, 197, 300, 10, 59]

print(f"MEAN" + 70 * '-')
print(f"  {tstat.mean(a)}")
# Expected result: 82.4
print(f"  {tstat.mean(b)}")

print(f"MEDIAN" + 70 * '-')
print(f"  {tstat.median(a)}")
# Expected result: 42.0
print(f"  {tstat.median(b)}")

print(f"QUARTILES" + 70 * '-')
print(f"  {tstat.quartile(a)}")
print(f"  {tstat.quartile(b)}")

print(f"VAR" + 70 * '-')
print(f"  {tstat.var(a)}")
# Expected result: 12279.439999999999
print(f"  {tstat.var(b)}")

print(f"STD" + 70 * '-')
print(f"  {tstat.std(a)}")
# Expected result: 110.81263465868862
print(f"  {tstat.std(b)}")
