# 📊 Streamlit Data Analysis Application

This is a **Streamlit-based web application** that allows users to perform exploratory data analysis (EDA) on built-in datasets or custom datasets. With an intuitive user interface and powerful visualizations, this app makes data analysis effortless and engaging.

## 🚀 Features
- Load popular built-in datasets like **Iris**, **Titanic**, **Tips**, and **Diamonds**.
- Upload and analyze your **custom dataset** (CSV or Excel files).
- Visualize data with **pair plots**, **heatmaps**, **distribution plots**, and more.
- **Outlier detection** and descriptive statistics.
- Clean and analyze null values easily.
- Interactive and responsive visualizations using **Seaborn** and **Plotly**.

---

## 📂 Folder Structure

```plaintext
.
├── .streamlit/             # Streamlit configuration files
│   └── config.toml         # Theme and settings for Streamlit
├── app.py                  # Main Python script for the Streamlit app
├── requirements.txt        # Dependencies for the application
```

---

## 🛠️ Installation

Follow these steps to set up the application locally:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/streamlit-data-analyzer.git
   cd streamlit-data-analyzer
   ```

2. **Install dependencies**:
   Make sure you have Python installed. Install required libraries using:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   Start the Streamlit app by running:
   ```bash
   streamlit run app.py
   ```

4. **Access the app**:
   Open the provided URL in your browser (e.g., `http://localhost:8501`).

---

## 📦 Dependencies

Here are the key libraries used in the project:
- **Streamlit**: For building the web app.
- **Pandas**: For data manipulation and analysis.
- **NumPy**: For numerical operations.
- **Matplotlib** & **Seaborn**: For data visualization.
- **Plotly**: For interactive heatmaps and charts.

The complete list of dependencies is in the [`requirements.txt`](requirements.txt) file.

---

## 📋 Usage

1. Select a dataset from the dropdown or upload your own dataset.
2. Explore the dataset's shape, column types, and null values.
3. Visualize relationships with pair plots or analyze correlations with a heatmap.
4. Perform statistical analysis or detect outliers.

---

## 🛡️ License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Fork the repository.
- Create a feature branch.
- Open a pull request.

---

## 👨‍💻 Author

Developed with ❤️ by (https://github.com/ashwathnakate).
