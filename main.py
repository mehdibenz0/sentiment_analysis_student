from utils.data_preprocessing import prepare_data
from utils.model import train_and_evaluate
from utils.predict import predict_sentiment

if __name__ == "__main__":
    X_train, X_test, y_train, y_test, vectorizer = prepare_data()
    
    # TODO: Train the model using train_and_evaluate and save it in 'model'
    model = 

    while True:
        text = input("Enter text to predict sentiment (or 'q' to quit): ")
        if text.lower() == 'q':
            break
        prediction = predict_sentiment(text, model, vectorizer)
        print(f"Predicted sentiment: {prediction}")
