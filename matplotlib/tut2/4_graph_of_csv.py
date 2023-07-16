from imports import *
gas = pd.read_csv("matplotlib\gas_prices.csv")
plt.figure(figsize=(7,4))

# method 1
plt.plot(gas["Year"], gas["USA"], label="USA")
plt.plot(gas["Year"], gas["Canada"], label="Canada")
plt.plot(gas["Year"], gas["South Korea"], label="South Korea")

# another method thats better
# specific_countries = ["USA", "South Korea", "Australia", "Mexico"]
# for country in specific_countries:
#     if country in specific_countries:
#         plt.plot(gas["Year"], gas[country], label=country)

plt.title("Gas price per Year [USD]", fontdict={"fontweight":"bold"})

plt.xlabel("Year")
plt.ylabel("Price")

plt.xticks(gas["Year"][::3])

plt.legend()
plt.show()

# plt.savefig('Gas_prices_figure.png', dpi=400)