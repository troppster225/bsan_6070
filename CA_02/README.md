# Spam Detection Using Naïves Bayes
In this project I create a spam detection model using the multinomial Naïves Bayes algorithm. This assignment entailed reading through a given code file, understanding it, explaining it in plain english, training and testing the model, and finally creating our own version of the code. This project required us to create a training dataset out of a set of emails that were labeled as spam or not spam. We had to programatically go through each file, clean and parse the text, and calculate the frequencies of unique words. The final dataset consists of 3000 of the most common words found in the emails, with counts of those words for each of the emails in the given files. In my version of the code, I was able to get the processing time of the data down to 10 seconds compared to the original codes processing time of over a minute.

## Steps for Running the Code:
1. Clone the repository:
```bash
   git clone git@github.com:troppster225/bsan_6070
```
2. Install the following dependencies if not already installed:
* python 3.11.5
* numpy
* sklearn
* collections
3. Open the CA 02 file
4. Open the Data file
5. Place the test-mails and train-mails folders in the Data file (data comes with the assignment, not available for download from GitHub)
6. Open the CA02_NB_assignment.ipynb file
7. Navigate to the fourth cell and edit the TRAIN_DIR and TEST_DIR variables to match the locations of the test-mails and train-mails folders on your system
8. Run the notebook
9. To see my version, open CA02_myversion.ipynb
10. Repeat step 6
11. Run the notebook