# Weather Prediction using Bayes' Theorem

total = 20
rain = 8
no_rain = 12
cloudy_rain = 7
cloudy_no_rain = 3


P_Rain = rain / total
P_NoRain = no_rain / total


P_Cloudy_Rain = cloudy_rain / rain
P_Cloudy_NoRain = cloudy_no_rain / no_rain

P_Rain_Cloudy = (P_Cloudy_Rain * P_Rain) / (
    (P_Cloudy_Rain * P_Rain) + (P_Cloudy_NoRain * P_NoRain)
)

P_NoRain_Cloudy = (P_Cloudy_NoRain * P_NoRain) / (
    (P_Cloudy_Rain * P_Rain) + (P_Cloudy_NoRain * P_NoRain)
)

print("P(Rain) =", round(P_Rain, 2))
print("P(Not Rain) =", round(P_NoRain, 2))
print("P(Cloudy | Rain) =", round(P_Cloudy_Rain, 2))
print("P(Cloudy | Not Rain) =", round(P_Cloudy_NoRain, 2))
print("P(Rain | Cloudy) =", round(P_Rain_Cloudy, 2))
print("P(Not Rain | Cloudy) =", round(P_NoRain_Cloudy, 2))

if P_Rain_Cloudy > P_NoRain_Cloudy:
    print("Predicted Weather = Rain")
else:
    print("Predicted Weather = Not Rain")