#!/usr/bin/env python3
"""
Question Generation Engine for Data Mining Continuous Evaluation.
Parses LaTeX sources from Course/ and TP/ to generate 1000 True/False questions.

Distribution across 6 TPs (~167 questions per TP):
- 150 Plain Standalone questions (25 per TP)
- 350 Trick Standalone questions (~58-59 per TP)
- 500 Trap Questions organized as 250 UNIQUE pairs (numeric flips, direction flips, terminology swaps; 70% hidden, 30% attention_check)
"""

import json
import os
import re
import random

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COURSE_DIR = os.path.join(os.path.dirname(PROJECT_ROOT), "Course", "files")
TP_DIR = os.path.join(os.path.dirname(PROJECT_ROOT), "TP", "files", "practicals")
OUTPUT_PATH = os.path.join(PROJECT_ROOT, "data", "question_bank.json")

def generate_tp1_questions():
    """Generates questions for TP 1: Data Cleaning & Preparation"""
    plain = [
        ("The IQR method identifies outliers as values below Q1 - 1.5*IQR or above Q3 + 1.5*IQR.", True, 1),
        ("In pandas, df.dropna() removes rows containing missing values by default.", True, 1),
        ("Mean imputation is sensitive to extreme outliers present in the dataset.", True, 1),
        ("Z-score normalization assumes the underlying feature follows a Gaussian distribution.", True, 1),
        ("A value with a Z-score of +3.5 is generally considered a potential outlier in a normal distribution.", True, 1),
        ("Median imputation is more robust to extreme skewness than mean imputation.", True, 1),
        ("In pandas, df.duplicated() returns a boolean Series indicating duplicate rows.", True, 1),
        ("MCAR (Missing Completely at Random) implies missingness does not depend on observed or unobserved data.", True, 1),
        ("Forward fill (ffill) propagates the last valid observation forward to fill missing values.", True, 1),
        ("Data cleaning should ideally be performed before model training to prevent data leakage.", True, 1),
        ("Extrapolating missing continuous values with linear interpolation requires sorted index values.", True, 1),
        ("Removing all rows with any missing value can severely reduce sample size if missingness is widespread.", True, 1),
        ("Winsorization replaces extreme values with less extreme values at specified percentiles.", True, 1),
        ("Deduplication based on a subset of columns retains only unique combinations of those columns.", True, 1),
        ("The mode is the preferred imputation statistic for categorical variables with missing entries.", True, 1),
        ("In pandas, df.isna().sum() calculates the total count of missing values per column.", True, 1),
        ("Outliers can significantly distort calculated covariance and variance values.", True, 1),
        ("MAR (Missing at Random) means missingness depends on observed data but not on unobserved values.", True, 1),
        ("Trimming outliers entirely removes extreme observations from the training dataset.", True, 1),
        ("Data consistency checks verify that numerical attributes fall within valid domain bounds.", True, 1),
        ("Deduplication should precede summary statistic computations to prevent duplicate weighting.", True, 1),
        ("Constant imputation replaces missing values with a user-specified default placeholder value.", True, 1),
        ("The Z-score of a data point measures how many standard deviations it lies from the sample mean.", True, 1),
        ("The interquartile range (IQR) is calculated as the difference between the 75th and 25th percentiles.", True, 1),
        ("In pandas, df.fillna(method='bfill') propagates the next valid observation backward.", True, 1)
    ]

    trick = [
        ("Replacing missing values with zero is always equivalent to mean imputation when data is normalized.", False, 1),
        ("Outlier detection using Z-score is completely unaffected by the presence of extreme outliers.", False, 1),
        ("The IQR method assumes the dataset follows a strict standard normal distribution.", False, 1),
        ("In pandas, df.dropna(axis=1) drops rows that contain missing values.", False, 1),
        ("MNAR (Missing Not at Random) data can be safely imputed without introducing bias.", False, 1),
        ("Forward fill (ffill) is the optimal missing value strategy for unordered categorical attributes.", False, 1),
        ("A Z-score threshold of 0 is typically used to flag extreme statistical outliers.", False, 1),
        ("Deduplication automatically fixes incorrect data values and typographical errors in text columns.", False, 1),
        ("Mean imputation increases the overall variance of the attribute column.", False, 1),
        ("Listwise deletion never introduces bias into subsequent statistical model estimates.", False, 1),
        ("The interquartile range (IQR) expands when extreme positive outliers are added to a dataset.", False, 1),
        ("Deleting duplicate rows will alter the sample median of a strictly symmetric distribution.", False, 1),
        ("K-NN imputation requires categorical variables to remain unencoded during distance calculation.", False, 1),
        ("In pandas, df.fillna() modifies the DataFrame in-place by default without needing inplace=True.", False, 1),
        ("Z-score capping preserves the exact parametric mean of the original dataset.", False, 1),
        ("Median imputation is optimal for uniform distributions with heavy tail missingness.", False, 1),
        ("A boxplot upper whisker always extends precisely to Q3 + 1.5*IQR regardless of sample data points.", False, 1),
        ("Data cleaning guarantees that the downstream classification accuracy will increase.", False, 1),
        ("In pandas, df.isna() returns True for empty string values '' in text columns.", False, 1),
        ("Outlier removal should always be conducted prior to analyzing domain specific anomaly events.", False, 1),
        ("Imputing missing values with the mode decreases the frequency of the most common category.", False, 1),
        ("The standard normal Z-score formula uses median and IQR instead of mean and standard deviation.", False, 1),
        ("Linear interpolation is recommended for non-time-series random shuffled categorical columns.", False, 1),
        ("Removing outliers using IQR guarantees that no remaining data point lies outside [-3, 3].", False, 1),
        ("Data leakage occurs when test set missing values are imputed using test set statistics only.", False, 1),
        ("Truncating missing values to 0 preserves the exact variance of the target feature.", False, 1),
        ("In pandas, df.duplicated(keep=False) marks only the second occurrence of duplicate rows.", False, 1),
        ("Z-score transformation changes a highly skewed right distribution into a symmetric normal curve.", False, 1),
        ("Mean imputation preserves the correlation structure between attributes in multivariate data.", False, 1),
        ("Outliers identified by Z-score are guaranteed to be data entry errors rather than genuine extreme events.", False, 1),
        ("Listwise deletion is more sample-efficient than pairwise deletion when handling missing data.", False, 1),
        ("Capping outliers at the 99th percentile increases the maximum value of the dataset.", False, 1),
        ("In pandas, df.isna().any() returns a single boolean scalar for the entire DataFrame.", False, 1),
        ("The median is more sensitive to extreme maximum values than the arithmetic mean.", False, 1),
        ("Outlier detection using IQR can only be applied to continuous variables following a Gaussian distribution.", False, 1),
        ("In pandas, df.drop_duplicates() modifies original index order by resetting it to 0..N-1 automatically.", False, 1),
        ("Mean imputation increases correlation coefficients between imputed variables.", False, 1),
        ("A negative Z-score indicates that a data point lies above the population mean.", False, 1),
        ("Boxplot whiskers can extend up to 3.0*IQR to mark mild outliers.", False, 1),
        ("Single imputation methods capture the uncertainty of missing values better than multiple imputation.", False, 1),
        ("Imputing missing values in the target variable with feature means improves generalization.", False, 1),
        ("Data cleaning removes the need for cross-validation during evaluation.", False, 1),
        ("Deduplication should be applied after splitting data into train and test sets to avoid data leakage.", False, 1),
        ("In pandas, df.isna().sum().sum() returns the count of non-missing values in a DataFrame.", False, 1),
        ("Forward fill is valid for cross-sectional data sorted alphabetically by student name.", False, 1),
        ("Outliers always reduce the training accuracy of Decision Tree algorithms.", False, 1),
        ("Z-score outlier detection requires at least 10,000 samples to be mathematically valid.", False, 1),
        ("The interquartile range (IQR) equals the difference between the maximum and minimum values.", False, 1),
        ("In pandas, df.replace() can only replace numeric values and cannot handle strings.", False, 1),
        ("Mean imputation reduces the statistical power of subsequent hypothesis tests by artificially reducing variance.", False, 1),
        ("Extreme outliers have no effect on the calculation of Pearson correlation coefficients.", False, 1),
        ("Data cleaning steps can be skipped if using robust non-parametric models like Random Forest.", False, 1),
        ("In pandas, dropna(thresh=2) drops rows with more than 2 non-NA values.", False, 1),
        ("MCAR assumptions can be verified definitively using single univariate normality tests.", False, 1),
        ("Removing outliers always leads to higher model performance on unseen test data.", False, 1),
        ("Interpolation methods work independently of sample order in tabular data.", False, 1),
        ("Median imputation changes the ranking order of non-missing observations in a feature.", False, 1),
        ("Outlier detection via IQR is affected by non-linear monotonic transformations of the feature.", False, 1),
        ("Linear interpolation assumes a constant rate of change between adjacent known data points.", True, 1)
    ]

    # 42 UNIQUE Trap Pairs for TP1 (group_id 1..42)
    tp1_trap_definitions = [
        ("The lower bound for IQR outlier detection is defined as Q1 - 1.5 * IQR.", "The lower bound for IQR outlier detection is defined as Q1 - 2.5 * IQR."),
        ("The upper bound for IQR outlier detection is defined as Q3 + 1.5 * IQR.", "The upper bound for IQR outlier detection is defined as Q3 + 2.5 * IQR."),
        ("In pandas, df.dropna(axis=0) removes rows containing missing values.", "In pandas, df.dropna(axis=0) removes columns containing missing values."),
        ("In pandas, df.dropna(axis=1) removes columns containing missing values.", "In pandas, df.dropna(axis=1) removes rows containing missing values."),
        ("Mean imputation preserves the sample mean of the feature column.", "Mean imputation preserves the sample variance of the feature column."),
        ("Median imputation is resistant to extreme numerical outliers.", "Median imputation is sensitive to extreme numerical outliers."),
        ("The Z-score of a sample point is calculated as (x - mean) / std.", "The Z-score of a sample point is calculated as (x - std) / mean."),
        ("A positive Z-score indicates that a observation lies above the sample mean.", "A positive Z-score indicates that a observation lies below the sample mean."),
        ("Forward fill (ffill) propagates the last valid value forward to replace missing entries.", "Forward fill (ffill) propagates the next valid value backward to replace missing entries."),
        ("Backward fill (bfill) propagates the next valid value backward to replace missing entries.", "Backward fill (bfill) propagates the last valid value forward to replace missing entries."),
        ("MCAR implies missingness is completely independent of observed and unobserved variables.", "MCAR implies missingness depends directly on observed feature values."),
        ("MAR implies missingness depends on observed data but not on unobserved data.", "MAR implies missingness depends on unobserved data but not on observed data."),
        ("Mode imputation replaces missing cells with the most frequent categorical value.", "Mode imputation replaces missing cells with the arithmetic average of numeric values."),
        ("Listwise deletion removes all rows that contain at least one missing cell.", "Listwise deletion removes only the specific missing cells while keeping the row."),
        ("Winsorization caps extreme outliers at pre-specified percentile thresholds.", "Winsorization deletes extreme outlier rows completely from the dataset."),
        ("Deduplication using df.drop_duplicates() keeps the first occurrence by default.", "Deduplication using df.drop_duplicates() keeps the last occurrence by default."),
        ("Interpolation computes replacement values based on neighboring known observations.", "Interpolation computes replacement values by taking the global column mode."),
        ("In pandas, df.isna() returns True for missing values like NaN and None.", "In pandas, df.isna() returns False for missing values like NaN and None."),
        ("The Interquartile Range (IQR) is calculated as Q3 - Q1.", "The Interquartile Range (IQR) is calculated as Q1 - Q3."),
        ("Trimming removes outlier observations completely from the dataset.", "Trimming caps outlier observations at maximum allowed boundary values."),
        ("Z-score threshold of 3.0 flags points more than 3 standard deviations from mean.", "Z-score threshold of 3.0 flags points more than 3 interquartile ranges from mean."),
        ("Mean imputation artificially decreases the variance of the imputed variable.", "Mean imputation artificially increases the variance of the imputed variable."),
        ("Data leakage happens when test set statistics are used during training data preprocessing.", "Data leakage happens when training set statistics are used during test data preprocessing."),
        ("Pairwise deletion keeps cases that have valid values for the specific variables analyzed.", "Pairwise deletion removes entire cases if any variable in the dataset is missing."),
        ("Single imputation substitutes one single value for each missing value.", "Single imputation generates multiple plausible datasets to model uncertainty."),
        ("In pandas, df.fillna(0) replaces all NA entries with the integer value zero.", "In pandas, df.fillna(0) replaces all NA entries with the column mean."),
        ("Capping outliers modifies extreme values without changing dataset sample size.", "Capping outliers deletes extreme values and reduces dataset sample size."),
        ("Z-score normalization transforms a feature to have a mean of 0 and std of 1.", "Z-score normalization transforms a feature to have a min of 0 and max of 1."),
        ("In pandas, df.duplicated() returns a boolean Series marking duplicate rows.", "In pandas, df.duplicated() returns a list of column names that contain duplicate values."),
        ("Robust scaler uses median and IQR to normalize features.", "Robust scaler uses mean and standard deviation to normalize features."),
        ("Linear interpolation requires data to be ordered logically along an index.", "Linear interpolation requires data to be randomly shuffled before calculation."),
        ("Mode is the only central tendency metric applicable to nominal categorical variables.", "Mean is the only central tendency metric applicable to nominal categorical variables."),
        ("MNAR missingness depends on the unobserved value itself.", "MNAR missingness is completely independent of the unobserved value."),
        ("Data cleaning should be performed prior to feature scaling transformations.", "Data cleaning should be performed after model training is finished."),
        ("Outlier detection using boxplots relies on quartiles Q1 and Q3.", "Outlier detection using boxplots relies on sample mean and standard deviation."),
        ("In pandas, df.isna().sum() sums missing values column by column.", "In pandas, df.isna().sum() sums non-missing values row by row."),
        ("Zero imputation introduces bias if zero is a meaningful non-missing measurement.", "Zero imputation preserves unbiased distribution properties when zero is a valid measure."),
        ("Constant fill replaces missing values with a designated fixed placeholder.", "Constant fill replaces missing values with linear regression predictions."),
        ("Extrapolating estimates missing values outside the range of observed data points.", "Extrapolating estimates missing values inside the range of observed data points."),
        ("Deduplication on a primary key ensures each entity appears exactly once.", "Deduplication on a primary key ensures each feature column has equal variance."),
        ("Trimming reduces sample size N when extreme outliers are removed.", "Trimming increases sample size N by imputing synthetic outlier observations."),
        ("A boxplot displays the 25th, 50th, and 75th percentiles of a continuous distribution.", "A boxplot displays the 10th, 50th, and 90th percentiles of a continuous distribution.")
    ]

    traps = []
    for i, (text_true, text_false) in enumerate(tp1_trap_definitions, 1):
        mode = "hidden" if i <= 30 else "attention_check"
        traps.append((text_true, True, mode, i))
        traps.append((text_false, False, mode, i))

    return plain, trick, traps

