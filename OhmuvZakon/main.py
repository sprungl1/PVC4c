
import ohm
from coulumb import epsilon, force, epsilon_0
import mydl.zakon as alternative

print(f"{ohm.ele_currnet(0.01, 1000):7f}")
print(f"{ohm.resistance(0.002,3):7f}")
print(f"{ohm.power(0.02, 20):1f}")
print("-------------------")
print(f"{alternative.calculate_I(0.01, 1000):7f}")
print(f"{alternative.calculate_R(0.002,3):7f}")
print(f"{alternative.calculate_U(0.02, 20):1f}")

print("-------------------")

print(force(0.00000005,0.00000007,1))
print(epsilon(epsilon_0, 1))

print("-------------------")

print(f"{alternative.calculate_Epsilon(0.5,0.7,1,1):7f}")


