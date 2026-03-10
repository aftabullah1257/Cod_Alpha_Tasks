from sklearn import svm
from sklearn.datasets import load_breast_cancer # Example dataset[cite: 3]

def disease_prediction():
    data = load_breast_cancer()
    X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2)

    # Applying Support Vector Machine (SVM)[cite: 3]
    clf = svm.SVC(kernel='linear')
    clf.fit(X_train, y_train)
    
    accuracy = clf.score(X_test, y_test)
    print(f"Disease Prediction Accuracy: {accuracy * 100:.2%}")

disease_prediction()