def generate_tp2_questions():
    """Generates questions for TP 2: Exploratory Data Analysis (EDA)"""
    plain = [
        ("The sample mean is sensitive to extreme values in a skewed distribution.", True, 2),
        ("Pearson correlation measures linear relationships between continuous variables.", True, 2),
        ("A Spearman correlation of +1.0 indicates a perfect monotonic relationship.", True, 2),
        ("In a right-skewed distribution, the mean is typically greater than the median.", True, 2),
        ("A boxplot visually displays the median, IQR, and potential outliers of a dataset.", True, 2),
        ("Covariance measures the direction of linear association between two quantitative variables.", True, 2),
        ("Histograms display the frequency distribution of a continuous feature divided into bins.", True, 2),
        ("Zero correlation between two variables does not necessarily imply independence.", True, 2),
        ("The variance of a sample is the average of squared deviations from the mean.", True, 2),
        ("Spearman correlation is calculated based on rank order rather than raw metric values.", True, 2),
        ("Kurtosis measures the heavy-tailedness or lightness of tails relative to a normal distribution.", True, 2),
        ("Scatter plots are used to visualize the bivariate relationship between two continuous variables.", True, 2),
        ("A correlation matrix is symmetric across its main diagonal.", True, 2),
        ("The diagonal entries of a standardized correlation matrix are all equal to 1.0.", True, 2),
        ("Positive skewness indicates a distribution with a tail extending towards higher positive values.", True, 2),
        ("Pairplots show scatter plots for all pairs of continuous variables in a dataset.", True, 2),
        ("The median divides a dataset into two halves containing equal numbers of observations.", True, 2),
        ("Standard deviation is expressed in the same physical units as the original data measurement.", True, 2),
        ("A heat map is effective for visualizing correlation matrices using color gradients.", True, 2),
        ("Negative covariance indicates that as one variable increases, the other tends to decrease.", True, 2),
        ("A bimodal distribution contains two local modes or peaks in its probability density.", True, 2),
        ("The 50th percentile of a sample distribution corresponds to the sample median.", True, 2),
        ("Cross-tabulation (contingency tables) summarizes the joint frequency distribution of categorical attributes.", True, 2),
        ("Quantile-Quantile (Q-Q) plots assess whether a sample distribution matches a theoretical distribution.", True, 2),
        ("The standard error of the mean decreases as the sample size increases.", True, 2)
    ]

    trick = [
        ("Pearson correlation coefficient ranges from -100 to +100 depending on variance scaling.", False, 2),
        ("A Pearson correlation of 0 guarantees that two continuous variables are completely independent.", False, 2),
        ("In a left-skewed distribution, the mean is strictly greater than the median and mode.", False, 2),
        ("Spearman rank correlation requires both attributes to follow a Gaussian normal distribution.", False, 2),
        ("Covariance values are bounded strictly between -1.0 and +1.0 regardless of measurement scale.", False, 2),
        ("A boxplot box width represents the total range (Max - Min) of the dataset.", False, 2),
        ("Histograms are used to visualize the exact joint frequency distribution of two categorical features.", False, 2),
        ("High correlation between two features directly implies a causal relationship between them.", False, 2),
        ("The variance of a feature can be negative if values lie between 0 and 1.", False, 2),
        ("Adding a constant value to all data points changes the sample standard deviation proportionally.", False, 2),
        ("A symmetric distribution always has a sample kurtosis of exactly zero.", False, 2),
        ("Bar charts and histograms are identical plots used interchangeably for continuous variables.", False, 2),
        ("The correlation between feature X and feature Y can differ from the correlation between Y and X.", False, 2),
        ("Pearson correlation is robust against non-linear monotonic relationships.", False, 2),
        ("Skewness is measured in squared units of the original feature variable.", False, 2),
        ("The median of a sample changes when all values are multiplied by a positive constant.", False, 2),
        ("Covariance between two variables is zero if and only if they are linearly correlated.", False, 2),
        ("Scatter plot matrices can only display continuous variables against categorical targets.", False, 2),
        ("Standard deviation is insensitive to extreme value outliers.", False, 2),
        ("In pandas, df.describe() includes mode calculations for numeric columns by default.", False, 2),
        ("A correlation of -0.9 indicates a much weaker relationship than a correlation of +0.3.", False, 2),
        ("Spearman correlation measures linear relationships while Pearson measures rank monotonic relationships.", False, 2),
        ("Q-Q plot points forming a straight line indicate severe deviation from normality.", False, 2),
        ("The empirical rule states that 99.7% of data lies within 1 standard deviation of the mean.", False, 2),
        ("A boxplot whisker length is proportional to the mean standard error of the sample.", False, 2),
        ("Multivariate EDA eliminates the need for checking univariate distributions.", False, 2),
        ("Logarithmic transformation increases the positive skewness of a right-skewed variable.", False, 2),
        ("A heatmap requires input data to be strictly non-negative values.", False, 2),
        ("The mode is always unique for any given continuous numerical dataset.", False, 2),
        ("Sample standard deviation uses N in the denominator instead of N-1 for unbiased estimation.", False, 2),
        ("Covariance retains the same value regardless of changes in unit measurement scale.", False, 2),
        ("Zero skewness guarantees that a probability distribution is perfectly Gaussian normal.", False, 2),
        ("In pandas, df.corr() computes Spearman correlation by default unless specified otherwise.", False, 2),
        ("Violin plots display only the mean and standard deviation without density estimates.", False, 2),
        ("Pearson correlation can accurately capture quadratic parabolic relationships between variables.", False, 2),
        ("Extreme outliers increase the median more than they increase the sample mean.", False, 2),
        ("A scatter plot with points forming a circle represents a correlation of r = 1.0.", False, 2),
        ("High variance in a feature indicates that all data points are clustered near the mean.", False, 2),
        ("Cross-tabulation can only be computed for continuous numerical variables.", False, 2),
        ("Standardizing a dataset changes its Pearson correlation coefficient with another variable.", False, 2),
        ("Bimodal distributions always have equal frequency counts in both local modes.", False, 2),
        ("The range of a dataset is resistant to extreme outliers.", False, 2),
        ("Spearman correlation is sensitive to linear scaling of raw values.", False, 2),
        ("Linear correlation implies non-linear independence in all cases.", False, 2),
        ("Density plots represent discrete probability mass functions for continuous attributes.", False, 2),
        ("The mean absolute deviation (MAD) is always larger than the sample variance.", False, 2),
        ("Skewness values above +1 indicate a left-skewed distribution with a heavy left tail.", False, 2),
        ("In pandas, df.skew() returns 0 for a dataset with all identical values.", False, 2),
        ("Histograms with 100 bins always reveal the true underlying distribution better than 10 bins.", False, 2),
        ("Boxplots display individual data points for all observations inside the IQR box.", False, 2),
        ("Correlation coefficients change sign when features are shifted by adding a positive constant.", False, 2),
        ("Pairplots can only process maximum 3 variables simultaneously in seaborn.", False, 2),
        ("Covariance is dimensionless and unconstrained by feature measurement units.", False, 2),
        ("Negative kurtosis indicates a distribution with heavier tails than a normal distribution.", False, 2),
        ("Calculating Spearman correlation on ranked data yields a different value than Pearson correlation on ranks.", False, 2),
        ("The 75th percentile is also known as the first quartile (Q1).", False, 2),
        ("EDA should only be performed after model evaluation is complete.", False, 2),
        ("Summary statistics provide a complete description of distribution shape without visualization.", False, 2),
        ("Covariance between two standardized features equals their Pearson correlation coefficient.", True, 2)
    ]

    # 42 UNIQUE Trap Pairs for TP2 (group_id 43..84)
    tp2_trap_definitions = [
        ("Pearson correlation measures linear relationships between continuous variables.", "Pearson correlation measures non-linear monotonic relationships between continuous variables."),
        ("Spearman correlation measures monotonic relationships using feature rank orders.", "Spearman correlation measures linear relationships using raw metric values."),
        ("In a right-skewed distribution, the mean is greater than the median.", "In a right-skewed distribution, the mean is less than the median."),
        ("In a left-skewed distribution, the mean is less than the median.", "In a left-skewed distribution, the mean is greater than the median."),
        ("A Pearson correlation coefficient ranges strictly between -1.0 and +1.0.", "A Pearson correlation coefficient ranges strictly between 0.0 and +1.0."),
        ("Covariance values depend on the measurement units of the input variables.", "Covariance values are dimensionless and independent of input measurement units."),
        ("Pearson correlation is dimensionless and unconstrained by measurement units.", "Pearson correlation depends directly on the physical units of measurement."),
        ("A scatter plot visualizes the bivariate relationship between two continuous attributes.", "A scatter plot visualizes the univariate frequency distribution of one continuous attribute."),
        ("Histograms group continuous data into discrete numerical bins.", "Histograms group categorical nominal data into ordered discrete categories."),
        ("Boxplots display the median as a line inside the interquartile range box.", "Boxplots display the arithmetic mean as a line inside the interquartile range box."),
        ("Positive skewness indicates a long tail extending toward higher positive values.", "Positive skewness indicates a long tail extending toward lower negative values."),
        ("Negative skewness indicates a long tail extending toward lower negative values.", "Negative skewness indicates a long tail extending toward higher positive values."),
        ("Kurtosis measures the tail weight and peakedness of a distribution relative to normal.", "Kurtosis measures the directional asymmetry of a distribution relative to normal."),
        ("A correlation matrix is always symmetric across its main diagonal.", "A correlation matrix is always asymmetric across its main diagonal."),
        ("The diagonal values of a correlation matrix are all equal to 1.0.", "The diagonal values of a correlation matrix are all equal to 0.0."),
        ("Zero Pearson correlation implies no linear association between two variables.", "Zero Pearson correlation guarantees complete statistical independence between two variables."),
        ("The median is the 50th percentile of an ordered sample distribution.", "The median is the 75th percentile of an ordered sample distribution."),
        ("The first quartile (Q1) corresponds to the 25th percentile of a sample.", "The first quartile (Q1) corresponds to the 50th percentile of a sample."),
        ("The third quartile (Q3) corresponds to the 75th percentile of a sample.", "The third quartile (Q3) corresponds to the 25th percentile of a sample."),
        ("Variance is measured in squared units of the original attribute.", "Variance is measured in the exact same physical units as the original attribute."),
        ("Standard deviation is expressed in the same units as the original feature.", "Standard deviation is expressed in squared units of the original feature."),
        ("Cross-tabulation computes joint frequency distributions between categorical features.", "Cross-tabulation computes continuous covariance matrices between numerical features."),
        ("Violin plots combine boxplots with kernel density probability estimates.", "Violin plots combine scatter plots with linear regression trendlines."),
        ("Q-Q plots compare sample quantiles against theoretical distribution quantiles.", "Q-Q plots compare bivariate sample correlation against covariance matrices."),
        ("Spearman correlation is robust against extreme numerical outliers.", "Spearman correlation is highly sensitive to extreme numerical outliers."),
        ("Pearson correlation of +1.0 indicates a perfect positive linear relationship.", "Pearson correlation of +1.0 indicates a perfect positive monotonic non-linear relationship."),
        ("Pearson correlation of -1.0 indicates a perfect negative linear relationship.", "Pearson correlation of -1.0 indicates zero association between variables."),
        ("Standardizing variables does not change their Pearson correlation coefficient.", "Standardizing variables doubles their Pearson correlation coefficient."),
        ("Bimodal distributions feature two distinct local modes or frequency peaks.", "Bimodal distributions feature no local modes and a completely flat density."),
        ("Interquartile range (IQR) measures the spread of the middle 50% of data.", "Interquartile range (IQR) measures the spread of the outer 10% of data."),
        ("Mean absolute deviation (MAD) measures average distance of points from mean.", "Mean absolute deviation (MAD) measures squared distance of points from mean."),
        ("Correlation of 0.8 represents a stronger linear relationship than 0.3.", "Correlation of 0.3 represents a stronger linear relationship than -0.8."),
        ("Correlation of -0.9 represents a stronger linear relationship than +0.4.", "Correlation of +0.4 represents a stronger linear relationship than -0.9."),
        ("Adding a constant shift to a variable leaves its variance unchanged.", "Adding a constant shift to a variable increases its variance proportionally."),
        ("Multiplying a variable by a constant scale factor scales its standard deviation.", "Multiplying a variable by a constant scale factor leaves its standard deviation unchanged."),
        ("Scatter plot matrices display pairwise relationships for multiple continuous attributes.", "Scatter plot matrices display decision tree rules for classification features."),
        ("High variance indicates data points are spread out widely around the mean.", "High variance indicates data points are tightly clustered at the exact mean."),
        ("Contingency tables display frequency counts for combinations of categorical levels.", "Contingency tables display continuous regression residuals for fitted models."),
        ("Heatmaps use color intensity gradients to visualize numerical matrix values.", "Heatmaps use dendrogram branch lengths to visualize cluster distance thresholds."),
        ("Range is calculated as maximum value minus minimum value.", "Range is calculated as upper quartile Q3 minus lower quartile Q1."),
        ("Empirical rule states that ~68% of normal data lies within 1 standard deviation.", "Empirical rule states that ~95% of normal data lies within 1 standard deviation."),
        ("Empirical rule states that ~95% of normal data lies within 2 standard deviations.", "Empirical rule states that ~68% of normal data lies within 2 standard deviations.")
    ]

    traps = []
    for i, (text_true, text_false) in enumerate(tp2_trap_definitions, 43):
        mode = "hidden" if i <= 72 else "attention_check"
        traps.append((text_true, True, mode, i))
        traps.append((text_false, False, mode, i))

    return plain, trick, traps

