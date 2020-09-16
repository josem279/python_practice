#!/usr/bin/env python
# coding: utf-8

# ## Modules for mastering_python file

# In[2]:


def check_if_not_numeric(**args):
    """Checks the dtype of all input arguments to see if it is not numeric"""
    retvalue = True
    for x in args:
        if not(isinstance(x,(int, float))):
            return False
    return True


# In[3]:


def add_all_numerics(*args):
    """Adds all the values and returns their sum"""
    s = 0
    for x in args:
        s += x
    return s


# In[4]:


myname = "PythonCourseParticipant"


# Download this file as a py file to import into desired file
