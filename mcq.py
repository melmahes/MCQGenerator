import streamlit as st
import cohere
import os
import pandas as pd

api_key = os.environ.get('CO_API_KEY')
co = cohere.Client(api_key)


def generate_mcq(text,number):
    """Generate multiple choice questions given the text and the number of questions. 
    Arguments: text
    number (int)
    Returns:
    MCQ:
    """
    prompt = f""" Given a TEXT, generate the specified NUMBER of multiple choice questions from the TEXT. Also include solutions and explanations. Here are two examples. Don't ask any variation of "Would you like me to generate questions for a different text or topic?".
    TEXT: {text}
    NUMBER: {number}
    Here are a few examples.


    TEXT: pandas
pandas is a Python library for data wrangling and analysis. It is built around a data
structure called the DataFrame that is modeled after the R DataFrame. Simply put, a
pandas DataFrame is a table, similar to an Excel spreadsheet. pandas provides a great
range of methods to modify and operate on this table; in particular, it allows SQL-like
queries and joins of tables. In contrast to NumPy, which requires that all entries in an
array be of the same type, pandas allows each column to have a separate type (for
example, integers, dates, floating-point numbers, and strings). Another valuable tool
provided by pandas is its ability to ingest from a great variety of file formats and data‐
bases, like SQL, Excel files, and comma-separated values (CSV) files.

matplotlib
matplotlib is the primary scientific plotting library in Python. It provides functions
for making publication-quality visualizations such as line charts, histograms, scatter
plots, and so on. Visualizing your data and different aspects of your analysis can give
you important insights.

First Things First: Look at Your Data
Before building a machine learning model it is often a good idea to inspect the data,
to see if the task is easily solvable without machine learning, or if the desired infor‐
mation might not be contained in the data.
Additionally, inspecting your data is a good way to find abnormalities and peculiari‐
ties. Maybe some of your irises were measured using inches and not centimeters, for
example. In the real world, inconsistencies in the data and unexpected measurements
are very common.
One of the best ways to inspect data is to visualize it. One way to do this is by using a
scatter plot. A scatter plot of the data puts one feature along the x-axis and another
along the y-axis, and draws a dot for each data point. Unfortunately, computer
screens have only two dimensions, which allows us to plot only two (or maybe three)
features at a time. It is difficult to plot datasets with more than three features this way.
One way around this problem is to do a pair plot, which looks at all possible pairs of
features. If you have a small number of features, such as the four we have here, this is
quite reasonable. You should keep in mind, however, that a pair plot does not show
the interaction of all of features at once, so some interesting aspects of the data may
not be revealed when visualizing it this way.


NUMBER: 2


MCQ: What is the primary data structure in the pandas library for data wrangling and analysis?
a) Array
b) DataFrame
c) List
d) Series

What type of visualization does the text recommend for inspecting data with more than three features in a small dataset?
a) Line chart
b) Histogram
c) Pair plot
d) Scatter plot


Here are the answers along with the relevant information from the text:
What is the primary data structure in the pandas library for data wrangling and analysis?
Answer: b) DataFrame
Relevant Text: "It is built around a data structure called the DataFrame that is modeled after the R DataFrame."

What type of visualization does the text recommend for inspecting data with more than three features in a small dataset?
Answer: c) Pair plot
Relevant Text: "One way around this problem is to do a pair plot, which looks at all possible pairs of features. If you have a small number of features, such as the four we have here, this is quite reasonable."
    
TEXT: Cell Transcription
Cell transcription is a fundamental process in molecular biology, where genetic information encoded in DNA is transcribed into RNA molecules. This process is crucial for the synthesis of proteins, the building blocks of cellular structures and functions.
During transcription, an enzyme called RNA polymerase reads the DNA sequence and synthesizes a complementary RNA strand. This newly formed RNA molecule, known as messenger RNA (mRNA), carries the genetic code from the nucleus to the ribosomes in the cytoplasm, where protein synthesis occurs.
Transcription is a highly regulated process, and different types of RNA molecules are transcribed from specific regions of the DNA. Besides mRNA, cells also transcribe transfer RNA (tRNA) and ribosomal RNA (rRNA), both essential for the translation of genetic information into functional proteins.
NUMBER: 2
MCQ: What is the primary role of RNA polymerase during cell transcription?
a) Synthesizing DNA
b) Reading RNA sequence
c) Synthesizing RNA
d) Translating proteins
Which RNA molecule carries the genetic code from the nucleus to the ribosomes for protein synthesis?
a) tRNA
b) rRNA
c) mRNA
d) DNA
Here are the answers along with the relevant information from the text:
What is the primary role of RNA polymerase during cell transcription?
Answer: c) Synthesizing RNA
Relevant Text: "During transcription, an enzyme called RNA polymerase reads the DNA sequence and synthesizes a complementary RNA strand."
Which RNA molecule carries the genetic code from the nucleus to the ribosomes for protein synthesis?
Answer: c) mRNA
Relevant Text: "This newly formed RNA molecule, known as messenger RNA (mRNA), carries the genetic code from the nucleus to the ribosomes in the cytoplasm, where protein synthesis occurs."

    
    """



    response = co.generate(
          model="command",
        prompt=prompt,
        max_tokens=5000,
        temperature=0.7,
        k=0,
    )
    MCQ = response.generations[0].text
    MCQ = MCQ.replace("\n\n--", "").replace("\n--", "").strip()
    MCQ = MCQ.split("\n")

    return MCQ






def run():
    st.title("MCQ GENERATOR")
    text = st.text_area("Paste the text that you would like to generate multiple choice questions for")
    number = st.number_input("number of multiple choice questions to be generated", value = None, step = 1)
    
    if st.button("Generate MCQ"):
        if text and number: 
            MCQ = generate_mcq(text,number)
            for i in MCQ: 
             st.write(i)

if __name__ == "__main__":
    run()
    