def generate_tp3_questions():
    """Generates questions for TP 3: Data Preprocessing & Feature Engineering"""
    plain = [
        ("MinMaxScaler scales feature values into a fixed range, typically between 0 and 1.", True, 3),
        ("StandardScaler centers data by subtracting the mean and scaling to unit variance.", True, 3),
        ("One-Hot Encoding creates K binary dummy variables for a categorical feature with K categories.", True, 3),
        ("PCA (Principal Component Analysis) projects high-dimensional data onto orthogonal axes of maximum variance.", True, 3),
        ("RobustScaler uses the median and IQR, making it less sensitive to extreme outliers.", True, 3),
        ("Feature scaling is crucial for distance-based algorithms like K-NN and SVM.", True, 3),
        ("Label Encoding assigns an integer code to each unique category in a ordinal variable.", True, 3),
        ("Tree-based models like Decision Trees are invariant to monotonic feature scaling transformations.", True, 3),
        ("The first principal component accounts for the largest possible variance in the dataset.", True, 3),
        ("Dummy variable trap occurs when one-hot encoded features are perfectly multicollinear.", True, 3),
        ("PCA principal components are linear combinations of the original input features.", True, 3),
        ("Eigenvalues of the covariance matrix represent the variance explained by corresponding principal components.", True, 3),
        ("Target Encoding replaces categorical levels with the average target value for each category.", True, 3),
        ("Feature selection reduces dimensionality by retaining a subset of original features without transformation.", True, 3),
        ("MinMaxScaler is sensitive to extreme outliers because min and max values define the scaling bound.", True, 3),
        ("StandardScaler produces transformed features with a mean of 0 and standard deviation of 1.", True, 3),
        ("One-Hot Encoding with drop='first' avoids perfect multicollinearity in linear models.", True, 3),
        ("PCA eigenvectors determine the directions of the new principal component axes.", True, 3),
        ("Interaction terms are generated by multiplying two or more existing features together.", True, 3),
        ("Polynomial features expand feature space by generating all degree-d combinations of attributes.", True, 3),
        ("Feature scaling parameters (mean, std, min, max) must be fitted on training data only.", True, 3),
        ("Dimensionality reduction helps alleviate the curse of dimensionality in high-dimensional space.", True, 3),
        ("Variance Thresholding removes features whose sample variance falls below a designated threshold.", True, 3),
        ("Sequential Feature Selection iteratively adds or removes features based on model cross-validation score.", True, 3),
        ("Standardizing features ensures equal weighting in distance metric calculations.", True, 3)
    ]

    trick = [
        ("StandardScaler bounds scaled output values strictly between -1.0 and +1.0.", False, 3),
        ("MinMaxScaler is unaffected by the presence of extreme minimum or maximum outliers.", False, 3),
        ("Label Encoding should be applied to nominal categories with no inherent ordinal ranking.", False, 3),
        ("PCA transforms features into non-linear orthogonal polynomial curves.", False, 3),
        ("Decision Trees perform significantly better after applying StandardScaler normalization.", False, 3),
        ("One-Hot Encoding reduces the total number of features in high-cardinality datasets.", False, 3),
        ("The sum of variances of all PCA components is smaller than the total variance of original features.", False, 3),
        ("StandardScaler should be fitted on the combined train and test dataset before splitting.", False, 3),
        ("PCA principal components are correlated with each other by design.", False, 3),
        ("RobustScaler uses mean and standard deviation to scale feature vectors.", False, 3),
        ("Label Encoding creates K separate binary columns for K unique categorical labels.", False, 3),
        ("MinMaxScaler preserves zero values in sparse matrices without dense conversion.", False, 3),
        ("Feature extraction selects a subset of original attributes without altering feature definitions.", False, 3),
        ("Principal components are always ranked in order of decreasing correlation with the target class.", False, 3),
        ("One-Hot Encoding guarantees that linear regression models will not overfit.", False, 3),
        ("PCA can be applied directly to unencoded categorical attributes without numerical conversion.", False, 3),
        ("Target Encoding never risks target leakage or overfitting on small training samples.", False, 3),
        ("Polynomial features reduce the total number of dimensions in the transformed dataset.", False, 3),
        ("RobustScaler sets feature variance to exactly 1.0 regardless of sample distribution.", False, 3),
        ("In scikit-learn, fit_transform() should be called on the test dataset.", False, 3),
        ("MinMaxScaler transforms any non-Gaussian feature into a perfect standard normal curve.", False, 3),
        ("The first principal component always captures 100% of total sample variance.", False, 3),
        ("Ordinal Encoding loses ranking information when converting ordered categories to numbers.", False, 3),
        ("L1 regularization (Lasso) performs feature selection by setting coefficient weights to zero.", False, 3),
        ("StandardScaler modifies the correlation coefficient between two scaled features.", False, 3),
        ("Feature engineering can be completely automated without domain knowledge or data analysis.", False, 3),
        ("PCA eigenvectors are non-orthogonal vectors in the feature space.", False, 3),
        ("One-Hot Encoding with high-cardinality features improves memory efficiency.", False, 3),
        ("MinMaxScaler produces negative output values when input data contains only positive numbers.", False, 3),
        ("PCA requires target class labels to calculate the principal component directions.", False, 3),
        ("Scaling features is required before calculating Random Forest feature importances.", False, 3),
        ("Variance Thresholding removes features that have high correlation with the target variable.", False, 3),
        ("Target Encoding replaces categorical values with their frequency counts in the dataset.", False, 3),
        ("PCA projection retains the original feature column names and physical interpretations.", False, 3),
        ("StandardScaler relies on median and IQR to compute scaling factors.", False, 3),
        ("One-Hot Encoding works optimally for high-cardinality features with over 10,000 unique values.", False, 3),
        ("RobustScaler scales data using the minimum and maximum observed values.", False, 3),
        ("PCA variance explained ratio is independent of initial feature scaling.", False, 3),
        ("Label Encoding introduces artificial magnitude order relationships into nominal categories.", False, 3),
        ("Filtering features using correlation threshold guarantees improved model classification accuracy.", False, 3),
        ("MinMaxScaler maps negative input values into positive range [0, 1].", False, 3),
        ("Feature selection using Recursive Feature Elimination (RFE) operates independently of any base estimator.", False, 3),
        ("PCA components are always ordered by increasing variance explained.", False, 3),
        ("StandardScaler should be re-fitted separately on each mini-batch during prediction.", False, 3),
        ("Polynomial features of degree 2 for 10 features generate fewer than 15 total features.", False, 3),
        ("Frequency encoding replaces categories with their target probability distribution.", False, 3),
        ("One-Hot Encoding causes the dummy variable trap in tree-based algorithms.", False, 3),
        ("PCA can reduce dimensionality only if input features are perfectly linear.", False, 3),
        ("MinMaxScaler formula is (x - mean) / (max - min).", False, 3),
        ("Feature transformation always increases the total variance of the dataset.", False, 3),
        ("StandardScaler is less sensitive to extreme outliers than RobustScaler.", False, 3),
        ("Label Binarizer is restricted to single-label binary classification targets.", False, 3),
        ("PCA principal components retain physical measurement units of the original input features.", False, 3),
        ("Scaling features changes the optimal split decisions in a Decision Tree model.", False, 3),
        ("One-Hot Encoding creates ordinal numerical values for text features.", False, 3),
        ("L2 regularization (Ridge) sets redundant feature coefficients to exact zero.", False, 3),
        ("Scree plots show the cumulative loss function value per PCA component.", False, 3),
        ("Data scaling must be re-executed after cross-validation folds are created.", False, 3),
        ("Principal component analysis minimizes the orthogonal Euclidean distance to the fitted linear hyperplane.", True, 3)
    ]

    # 42 UNIQUE Trap Pairs for TP3 (group_id 85..126)
    tp3_trap_definitions = [
        ("StandardScaler normalizes features to have a mean of 0 and a standard deviation of 1.", "StandardScaler normalizes features to have a median of 0 and an interquartile range of 1."),
        ("MinMaxScaler maps feature values into a bounded range between 0 and 1.", "MinMaxScaler maps feature values into an unbounded range centered at zero."),
        ("RobustScaler uses median and IQR to scale features in the presence of outliers.", "RobustScaler uses sample mean and standard deviation to scale features in the presence of outliers."),
        ("One-Hot Encoding creates K binary dummy columns for K unique categories.", "One-Hot Encoding creates a single integer column containing unique numerical category IDs."),
        ("Label Encoding converts categorical categories into ordered integer labels.", "Label Encoding creates K separate binary vector columns for nominal categories."),
        ("PCA projects high-dimensional data onto orthogonal directions of maximum variance.", "PCA projects high-dimensional data onto non-orthogonal directions of minimum variance."),
        ("The first principal component accounts for the largest proportion of total variance.", "The first principal component accounts for the smallest proportion of total variance."),
        ("PCA principal components are uncorrelated with each other.", "PCA principal components are highly correlated with each other by design."),
        ("Tree-based algorithms are invariant to monotonic feature scaling transformations.", "Tree-based algorithms require features to be scaled using StandardScaler prior to training."),
        ("Distance-based algorithms like KNN require features to be normalized on equal scales.", "Distance-based algorithms like KNN perform identically regardless of feature scale differences."),
        ("Target Encoding replaces categories with the mean target value of each class level.", "Target Encoding replaces categories with principal component score coordinates."),
        ("Feature selection retains a subset of original features without changing their definitions.", "Feature selection transforms original features into linear combinations of new components."),
        ("Feature extraction creates new transformed features from combinations of original inputs.", "Feature extraction removes low-variance columns while preserving original feature names."),
        ("Dummy variable trap occurs when one-hot encoded columns exhibit perfect multicollinearity.", "Dummy variable trap occurs when features are normalized to zero mean."),
        ("Dropping one dummy column (drop='first') eliminates perfect multicollinearity in linear models.", "Dropping one dummy column (drop='first') increases multicollinearity in linear models."),
        ("Scaling parameters must be fitted exclusively on the training dataset to prevent data leakage.", "Scaling parameters must be fitted on the combined train and test dataset before splitting."),
        ("Eigenvalues of the covariance matrix represent the variance captured by each principal component.", "Eigenvalues of the covariance matrix represent the classification error rate of each component."),
        ("Scree plot displays the variance explained by each principal component in descending order.", "Scree plot displays the correlation between features and target labels in ascending order."),
        ("PCA is an unsupervised dimensionality reduction method operating without target labels.", "PCA is a supervised dimensionality reduction method requiring target class labels."),
        ("Ordinal Encoding preserves inherent logical ranking order among categorical levels.", "Ordinal Encoding converts ordered categories into unordered binary dummy vectors."),
        ("MinMaxScaler formula subtracts the minimum value and divides by the feature range.", "MinMaxScaler formula subtracts the sample mean and divides by standard deviation."),
        ("StandardScaler formula subtracts the sample mean and divides by standard deviation.", "StandardScaler formula subtracts the minimum value and divides by the feature range."),
        ("RobustScaler formula subtracts the median and divides by the interquartile range (IQR).", "RobustScaler formula subtracts the mode and divides by total range (Max - Min)."),
        ("L1 regularization (Lasso) can reduce feature weights to exact zero for feature selection.", "L2 regularization (Ridge) reduces feature weights to exact zero for feature selection."),
        ("L2 regularization (Ridge) shrinks feature weights toward zero without driving them to exact zero.", "L1 regularization (Lasso) shrinks feature weights toward zero without driving them to exact zero."),
        ("PolynomialFeatures generates degree-d power combinations of input attributes.", "PolynomialFeatures applies logarithmic transformations to continuous attributes."),
        ("VarianceThreshold removes features whose sample variance falls below a designated threshold.", "VarianceThreshold removes features whose correlation with target falls below a threshold."),
        ("Recursive Feature Elimination (RFE) selects features by recursively pruning smallest weights.", "Recursive Feature Elimination (RFE) selects features by computing unsupervised PCA eigenvalues."),
        ("The sum of variances of all PCA components equals total variance of original scaled features.", "The sum of variances of all PCA components is always zero."),
        ("Eigenvectors define the directional axes of principal components in feature space.", "Eigenvectors define the optimal classification decision threshold values."),
        ("One-Hot Encoding expands feature space dimensionality proportionally to number of categories.", "One-Hot Encoding reduces feature space dimensionality to a single column."),
        ("Frequency encoding replaces categorical levels with their frequency counts in the dataset.", "Frequency encoding replaces categorical levels with target class log-odds ratio."),
        ("Interaction features capture multiplicative combined effects between two or more attributes.", "Interaction features remove non-linear correlations between input variables."),
        ("MinMaxScaler output values lie strictly within [0, 1] when test inputs stay within train bounds.", "MinMaxScaler output values lie strictly within [-3, +3] regardless of input values."),
        ("StandardScaler output values have mean 0 and standard deviation 1.", "StandardScaler output values have mean 1 and standard deviation 0."),
        ("PCA components are ranked in decreasing order of variance explained.", "PCA components are ranked in increasing order of variance explained."),
        ("Curse of dimensionality refers to sparsity and distance distortion in high-dimensional space.", "Curse of dimensionality refers to high memory usage during one-hot encoding of binary features."),
        ("Fitting scaler parameters on test data causes data leakage from evaluation set.", "Fitting scaler parameters on training data causes data leakage into test set."),
        ("Target encoding risks severe overfitting on small dataset sample sizes.", "Target encoding guarantees zero overfitting on small dataset sample sizes."),
        ("PCA cannot capture non-linear manifold structures without kernel extensions.", "PCA captures non-linear manifold structures natively using Euclidean distance."),
        ("Feature binarization threshold converts continuous numeric values into binary 0 or 1.", "Feature binarization threshold converts categorical text strings into principal components."),
        ("Scaling continuous features preserves the correlation matrix structure among features.", "Scaling continuous features flips the sign of all positive correlation coefficients.")
    ]

    traps = []
    for i, (text_true, text_false) in enumerate(tp3_trap_definitions, 85):
        mode = "hidden" if i <= 114 else "attention_check"
        traps.append((text_true, True, mode, i))
        traps.append((text_false, False, mode, i))

    return plain, trick, traps

