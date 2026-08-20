# TP 1 — Raw Data Cleaning (200 Questions: 90 Normal, 50 Tricky, 60 Trap)

def get_tp1_questions():
    questions = []
    
    # ---------------------------------------------------------
    # 90 NORMAL QUESTIONS (TP1_001 to TP1_090)
    # ---------------------------------------------------------
    normal_data = [
        # Data Quality & Problems (Easy/Medium)
        ("Data cleaning is the phase where errors, inconsistencies, and missing values in raw data are corrected before modeling.", True, "Cleaning raw data prevents biased estimators and distorted model predictions."),
        ("In pandas, df.shape returns a tuple representing the number of rows and columns in a DataFrame.", True, "df.shape[0] gives row count and df.shape[1] gives column count."),
        ("Raw real-world datasets often contain typos, inconsistent formatting, and missing values.", True, "Real-world data collection processes frequently introduce noisy records."),
        ("Ignoring missing data in statistical calculations can introduce systematic bias into the results.", True, "Dropping or misinterpreting missing data distorts sample statistics."),
        ("In pandas, df.head(10) displays the first 10 rows of a DataFrame.", True, "df.head(n) defaults to 5 rows but accepts an integer parameter n."),
        ("The pandas read_csv() function is used to load comma-separated values files into a DataFrame.", True, "read_csv() is the primary pandas utility for loading CSV tabular datasets."),
        ("A DataFrame in pandas consists of labeled rows and labeled columns.", True, "Pandas DataFrames are 2D tabular structures with index labels and column names."),
        ("Data cleaning operations should be applied consistently across both training and validation sets.", True, "Consistent cleaning maintains identical feature definitions and prevents formatting errors."),
        ("Removing metadata columns such as patient names or emails helps protect privacy under GDPR regulations.", True, "Personal identifiers carry zero predictive value and violate data privacy standards."),
        ("An outlier is an observation that deviates significantly from the rest of the dataset.", True, "Outliers represent extreme values that fall far outside typical statistical distributions."),

        # String Cleaning & Standardizing (Medium)
        ("In pandas, str.split('_') splits string values in a column by an underscore delimiter.", True, "str.split() breaks strings into lists of substrings based on the specified separator."),
        ("Applying str.title() converts the first character of each word to uppercase.", True, "str.title() capitalizes the start of each word while lowercasing remaining characters."),
        ("Dictionary mapping with .map() or .replace() can unify synonymous species names like 'E.coi' and 'E.coli'.", True, "Replacing typos with a dictionary unifies inconsistent string labels into a single category."),
        ("Applying str.strip() removes leading and trailing whitespace from string values in pandas.", True, "str.strip() eliminates unwanted padding spaces around text entries."),
        ("If inconsistent species names are left uncorrected, machine learning models treat them as separate categories.", True, "String algorithms rely on exact matches; 'E.coi' and 'E.coli' form distinct categories if uncleaned."),
        ("The .str.upper() method converts all characters in a string Series to uppercase.", True, "str.upper() standardizes string casing to uppercase for uniform matching."),
        ("In pandas, df['Souches'].unique() returns an array of distinct values in the Souches column.", True, ".unique() isolates all non-duplicate values present in a Series."),
        ("Replacing multi-character codes with single-letter codes (R, S, I) standardizes antibiogram susceptibility results.", True, "Standardizing synonyms like 'RESISTANT' to 'R' unifies categorical antibiogram records."),
        ("Values in categorical columns that fail parsing checks can be coerced to np.nan.", True, "Coercing unparseable text entries to NaN allows systematic handling of invalid records."),
        ("Converting string responses to lowercase before synonym checking ensures case-insensitive matching.", True, "Lowercasing normalizes text so 'Yes', 'YES', and 'yes' match the same lookup condition."),

        # Column Splitting & Parsing (Medium)
        ("Compound columns like 'Age/Gender' (e.g., '45/F') must be split into separate numeric and categorical features.", True, "Machine learning models require separated numeric and categorical variables."),
        ("Using str.split('/', expand=True) creates a new DataFrame with separate columns for each split component.", True, "expand=True expands split substrings into separate DataFrame columns."),
        ("pd.to_numeric(..., errors='coerce') converts invalid string entries into np.nan instead of raising an error.", True, "errors='coerce' replaces unparseable numeric strings with NaN safely."),
        ("Setting biological age boundaries (e.g., capping Age between 0 and 120) eliminates impossible data entry errors.", True, "Filtering out negative ages or ages over 120 removes corrupted biomedical records."),
        ("String indexing str[0] can be used to extract the first character of a string in a pandas Series.", True, "str[0] extracts single characters such as 'M' or 'F' from gender text entries."),
        ("Converting string boolean flags ('yes'/'no') to binary indicators (1/0) enables numerical computation.", True, "Binary numerical flags allow algebraic operations and algorithm ingestion."),
        ("Mapping ordinal categorical variables to sequential integers (e.g., 0, 1, 2, 3) preserves their natural order.", True, "Ordinal encoding assigns higher integers to higher ranks, preserving relative progression."),
        ("In pandas, df.columns.tolist() returns a list of all column names in the DataFrame.", True, ".tolist() exports Series or Index structures into Python standard lists."),
        ("Splitting a column without expand=True returns a Series containing lists of split strings.", True, "Without expand=True, pd.Series.str.split() yields a Series of list objects."),
        ("Biological bounds checks rely on domain knowledge to flag impossible feature values.", True, "Domain expertise defines valid ranges such as human age limits or blood pressure bounds."),

        # Derived Feature Creation & Domain Logic (Medium/Hard)
        ("Creating a derived feature like MultiResistance synthesizes complex multi-column antibiotic tests into a single flag.", True, "Domain-specific feature engineering aggregates multiple raw clinical indicators into actionable target flags."),
        ("Checking if at least one antibiotic per chemical family is resistant measures multi-family resistance.", True, "Grouping antibiotics by pharmacological class allows counting resistance across distinct drug families."),
        ("Applying a custom function row-by-row using df.apply(axis=1) allows evaluating complex multi-column logic.", True, "axis=1 instructs df.apply to iterate row-wise across columns."),
        ("In pandas, .astype(int) converts boolean true/false flags into numeric 1 and 0 integers.", True, "Boolean arrays map True to 1 and False to 0 when cast to integer types."),
        ("Derived features can capture clinical domain knowledge that raw individual columns do not explicitly state.", True, "Engineering aggregated flags transforms raw observations into explicit analytical indicators."),
        ("Calculating df['MultiResistance'].mean() yields the proportion of multiresistant samples in the dataset.", True, "The mean of a binary 0/1 variable equals the proportion of 1s in the sample."),
        ("Filtering a DataFrame with df.loc[condition] allows overwriting specific invalid cell values with np.nan.", True, "df.loc[row_indexer, col_indexer] isolates specific cells for targeted modification."),
        ("Aggregating resistance across chemical families is more informative than counting raw resistant drugs.", True, "Bacterial cross-resistance occurs at the antibiotic class level rather than per individual drug."),
        ("Creating binary indicator variables simplifies target definition for classification models.", True, "A 0/1 target column establishes a clean target for binary classification tasks."),
        ("Custom Python row functions applied with df.apply() must handle np.nan values safely to avoid runtime exceptions.", True, "Row functions should check for pd.notna() before evaluating conditional rules."),

        # Missing Values & Deduplication (Easy/Medium)
        ("In pandas, df.isna().sum() calculates the number of missing values in each column.", True, "df.isna() returns a boolean mask, and .sum() totals True values per column."),
        ("The df.dropna() method removes rows containing missing values from a DataFrame by default.", True, "By default, dropna(axis=0, how='any') drops any row containing at least one NaN."),
        ("Calling df.drop_duplicates() removes identical duplicate rows from a DataFrame.", True, "drop_duplicates() keeps unique observations and removes exact duplicate rows."),
        ("Unremoved duplicate rows can artificially inflate statistical counts and bias machine learning models.", True, "Duplicate observations over-weight specific data points, altering true underlying sample distributions."),
        ("The inplace=True parameter modifies the DataFrame directly without requiring reassigning to a new variable.", True, "inplace=True updates the caller object in place and returns None."),
        ("df.isna().sum().sum() computes the grand total of missing values across the entire DataFrame.", True, "Chaining .sum().sum() sums missing counts across all columns into a single scalar."),
        ("The df.fillna(value) method replaces all missing values in a DataFrame with a specified scalar value.", True, "fillna() substitutes NaN occurrences with the provided fill argument."),
        ("Deduplication should generally occur before calculating summary statistics to prevent duplicate weighting.", True, "Cleaning duplicates first ensures sample means and variances reflect unique physical subjects."),
        ("By default, df.drop_duplicates() retains the first occurrence of duplicate rows.", True, "The default parameter keep='first' retains the initial row and drops subsequent duplicates."),
        ("Forward fill (method='ffill') propagates the last known valid observation forward to overwrite NaN values.", True, "ffill replaces missing entries with the most recent non-null entry above them."),

        # Outliers & Data Consistency (Medium/Hard)
        ("The Interquartile Range (IQR) is calculated as the difference between the 75th percentile (Q3) and 25th percentile (Q1).", True, "IQR = Q3 - Q1 measures the range of the middle 50% of the data."),
        ("Under the standard IQR method, extreme outliers lie below Q1 - 1.5*IQR or above Q3 + 1.5*IQR.", True, "Tukey's fence rule flags values outside 1.5 times the IQR from the quartiles."),
        ("The Z-score measures how many standard deviations an observation lies away from the mean.", True, "Z = (X - mean) / std_dev quantifies relative distance from the sample mean."),
        ("A Z-score absolute value greater than 3.0 is commonly used to flag potential statistical outliers.", True, "In normal distributions, values beyond 3 standard deviations comprise less than 0.3% of data."),
        ("Mean imputation is sensitive to extreme outliers present in the feature column.", True, "Extreme outliers pull the sample mean toward themselves, corrupting the imputed fill value."),
        ("Median imputation is more robust to skewed distributions and outliers than mean imputation.", True, "The median represents the central 50th percentile and remains unaffected by extreme tail values."),
        ("Outliers can distort numerical variance and covariance calculations in data analysis.", True, "Squared difference terms in variance and covariance magnify the impact of extreme values."),
        ("Winsorization handles outliers by capping extreme values to specified upper and lower percentile limits.", True, "Winsorizing replaces values beyond percentiles (e.g., 1st and 99th) with the percentile boundary values."),
        ("Trimming outliers entirely removes extreme data points from the dataset.", True, "Trimming filters out rows containing flagged outlier values, reducing sample size."),
        ("Data consistency checks confirm that numerical values satisfy realistic domain constraints.", True, "Consistency rules verify that inputs conform to physical and operational requirements."),

        # Scikit-Learn Imputation & pandas operations (Medium)
        ("In pandas, df.drop(columns=['col1', 'col2']) drops specified columns from the DataFrame.", True, "Specifying columns= explicitly selects column labels for removal."),
        ("Scikit-learn SimpleImputer with strategy='mean' imputes missing continuous values with the column average.", True, "SimpleImputer(strategy='mean') calculates column-wise averages for numeric NaN replacement."),
        ("SimpleImputer with strategy='most_frequent' replaces missing entries with the modal value.", True, "The most_frequent strategy calculates column modes, suitable for categorical attributes."),
        ("SimpleImputer with strategy='constant' replaces missing values with a user-defined fill_value.", True, "The constant strategy substitutes NaNs with a fixed scalar such as 0 or 'Missing'."),
        ("df.duplicated() returns a boolean Series where True marks duplicate rows.", True, "df.duplicated() flags duplicate rows based on specified subset columns."),
        ("The pandas function pd.to_numeric() converts object Series into numerical float or integer dtypes.", True, "to_numeric parses numeric strings into standard float64 or int64 formats."),
        ("In pandas, df.dtypes lists the data types of all columns in a DataFrame.", True, "df.dtypes outputs a Series mapping column names to their storage data types."),
        ("Constant imputation with a placeholder value like -999 can distort distance-based algorithms if unhandled.", True, "Numerical algorithms treat -999 as a literal magnitude, distorting spatial distance computations."),
        ("Removing columns with over 80% missing data is often preferable to heavy imputation.", True, "Extremely sparse columns provide little signal and high imputation noise."),
        ("Mode imputation is the standard strategy for filling missing nominal categorical data.", True, "Categorical columns lack mean or median metrics, making the mode the standard central statistic."),

        # Operational Practice & Domain Cleaning (Medium/Hard)
        ("In antibiogram data, 'S' stands for Sensitive, 'I' for Intermediate, and 'R' for Resistant.", True, "Standard microbiological guidelines categorize antibiotic response into S, I, and R."),
        ("Ignoring case variations causes pandas value_counts() to list 'Male' and 'male' as separate groups.", True, "value_counts() performs exact string matching without automatic case normalization."),
        ("Using df.value_counts(dropna=False) reveals the count of missing NaN values alongside valid categories.", True, "dropna=False includes NaN counts in the output frequency table."),
        ("Replacing missing values with zero is only valid if zero holds real physical meaning in domain logic.", True, "Arbitrarily substituting 0 for NaN alters feature distributions and means."),
        ("A negative age value in a medical record indicates a data entry error that must be cleaned.", True, "Age cannot be negative in biological datasets; such records require correction or NaN coercion."),
        ("Data cleaning must precede feature scaling to prevent scaling calculations from including invalid entries.", True, "Scaling on dirty data incorporates extreme typos and missing values into mean and range metrics."),
        ("Checking df.info() displays column data types, non-null counts, and memory usage.", True, "df.info() provides a concise technical summary of DataFrame structure and completeness."),
        ("In pandas, df.rename(columns={'old':'new'}) renames specified column labels.", True, "df.rename() maps old column names to new labels via a dictionary."),
        ("Re-indexing or resetting DataFrame indices with reset_index(drop=True) fixes broken index sequences after dropping rows.", True, "reset_index(drop=True) discards old non-sequential indices and builds a fresh integer index."),
        ("Dropping rows with missing target labels is standard practice in supervised learning dataset preparation.", True, "Models cannot learn from training observations that lack valid ground truth labels."),

        # Additional Core Cleaning Concepts (Easy/Medium)
        ("Data leakage occurs if dataset-wide statistics calculated after splitting are used to clean pre-split data.", True, "Computing cleaning parameters on all data leaks test set statistics into training steps."),
        ("In pandas, df.select_dtypes(include=['number']) selects only numeric columns.", True, "select_dtypes filters DataFrame columns based on specified data types."),
        ("The pandas function pd.get_dummies() converts categorical variables into dummy one-hot indicator columns.", True, "pd.get_dummies() creates binary 0/1 columns for each unique categorical value."),
        ("Duplicate check on a subset of columns (subset=['Name', 'DOB']) detects duplicate patient entries.", True, "subset specifies key columns to check for row duplication."),
        ("Unresolved typographical errors in text columns increase the total number of unique categories artificially.", True, "Typos create spurious unique category labels, increasing feature dimensionality unnecessarily."),
        ("Replacing NaN values in text columns with 'Unknown' preserves missingness information explicitly.", True, "Converting NaN to 'Unknown' retains missing indicators as an explicit categorical state."),
        ("Statistical outliers can be caused by data entry errors, measurement errors, or natural extreme variations.", True, "Outliers stem from either valid extreme physical events or invalid reporting flaws."),
        ("Applying regex replacements with df.str.replace(regex=True) cleans complex text patterns.", True, "Regular expressions allow pattern-based text cleaning across pandas Series."),
        ("In pandas, df.memory_usage(deep=True) reports the exact memory consumed by object columns.", True, "deep=True inspects memory usage of dynamically allocated string objects in object columns."),
        ("Saving a cleaned dataset to CSV with index=False prevents writing an extra unnamed index column.", True, "index=False omits DataFrame integer index labels from output CSV files.")
    ]

    for i, (q, a, exp) in enumerate(normal_data, 1):
        questions.append({
            "id": f"TP1_{i:03d}",
            "tp": 1,
            "category": "normal",
            "question": q,
            "answer": a,
            "explanation": exp
        })

    # ---------------------------------------------------------
    # 50 TRICKY QUESTIONS (TP1_091 to TP1_140)
    # ---------------------------------------------------------
    tricky_data = [
        ("Replacing missing continuous values with zero is mathematically equivalent to mean imputation.", False, "Imputing zero alters the sample mean and variance, whereas mean imputation preserves the sample mean."),
        ("The Z-score method of outlier detection is completely immune to the presence of extreme outliers.", False, "Extreme outliers distort both the sample mean and standard deviation, reducing Z-score sensitivity."),
        ("The IQR outlier detection method assumes that the underlying dataset follows a strict Gaussian distribution.", False, "The IQR method is non-parametric and does not assume a Gaussian distribution."),
        ("In pandas, df.dropna(axis=1) drops rows that contain missing values.", False, "axis=1 drops columns containing missing values; axis=0 drops rows."),
        ("Forward fill (ffill) is the optimal missing value strategy for unordered categorical attributes.", False, "Forward fill assumes sequential temporal order and is inappropriate for unordered categorical data."),
        ("A Z-score threshold of 0 is typically used to flag extreme statistical outliers.", False, "A Z-score of 0 represents the exact sample mean, not an extreme outlier threshold."),
        ("Deduplication automatically corrects typographical errors present in text columns.", False, "Deduplication only removes identical rows; typos create distinct non-duplicate strings."),
        ("In pandas, df.fillna(method='bfill') fills missing values using the mean of preceding rows.", False, "bfill performs backward fill using the next valid observation, not the mean."),
        ("The mode of a continuous variable with unique values is always equal to its median.", False, "If continuous values are unique, no mode exists, whereas the median is the 50th percentile."),
        ("Using inplace=True on a pandas DataFrame slice modifies the original DataFrame and returns the modified object.", False, "inplace=True returns None, not the modified DataFrame object."),

        ("SimpleImputer(strategy='mean') can be applied directly to string columns containing missing text.", False, "Mean imputation requires numeric data and raises a TypeError when applied to strings."),
        ("Extrapolating missing values using linear interpolation produces accurate results regardless of row order.", False, "Linear interpolation depends strictly on the sequential order of index or row entries."),
        ("Trimming outliers from a dataset increases the total sample size.", False, "Trimming removes rows containing outliers, thereby reducing the total sample size."),
        ("In pandas, df.isna() returns True for empty string entries '' by default.", False, "Empty strings '' are considered valid non-null strings by pandas; pd.isna('') returns False."),
        ("The IQR metric is calculated as Q1 minus Q3.", False, "IQR is calculated as Q3 minus Q1 (the 75th percentile minus the 25th percentile)."),
        ("Overwriting missing continuous entries with a constant value of 0 never affects feature correlation.", False, "Imputing 0 alters variance and covariance, changing correlation coefficients."),
        ("In pandas, df.drop_duplicates(keep=False) retains the first duplicate row and drops remaining duplicates.", False, "keep=False drops ALL duplicate rows, leaving no copies."),
        ("Replacing NaNs in a binary feature with 0.5 preserves its integer data type.", False, "Inserting float 0.5 coerces the column data type to float64."),
        ("Removing all rows containing any NaN value is optimal when missingness exceeds 50% across all columns.", False, "Dropping rows when missingness is widespread destroys most of the sample size."),
        ("Mean imputation decreases the peak of a feature distribution while increasing its variance.", False, "Mean imputation spikes the distribution peak at the mean and reduces overall variance."),

        ("The expression df['Age'] < 0 | df['Age'] > 120 executes correctly in Python without parentheses around comparisons.", False, "Bitwise operators '|' have higher precedence than '<' and '>', requiring explicit parentheses."),
        ("In pandas, str.split('/') on '45/F' returns two separate DataFrames.", False, "str.split('/') returns a Series of lists unless expand=True is specified."),
        ("pd.to_numeric() with errors='ignore' converts unparseable strings into np.nan.", False, "errors='ignore' returns the original unparsed input unchanged; errors='coerce' yields np.nan."),
        ("SimpleImputer with strategy='median' can be fitted on categorical string columns.", False, "Median calculation requires ordered numerical data and fails on string columns."),
        ("The Z-score of a value equal to the mean is always 1.0.", False, "When a value equals the mean, its Z-score is 0.0."),
        ("Deduplication based on a subset of columns alters the number of columns in the DataFrame.", False, "Subset deduplication filters rows based on column values without dropping columns."),
        ("In pandas, df.astype(int) automatically converts NaN values into 0 without throwing an error.", False, "Converting NaN to int raises a ValueError because integer types cannot represent NaN in standard pandas."),
        ("An outlier identified by Tukey's IQR rule is always a corrupt data entry error that must be deleted.", False, "Outliers can represent legitimate extreme physical occurrences rather than data errors."),
        ("Standardizing antibiotics to binary 1/0 flags preserves intermediate 'I' susceptibility distinctions.", False, "Binarizing into 1/0 merges 'I' into either Resistant or Sensitive, losing intermediate state detail."),
        ("The pandas function df.dropna(how='all') drops rows that contain at least one NaN value.", False, "how='all' drops rows only if ALL values in the row are NaN; how='any' drops on a single NaN."),

        ("Applying mean imputation before splitting data into train and test sets prevents data leakage.", False, "Computing the global mean across all data before splitting leaks test set statistics into training."),
        ("In pandas, df.columns.drop('col') permanently deletes the column from disk and DataFrame.", False, "df.columns.drop() returns a new Index object without modifying the DataFrame in place."),
        ("Winsorization removes extreme rows from the DataFrame, reducing total row count.", False, "Winsorization caps extreme values to threshold boundaries without removing rows."),
        ("In pandas, df.drop(['col1'], axis=0) drops the column named 'col1'.", False, "axis=0 drops rows by index label; dropping columns requires axis=1 or columns=['col1']."),
        ("A negative correlation between missingness and an observed feature confirms MCAR missingness.", False, "If missingness correlates with an observed feature, data is MAR (Missing at Random), not MCAR."),
        ("SimpleImputer returns a pandas DataFrame when fitted on a DataFrame.", False, "Scikit-learn SimpleImputer fit_transform() returns a NumPy ndarray, not a DataFrame."),
        ("The mode of a categorical Series always returns a single scalar string value.", False, "df.mode() returns a Series, which may contain multiple values if there is a tie for highest frequency."),
        ("The IQR rule flags 50% of any dataset as outliers by definition.", False, "The IQR covers the middle 50% of data; outliers are points beyond 1.5*IQR from Q1/Q3."),
        ("In pandas, df.fillna(method='ffill') fills the first row of a Series if it contains NaN.", False, "Forward fill cannot populate a missing first row because no preceding value exists."),
        ("Using df.replace({'a': 'b'}) modifies string values in place without returning a copy.", False, "df.replace() returns a modified copy unless inplace=True is explicitly set."),

        ("The mean of Z-scores for any non-constant numerical feature is always equal to 1.0.", False, "Z-scores are centered around zero; the mean of Z-scores is always 0.0."),
        ("In pandas, df['Age'].min() returns NaN if the Series contains missing values.", False, "Pandas statistical functions skip NaN values by default (skipna=True) and return valid numeric bounds."),
        ("Deduplication should be performed after building final model evaluation metrics.", False, "Deduplication must occur during early data cleaning to prevent evaluation data corruption."),
        ("SimpleImputer(strategy='most_frequent') chooses the numerical mean in case of categorical ties.", False, "Most frequent strategy chooses the smallest categorical mode in case of ties, not the numerical mean."),
        ("The standard deviation of a dataset increases after imputing missing values with the mean.", False, "Imputing missing values with the exact sample mean reduces overall variance and standard deviation."),
        ("In pandas, df.rename() raises a KeyError if a column name in the mapping dict does not exist.", False, "df.rename() ignores missing dictionary keys silently without raising errors."),
        ("Outliers have no effect on the calculation of sample standard deviation.", False, "Standard deviation relies on squared deviations from the mean, making it highly sensitive to outliers."),
        ("The expression df[df['Age'].isna()] returns all rows where Age is a valid numeric value.", False, "df['Age'].isna() returns True for missing values; valid numeric rows require df['Age'].notna()."),
        ("Capping ages between 0 and 120 using df.loc[] alters the DataFrame column names.", False, "df.loc[] modifies cell content in matching rows without changing column labels."),
        ("Scikit-learn SimpleImputer automatically handles string column encoding during missing value replacement.", False, "SimpleImputer replaces missing values but does not perform categorical-to-numeric encoding.")
    ]

    for i, (q, a, exp) in enumerate(tricky_data, 91):
        questions.append({
            "id": f"TP1_{i:03d}",
            "tp": 1,
            "category": "tricky",
            "question": q,
            "answer": a,
            "explanation": exp
        })

    # ---------------------------------------------------------
    # 60 TRAP QUESTIONS (TP1_141 to TP1_200)
    # ---------------------------------------------------------
    trap_data = [
        ("Confusing missing values with zeros during cleaning leads to accurate mean calculations.", False, "Treating NaNs as 0s distorts calculations by artificially pulling down the true feature mean."),
        ("Assuming that dropping missing values (dropna) is always superior to imputation is correct.", False, "Indiscriminate row deletion destroys sample size and introduces selection bias when missingness is not MCAR."),
        ("Assuming that Z-score outlier detection works equally well on heavily skewed distributions is valid.", False, "Z-score assumes approximate normality; highly skewed distributions require non-parametric methods like IQR."),
        ("Believing that deduplication removes rows with subtle typographical differences in patient names.", False, "Deduplication requires exact matches; string typos like 'Smith' vs 'Smithe' evade standard deduplication."),
        ("Assuming that string cleaning operations can be executed on numeric int64 columns without casting.", False, "Pandas .str accessor methods require string/object dtypes and fail on numeric columns."),
        ("Confusing Forward Fill (ffill) with Backward Fill (bfill) results in identical imputed datasets.", False, "ffill propagates prior valid values forward while bfill propagates subsequent valid values backward."),
        ("Believing that SimpleImputer(strategy='mean') can impute missing values in categorical string columns.", False, "Mean calculation requires numeric values; applying mean strategy to string columns throws a TypeError."),
        ("Assuming that Tukey's IQR rule flags outliers based on distance from the sample mean.", False, "IQR flags outliers based on distance from quartiles (Q1 and Q3), not from the mean."),
        ("Confusing df.drop(axis=0) with df.drop(axis=1) when dropping unneeded DataFrame columns.", False, "axis=0 targets row indices; dropping column labels requires setting axis=1 or specifying columns=."),
        ("Assuming that replacing missing entries with -999 does not affect distance calculations in k-NN models.", False, "Distance-based algorithms treat -999 as a real scalar magnitude, distorting spatial distance metrics severely."),

        ("Believing that converting string flags 'Yes'/'No' to 1/0 changes the number of rows in a DataFrame.", False, "Encoding transforms column representations without altering row counts."),
        ("Confusing MAR (Missing at Random) with MCAR (Missing Completely at Random) leads to wrong bias assumptions.", False, "MCAR means missingness is independent of all data; MAR means missingness depends on observed data."),
        ("Assuming that outliers identified by Z-score > 3 must always be deleted prior to model training.", False, "Outliers may contain critical valid signals; deletion should be justified rather than automatic."),
        ("Believing that df.head() modifies the underlying DataFrame by keeping only the top 5 rows.", False, "df.head() returns a new preview slice without mutating the original DataFrame."),
        ("Confusing Ordinal Encoding with Nominal One-Hot Encoding distorts non-ordered categorical relationships.", False, "Ordinal encoding imposes an artificial implicit ordering on nominal categories without intrinsic rank."),
        ("Assuming that pd.to_numeric() automatically strips surrounding whitespace from text strings.", False, "Unstripped text strings cause pd.to_numeric() to fail unless errors='coerce' or str.strip() is used."),
        ("Believing that SimpleImputer fit_transform preserves pandas DataFrame column headers.", False, "fit_transform returns a raw NumPy ndarray, stripping DataFrame column headers."),
        ("Confusing sample mean with sample median when choosing an imputation statistic for highly skewed data.", False, "Skewed distributions shift the mean toward the tail, making the median the robust central choice."),
        ("Assuming that df.dropna() modifies the DataFrame in place without setting inplace=True or reassigning.", False, "df.dropna() returns a new DataFrame copy unless inplace=True is explicitly passed."),
        ("Believing that calculating Z-scores before removing extreme outliers prevents z-score distortion.", False, "Extreme outliers distort initial mean and standard deviation estimates, reducing Z-score detection accuracy."),

        ("Confusing row-wise operations (axis=1) with column-wise operations (axis=0) in df.apply().", False, "axis=1 passes rows to the custom function; axis=0 passes entire columns."),
        ("Assuming that duplicate rows only affect dataset size without impacting model accuracy or evaluation.", False, "Duplicates over-represent specific instances, biasing training boundaries and inflating validation metrics."),
        ("Believing that Winsorization deletes extreme rows from a dataset.", False, "Winsorization caps extreme values to specified percentile boundaries without deleting rows."),
        ("Confusing df.isna() with df.notna() produces identical boolean filtering masks.", False, "df.isna() flags missing values as True, while df.notna() flags valid non-null entries as True."),
        ("Assuming that errors='coerce' in pd.to_numeric() deletes rows containing invalid text strings.", False, "errors='coerce' replaces unparseable text with NaN values rather than deleting rows."),
        ("Believing that replacing NaNs with the mode is appropriate for continuous numerical attributes.", False, "Mode reflects discrete frequencies; continuous attributes rarely have meaningful repeated modes."),
        ("Confusing df.columns.tolist() with df.index.tolist() when inspecting DataFrame column headers.", False, "df.columns.tolist() lists column labels; df.index.tolist() lists row indices."),
        ("Assuming that string methods like str.lower() operate directly on standard Python lists of strings.", False, "Pandas .str methods operate on pandas Series, not native Python lists."),
        ("Believing that IQR is calculated by subtracting the minimum value from the maximum value.", False, "The difference between maximum and minimum is the Range; IQR is Q3 minus Q1."),
        ("Confusing data cleaning with feature scaling when preparing raw biomedical datasets.", False, "Data cleaning fixes errors, NaNs, and typos; feature scaling transforms numerical ranges."),

        ("Assuming that dropping privacy-sensitive metadata columns like 'Name' reduces model predictive power.", False, "Unique personal metadata like names carry no generalizable predictive signal and introduce noise."),
        ("Believing that SimpleImputer(strategy='most_frequent') can be used without specifying a missing_values target.", False, "SimpleImputer defaults missing_values to np.nan; custom missing representations must be specified."),
        ("Confusing categorical species typos ('E.coi') with valid distinct bacterial species.", False, "Typos are data entry errors representing the same underlying species, requiring standardization."),
        ("Assuming that df.duplicated().sum() counts the total number of non-duplicate unique rows.", False, "df.duplicated().sum() counts the total number of redundant duplicate rows."),
        ("Believing that imputing missing values after splitting data leads to severe data leakage.", False, "Imputing AFTER splitting using train-derived parameters prevents data leakage; imputing BEFORE causes leakage."),
        ("Confusing df.shape[0] (rows) with df.shape[1] (columns) when auditing dataset dimensions.", False, "df.shape[0] represents the total row count; df.shape[1] represents the total column count."),
        ("Assuming that all antibiotics in an antibiogram belong to the same chemical family.", False, "Antibiotics span distinct pharmacological families (e.g., beta-lactams, quinolones, aminoglycosides)."),
        ("Believing that replacing NaNs with mean values preserves the standard deviation of the feature.", False, "Mean imputation accumulates values at the mean, artificially reducing feature standard deviation."),
        ("Confusing categorical string encoding with numerical scaling in data preparation pipelines.", False, "Categorical encoding maps text to numbers; scaling adjusts numerical values to a unified range."),
        ("Assuming that df.drop_duplicates() modifies the index labels to be strictly sequential.", False, "drop_duplicates() retains original row index labels, leaving gaps where rows were removed."),

        ("Believing that pd.to_numeric() converts categorical string labels like 'Female' into integers automatically.", False, "pd.to_numeric() fails or coerces non-numeric text to NaN; categorical text requires explicit mapping or encoding."),
        ("Confusing Z-score normalization with Min-Max scaling when handling extreme outliers.", False, "Z-score scales based on mean and standard deviation; Min-Max scales strictly between 0 and 1."),
        ("Assuming that df.loc[condition, 'col'] = value overwrites the entire DataFrame.", False, "df.loc[condition, 'col'] updates only the cells matching the specified row condition and column label."),
        ("Believing that applying str.strip() on a string column removes internal spaces between words.", False, "str.strip() removes only leading and trailing whitespace, leaving internal spaces intact."),
        ("Confusing missing data mechanism MNAR (Missing Not at Random) with random noise.", False, "MNAR missingness depends on the unobserved value itself, introducing systematic non-random bias."),
        ("Assuming that checking df.dtypes displays the number of missing values in each column.", False, "df.dtypes displays column data types; missing values are checked via df.isna().sum()."),
        ("Believing that custom row-wise functions applied via df.apply(axis=1) run faster than vectorized pandas operations.", False, "Row-wise apply() iterates in Python and is significantly slower than vectorized pandas operations."),
        ("Confusing the lower outlier threshold (Q1 - 1.5*IQR) with the upper outlier threshold (Q3 + 1.5*IQR).", False, "Lower outliers fall below Q1 - 1.5*IQR; upper outliers exceed Q3 + 1.5*IQR."),
        ("Assuming that removing metadata columns like 'Address' makes a medical dataset non-compliant with GDPR.", False, "Removing personal identifiers like addresses ENHANCES GDPR privacy compliance."),
        ("Believing that df.reset_index(drop=True) creates a new index column while retaining the old index as a feature.", False, "drop=True discards the old index; setting drop=False retains the old index as a column."),

        ("Confusing antibiogram susceptibility codes 'R', 'S', and 'I' with numerical measurements.", False, "'R', 'S', and 'I' are discrete categorical susceptibility categories, not continuous numerical measurements."),
        ("Assuming that simple mean imputation on an imbalanced target column is standard practice.", False, "Mean imputation applies to continuous features, not binary target classification labels."),
        ("Believing that df.isna() modifies the DataFrame by replacing NaNs with True/False in place.", False, "df.isna() returns a new boolean DataFrame mask without modifying the original DataFrame."),
        ("Confusing data cleaning (error correction) with model evaluation (scoring model predictions).", False, "Data cleaning prepares raw data; model evaluation scores trained algorithm predictions."),
        ("Assuming that string concatenation ('45' + '/F') creates a numeric float value in Python.", False, "String concatenation joins text strings ('45/F'), creating an object string, not a numeric float."),
        ("Believing that pandas dropna(thresh=N) keeps only rows with at least N non-null values.", True, "thresh=N keeps rows that have at least N non-null (valid) entries."),
        ("Confusing df.iloc (integer-position indexing) with df.loc (label-based indexing).", False, "df.iloc uses 0-indexed integer positions; df.loc uses explicit index and column labels."),
        ("Assuming that median imputation on a bimodal distribution accurately represents both peaks.", False, "The median of a bimodal distribution falls between the peaks, where data density may be lowest."),
        ("Believing that deduplication on a single column drops duplicate values across all other columns unconditionally.", False, "Deduplication on a single column keeps the first row matching each unique value in that column."),
        ("Confusing raw data exploration with automated feature extraction in biomedical pipelines.", False, "Raw data exploration inspects distributions and errors; feature extraction engineers new variables.")
    ]

    for i, (q, a, exp) in enumerate(trap_data, 141):
        questions.append({
            "id": f"TP1_{i:03d}",
            "tp": 1,
            "category": "trap",
            "question": q,
            "answer": a,
            "explanation": exp
        })

    return questions

if __name__ == "__main__":
    qs = get_tp1_questions()
    print(f"TP1 Total: {len(qs)}")
    print("Normal:", sum(1 for q in qs if q["category"] == "normal"))
    print("Tricky:", sum(1 for q in qs if q["category"] == "tricky"))
    print("Trap:", sum(1 for q in qs if q["category"] == "trap"))
