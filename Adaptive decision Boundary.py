import numpy as np

def sgn(x):
    return 1 if x >= 0 else -1

c = 1
k = 1
w0 = 0
w1 = 0

weights_updated = True

training_set = np.array([[-4], [-1]])
true_classes = np.array([-1, 1])

iter = 0

while weights_updated:
    weights_updated = False

    for i in range(training_set.shape[0]):
        print(f"Iteration: {iter}")
        D = w0 + w1 * training_set[i, 0]

        if sgn(D) != true_classes[i]:
            print("Error = Yes")
            iter += 1
            w0 += c * true_classes[i] * k
            w1 += c * true_classes[i] * training_set[i, 0]
            print(f"w0 = {w0}, w1 = {w1}\n")
            weights_updated = True
        else:
            print("Error = No")
            print(f"w0 = {w0}, w1 = {w1}\n")
            iter += 1

print(f"Final weights: w0 = {w0}, w1 = {w1}")
