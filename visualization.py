from model import y_test, y_predict
import matplotlib.pyplot as plt

plt.scatter(y_test, y_predict, alpha=0.4)
plt.xlabel("Prices")
plt.ylabel("Predicted prices")
plt.title("Actual Rent vs Predicted Rent")
plt.show()
