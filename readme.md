# Dataset: Primer meting temperature

## sequence regression - toy dataset

Predict Primer melting tmeperature (Tm) from DNA sequence

``` CATGCATGCTAT..... -> 59.3 ```

## about

bg on primers

## task

regression

## files

- `q5tm.csv` - 504740 data points
- `get_data.py` - uses a `selenium` browser to get data from an online [primer melting temperature web tool](https://tmcalculator.neb.com/#!/main) - little bit silly because the computatin happens locally using `neb-stuff/*` - but I have no idea with js stuff 
- `data.py` - pytorch dataset `TmData` with `x.shape = 504740, 30, 4]` and `y.shape = 504740` - DNA is one hot encoded.
- `neb-stuff/` - files from the web tool page - if anyone knows any js then it'd be great to know how it works
