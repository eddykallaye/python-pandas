#!/usr/bin/env python
# coding: utf-8

# In[19]:


import pandas as pd


# Import all the files

# In[20]:


visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
                   
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])


# Step 1: Inspect the DataFrames using `print` and `head`

# In[21]:


print(visits.head(5))
print(cart.head(5))
print(checkout.head(5))
print(purchase.head(5))


# Step 2: Left merging visits and cart

# In[22]:


visits_cart = pd.merge(visits,cart,how='left')


# Step 3: How long is `visits_cart`?

# In[23]:


print(visits_cart)


# Step 4: How many timestamps are null for `cart_time`?

# In[24]:


null_timestamps_count = visits_cart[visits_cart.cart_time.isnull()]
print(null_timestamps_count)
#Answer: 1652


# Step 5: What percentage only visited?

# In[25]:


percent = (visits_cart['cart_time'].isnull().sum() / len(visits_cart)) * 100
print(percent)
#Answer : 82.6%


# Step 6: What percentage placed a t-shirt in their cart but did not checkout?

# In[26]:


cart_checkout = pd.merge(cart,checkout,how='left')
print(cart_checkout.head())
percent = (cart_checkout['checkout_time'].isnull().sum() / len(cart_checkout)) * 100
print(percent)
#Answer: 35.0%


# Step 7: Merge it all together

# In[27]:


all_data = visits.merge(cart, how='left').merge(checkout,how='left').merge(purchase,how='left')
print(all_data.head())


# Step 8: % of users who got to checkout but did not purchase

# In[28]:


checkouts_notnull= all_data[all_data['checkout_time'].notnull()]
percent = (checkouts_notnull['purchase_time'].isnull().sum() / len(checkouts_notnull)) * 100
print(round(percent,2))
#Answer: 24.55%


# Step 9: check each part of the funnel, let's print all 3 of them again

# In[29]:


# visit to cart: 17.8%
# cart to checkout: 64.95%
# checkout to purchase: 75.45%


# *The weakest part of the funnel is clearly getting a person who visited the site to add a tshirt to their cart. Once they've added a t-shirt to their cart it is fairly likely they end up purchasing it. A suggestion could be to make the add-to-cart button more prominent on the front page.*
# 
# 
# Step 10: adding new column

# In[30]:


all_data['visit_purchase_time'] = all_data['purchase_time'] - all_data['visit_time']


# Step 11: examine the results

# In[31]:


print(all_data.head())


# Step 12: average time to purchase

# In[32]:


print(all_data.visit_purchase_time.mean())