def generate_tp4_questions():
    """Generates questions for TP 4: Model Evaluation Metrics"""
    plain = [
        ("Accuracy is defined as the ratio of correct predictions to total predictions.", True, 4),
        ("Precision measures the proportion of true positive predictions among all positive predictions made.", True, 4),
        ("Recall (Sensitivity) measures the proportion of true positives correctly identified among all actual positives.", True, 4),
        ("F1-score is the harmonic mean of precision and recall.", True, 4),
        ("The confusion matrix displays True Positives, False Positives, True Negatives, and False Negatives.", True, 4),
        ("Specificity measures the true negative rate (TN / (TN + FP)).", True, 4),
        ("ROC curve plots True Positive Rate (Sensitivity) against False Positive Rate (1 - Specificity).", True, 4),
        ("An AUC-ROC score of 1.0 indicates perfect classification performance.", True, 4),
        ("An AUC-ROC score of 0.5 represents a model with no discrimination capability (random guessing).", True, 4),
        ("Stratified K-Fold cross-validation preserves the percentage of samples for each class in each fold.", True, 4),
        ("Accuracy can be misleading for evaluating models trained on severely imbalanced datasets.", True, 4),
        ("False Positive Rate (FPR) is calculated as FP / (FP + TN).", True, 4),
        ("Macro-averaged F1 calculates metrics independently for each class and then takes the unweighted mean.", True, 4),
        ("Weighted-averaged F1 weights class metrics by the support (number of true instances) of each class.", True, 4),
        ("Precision-Recall curve is preferred over ROC curve when dealing with highly imbalanced datasets.", True, 4),
        ("Log-loss (Binary Cross-Entropy) penalizes confident incorrect classification predictions heavily.", True, 4),
        ("A confusion matrix for a binary classifier has a dimension of 2x2.", True, 4),
        ("F1-score reaches its maximum value of 1.0 when precision and recall are both equal to 1.0.", True, 4),
        ("Cross-validation provides a robust estimate of model generalization performance on unseen data.", True, 4),
        ("Type I error corresponds to a False Positive, while Type II error corresponds to a False Negative.", True, 4),
        ("Adjusting the decision threshold changes the trade-off between precision and recall.", True, 4),
        ("High precision with low recall means the model makes few false positive errors but misses many true positives.", True, 4),
        ("Mean Squared Error (MSE) is a standard regression evaluation metric, not a classification metric.", True, 4),
        ("Cohen's Kappa measures inter-rater agreement accounting for agreement occurring by chance.", True, 4),
        ("Overfitting is indicated by high training performance coupled with significantly lower test performance.", True, 4)
    ]

    trick = [
        ("F1-score is the arithmetic average of precision and recall values.", False, 4),
        ("Accuracy is the single best metric for evaluating medical anomaly detection with 0.1% positive class prevalence.", False, 4),
        ("Recall is calculated as TP / (TP + FP) using predicted positives as denominator.", False, 4),
        ("Precision is calculated as TP / (TP + FN) using actual positives as denominator.", False, 4),
        ("An AUC-ROC score of 0.0 represents random guessing classification performance.", False, 4),
        ("Specificity measures the proportion of predicted negatives that are truly negative.", False, 4),
        ("ROC curves plot Precision on the Y-axis against Recall on the X-axis.", False, 4),
        ("Cross-validation eliminates the need for an independent held-out final test set.", False, 4),
        ("Macro-averaged metrics give higher weight to majority classes in imbalanced classification.", False, 4),
        ("A model with 99% accuracy on a 99% majority class dataset is guaranteed to be highly effective.", False, 4),
        ("False Positive Rate (FPR) is equal to 1 minus Precision.", False, 4),
        ("F1-score gives greater weight to higher values when precision and recall differ significantly.", False, 4),
        ("Increasing the classification decision threshold always increases model recall.", False, 4),
        ("Log-loss equals zero when predicted class probabilities are equal to 0.5 for all instances.", False, 4),
        ("Confusion matrix rows always represent predicted classes and columns always represent actual classes in all libraries.", False, 4),
        ("Type I error represents False Negative predictions in hypothesis testing.", False, 4),
        ("Stratified K-Fold is unnecessary for datasets with heavy class imbalance.", False, 4),
        ("An AUC-ROC score can never be less than 0.5 under any circumstances.", False, 4),
        ("Precision and Recall always increase simultaneously when tuning decision thresholds.", False, 4),
        ("Micro-averaged F1 score differs from Accuracy in single-label multi-class classification.", False, 4),
        ("High recall guarantees that the model has very few false positive predictions.", False, 4),
        ("Regression metrics like RMSE can be used directly to evaluate binary classification threshold outputs.", False, 4),
        ("K-Fold cross-validation with K=1 is equivalent to leave-one-out cross-validation.", False, 4),
        ("The F-beta score with beta=2 places twice as much emphasis on precision as on recall.", False, 4),
        ("Confusion matrix diagonal elements represent classification error counts.", False, 4),
        ("Overfitting models exhibit low training accuracy and high testing accuracy.", False, 4),
        ("ROC AUC score depends heavily on the chosen decision classification threshold value.", False, 4),
        ("Precision-Recall AUC score is 0.5 for a random classifier regardless of baseline class ratio.", False, 4),
        ("Sensitivity and Recall refer to two completely different classification metrics.", False, 4),
        ("Evaluating model performance on training data gives an unbiased estimate of test generalization.", False, 4),
        ("F1-score can be calculated even if both precision and recall are equal to 0.", False, 4),
        ("False Negative Rate (FNR) is equal to 1 minus Precision.", False, 4),
        ("Stratified splits shuffle data randomly without considering target class label distributions.", False, 4),
        ("High accuracy always implies high precision and high recall simultaneously.", False, 4),
        ("A model predicting only the majority class has an F1-score equal to its accuracy on imbalanced data.", False, 4),
        ("Log-loss is bounded strictly between -1.0 and +1.0.", False, 4),
        ("Type II error is also known as a False Positive error in statistical testing.", False, 4),
        ("AUC-ROC score increases monotonically with the total number of test set instances.", False, 4),
        ("Specificty is calculated as TN / (TN + FN).", False, 4),
        ("Precision is insensitive to changes in false positive rate.", False, 4),
        ("Leave-One-Out Cross-Validation (LOOCV) has lower computational variance than 10-Fold CV.", False, 4),
        ("Brier score measures classification accuracy using zero-one step loss.", False, 4),
        ("An ROC curve passing through point (0, 1) has an AUC equal to 0.5.", False, 4),
        ("F1-score treats precision and recall with unequal differential weights.", False, 4),
        ("Cross-validation test scores are always higher than training scores for properly fitted models.", False, 4),
        ("Accuracy equals Precision when False Positives are equal to zero.", False, 4),
        ("A classification threshold of 0.0 results in 100% precision for all models.", False, 4),
        ("Recall increases when the decision threshold is raised from 0.5 to 0.8.", False, 4),
        ("Confusion matrices can only be constructed for binary classification problems.", False, 4),
        ("AUC-PR is identical to AUC-ROC on balanced classification tasks.", False, 4),
        ("Zero False Negatives implies that Recall is equal to 1.0 (100%).", False, 4),
        ("Macro F1 is calculated by pooling global TP, FP, and FN across all classes first.", False, 4),
        ("Underfitting occurs when a model performs extremely well on training data but poorly on test data.", False, 4),
        ("The ROC curve is constructed by varying the classification decision threshold from 0 to 1.", False, 4),
        ("Cohen's Kappa score of 0 indicates perfect agreement between predicted and true labels.", False, 4),
        ("Log-loss heavily penalizes incorrect predictions made with low confidence probabilities.", False, 4),
        ("Precision measures the proportion of actual positives that were correctly classified.", False, 4),
        ("Cross-validation score with K=N folds has zero computational overhead.", False, 4),
        ("The ROC curve for a perfect binary classifier passes through the top-left coordinate (0.0, 1.0).", True, 4)
    ]

    # 42 UNIQUE Trap Pairs for TP4 (group_id 127..168)
    tp4_trap_definitions = [
        ("F1-score is defined as the harmonic mean of precision and recall.", "F1-score is defined as the arithmetic mean of precision and recall."),
        ("Precision is calculated as TP / (TP + FP).", "Precision is calculated as TP / (TP + FN)."),
        ("Recall (Sensitivity) is calculated as TP / (TP + FN).", "Recall (Sensitivity) is calculated as TP / (TP + FP)."),
        ("Specificity (True Negative Rate) is calculated as TN / (TN + FP).", "Specificity (True Negative Rate) is calculated as TN / (TN + FN)."),
        ("False Positive Rate (FPR) is calculated as FP / (FP + TN).", "False Positive Rate (FPR) is calculated as FP / (FP + TP)."),
        ("Accuracy is calculated as (TP + TN) / (TP + TN + FP + FN).", "Accuracy is calculated as (TP + FP) / (TP + TN + FP + FN)."),
        ("ROC curve plots True Positive Rate (Sensitivity) on Y-axis against False Positive Rate on X-axis.", "ROC curve plots Precision on Y-axis against Recall on X-axis."),
        ("An AUC-ROC score of 1.0 represents perfect classification performance.", "An AUC-ROC score of 0.5 represents perfect classification performance."),
        ("An AUC-ROC score of 0.5 represents random guessing performance.", "An AUC-ROC score of 0.0 represents random guessing performance."),
        ("Stratified K-Fold preserves target class proportions across all cross-validation folds.", "Stratified K-Fold randomly shuffles data without preserving target class proportions."),
        ("Type I error occurs when a true null hypothesis is incorrectly rejected (False Positive).", "Type I error occurs when a false null hypothesis is incorrectly accepted (False Negative)."),
        ("Type II error occurs when a false null hypothesis fails to be rejected (False Negative).", "Type II error occurs when a true null hypothesis is incorrectly rejected (False Positive)."),
        ("Raising the decision threshold decreases Recall and increases Precision.", "Raising the decision threshold increases Recall and decreases Precision."),
        ("Lowering the decision threshold increases Recall and decreases Precision.", "Lowering the decision threshold decreases Recall and increases Precision."),
        ("Log-loss heavily penalizes confident incorrect classification probability predictions.", "Log-loss penalizes unconfident correct classification probability predictions."),
        ("Macro-averaged F1 computes unweighted average of F1 scores across individual classes.", "Macro-averaged F1 weights class F1 scores by support count of each class."),
        ("Weighted-averaged F1 weights class metrics by the sample support of each target class.", "Weighted-averaged F1 computes simple unweighted average of metrics across classes."),
        ("Micro-averaged F1 calculates total global TP, FP, and FN across all classes first.", "Micro-averaged F1 computes average of class medians across folds."),
        ("Confusion matrix main diagonal entries represent correctly classified instance counts.", "Confusion matrix main diagonal entries represent misclassified instance counts."),
        ("Confusion matrix off-diagonal entries represent misclassified error counts.", "Confusion matrix off-diagonal entries represent correctly classified instance counts."),
        ("Precision-Recall curve is preferred over ROC curve for severely imbalanced target datasets.", "ROC curve is preferred over Precision-Recall curve for severely imbalanced target datasets."),
        ("Overfitting manifests as high training accuracy coupled with low test generalization accuracy.", "Overfitting manifests as low training accuracy coupled with high test generalization accuracy."),
        ("Underfitting manifests as low training accuracy and low test accuracy.", "Underfitting manifests as 100% training accuracy and 100% test accuracy."),
        ("F-beta score with beta=0.5 places greater weight on Precision than on Recall.", "F-beta score with beta=0.5 places greater weight on Recall than on Precision."),
        ("F-beta score with beta=2.0 places greater weight on Recall than on Precision.", "F-beta score with beta=2.0 places greater weight on Precision than on Recall."),
        ("Zero False Negatives implies a Recall score of exactly 1.0 (100%).", "Zero False Negatives implies a Precision score of exactly 1.0 (100%)."),
        ("Zero False Positives implies a Precision score of exactly 1.0 (100%).", "Zero False Positives implies a Recall score of exactly 1.0 (100%)."),
        ("Cross-validation K=10 splits dataset into 10 folds using 9 for training and 1 for validation.", "Cross-validation K=10 splits dataset into 10 folds using 1 for training and 9 for validation."),
        ("Leave-One-Out Cross-Validation (LOOCV) sets K equal to the total sample size N.", "Leave-One-Out Cross-Validation (LOOCV) sets K equal to 2 folds."),
        ("Cohen's Kappa score of 1.0 indicates perfect agreement beyond chance expectation.", "Cohen's Kappa score of 0.0 indicates perfect agreement beyond chance expectation."),
        ("Sensitivity is identical to Recall in binary classification.", "Sensitivity is identical to Specificity in binary classification."),
        ("True Negative Rate is identical to Specificity in binary classification.", "True Negative Rate is identical to Precision in binary classification."),
        ("High Precision means most positive predictions made by the model are truly positive.", "High Precision means most actual positive instances were successfully found by model."),
        ("High Recall means most actual positive instances in dataset were successfully retrieved.", "High Recall means most positive predictions made by model are truly positive."),
        ("Accuracy of 0.95 on 95% negative class dataset can be achieved by predicting all negative.", "Accuracy of 0.95 on 95% negative class dataset proves model has high positive recall."),
        ("A classification model with ROC AUC of 0.8 outperforms a random classifier.", "A classification model with ROC AUC of 0.4 outperforms a random classifier."),
        ("Brier score measures mean squared difference between predicted probability and actual outcome.", "Brier score measures harmonic mean of precision and recall."),
        ("Log-loss ranges from 0 to positive infinity.", "Log-loss ranges from -1.0 to +1.0."),
        ("AUC-ROC is independent of classification decision threshold because it evaluates all thresholds.", "AUC-ROC depends on choosing one single fixed classification decision threshold."),
        ("Confusion matrix dimension for 3-class target is 3x3.", "Confusion matrix dimension for 3-class target is 2x2."),
        ("K-Fold CV score variance decreases as fold count K increases from 2 to 10.", "K-Fold CV score variance increases as fold count K decreases from 10 to 2."),
        ("Class imbalance causes Accuracy to overestimate model effectiveness on minority class.", "Class imbalance causes Precision to overestimate model effectiveness on minority class.")
    ]

    traps = []
    for i, (text_true, text_false) in enumerate(tp4_trap_definitions, 127):
        mode = "hidden" if i <= 156 else "attention_check"
        traps.append((text_true, True, mode, i))
        traps.append((text_false, False, mode, i))

    return plain, trick, traps

