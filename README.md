CHEMICALS IN COSMETICS - PROJECT

The Chemicals in Cosmetics dataset is from the California Safe Cosmetics Program (CSCP) in the California Department of Public Health (CDPH). The data table consists of: label names of cosmetic/personal care products, company/manufacturer names, product brand names, product categories, Chemical Abstracts Service registry numbers (CAS#) of the reported chemical ingredients, names of reported chemical ingredients, the number of reported chemicals for each product, and dates of reporting, product discontinuation or reformulation if applicable. All products containing carcinogens or developmental or reproductive toxicants may not be included due to companies failing to report.
https://data.ca.gov/dataset/chemicals-in-cosmetics/resource/ce65a869-0cae-4742-8118-189c4a2f9847

I have cleaned the data using different methods as:
Dropping columns
Forward filling
Dropping duplicates
Changing the type of columns when necessary
Creating functions to deal with missing values etc.,

My clean data consist of 114381 rows and 16 columns.


Questions to answer after analyzing the data:

1) Which are the Brands who produce and sell the largest breadth of cosmetic products w/o chemicals?

2) Which is the most common chemical present in cosmetic products?

3) How do chemicals distribute across different product categories and in what range?

4) How many chemicals can a specific product contain and what are the corresponding categories for these unique values?

5) How many products removed chemicals during years?

Conclusions:

- There are 123 different chemicals present in cosmetic products. Titanium ioxide is the most common one with a significant difference from the others.

- Make up Products Category has the highest number of products with chemicals, meanwhile Skin Care Products Category has the highest number of chemicals per product.

- The range of chemicals in products varios 0-9 but in average, products contain at least one chemical.

- There are products who removed chemicals during years but the number is negligible.

