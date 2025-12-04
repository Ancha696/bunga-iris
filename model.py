{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 4,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "lhWpUwDgEeKw",
        "outputId": "88f6728e-6268-4ab3-ebf1-13263a820710"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.12/dist-packages/sklearn/base.py:1389: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples,), for example using ravel().\n",
            "  return fit_method(estimator, *args, **kwargs)\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Accuracy: 0.8888888888888888\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['rf_model.sav']"
            ]
          },
          "metadata": {},
          "execution_count": 4
        }
      ],
      "source": [
        "import pandas as pd\n",
        "from sklearn.ensemble import RandomForestClassifier\n",
        "from sklearn.metrics import accuracy_score\n",
        "from sklearn.model_selection import train_test_split\n",
        "import joblib\n",
        "\n",
        "# random seed\n",
        "seed = 42\n",
        "\n",
        "# Read original dataset\n",
        "iris_df = pd.read_csv(\"Iris.csv\")\n",
        "iris_df.sample(frac=1, random_state=seed)\n",
        "\n",
        "# selecting features and target data\n",
        "X = iris_df[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]\n",
        "y = iris_df[['Species']]\n",
        "\n",
        "# split data into train and test sets\n",
        "# 70% training and 30% test\n",
        "X_train, X_test, y_train, y_test = train_test_split(\n",
        "    X, y, test_size=0.3, random_state=seed, stratify=y\n",
        ")\n",
        "\n",
        "# create an instance of the random forest classifier\n",
        "clf = RandomForestClassifier(n_estimators=100, random_state=seed)\n",
        "\n",
        "# train the classifier on the training data\n",
        "clf.fit(X_train, y_train)\n",
        "\n",
        "# predict on the test set\n",
        "y_pred = clf.predict(X_test)\n",
        "\n",
        "# calculate accuracy\n",
        "accuracy = accuracy_score(y_test, y_pred)\n",
        "print(f\"Accuracy: {accuracy}\")   # Accuracy: 0.91\n",
        "\n",
        "# save the model to disk\n",
        "joblib.dump(clf, \"rf_model.sav\")"
      ]
    }
  ]
}