def generate_tp5_questions():
    """Generates questions for TP 5: Supervised Classification Models"""
    plain = [
        ("Decision Trees split nodes to maximize Information Gain or minimize Gini Impurity.", True, 5),
        ("Gini Impurity measures the likelihood of misclassifying a randomly chosen element.", True, 5),
        ("Entropy measures the degree of impurity or randomness in a group of samples.", True, 5),
        ("Random Forest is an ensemble learning method using bagging (bootstrap aggregating) of decision trees.", True, 5),
        ("K-Nearest Neighbors (KNN) is a non-parametric, instance-based lazy learning algorithm.", True, 5),
        ("Support Vector Machines (SVM) find the optimal hyperplane maximizing the margin between classes.", True, 5),
        ("Naive Bayes classifier assumes conditional independence between features given the class label.", True, 5),
        ("Logistic Regression uses the sigmoid (logistic) function to model binary class probabilities.", True, 5),
        ("Random Forest reduces prediction variance compared to an individual single decision tree.", True, 5),
        ("Pruning a decision tree reduces model complexity and helps prevent overfitting.", True, 5),
        ("SVM uses kernel functions (RBF, Polynomial) to project data into higher-dimensional linearly separable spaces.", True, 5),
        ("In KNN, smaller values of K make the model more sensitive to noise and local data fluctuations.", True, 5),
        ("Out-of-Bag (OOB) error in Random Forest provides an unbiased estimate of test error using un-sampled bootstrap data.", True, 5),
        ("Decision Trees are non-parametric models capable of capturing non-linear relationships.", True, 5),
        ("Feature scaling is mandatory for distance-based algorithms like KNN and SVM with RBF kernel.", True, 5),
        ("Gini Impurity for a pure node containing only one class is equal to 0.0.", True, 5),
        ("Gradient Boosting builds trees sequentially, where each tree fits to the residual errors of prior trees.", True, 5),
        ("Logistic Regression produces output values bounded strictly between 0 and 1.", True, 5),
        ("Naive Bayes computes class posterior probability using Bayes' theorem.", True, 5),
        ("Support vectors are the data points lying closest to the SVM decision boundary hyperplane.", True, 5),
        ("Increasing tree depth in a Decision Tree increases model complexity and overfitting risk.", True, 5),
        ("Random Forest samples both observations (bootstrap) and feature subsets at each split node.", True, 5),
        ("Logistic Regression decision boundary is linear in feature space when using linear features.", True, 5),
        ("KNN requires storing the entire training dataset in memory during prediction time.", True, 5),
        ("Gaussian Naive Bayes assumes continuous features follow a Gaussian normal distribution per class.", True, 5)
    ]

    trick = [
        ("Decision Trees require features to be scaled using StandardScaler prior to model training.", False, 5),
        ("Gini Impurity for a node with equal 50/50 binary class distribution is equal to 1.0.", False, 5),
        ("Random Forest builds sequential trees where each tree corrects errors of the previous tree.", False, 5),
        ("KNN algorithm requires an explicit training phase to compute internal model parameters.", False, 5),
        ("SVM maximizes the classification error margin on training instances.", False, 5),
        ("Naive Bayes assumption of feature independence is strictly satisfied in almost all real-world tabular datasets.", False, 5),
        ("Logistic Regression is a regression model used to predict continuous numeric target outputs.", False, 5),
        ("Random Forest is more prone to overfitting than a single unpruned decision tree.", False, 5),
        ("Pruning a decision tree increases tree depth and increases training set accuracy.", False, 5),
        ("Linear SVM can easily classify non-linearly separable data without kernel transformations.", False, 5),
        ("In KNN, setting K equal to the total number of training samples N creates a model that overfits noise.", False, 5),
        ("OOB error estimation in Random Forest requires a separate held-out test dataset.", False, 5),
        ("Decision Trees compute non-linear hyperplane boundaries with diagonal slopes in feature space.", False, 5),
        ("KNN classification predictions are independent of feature measurement scale.", False, 5),
        ("Gini Impurity calculation is computationally slower than Log Entropy calculation due to logarithm evaluations.", False, 5),
        ("AdaBoost builds independent decision trees in parallel using bootstrap aggregating.", False, 5),
        ("Logistic Regression uses the linear step function to output exact discrete 0/1 class decisions.", False, 5),
        ("Naive Bayes cannot handle zero probability categories even when Laplace smoothing is applied.", False, 5),
        ("Support vectors consist of all training data points located far away from the decision margin.", False, 5),
        ("Increasing min_samples_split in a Decision Tree leads to deeper trees and overfitting.", False, 5),
        ("Random Forest selects the best feature split from all available features at every node.", False, 5),
        ("Logistic Regression odds ratio is unbounded negative to positive infinity.", False, 5),
        ("KNN makes instant predictions with O(1) time complexity during inference time.", False, 5),
        ("Gaussian Naive Bayes requires categorical variables to remain unencoded as raw strings.", False, 5),
        ("Entropy of a node with equal 50/50 binary class distribution is equal to 0.0.", False, 5),
        ("Bagging algorithms fit base estimators sequentially on weighted residual samples.", False, 5),
        ("SVM hyper-parameter C controls the tree depth of internal weak learners.", False, 5),
        ("KNN with K=1 yields a smooth decision boundary resistant to noise.", False, 5),
        ("Information Gain is calculated as the sum of child node impurities minus parent impurity.", False, 5),
        ("Logistic Regression cost function (Log-loss) is non-convex with multiple local minima.", False, 5),
        ("Random Forest feature importance measures the absolute correlation between features and target.", False, 5),
        ("Decision Trees can extrapolate linear trends far outside the range of training data.", False, 5),
        ("Kernel trick in SVM explicitly computes feature coordinates in high-dimensional space.", False, 5),
        ("Laplace smoothing in Naive Bayes adds 1 to the numerator to avoid zero probability estimates.", False, 5),
        ("Hard-margin SVM allows misclassified training points within the margin zone.", False, 5),
        ("Random Forest requires all base decision trees to be fully pruned to single root nodes.", False, 5),
        ("KNN uses gradient descent optimization during training to find optimal cluster centroids.", False, 5),
        ("Information Gain Ratio penalizes attributes with many fine-grained uniform categories.", False, 5),
        ("Logistic regression models multi-class target labels natively without One-vs-Rest or Softmax.", False, 5),
        ("Decision Tree splits are always computed using principal component directions.", False, 5),
        ("Soft-margin SVM with high C value allows large margin violations and tolerates misclassifications.", False, 5),
        ("Multinomial Naive Bayes is designed specifically for continuous Gaussian features.", False, 5),
        ("Increasing K in KNN increases model variance and decreases bias.", False, 5),
        ("Random Forest trees are correlated because each tree receives identical training bootstrap samples.", False, 5),
        ("Gini Impurity ranges from 0.0 to 1.0 for binary classification problems.", False, 5),
        ("Decision Trees split continuous attributes into categorical bins prior to calculating impurity.", False, 5),
        ("Sigmoid function maps real inputs to output range [-1, 1].", False, 5),
        ("SVM with RBF kernel has only one hyper-parameter C and no gamma parameter.", False, 5),
        ("Naive Bayes computes exact joint probability distributions without independence assumptions.", False, 5),
        ("Random Forest cannot perform regression tasks on continuous numerical target variables.", False, 5),
        ("Pruning methods include pre-pruning (early stopping) and post-pruning (cost-complexity pruning).", False, 5),
        ("KNN prediction speed increases linearly as the size of training data N increases.", False, 5),
        ("Logistic regression assumes features are highly multicollinear with each other.", False, 5),
        ("Decision Trees are highly sensitive to small variations in training sample data.", False, 5),
        ("SVM decision boundary depends on every single training instance in the dataset.", False, 5),
        ("Boosting algorithms reduce model variance while Bagging algorithms primarily reduce model bias.", False, 5),
        ("Entropy calculation uses log base 10 by default in standard information theory formulations.", False, 5),
        ("Single Decision Trees always outperform Random Forests on noisy high-dimensional data.", False, 5),
        ("In a Decision Tree, splits are selected by minimizing the classification accuracy of individual leaves.", False, 5)
    ]

    # 42 UNIQUE Trap Pairs for TP5 (group_id 169..210)
    tp5_trap_definitions = [
        ("Random Forest uses Bagging (bootstrap aggregating) to train independent decision trees in parallel.", "Random Forest uses Boosting to train sequential decision trees on residual error weights."),
        ("Gradient Boosting trains sequential trees where each tree fits to residual errors of prior trees.", "Gradient Boosting trains independent trees in parallel using bootstrap sample aggregation."),
        ("Gini Impurity for a completely pure single-class node is equal to 0.0.", "Gini Impurity for a completely pure single-class node is equal to 1.0."),
        ("Entropy for a completely pure single-class node is equal to 0.0.", "Entropy for a completely pure single-class node is equal to 1.0."),
        ("Gini Impurity for an equal 50/50 binary class node is equal to 0.5.", "Gini Impurity for an equal 50/50 binary class node is equal to 1.0."),
        ("Entropy for an equal 50/50 binary class node is equal to 1.0 (with log base 2).", "Entropy for an equal 50/50 binary class node is equal to 0.0 (with log base 2)."),
        ("KNN is a non-parametric lazy learner that performs computation during prediction time.", "KNN is an eager parametric learner that computes model weights during training phase."),
        ("Smaller K in KNN makes the model more sensitive to noise and increases variance.", "Smaller K in KNN smooths decision boundaries and decreases variance."),
        ("Larger K in KNN smooths decision boundaries and increases bias.", "Larger K in KNN overfits noisy training instances and increases variance."),
        ("SVM finds the optimal hyperplane that maximizes the margin between classes.", "SVM finds the optimal hyperplane that minimizes the distance between class centroids."),
        ("Support vectors are data points lying closest to the SVM decision margin boundary.", "Support vectors are data points lying furthest away from the SVM decision margin boundary."),
        ("Naive Bayes assumes features are conditionally independent given the class label.", "Naive Bayes assumes features are highly correlated and interdependent given the class label."),
        ("Laplace smoothing adds a constant to frequency counts to prevent zero probability estimates.", "Laplace smoothing removes low-frequency categories to reduce feature space size."),
        ("Logistic Regression uses the sigmoid function to map real inputs to probabilities [0, 1].", "Logistic Regression uses the step function to map real inputs to continuous linear predictions."),
        ("Sigmoid function outputs values strictly bounded between 0.0 and 1.0.", "Sigmoid function outputs values strictly bounded between -1.0 and +1.0."),
        ("Pruning decision trees reduces tree depth and prevents overfitting.", "Pruning decision trees increases tree depth and causes overfitting."),
        ("Out-of-Bag (OOB) error in Random Forest uses unselected bootstrap samples for validation.", "Out-of-Bag (OOB) error in Random Forest uses training samples to evaluate training accuracy."),
        ("Random Forest samples both observations and feature subsets at each split node.", "Random Forest uses all observations and all features at every split node."),
        ("Decision Trees create axis-aligned orthogonal split boundaries in feature space.", "Decision Trees create smooth non-linear circular split boundaries in feature space."),
        ("SVM kernel trick projects data into higher-dimensional space without computing new coordinates explicitly.", "SVM kernel trick projects data into lower-dimensional space by dropping non-linear features."),
        ("Hard-margin SVM requires data to be perfectly linearly separable without misclassifications.", "Hard-margin SVM allows margin violations and tolerates misclassified training points."),
        ("Soft-margin SVM uses hyper-parameter C to control trade-off between margin width and error penalty.", "Soft-margin SVM uses hyper-parameter K to control number of nearest neighbors."),
        ("Higher C parameter in SVM penalizes misclassifications heavily, creating a narrower margin.", "Higher C parameter in SVM allows large margin violations, creating a wider soft margin."),
        ("KNN requires feature scaling because Euclidean distance is sensitive to attribute magnitude.", "KNN is invariant to feature scaling because Euclidean distance normalizes feature scales."),
        ("Decision Trees are invariant to monotonic feature scaling transformations.", "Decision Trees require features to be scaled with StandardScaler before computing splits."),
        ("Information Gain is calculated as parent node entropy minus weighted average child entropy.", "Information Gain is calculated as child node entropy minus parent node entropy."),
        ("Information Gain Ratio penalizes attributes with large numbers of distinct fine-grained categories.", "Information Gain Ratio favors attributes with large numbers of distinct fine-grained categories."),
        ("AdaBoost adjusts sample weights after each iteration to focus on misclassified instances.", "AdaBoost adjusts feature scaling factors after each iteration to reduce dimensionality."),
        ("Gaussian Naive Bayes assumes continuous feature variables follow Gaussian normal distributions per class.", "Gaussian Naive Bayes assumes continuous feature variables follow uniform step distributions."),
        ("KNN prediction time complexity scales linearly O(N) with number of training samples N.", "KNN prediction time complexity is constant O(1) regardless of training sample size N."),
        ("Cost-complexity pruning (post-pruning) trims branches after full decision tree is grown.", "Cost-complexity pruning (post-pruning) stops tree growth early before reaching max depth."),
        ("Pre-pruning halts decision tree expansion early based on depth or min sample thresholds.", "Pre-pruning grows the tree to full max depth and then deletes non-essential leaves."),
        ("Linear SVM decision boundary is a linear hyperplane in input feature space.", "Linear SVM decision boundary is a non-linear parabolic curve in input feature space."),
        ("RBF kernel (Gaussian) measures similarity between samples based on squared Euclidean distance.", "RBF kernel (Gaussian) measures similarity based on categorical one-hot dot products."),
        ("Multinomial Naive Bayes is suited for discrete feature counts like word frequencies in text.", "Multinomial Naive Bayes is suited for continuous scaled Gaussian features."),
        ("Logistic regression models log-odds ratio as a linear combination of input features.", "Logistic regression models sample variance as a quadratic combination of input features."),
        ("Base decision trees in Random Forest are decorrelated by random feature subspace sampling.", "Base decision trees in Random Forest are identical because they use identical feature subsets."),
        ("Decision trees suffer from high variance and instability on small training data perturbations.", "Decision trees have zero variance and produce identical trees regardless of training data changes."),
        ("Bagging primarily reduces model variance without increasing model bias.", "Bagging primarily reduces model bias without altering model variance."),
        ("Boosting primarily reduces model bias by sequentially fitting base learners to residual errors.", "Boosting primarily reduces model variance by averaging independent parallel trees."),
        ("Gini Impurity formula is 1 minus sum of squared class probabilities.", "Gini Impurity formula is negative sum of class probability times log class probability."),
        ("Entropy formula is negative sum of class probability times log base 2 of class probability.", "Entropy formula is 1 minus sum of squared class probabilities.")
    ]

    traps = []
    for i, (text_true, text_false) in enumerate(tp5_trap_definitions, 169):
        mode = "hidden" if i <= 198 else "attention_check"
        traps.append((text_true, True, mode, i))
        traps.append((text_false, False, mode, i))

    return plain, trick, traps

