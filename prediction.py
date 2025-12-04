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
      "execution_count": 1,
      "metadata": {
        "id": "6SSWokXBHOg1"
      },
      "outputs": [],
      "source": [
        "import joblib\n",
        "\n",
        "def predict(data):\n",
        "    clf = joblib.load(\"rf_model.sav\")\n",
        "    return clf.predict(data)"
      ]
    }
  ]
}