from model import mlr, x_train, y_train, x_test, y_test

print("Train score:")
print(mlr.score(x_train, y_train))
print("Test score:")
print(mlr.score(x_test, y_test))
