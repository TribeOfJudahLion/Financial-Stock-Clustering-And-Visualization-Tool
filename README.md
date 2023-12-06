<br/>
<p align="center">
  <h3 align="center">Unveiling Market Synergies with Advanced Analytics</h3>

  <p align="center">
    Discover the hidden patterns and forge your path to smarter investments with our Financial Stock Clustering and Visualization Tool!
    <br/>
    <br/>
  </p>
</p>



## Table Of Contents

* [About the Project](#about-the-project)
* [Built With](#built-with)
* [Getting Started](#getting-started)
* [Contributing](#contributing)
* [License](#license)
* [Authors](#authors)
* [Acknowledgements](#acknowledgements)

## About The Project

### Problem Scenario

A financial analytics company wants to understand the market dynamics by analyzing how different stocks move with respect to each other. Specifically, the company is interested in identifying clusters of stocks that exhibit similar trading patterns, which could imply a correlation in their price movements due to various factors such as belonging to the same sector, being impacted by similar economic events, or having comparable market capitalizations.

However, the company faces several challenges:
- The financial data is scattered across different sources and not readily available in a structured format.
- The amount of data is vast, and manual analysis is not feasible.
- They need to model the relationships between the fluctuations of different stocks in a statistically sound way.
- After identifying clusters, the company wants to visualize the results for easier interpretation and presentation to stakeholders.

### Solution

The provided Python code is designed to address these challenges by automating the process of fetching, analyzing, and visualizing financial data:

1. **Data Acquisition**:
   - `load_symbols`: This function reads a JSON file (`symbol_map.json`) containing stock symbols, which serves as an input for which stocks to analyze.

2. **Data Fetching**:
   - `fetch_financial_data`: For each stock symbol, it fetches historical stock data (such as opening and closing prices) from a public GitHub repository. It handles any potential URL errors during the fetching process.

3. **Data Processing**:
   - `calculate_fluctuations`: It calculates the daily fluctuations for each stock by subtracting the opening price from the closing price, providing a measure of daily volatility.

4. **Statistical Modeling**:
   - `build_graph_model`: The fluctuations data is then used to construct a graphical model using the Graphical Lasso algorithm, which estimates a sparse inverse covariance matrix. The model identifies the relationships between the movements of different stocks.

5. **Clustering**:
   - `perform_clustering`: With the graphical model as a basis, the function applies affinity propagation clustering to group stocks that have similar patterns of fluctuations.

6. **Visualization**:
   - `visualize_clusters`: Finally, the clusters are visualized using a scatter plot, making it easy to see which stocks are grouped together.

7. **Execution**:
   - The `main` function orchestrates the entire process, and the script is designed to be run as a standalone program.

By executing this script, the company can achieve its goal of identifying clusters of stocks with similar movements. This information can be used for various purposes, such as creating diversified portfolios, identifying market sectors that move together, and understanding broader market trends. The automated process is scalable and can be run periodically to monitor changes in market dynamics over time.

This Python script is designed to analyze and cluster financial data. The functionality of each part of the script is as follows:

1. **Importing Libraries**:
   - `json`: To handle JSON files.
   - `sys`: To interact with the Python interpreter.
   - `pandas` (as `pd`): For data manipulation and analysis.
   - `numpy` (as `np`): For numerical operations.
   - `matplotlib.pyplot` (as `plt`): For plotting graphs.
   - `sklearn.covariance`: For statistical modeling.
   - `sklearn.cluster`: For clustering algorithms.
   - `urllib.error.URLError`: To handle URL errors during data fetching.

2. **Function `load_symbols`**:
   - Purpose: To load financial symbols from a JSON file.
   - Inputs: The path to the JSON file containing symbol data.
   - Process: Opens the file, reads the JSON content, and sorts the items.
   - Output: Returns a NumPy array of sorted symbols.

3. **Function `fetch_financial_data`**:
   - Purpose: Fetch financial data for the given symbols from a URL.
   - Inputs: A list of financial symbols.
   - Process: Iterates over symbols, fetches data from a specified URL, and appends it to a list. Handles URL errors.
   - Output: A list of pandas DataFrames containing financial data for each symbol.

4. **Function `calculate_fluctuations`**:
   - Purpose: Calculate the fluctuation between closing and opening quotes.
   - Inputs: A list of quotes (DataFrames).
   - Process: Extracts closing and opening quotes and calculates the difference.
   - Output: A NumPy array of fluctuations.

5. **Function `build_graph_model`**:
   - Purpose: Build a graph model using covariance.
   - Inputs: Delta quotes (fluctuations).
   - Process: Normalizes data, then fits it to a `GraphicalLassoCV` model.
   - Output: The fitted edge model.

6. **Function `perform_clustering`**:
   - Purpose: Perform clustering on the edge model.
   - Inputs: Edge model and the names of the companies.
   - Process: Uses affinity propagation to cluster the data based on the covariance matrix.
   - Output: Cluster labels for each company.

7. **Function `visualize_clusters`**:
   - Purpose: Visualize the clustering result.
   - Inputs: Cluster labels and company names.
   - Process: Plots a scatter plot showing clusters of companies.
   - Output: Displays the plot.

8. **`main` Function**:
   - Orchestrates the execution of the script. It calls the functions in the following order:
     - Loads symbols.
     - Fetches financial data.
     - Calculates fluctuations.
     - Builds the graph model.
     - Performs clustering.
     - Visualizes the clusters.

9. **Execution Block (`if __name__ == "__main__":`)**:
   - This is the entry point of the script, calling the `main` function when the script is run directly.

In summary, the script is a complete pipeline for loading financial data, analyzing it, performing clustering based on fluctuations, and visualizing the results. It showcases the use of data manipulation, statistical modeling, clustering algorithms, and data visualization in Python.

The image is a scatter plot visualizing the clustering of companies based on financial data, likely fluctuations between opening and closing stock prices. Each point on the plot represents a company, positioned on the x-axis according to the company name and on the y-axis according to the cluster to which it has been assigned.

- **Clusters**: There are eight distinct clusters identified in the financial data. Each cluster is represented by a different color and is labeled from Cluster 1 to Cluster 8 in the legend.
  
- **X-Axis (Company Names)**: The x-axis lists the names of companies that were included in the analysis. These companies span various industries, as indicated by the variety of names on the axis.

- **Y-Axis (Cluster)**: The y-axis indicates the cluster number assigned to each company. The companies are evenly distributed across the y-axis based on the cluster they belong to, but there is no vertical scaling that would provide additional information about the distance or similarity between the clusters.

- **Plot Points**: Each dot on the scatter plot represents a company. Companies within the same cluster are aligned horizontally since they share the same cluster number on the y-axis.

- **Cluster Composition**:
  - **Cluster 1**: Includes tech-related companies (Apple, Amazon, Yahoo).
  - **Cluster 2**: Comprises a diverse set of companies, including financial institutions (AIG, American Express, Bank of America), industrial corporations (DuPont de Nemours, General Dynamics, General Electrics), and others like Goldman Sachs, GlaxoSmithKline, and Home Depot.
  - **Cluster 3**: Contains manufacturers like Boeing, Canon, Caterpillar, Ford, and Honda.
  - **Cluster 4**: Focused on energy companies (ConocoPhillips, Chevron).
  - **Cluster 5**: Has tech companies (Cisco, Dell, HP, IBM).
  - **Cluster 6**: Includes media and telecommunications (Comcast, Cablevision).
  - **Cluster 7**: Is a single-company cluster with CVS.
  - **Cluster 8**: Contains consumer goods companies (Colgate-Palmolive, Kimberly-Clark).

The console output below the image shows the script's execution trace, where it fetched quote history for the listed companies, followed by the clustering results.

The significance of the clustering could be multiple: 
- Companies within the same cluster may have similar financial performance or stock price behaviors.
- The clustering might reflect sector similarities or market perceptions that group these companies together based on their stock movements.
- It may also reflect the model's view of the financial data structure, where companies that react similarly to market events are clustered together.

The clustering results are valuable for portfolio diversification, risk management, and understanding market dynamics. It should be noted that the clusters are algorithmically generated based on the model's criteria, and a financial analyst would likely incorporate additional data and qualitative analysis to interpret these clusters fully.

## Built With

#### Languages and Tools

- **Python**: The primary programming language used for writing the script. Python's simplicity and readability make it an ideal choice for data analysis and scientific computing tasks.

#### Libraries

- **json**: A built-in Python library used for parsing JSON files. It is essential for handling data serialization and deserialization in the JSON format.
  
- **sys**: Another built-in Python library that was used to provide access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter. It is used here primarily for writing output to `stderr`.

- **pandas (pd)**: An open-source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for Python. It is used for reading CSV files into DataFrame objects and handling data manipulation tasks.

- **NumPy (np)**: A library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays. It's used for numerical operations on arrays.

- **matplotlib.pyplot (plt)**: A plotting library for the Python programming language and its numerical mathematics extension NumPy. It provides an object-oriented API for embedding plots into applications using general-purpose GUI toolkits like Tkinter, wxPython, Qt, or GTK. It is used for creating the scatter plot visualization of the clusters.

#### Machine Learning Tools

- **scikit-learn (covariance, cluster)**: Scikit-learn is a free software machine learning library for the Python programming language. It features various classification, regression, and clustering algorithms, including support vector machines, random forests, gradient boosting, k-means, and DBSCAN. The `covariance` module is used to apply the Graphical Lasso algorithm, and the `cluster` module is used for the affinity propagation algorithm for clustering the data.

#### Error Handling

- **urllib.error (URLError)**: Part of the urllib module, it is used to handle the exceptions raised by the `urllib` library used for URL fetching.

#### Data Sources

- **GitHub (Raw Content Delivery)**: The financial data is fetched from a GitHub repository that hosts financial data in CSV format. GitHub serves as a data hosting and delivery platform in this context.

## Getting Started

This section provides instructions on setting up the project locally. To get a local copy up and running, follow these simple steps.

#### Prerequisites

Before running this script, you will need to have Python installed on your machine. Python 3.6 or later is recommended. Additionally, you will need the following Python packages:

- pandas
- numpy
- matplotlib
- scikit-learn

These can be installed using pip if they are not already installed:

```sh
pip install pandas numpy matplotlib scikit-learn
```

#### Installation

1. **Clone the repo**
   ```sh
   git clone https://github.com/your_username_/Project-Name.git
   ```
   Replace `https://github.com/your_username_/Project-Name.git` with the actual repository URL.

2. **Set up a virtual environment (optional but recommended)**
   - For Windows:
     ```sh
     python -m venv venv
     .\venv\Scripts\activate
     ```
   - For Unix or MacOS:
     ```sh
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install required packages**
   ```sh
   pip install -r requirements.txt
   ```
   Ensure you have a `requirements.txt` file that lists the above packages.

4. **Add the symbol map**
   - Create a `symbol_map.json` file in the project directory with the following format:
     ```json
     {
       "AAPL": "Apple Inc.",
       "AMZN": "Amazon.com, Inc.",
       ...
     }
     ```
     Replace the ellipsis (`...`) with additional stock symbols and company names as needed.

5. **Run the script**
   ```sh
   python main.py
   ```
   Replace `main.py` with the actual name of your script.

#### Usage

After installation, run the script using Python to fetch financial data, calculate fluctuations, build a graph model, perform clustering, and visualize the results. The output will include cluster assignments in the console and a scatter plot showing the clustering of financial data.

Remember to check for any errors during the fetching process and ensure that the `symbol_map.json` file is correctly formatted and accessible.

#### Troubleshooting

- If you encounter any errors related to missing packages, make sure you have activated your virtual environment and that you have run the installation command correctly.
- In case of URLError exceptions, ensure that your internet connection is stable and that the URLs in the script are up-to-date and pointing to the correct data sources.

By following these steps, you should have a running instance of the financial data clustering project. For any additional help or if you encounter specific issues, consider reaching out to the community or the maintainers of the project.

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.
* If you have suggestions for adding or removing projects, feel free to [open an issue](https://github.com/TribeOfJudahLion/Financial-Stock-Clustering-And-Visualization-Tool /issues/new) to discuss it, or directly create a pull request after you edit the *README.md* file with necessary changes.
* Please make sure you check your spelling and grammar.
* Create individual PR for each suggestion.
* Please also read through the [Code Of Conduct](https://github.com/TribeOfJudahLion/Financial-Stock-Clustering-And-Visualization-Tool /blob/main/CODE_OF_CONDUCT.md) before posting your first idea as well.

### Creating A Pull Request

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See [LICENSE](https://github.com/TribeOfJudahLion/Financial-Stock-Clustering-And-Visualization-Tool /blob/main/LICENSE.md) for more information.

## Authors

* **Robbie** - *PhD Computer Science Student * - [Robbie](https://github.com/TribeOfJudahLio) - **

## Acknowledgements

* []()
* []()
* []()
