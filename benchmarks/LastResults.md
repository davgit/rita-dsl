AMD Ryzen 2600, running: `python -m pytest --benchmark-only tests/`


Name| (time in ms)|Min|Max|Mean|StdDev|Median|IQR|Outliers|OPS|Rounds|Iterations|
|---|-------------|---|---|----|------|------|---|--------|---|------|----------|
test_benchmark[standalone_engine]|35.0229 (1.0)|36.4301 (1.0)|35.9338 (1.0)|0.7899 (1.0)|36.3484 (1.0)|1.0554 (1.0)|1|0|27.8289 (1.0)|3|3|
test_benchmark[spacy_engine]|27,214.8203 (777.06)|27,887.0480 (765.49)|27,588.3878 (767.76)|342.3169 (433.36)|27,663.2953 (761.06)|  504.1708 (477.72)|1|0|0.0362 (0.00)|3|3|

