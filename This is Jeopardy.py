#!/usr/bin/env python
# coding: utf-8

# # This is Jeopardy!

# #### Overview

# This project is slightly different than others you have encountered thus far. Instead of a step-by-step tutorial, this project contains a series of open-ended requirements which describe the project you'll be building. There are many possible ways to correctly fulfill all of these requirements, and you should expect to use the internet, Codecademy, and/or other resources when you encounter a problem that you cannot easily solve.

# #### Project Goals

# You will work to write several functions that investigate a dataset of _Jeopardy!_ questions and answers. Filter the dataset for topics that you're interested in, compute the average difficulty of those questions, and train to become the next Jeopardy champion!

# ## Prerequisites

# In order to complete this project, you should have completed the Pandas lessons in the <a href="https://www.codecademy.com/learn/paths/analyze-data-with-python">Analyze Data with Python Skill Path</a>. You can also find those lessons in the <a href="https://www.codecademy.com/learn/data-processing-pandas">Data Analysis with Pandas course</a> or the <a href="https://www.codecademy.com/learn/paths/data-science/">Data Scientist Career Path</a>.
# 
# Finally, the <a href="https://www.codecademy.com/learn/practical-data-cleaning">Practical Data Cleaning</a> course may also be helpful.

# ## Project Requirements

# 1. We've provided a csv file containing data about the game show _Jeopardy!_ in a file named `jeopardy.csv`. Load the data into a DataFrame and investigate its contents. Try to print out specific columns.
# 
#    Note that in order to make this project as "real-world" as possible, we haven't modified the data at all - we're giving it to you exactly how we found it. As a result, this data isn't as "clean" as the datasets you normally find on Codecademy. More specifically, there's something odd about the column names. After you figure out the problem with the column names, you may want to rename them to make your life easier for the rest of the project.
#    
#    In order to display the full contents of a column, we've added this line of code for you:
#    
#    ```py
#    pd.set_option('display.max_colwidth', None)
#    ```

# In[2]:


import pandas as pd
pd.set_option('display.max_colwidth', None)
df = pd.read_csv('jeopardy.csv')
df.rename(columns=lambda x: x.replace(' ','') if x[0]== ' ' else x.replace(' ','_'), inplace= True)


# 2. Write a function that filters the dataset for questions that contains all of the words in a list of words. For example, when the list `["King", "England"]` was passed to our function, the function returned a DataFrame of 49 rows. Every row had the strings `"King"` and `"England"` somewhere in its `" Question"`.
# 
#    Test your function by printing out the column containing the question of each row of the dataset.

# In[3]:


def filter_dataset(df, words_list):
  filtered_dataframe = df[df['Question'].apply(lambda x: all(word in x.split() for word in words_list))]
  return filtered_dataframe
filtered_dataset = filter_dataset(df,['King', 'England'])
print(filtered_dataset.Question)


# 3. Test your original function with a few different sets of words to try to find some ways your function breaks. Edit your function so it is more robust.
# 
#    For example, think about capitalization. We probably want to find questions that contain the word `"King"` or `"king"`.
#    
#    You may also want to check to make sure you don't find rows that contain substrings of your given words. For example, our function found a question that didn't contain the word `"king"`, however it did contain the word `"viking"` &mdash; it found the `"king"` inside `"viking"`. Note that this also comes with some drawbacks &mdash; you would no longer find questions that contained words like `"England's"`.

# In[4]:


def filter_dataset(df, words_list):
  filtered_dataframe = df[df['Question'].apply(lambda x: all(word.lower() in x.lower().split() for word in words_list))]
  return filtered_dataframe
filtered_dataset = filter_dataset(df,['King', 'England'])
print(filtered_dataset.Question)


# 4. We may want to eventually compute aggregate statistics, like `.mean()` on the `" Value"` column. But right now, the values in that column are strings. Convert the`" Value"` column to floats. If you'd like to, you can create a new column with float values.
# 
#    While most of the values in the `" Value"` column represent a dollar amount as a string, note that some do not &mdash; these values will need to be handled differently!
# 
#    Now that you can filter the dataset of question, use your new column that contains the float values of each question to find the "difficulty" of certain topics. For example, what is the average value of questions that contain the word `"King"`?
#    
#    Make sure to use the dataset that contains the float values as the dataset you use in your filtering function.

# In[5]:


def calculate_average_value(df, word):
    df['Value(float)'] = df['Value'].apply(lambda x: float(x.strip('$').replace(',', '')) if x != 'no value' else 0)
    filtered_dataset = df[df['Question'].str.lower().str.contains(word.lower())]
    average_value = filtered_dataset['Value(float)'].mean()
    return average_value

average_value = calculate_average_value(df,'england')
print(average_value)


# 5. Write a function that returns the count of unique answers to all of the questions in a dataset. For example, after filtering the entire dataset to only questions containing the word `"King"`, we could then find all of the unique answers to those questions. The answer "Henry VIII" appeared 55 times and was the most common answer.

# In[6]:


def count_unique_answers(df,word):
  count = df['Answer'].value_counts()
  return count
unique_answers_count = count_unique_answers(df,'king')
print(unique_answers_count)


# ## Solution

# 7. Compare your program to our <a href="https://content.codecademy.com/PRO/independent-practice-projects/jeopardy/jeopardy_solution.zip">sample solution code</a> - remember, that your program might look different from ours (and probably will) and that's okay!

# 8. Great work! Visit <a href="https://discuss.codecademy.com/t/this-is-jeopardy-challenge-project-python-pandas/462365">our forums</a> to compare your project to our sample solution code. You can also learn how to host your own solution on GitHub so you can share it with other learners! Your solution might look different from ours, and that's okay! There are multiple ways to solve these projects, and you'll learn more by seeing others' code.