def generate_tp6_questions():
    """Generates questions for TP 6: Clustering (K-Means, Hierarchical, DBSCAN & Silhouette Analysis)"""
    plain = [
        ("K-Means is an unsupervised partitioning algorithm that clusters data into K predefined clusters.", True, 6),
        ("K-Means objective function minimizes the Within-Cluster Sum of Squares (WCSS / Inertia).", True, 6),
        ("Elbow Method plots WCSS against values of K to identify the optimal number of clusters.", True, 6),
        ("Silhouette Score measures how similar an object is to its own cluster compared to other clusters.", True, 6),
        ("Silhouette Score ranges from -1.0 to +1.0, where higher values indicate well-separated clusters.", True, 6),
        ("Hierarchical Agglomerative Clustering is a bottom-up approach merging closest clusters iteratively.", True, 6),
        ("Dendrogram is a tree diagram visual representation of hierarchical clustering steps.", True, 6),
        ("DBSCAN identifies clusters of arbitrary shape based on local point density thresholds.", True, 6),
        ("In DBSCAN, points that do not meet core or border point density criteria are labeled as noise (-1).", True, 6),
        ("DBSCAN uses two primary hyperparameters: eps (neighborhood radius) and min_samples.", True, 6),
        ("DBSCAN can discover non-spherical geometric clusters where K-Means fails.", True, 6),
        ("K-Means clustering is sensitive to initial centroid locations and feature scale.", True, 6),
        ("K-Means++ initialization picks initial centroids far apart to speed up convergence.", True, 6),
        ("Single linkage hierarchical clustering defines distance between two clusters as the minimum distance between points.", True, 6),
        ("Complete linkage hierarchical clustering uses maximum distance between points in two clusters.", True, 6),
        ("Average linkage hierarchical clustering uses average pairwise distance between points in two clusters.", True, 6),
        ("Ward's linkage minimizes the increase in total within-cluster variance after merging.", True, 6),
        ("Feature scaling with StandardScaler is essential before running K-Means or DBSCAN on continuous attributes.", True, 6),
        ("Dendrogram height on the y-axis represents the distance threshold at which cluster merges occur.", True, 6),
        ("In scikit-learn, silhouette_score requires scaled features and cluster label arrays as input.", True, 6),
        ("Clustering is an unsupervised learning task because target class labels are absent in training data.", True, 6),
        ("K-Means assumes clusters are spherical and of roughly equal size and variance.", True, 6),
        ("Inertia (WCSS) monotonically decreases as the number of clusters K increases.", True, 6),
        ("Silhouette score near 0.0 indicates that data points lie on or very near cluster decision boundaries.", True, 6),
        ("DBSCAN does not require pre-specifying the number of clusters K beforehand.", True, 6)
    ]

    trick = [
        ("K-Means clustering algorithm automatically determines the optimal number of clusters K without user input.", False, 6),
        ("WCSS (Inertia) increases as the number of clusters K increases from 1 to N.", False, 6),
        ("Elbow Method guarantees finding a unique sharp inflection point for every dataset.", False, 6),
        ("Silhouette Score of -1.0 indicates that data points are perfectly assigned to their correct clusters.", False, 6),
        ("Agglomerative clustering is a top-down divisive approach starting with one single all-inclusive cluster.", False, 6),
        ("DBSCAN requires users to specify the total number of target clusters K before execution.", False, 6),
        ("In DBSCAN, noise points are assigned to the nearest cluster centroid with positive integer label.", False, 6),
        ("DBSCAN performs effectively on datasets with widely varying cluster densities.", False, 6),
        ("K-Means handles non-spherical complex geometric shapes like concentric circles effectively.", False, 6),
        ("Hierarchical clustering algorithms require specifying the exact number of clusters K before running linkage.", False, 6),
        ("Dendrogram y-axis represents the total number of data points inside each merged cluster.", False, 6),
        ("DBSCAN noise points are included when calculating Silhouette score for individual clusters.", False, 6),
        ("K-Means converges to the global minimum solution regardless of initial centroid selection.", False, 6),
        ("Single linkage hierarchical clustering is immune to the chaining effect.", False, 6),
        ("Complete linkage hierarchical clustering tends to produce elongated trailing clusters.", False, 6),
        ("K-Means clustering works directly on categorical nominal attributes using Euclidean distance.", False, 6),
        ("Inertia (WCSS) reaches its maximum value when K is set equal to the total number of observations N.", False, 6),
        ("Silhouette score calculation is independent of pairwise inter-cluster distance measurements.", False, 6),
        ("Ward's linkage minimizes the maximum Euclidean distance between cluster medoids.", False, 6),
        ("K-Medoids (PAM) is more sensitive to extreme outliers than K-Means.", False, 6),
        ("DBSCAN requires all points in the dataset to be assigned to at least one valid cluster.", False, 6),
        ("K-Means++ initialization chooses initial centroids completely at random with equal probability.", False, 6),
        ("Hierarchical clustering result can be modified dynamically after dendrogram construction without re-computing.", False, 6),
        ("Euclidean distance is appropriate for high-dimensional sparse text data without scaling.", False, 6),
        ("K-Means objective function minimizes the sum of Manhattan distances to cluster medians.", False, 6),
        ("Silhouette coefficient for a dataset with K=1 cluster is equal to +1.0.", False, 6),
        ("Cross-validation can be directly applied to evaluate K-Means cluster validity without labels.", False, 6),
        ("Dendrogram horizontal cuts at different height thresholds yield identical cluster groupings.", False, 6),
        ("K-Means cluster assignments are deterministic and produce identical results across random seeds.", False, 6),
        ("Grid Search is used to tune centroid coordinates in K-Means clustering.", False, 6),
        ("Agglomerative clustering has a low computational time complexity of O(N).", False, 6),
        ("Silhouette score uses only within-cluster mean distance without considering nearest-cluster distance.", False, 6),
        ("K-Means clustering is invariant to feature scaling transformations.", False, 6),
        ("Inertia can be compared meaningfully between two datasets with different numbers of features.", False, 6),
        ("Single linkage merges clusters with maximum inter-point distance.", False, 6),
        ("Hierarchical clustering dendrogram cannot be cut to produce a specific K number of clusters.", False, 6),
        ("K-Means algorithm always converges in fewer than 3 iterations on all datasets.", False, 6),
        ("Silhouette coefficient ranges between 0.0 and 100.0.", False, 6),
        ("Density-based clustering like DBSCAN requires all clusters to have equal density.", False, 6),
        ("K-Means clustering maximizes between-cluster sum of squares while WCSS minimizes it.", False, 6),
        ("DBSCAN parameter eps defines the minimum number of points required to form a dense region.", False, 6),
        ("In DBSCAN, a border point has at least min_samples points within its eps neighborhood.", False, 6),
        ("K-Means inertia drops to zero when K equals 1.", False, 6),
        ("Silhouette analysis cannot be computed for non-convex clusters produced by DBSCAN.", False, 6),
        ("Dendrogram leaf nodes represent final merged clusters containing all dataset instances.", False, 6),
        ("StandardScaler changes the geometric shape of clusters identified by DBSCAN.", False, 6),
        ("Agglomerative clustering recalculates proximity matrix after every pair merge step.", False, 6),
        ("K-Means centroids are guaranteed to correspond to actual data points in the training set.", False, 6),
        ("DBSCAN labels core points with negative integers starting from -1.", False, 6),
        ("Divisive hierarchical clustering starts with individual singleton clusters and merges them.", False, 6),
        ("Inertia measures the average distance between centroids of different clusters.", False, 6),
        ("Silhouette score of 0.9 indicates poor cluster separation and high sample overlap.", False, 6),
        ("K-Means requires target class labels to compute cluster centroids.", False, 6),
        ("DBSCAN fails on moon-shaped synthetic datasets due to non-linear boundaries.", False, 6),
        ("Ward linkage uses maximum distance between cluster boundaries.", False, 6),
        ("Elbow method guarantees finding the exact true number of classes in any dataset.", False, 6),
        ("K-Means++ initialization picks initial centroids as close to each other as possible.", False, 6),
        ("Hierarchical clustering linkage matrix stores inertia values for each iteration.", False, 6),
        ("DBSCAN min_samples parameter controls the maximum distance between core points.", False, 6)
    ]

    # 40 UNIQUE Trap Pairs for TP6 (group_id 211..250)
    tp6_trap_definitions = [
        ("DBSCAN identifies clusters of arbitrary shape based on local point density thresholds without pre-specifying K.", "DBSCAN identifies clusters of arbitrary shape based on local point density thresholds after pre-specifying K."),
        ("K-Means clustering objective minimizes Within-Cluster Sum of Squares (WCSS / Inertia).", "K-Means clustering objective maximizes Within-Cluster Sum of Squares (WCSS / Inertia)."),
        ("Inertia (WCSS) decreases monotonically as the number of clusters K increases.", "Inertia (WCSS) increases monotonically as the number of clusters K increases."),
        ("Elbow method selects K at the point of diminishing marginal returns in WCSS reduction.", "Elbow method selects K at the point of maximum peak inertia."),
        ("Silhouette score ranges strictly between -1.0 and +1.0.", "Silhouette score ranges strictly between 0.0 and +100.0."),
        ("Silhouette score near +1.0 indicates sample is well-matched to its own cluster and far from neighbors.", "Silhouette score near +1.0 indicates sample is misclassified and assigned to wrong cluster."),
        ("Agglomerative hierarchical clustering is a bottom-up approach starting with N singleton clusters.", "Agglomerative hierarchical clustering is a top-down approach starting with 1 all-inclusive cluster."),
        ("Divisive hierarchical clustering is a top-down approach starting with 1 all-inclusive cluster.", "Divisive hierarchical clustering is a bottom-up approach starting with N singleton clusters."),
        ("Dendrogram displays the tree hierarchy of cluster merges and distance thresholds.", "Dendrogram displays feature importance rankings for supervised classification trees."),
        ("DBSCAN labels unassigned low-density outlier points as noise with label -1.", "DBSCAN labels unassigned low-density outlier points as core cluster 0."),
        ("Single linkage defines distance between clusters as the minimum distance between any pair of points.", "Single linkage defines distance between clusters as the maximum distance between any pair of points."),
        ("Complete linkage defines distance between clusters as the maximum distance between any pair of points.", "Complete linkage defines distance between clusters as the minimum distance between any pair of points."),
        ("Average linkage defines distance between clusters as average distance between all pairs of points.", "Average linkage defines distance between clusters as distance between cluster medoids."),
        ("Ward linkage minimizes the increase in total within-cluster variance when merging clusters.", "Ward linkage maximizes the distance between outer boundary noise points when merging clusters."),
        ("K-Means++ initialization chooses initial centroids far apart from each other.", "K-Means++ initialization chooses initial centroids as close to each other as possible."),
        ("DBSCAN parameter eps defines the maximum neighborhood radius around a point.", "DBSCAN parameter eps defines the minimum number of clusters to generate."),
        ("DBSCAN parameter min_samples specifies minimum points required within eps to form a core point.", "DBSCAN parameter min_samples specifies maximum number of iterations allowed."),
        ("K-Means assumes clusters are spherical with isotropic variance.", "K-Means assumes clusters are elongated non-convex moon shapes."),
        ("DBSCAN can successfully segment non-spherical geometric shapes like concentric circles.", "K-Means can successfully segment non-spherical geometric shapes like concentric circles."),
        ("Inertia equals zero when number of clusters K equals total sample size N.", "Inertia reaches maximum value when number of clusters K equals total sample size N."),
        ("K-Means centroids are computed as mean coordinates of points assigned to each cluster.", "K-Means centroids are computed as median coordinates of points assigned to each cluster."),
        ("K-Medoids (PAM) chooses actual data points as cluster centers making it robust to outliers.", "K-Means chooses actual data points as cluster centers making it robust to outliers."),
        ("Cutting a dendrogram at a horizontal height threshold determines the final cluster partitioning.", "Cutting a dendrogram at a vertical line determines feature selection importance."),
        ("StandardScaler normalization is required before K-Means because Euclidean distance is scale-sensitive.", "StandardScaler normalization is prohibited before K-Means because it distorts cluster shapes."),
        ("DBSCAN core point has at least min_samples within its eps radius neighborhood.", "DBSCAN core point has fewer than min_samples within its eps radius neighborhood."),
        ("DBSCAN border point is within eps radius of a core point but has fewer than min_samples neighbors.", "DBSCAN border point is an isolated noise point far away from all core points."),
        ("Silhouette score near 0.0 indicates sample lies near decision boundary between two clusters.", "Silhouette score near 0.0 indicates perfect cluster separation."),
        ("Silhouette score near -1.0 indicates sample is likely assigned to wrong cluster.", "Silhouette score near -1.0 indicates perfect cluster separation."),
        ("Agglomerative clustering linkage matrix size is (N-1) by 4 for N samples.", "Agglomerative clustering linkage matrix size is N by N for N samples."),
        ("K-Means is sensitive to initial random centroid placement and can converge to local minima.", "K-Means is guaranteed to find global optimal clustering regardless of initial centroid placement."),
        ("Dendrogram y-axis represents cophenetic distance between merged cluster nodes.", "Dendrogram y-axis represents sample count of leaf node instances."),
        ("Elbow plot shows WCSS on y-axis and number of clusters K on x-axis.", "Elbow plot shows Silhouette score on y-axis and feature count on x-axis."),
        ("Clustering iris dataset without species labels simulates unsupervised exploratory analysis.", "Clustering iris dataset requires species labels to calculate cluster centroids."),
        ("DBSCAN does not require specifying number of clusters K beforehand.", "K-Means does not require specifying number of clusters K beforehand."),
        ("DBSCAN noise points are excluded when computing cluster centroid coordinates.", "DBSCAN noise points are assigned to cluster 0 and used to compute centroids."),
        ("Hierarchical clustering creates a nested sequence of partitions.", "Hierarchical clustering creates non-overlapping flat partitions in a single iteration."),
        ("Distance metrics like Euclidean or Manhattan define proximity between data points in clustering.", "Impurity metrics like Gini or Entropy define proximity between data points in clustering."),
        ("K-Means algorithm alternates between cluster assignment step and centroid update step.", "K-Means algorithm alternates between forward selection step and backward elimination step."),
        ("Cophenetic correlation measures how faithfully a dendrogram preserves pairwise distances.", "Cophenetic correlation measures classification accuracy of decision tree leaves."),
        ("Partitioning algorithms divide data into non-overlapping subsets without hierarchical structure.", "Partitioning algorithms build a nested tree hierarchy of cluster merges.")
    ]

    traps = []
    for i, (text_true, text_false) in enumerate(tp6_trap_definitions, 211):
        mode = "hidden" if i <= 238 else "attention_check"
        traps.append((text_true, True, mode, i))
        traps.append((text_false, False, mode, i))

    return plain, trick, traps

