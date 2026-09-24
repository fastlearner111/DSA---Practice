
training_data = [
    # Insert tuple here
]

new_student = (
    # Inser Question 3 here 
)



pred_k1 = knn_predict(training_data, new_student, k=1)


pred_k3 = knn_predict(training_data, new_student, k=3)


print(f"Prediction with k = 1: {pred_k1}")
print(f"Prediction with k = 3: {pred_k3}")

print(
    "Comparison"
)