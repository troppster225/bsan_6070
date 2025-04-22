# Movie Recommendation Engine using kNN
In this project I create a movie recommendation engine using a kNN model and deploy it using Streamlits cloud services. The data used comes from UCI's machine learning repository and has been subset to only include movie genres and IMDB scores. The end goal of the product is to return the top 5 recommended movies to a user looking for movies similar to another movie, in this case "The Post".

## Steps for Running the Code:
1. Clone the repository:
```bash
   git clone git@github.com:troppster225/bsan_6070
```
2. Install the following dependencies if not already installed:
* python 3.11.5
* pandas
* sklearn
* seaborn
* matplotlib
3. Open the CA 05 file
4. Open the CA05.ipynb file
5. Run each cell and read the comments and markdown to understand the process
6. Open the folder in your terminal
7. Type the following:
```bash
   streamlit run app.py
```
8. To access the deployed version, go to this link:
https://mymovierec.streamlit.app/