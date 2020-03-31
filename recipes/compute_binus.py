# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
mytest = dataiku.Dataset("mytest")
mytest_df = mytest.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

binus_df = mytest_df # For this sample code, simply copy input to output


# Write recipe outputs
binus = dataiku.Dataset("binus")
binus.write_with_schema(binus_df)
