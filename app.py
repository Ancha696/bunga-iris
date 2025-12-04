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
      "source": [
        "import streamlit as st\n",
        "import pandas as pd\n",
        "import numpy as np\n",
        "from prediction import predict\n",
        "\n",
        "st.title('Classifying Iris Flowers')\n",
        "st.markdown('Toy model to play to classify iris flowers into \\\n",
        "(setosa, versicolor, virginica) based on their sepal/petal \\\n",
        "and length/width.')\n",
        "\n",
        "st.header(\"Plant Features\")\n",
        "col1, col2 = st.columns(2)\n",
        "\n",
        "with col1:\n",
        "    st.text(\"Sepal characteristics\")\n",
        "    sepal_l = st.slider('Sepal length (cm)', 1.0, 8.0, 0.5)\n",
        "    sepal_w = st.slider('Sepal width (cm)', 2.0, 4.4, 0.5)\n",
        "\n",
        "with col2:\n",
        "    st.text(\"Petal characteristics\")\n",
        "    petal_l = st.slider('Petal length (cm)', 1.0, 7.0, 0.5)\n",
        "    petal_w = st.slider('Petal width (cm)', 0.1, 2.5, 0.5)\n",
        "\n",
        "st.text('')\n",
        "if st.button(\"Predict type of Iris\"):\n",
        "    result = predict(\n",
        "        np.array([[sepal_l, sepal_w, petal_l, petal_w]])\n",
        "    )\n",
        "    st.text(result[0])\n",
        "\n",
        "st.text('')\n",
        "st.markdown('')"
      ],
      "metadata": {
        "id": "CSO_RnqFPhzs"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}