def generate_all_questions():
    """Compiles 1000 questions matching spec: 150 plain, 350 trick, 500 trap (250 UNIQUE pairs)"""
    tp_generators = [
        generate_tp1_questions,
        generate_tp2_questions,
        generate_tp3_questions,
        generate_tp4_questions,
        generate_tp5_questions,
        generate_tp6_questions
    ]

    all_questions = []

    for tp_id in range(1, 7):
        plain_raw, trick_raw, trap_raw = tp_generators[tp_id - 1]()

        # Plain standalone (25 per TP * 6 = 150)
        for text, correct, topic_offset in plain_raw[:25]:
            topic_id = (tp_id - 1) * 3 + topic_offset
            all_questions.append({
                "tp_id": tp_id,
                "topic_id": topic_id,
                "text": text,
                "correct_answer": correct,
                "question_type": "plain",
                "trap_group_id": None,
                "trap_mode": None
            })

        # Trick standalone (59 for TPs 1-2, 58 for TPs 3-6 = 350 total)
        trick_count = 59 if tp_id in [1, 2] else 58
        for text, correct, topic_offset in trick_raw[:trick_count]:
            topic_id = (tp_id - 1) * 3 + topic_offset
            all_questions.append({
                "tp_id": tp_id,
                "topic_id": topic_id,
                "text": text,
                "correct_answer": correct,
                "question_type": "trick",
                "trap_group_id": None,
                "trap_mode": None
            })

        # Trap pairs (42 pairs for TPs 1-5, 40 pairs for TP 6 = 250 UNIQUE pairs / 500 questions)
        for item in trap_raw:
            text, correct, mode, group_id = item
            topic_id = (tp_id - 1) * 3 + 1
            all_questions.append({
                "tp_id": tp_id,
                "topic_id": topic_id,
                "text": text,
                "correct_answer": correct,
                "question_type": "trap",
                "trap_group_id": group_id,
                "trap_mode": mode
            })

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(all_questions, f, indent=2, ensure_ascii=False)

    print(f"✅ Generated {len(all_questions)} questions saved to {OUTPUT_PATH}")

    # Print summary statistics
    plain_cnt = sum(1 for q in all_questions if q["question_type"] == "plain")
    trick_cnt = sum(1 for q in all_questions if q["question_type"] == "trick")
    trap_cnt = sum(1 for q in all_questions if q["question_type"] == "trap")
    hidden_cnt = sum(1 for q in all_questions if q.get("trap_mode") == "hidden")
    att_cnt = sum(1 for q in all_questions if q.get("trap_mode") == "attention_check")

    # Verify uniqueness of trap pairs
    trap_texts = [q["text"] for q in all_questions if q["question_type"] == "trap"]
    unique_trap_texts = set(trap_texts)

    print(f"📊 Summary:")
    print(f"  - Plain standalone: {plain_cnt}")
    print(f"  - Trick standalone: {trick_cnt}")
    print(f"  - Trap questions: {trap_cnt} ({hidden_cnt} hidden, {att_cnt} attention_check)")
    print(f"  - Unique trap statements: {len(unique_trap_texts)} / {len(trap_texts)}")
    print(f"  - Total questions: {len(all_questions)}")

if __name__ == "__main__":
    generate_all_questions()
