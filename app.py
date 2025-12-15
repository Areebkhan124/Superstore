{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMhDX2k17YuN1JRULVHj1Xn",
      "include_colab_link": true
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
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Areebkhan124/Superstore/blob/main/app.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        " %%writefile app.py\n",
        " from tensorflow.keras.models import load_model\n",
        " from tensorflow.keras.preprocessing import image\n",
        " from PIL import Image\n",
        " import numpy as np\n",
        "\n",
        " st.title(\"Brain Tumor Detection System (AI Powered)\")\n",
        "\n",
        " model = load_model(\"brain_tumor_model.keras\")\n",
        "\n",
        " uploaded_file = st.file_uploader(\"Upload MRI image\", type=[\"jpg\",\"png\"])\n",
        " if uploaded_file is not None:\n",
        "     img = Image.open(uploaded_file)\n",
        "     st.image(img, caption=\"Uploaded MRI Image\", use_column_width=True)\n",
        "\n",
        "     if st.button(\"Detect Tumor\"):\n",
        "         img_array = image.img_to_array(img.resize((224,224)))\n",
        "         img_array = np.expand_dims(img_array, axis=0)/255.0\n",
        "         pred = model.predict(img_array)\n",
        "\n",
        "         result = \"Tumor\" if pred[0][0] > 0.5 else \"No Tumor\"\n",
        "         confidence = pred[0][0]*100 if pred[0][0] > 0.5 else (1-pred[0][0])*100\n",
        "\n",
        "         st.write(f\"Prediction: {result}\")\n",
        "         st.write(f\"Confidence: {confidence:.2f}%\")"
      ],
      "metadata": {
        "id": "vCju78Nl5ZxW",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "71a95586-a736-4db7-f740-fa1021f28675"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Overwriting app.py\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "GG9_2eG5t8xZ"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}