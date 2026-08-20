# TP 2 — Exploratory Data Analysis and Visualization (200 Questions: 90 Normal, 50 Tricky, 60 Trap)

def get_tp2_questions():
    questions = []
    
    # ---------------------------------------------------------
    # 90 NORMAL QUESTIONS (TP2_001 to TP2_090)
    # ---------------------------------------------------------
    normal_data = [
        # Exploratory Data Analysis & Pandas Basics (Easy/Medium)
        ("Exploratory Data Analysis (EDA) is the process of summarizing dataset main characteristics, often using visual methods.", True, "EDA uses descriptive statistics and graphics to discover patterns and anomaly signals before modeling."),
        ("In pandas, df.describe() generates summary statistics including mean, std, min, percentiles, and max for numeric columns.", True, "describe() outputs key descriptive statistics for numerical columns in a DataFrame."),
        ("The pandas DataFrame is a two-dimensional labeled data structure with columns of potentially different types.", True, "DataFrames store tabular data with index rows and named heterogenous columns."),
        ("In pandas, df.shape returns a tuple where the first element is the row count and the second is the column count.", True, "df.shape[0] gives the total number of rows and df.shape[1] the column count."),
        ("A pandas Series is a one-dimensional labeled array capable of holding any data type.", True, "A Series is a 1D labeled array representing a single DataFrame column or standalone sequence."),
        ("Calling df.info() provides a summary of column data types, non-null counts, and memory usage.", True, "info() prints a concise summary of DataFrame structural metadata and nullness."),
        ("In pandas, df.head() displays the first 5 rows of a DataFrame by default.", True, "head() defaults to returning the top 5 rows unless a different integer parameter is passed."),
        ("The df.tail(n) method displays the last n rows of a DataFrame.", True, "tail(n) extracts the bottom n rows from a DataFrame."),
        ("EDA helps identify class imbalance in target categorical variables prior to model training.", True, "Examining category counts during EDA highlights severe class proportion imbalances."),
        ("Pandas read_excel() is used to read data from Microsoft Excel files into a DataFrame.", True, "read_excel() parses spreadsheet formats like .xls and .xlsx into pandas DataFrames."),

        # Descriptive Statistics & Distributions (Medium)
        ("The mean is the arithmetic average of a set of numerical values.", True, "Mean is calculated by dividing the sum of all values by the sample count."),
        ("The median represents the middle value when a numerical dataset is ordered from smallest to largest.", True, "The median divides an ordered distribution into two equal halves."),
        ("The standard deviation measures the dispersion or spread of numerical values relative to their mean.", True, "Standard deviation quantifies the average deviation of data points from the sample mean."),
        ("In a symmetric normal distribution, the mean, median, and mode are approximately equal.", True, "Normal distributions exhibit perfect symmetry where mean, median, and mode coincide at the center."),
        ("Variance is the average of the squared deviations from the mean.", True, "Variance equals the square of the standard deviation, measuring dispersion in squared units."),
        ("The 25th percentile (Q1) marks the value below which 25% of the data falls.", True, "Q1 represents the first quartile, marking the lower 25% boundary of ordered data."),
        ("The 75th percentile (Q3) marks the value below which 75% of the data falls.", True, "Q3 represents the third quartile, separating the lower 75% of data from the top 25%."),
        ("Skewness measures the asymmetry of a probability distribution around its mean.", True, "Positive skew indicates a long right tail; negative skew indicates a long left tail."),
        ("Kurtosis measures the heavy-tailedness or light-tailedness of a distribution relative to a normal distribution.", True, "Kurtosis quantifies extreme tail weights and peak sharpness in a distribution."),
        ("The range of a numerical variable is computed as the maximum value minus the minimum value.", True, "Range measures total spread from the smallest to the largest observed value."),

        # Pandas Filtering, Indexing & Groupby (Medium)
        ("In pandas, boolean indexing filters rows using boolean conditional expressions like df[df['age'] > 18].", True, "Boolean indexing passes a boolean mask Series to filter DataFrame rows matching True."),
        ("The df.groupby('sex').mean() method computes the mean of numerical columns separately for each sex category.", True, "groupby() splits data into groups by category and applies an aggregation function to each group."),
        ("In pandas, df['pclass'].value_counts() returns the frequency count of each unique value in the pclass column.", True, "value_counts() computes discrete counts of unique occurrences in a Series."),
        ("Grouping by multiple columns, such as df.groupby(['sex', 'pclass']).mean(), produces multi-level group aggregations.", True, "groupby accepts a list of column names to aggregate data across combinations of categories."),
        ("In pandas, df['age'].isnull().sum() counts the total number of missing NaN values in the age column.", True, "isnull() returns True for missing entries and sum() counts total missing items."),
        ("Slicing a pandas Series with data['age'][0:10] selects the first 10 element entries.", True, "Series positional slicing returns elements from start index up to end index minus one."),
        ("The df.sort_values(by='age', ascending=False) method sorts rows by age in descending order.", True, "sort_values() orders DataFrame rows by specified column values; ascending=False sorts high to low."),
        ("In pandas, df['fare'].nunique() returns the number of distinct unique non-null values in the fare column.", True, "nunique() counts unique scalar values, excluding NaNs by default."),
        ("Pandas crosstab function pd.crosstab(df['sex'], df['survived']) computes a frequency cross-tabulation table.", True, "pd.crosstab() constructs a contingency table showing joint frequencies of two categorical variables."),
        ("Resetting group indices with df.groupby(...).mean().reset_index() converts group keys back into standard columns.", True, "reset_index() flattens multi-level group indices into standard DataFrame columns."),

        # Matplotlib & Seaborn Visualizations (Medium)
        ("A histogram displays the frequency distribution of a continuous numerical variable using adjacent bars (bins).", True, "Histograms bin continuous range intervals to visualize distribution shapes and frequencies."),
        ("A box plot (box-and-whisker plot) visually depicts median, quartiles, and potential outliers of a distribution.", True, "Box plots draw a central box between Q1 and Q3, a median line, whiskers, and individual outlier points."),
        ("In Seaborn, sns.countplot(x='sex', data=df) creates a bar plot showing category counts for a categorical variable.", True, "countplot() renders discrete frequency bars for categorical column levels."),
        ("A scatter plot graphs individual data points on two continuous axes to inspect relationships between variables.", True, "Scatter plots display pairs of continuous values as points to reveal correlations and patterns."),
        ("In Seaborn, sns.heatmap(df.corr(), annot=True) displays a color-coded matrix of correlation values with numbers.", True, "heatmap() renders a colored matrix grid; annot=True prints numerical values inside cells."),
        ("A bar chart is appropriate for comparing discrete values or summary statistics across distinct categories.", True, "Bar charts represent discrete categorical levels using rectangular bars proportional to values."),
        ("In Matplotlib, plt.figure(figsize=(10, 6)) sets the canvas width to 10 inches and height to 6 inches.", True, "plt.figure(figsize=(w, h)) defines figure dimensions prior to plotting graphics."),
        ("Adding a legend with plt.legend() helps label different data series or groups in a plot.", True, "plt.legend() displays descriptive labels associated with plot markers and lines."),
        ("Seaborn sns.boxplot(x='pclass', y='age', data=df) compares age distributions across passenger classes.", True, "Passing categorical x and numerical y to boxplot() draws parallel boxplots per category."),
        ("A density plot (KDE plot) estimates and visualizes the smooth probability density function of a continuous variable.", True, "Kernel Density Estimation (KDE) generates a smooth continuous probability curve over data points."),

        # Correlations & Relationships (Medium/Hard)
        ("The Pearson correlation coefficient measures the strength and direction of linear relationship between two continuous variables.", True, "Pearson's r quantifies linear dependency, ranging from -1.0 (perfect negative) to +1.0 (perfect positive)."),
        ("A Pearson correlation coefficient of 0 indicates no linear relationship between two continuous variables.", True, "An r value of 0 signifies absence of linear association, though non-linear relationships may still exist."),
        ("Correlation does not imply causation.", True, "Statistical correlation between two variables does not prove that one variable causes the other."),
        ("Spearman rank correlation assesses monotonic relationships between two ranked or continuous variables.", True, "Spearman's rho evaluates rank-order monotonicity without requiring linear relationship assumptions."),
        ("In pandas, df.corr() computes the pairwise correlation of numerical columns in a DataFrame.", True, "df.corr() calculates a square pairwise correlation matrix across numeric DataFrame columns."),
        ("A correlation coefficient close to +1.0 indicates a strong positive linear relationship.", True, "As one variable increases, the other increases proportionally in a strong positive correlation."),
        ("A correlation coefficient close to -1.0 indicates a strong negative linear relationship.", True, "As one variable increases, the other decreases proportionally in a strong negative correlation."),
        ("A pair plot (sns.pairplot) renders pairwise scatter plots and marginal distributions across multiple numerical variables.", True, "pairplot() constructs a matrix grid of scatter plots for all numerical variable pairs."),
        ("Strong multicollinearity occurs when two or more predictor features are highly correlated with each other.", True, "Multicollinearity describes strong linear dependencies among independent input variables."),
        ("Examining correlations between features and target labels identifies top predictive variables during EDA.", True, "High target correlation highlights attributes that contain strong predictive signal for modeling."),

        # Outlier Detection & Distribution Inspection (Medium/Hard)
        ("Outliers appear as individual data points plotted beyond the whiskers in a standard box plot.", True, "Whiskers extend to 1.5*IQR beyond Q1/Q3; points outside are drawn as standalone outlier points."),
        ("A right-skewed (positively skewed) distribution has a long tail extending toward higher positive values.", True, "Right skew pulls the sample mean to the right of the median toward large positive values."),
        ("A left-skewed (negatively skewed) distribution has a long tail extending toward lower negative values.", True, "Left skew pulls the sample mean to the left of the median toward small negative values."),
        ("In right-skewed distributions, the mean is typically greater than the median.", True, "Large extreme values in the right tail inflate the mean above the 50th percentile median."),
        ("In left-skewed distributions, the mean is typically less than the median.", True, "Small extreme values in the left tail pull the mean below the 50th percentile median."),
        ("Logarithmic transformation can reduce positive skewness in non-negative continuous features like income or fare.", True, "Applying log(x + 1) compresses large positive values, normalizing right-skewed distributions."),
        ("Bimodal distributions exhibit two distinct prominent peaks in their frequency histograms.", True, "Bimodality indicates two separate sub-populations or modes within the same feature distribution."),
        ("Summary statistics should include both central tendency (mean/median) and dispersion (std/IQR).", True, "Reporting spread alongside central tendency provides a complete description of distribution properties."),
        ("Using plt.savefig('plot.png') saves the current Matplotlib figure to an image file on disk.", True, "plt.savefig() exports the rendered plot graphic to specified file formats like PNG or PDF."),
        ("Outliers can significantly skew the mean while having minimal impact on the median.", True, "The mean incorporates extreme magnitudes, whereas the median depends only on rank order position."),

        # Categorical Analysis & Group Comparisons (Medium)
        ("Examining survival rates by gender in the Titanic dataset reveals a higher survival proportion for females.", True, "df.groupby('sex')['survived'].mean() shows female survival (~75%) exceeds male survival (~20%)."),
        ("Analyzing passenger class survival demonstrates that 1st class passengers survived at a higher rate than 3rd class.", True, "PClass 1 survival rate is significantly higher than PClass 3 survival rate in Titanic EDA."),
        ("Categorical variables can be nominal (unordered labels like Gender) or ordinal (ranked categories like Class).", True, "Nominal categories have no intrinsic ordering; ordinal categories possess a natural progression."),
        ("A pie chart represents categorical proportions as slices of a circle totaling 100%.", True, "Pie charts display relative percentage contributions of discrete categories as circular slices."),
        ("Bar charts are generally preferred over pie charts for comparing multiple categorical levels accurately.", True, "Human visual perception assesses linear bar lengths more accurately than circular slice angles."),
        ("In Seaborn, sns.barplot(x='sex', y='survived', data=df) plots mean survival rates with error bars by gender.", True, "sns.barplot automatically computes group means for y and renders confidence interval error bars."),
        ("Cross-tabulation normalization pd.crosstab(df['sex'], df['survived'], normalize='index') yields row percentages.", True, "normalize='index' calculates proportions within each row category, converting counts to relative percentages."),
        ("Visualizing missing values with a heatmap (sns.heatmap(df.isnull())) reveals missingness patterns across rows.", True, "Null heatmaps render missing entries in a distinct color to expose missingness clusters across columns."),
        ("Filtering children (age < 18) in EDA helps compare minor vs adult survival trends explicitly.", True, "Boolean indexing df[df['age'] < 18] isolates child subset records for demographic breakdown."),
        ("Modifying plot aesthetics using plt.style.use('ggplot') applies the popular ggplot visual style.", True, "plt.style.use() alters default Matplotlib gridlines, background shading, and color palettes."),

        # Practical EDA Patterns & Code Snippets (Medium)
        ("In pandas, df.value_counts(normalize=True) calculates the relative proportions of unique values instead of raw counts.", True, "normalize=True scales count output so all unique category frequencies sum to 1.0."),
        ("Setting alpha parameter (e.g., plt.scatter(x, y, alpha=0.5)) reduces marker opacity to visualize overlapping points.", True, "Alpha transparency highlights point density in regions where scatter plot markers overlap heavily."),
        ("In Matplotlib, plt.xlabel() and plt.ylabel() add custom text labels to plot axes.", True, "xlabel() and ylabel() annotate x and y axes with descriptive titles."),
        ("Calling plt.show() displays all constructed plot figures in the user interface.", True, "plt.show() renders active figure canvases to the visual output device."),
        ("The pandas function df.sample(n=5) returns a random sample of 5 rows from the DataFrame.", True, "df.sample() extracts a random subset of rows without changing original data order."),
        ("In Seaborn, hue parameter in sns.scatterplot(x, y, hue='survived') colors scatter points by class label.", True, "hue maps a categorical variable to distinct colors, adding a 3rd dimension to 2D scatter plots."),
        ("Calling plt.clf() or plt.close() clears the active figure to prevent plot overlap in script loops.", True, "Clearing the figure canvas prevents subsequent plots from drawing over previous graphic axes."),
        ("In Matplotlib, plt.subplots(2, 2) creates a grid layout containing 2 rows and 2 columns of subplots.", True, "plt.subplots(nrows, ncols) returns a figure and an array of subplot axes for multi-panel plotting."),
        ("Box plots draw a horizontal or vertical line inside the interquartile box to indicate the median value.", True, "The line inside the Q1-Q3 box explicitly marks the 50th percentile median."),
        ("Histograms with small bin counts can oversmoot distributions, hiding underlying multi-modal features.", True, "Using too few bins lumps data into wide intervals, masking detailed structural features."),

        # Advanced EDA Concepts & Best Practices (Medium/Hard)
        ("Exploratory Data Analysis should always precede feature engineering and model building steps.", True, "EDA provides necessary insights into distribution shapes, missingness, and outliers to guide preprocessing."),
        ("In a left-skewed distribution, the tail extends toward lower values on the left side of the plot.", True, "Left-skewed distributions feature an elongated tail stretching toward negative or small values."),
        ("Violin plots combine box plot statistics with kernel density estimation curves on each side.", True, "sns.violinplot displays density width profiles alongside inner quartile box markers."),
        ("Pair plots with hue parameter (sns.pairplot(df, hue='target')) visualize class separability across feature pairs.", True, "Color-coding pair plots by target label reveals which feature pairs effectively separate classes."),
        ("Analyzing feature correlations prevents introducing redundant collinear inputs into linear models.", True, "Identifying highly correlated predictor pairs enables removing redundant inputs before modeling."),
        ("In pandas, df.describe(include='all') computes descriptive statistics for both numeric and categorical columns.", True, "include='all' forces describe() to report top category, frequency, and unique count for non-numeric columns."),
        ("Histograms with high bin counts can display sample noise, masking the smooth underlying distribution.", True, "Excessive binning breaks data into tiny sparse intervals, creating noisy jagged bars."),
        ("Correlation matrices are always symmetric along their main diagonal.", True, "The correlation between Variable A and Variable B equals the correlation between B and A."),
        ("The main diagonal of a correlation matrix always contains values equal to 1.0.", True, "Every numerical variable has a perfect positive linear correlation (1.0) with itself."),
        ("Exploratory visualizations allow discovering unexpected data recording errors and corrupted entries.", True, "Visual plots quickly expose unrealistic boundary spikes, zero-imputation artifacts, and extreme typos.")
    ]

    for i, (q, a, exp) in enumerate(normal_data, 1):
        questions.append({
            "id": f"TP2_{i:03d}",
            "tp": 2,
            "category": "normal",
            "question": q,
            "answer": a,
            "explanation": exp
        })

    # ---------------------------------------------------------
    # 50 TRICKY QUESTIONS (TP2_091 to TP2_140)
    # ---------------------------------------------------------
    tricky_data = [
        ("A Pearson correlation coefficient of 0.0 guarantees that two variables have no relationship of any kind.", False, "Pearson correlation only detects linear relationships; two variables can have a strong non-linear relationship while r = 0."),
        ("The median of a numerical column is always equal to its arithmetic mean.", False, "Mean and median differ in skewed distributions; they are equal only in perfectly symmetric distributions."),
        ("In pandas, df.describe() includes categorical string columns in its summary table by default.", False, "By default, describe() processes only numerical columns unless include='all' or include=['object'] is passed."),
        ("Increasing the number of bins in a histogram always makes the distribution look smoother.", False, "Increasing bin counts creates narrower bins, making the histogram look more jagged and noisy."),
        ("The standard deviation of a feature can be negative if the dataset contains negative numbers.", False, "Standard deviation is the square root of variance and is always non-negative (>= 0)."),
        ("In pandas, df.groupby('sex').mean() automatically includes string columns in the calculated averages.", False, "Pandas mean() excludes non-numeric string columns automatically because text cannot be averaged."),
        ("A scatter plot is the primary visualization for displaying frequency counts of a single nominal categorical variable.", False, "Scatter plots compare two continuous variables; categorical frequencies are displayed using bar or count plots."),
        ("A correlation coefficient of -0.9 indicates a much weaker relationship than a correlation coefficient of +0.3.", False, "The magnitude (|r|) determines relationship strength; |-0.9| = 0.9 is much stronger than |0.3| = 0.3."),
        ("In Seaborn, sns.heatmap() requires all input columns to be string object data types.", False, "Heatmaps require a numerical matrix (e.g., correlation matrix of floats), failing on string objects."),
        ("Box plots display the exact mean of a continuous variable as the line inside the interquartile box.", False, "The line inside the box marks the median (50th percentile), not the arithmetic mean."),

        ("Adding a constant value (e.g., +10) to every numerical observation in a column doubles its standard deviation.", False, "Adding a constant shifts the distribution location without altering its spread or standard deviation."),
        ("In pandas, df['age'].value_counts() returns values sorted by age in ascending order by default.", False, "value_counts() sorts output by frequency counts in descending order by default, not by key values."),
        ("If a feature has a right-skewed distribution, its median is typically larger than its mean.", False, "Right-skewed distributions have a long positive tail that pulls the mean to the RIGHT of (greater than) the median."),
        ("A pair plot (sns.pairplot) can only be generated for datasets with exactly two continuous variables.", False, "pairplot generates an N x N matrix grid for any number of numerical features in a DataFrame."),
        ("In Matplotlib, plt.legend() creates axis tick labels for numeric dimensions.", False, "plt.legend() displays color/marker label keys; axis tick labels are controlled by xticks/yticks."),
        ("Calculating df.corr() on a DataFrame automatically includes missing NaN values in pairwise products.", False, "Pandas corr() skips NaN values pairwise by default when computing correlation coefficients."),
        ("Histograms and bar charts are identical visualizations that can be used interchangeably for any data type.", False, "Histograms plot continuous numeric bin intervals; bar charts display discrete separate categorical groups."),
        ("The interquartile range (IQR) covers 75% of the data in any distribution.", False, "The IQR (Q3 - Q1) covers the middle 50% of the data distribution by definition."),
        ("In pandas, boolean indexing with df[df['age'] = 20] correctly filters rows where age equals 20.", False, "Single '=' is an assignment operator and causes a SyntaxError; comparison requires double '=='."),
        ("Spearman rank correlation coefficient evaluates linear relationships exclusively.", False, "Spearman rank correlation evaluates monotonic relationships based on ranks, not strictly linear associations."),

        ("A box plot whisker always extends to the absolute maximum value of the dataset, regardless of outliers.", False, "Whiskers extend up to 1.5*IQR from quartiles; values beyond are plotted as individual outlier points."),
        ("In pandas, df.head(10) creates a permanent standalone file on disk named head10.csv.", False, "df.head() returns a memory slice preview in Python without saving files to disk."),
        ("Replacing missing values with the column median always increases the interquartile range (IQR).", False, "Imputing the median accumulates values at the center, leaving IQR unchanged or slightly compressed."),
        ("In Seaborn, sns.countplot(x='age', data=df) is optimal for continuous floating-point variables with 1000 unique values.", False, "countplot renders separate bars for every unique value; continuous floats create an unreadable overcrowded plot."),
        ("If two variables have a Pearson correlation of +1.0, an increase in one variable guarantees an identical absolute unit increase in the other.", False, "Correlation of +1.0 indicates a perfect positive LINEAR relationship (y = a*x + b); the slope 'a' can be any positive constant, not necessarily 1."),
        ("In pandas, df.shape[0] returns the total number of columns in the DataFrame.", False, "df.shape[0] returns the total number of ROWS; df.shape[1] returns the column count."),
        ("A distribution with kurtosis of 0 has infinitely heavy extreme tails.", False, "A kurtosis of 0 (or excess kurtosis 0) corresponds to a standard normal distribution."),
        ("The variance of a feature is measured in the same units as the original feature values.", False, "Variance is measured in SQUARED units of the original feature; standard deviation retains original units."),
        ("In Matplotlib, plt.savefig() must always be called AFTER plt.show() to save the rendered figure properly.", False, "Calling plt.show() clears the active figure canvas in Matplotlib; calling savefig() after show() saves a blank image."),
        ("A pie chart is the recommended visual tool for displaying continuous time-series trend lines.", False, "Time-series trends are displayed using line plots; pie charts show static categorical proportions."),

        ("In pandas, df.groupby('sex')['age'].mean() returns a 2D DataFrame with 10 columns.", False, "Grouping a single column by a category returns a 1D pandas Series indexed by category."),
        ("A negative covariance between two numerical features implies that both features decrease together.", False, "Negative covariance means as one feature increases, the other feature tends to DECREASE."),
        ("Log-transforming a left-skewed distribution with negative values makes it normally distributed.", False, "Log transforms require positive values (x > 0) and are used to fix RIGHT-skewness, not left-skewness."),
        ("The pandas function pd.crosstab() can only process boolean 0/1 indicator columns.", False, "pd.crosstab() accepts any categorical, ordinal, or discrete Series to compute joint frequency tables."),
        ("Adding an extreme positive outlier to a numerical column significantly shifts its median to the right while leaving its mean unchanged.", False, "Outliers heavily pull the MEAN toward the extreme value while having minimal impact on the rank-based MEDIAN."),
        ("In Seaborn, setting hue='age' in a scatter plot automatically bins age into 3 discrete age brackets.", False, "Setting a continuous numerical variable as hue applies a continuous gradient color spectrum without binning."),
        ("The 50th percentile of a dataset is mathematically identical to its sample mean.", False, "The 50th percentile is the MEDIAN, which equals the mean only in symmetric distributions."),
        ("In pandas, df.drop(columns=['age']) modifies the original DataFrame on disk without re-saving.", False, "Pandas operates strictly in in-memory RAM; disk files are unaffected unless explicitly written with to_csv/to_excel."),
        ("A correlation matrix computed on 5 features has dimensions 5 x 10.", False, "A pairwise correlation matrix for N features is always a square N x N matrix (5 x 5)."),
        ("In Seaborn, sns.boxplot() cannot draw horizontal box plots.", False, "Passing a continuous feature to x (or setting orient='h') draws horizontal box plots in Seaborn."),

        ("The area under a frequency histogram equals 100 by definition.", False, "The total area under a standard frequency histogram equals bin width times sample count; probability density histograms sum area to 1.0."),
        ("In pandas, df.isnull().sum() computes the total number of valid non-null rows in each column.", False, "isnull().sum() counts MISSING NaN values; non-null values are counted via df.notnull().sum() or df.count()."),
        ("A scatter plot matrix (pairplot) displays target class probabilities directly.", False, "Pair plots graph feature vs feature scatter plots; class probabilities require trained probabilistic models."),
        ("The variance of a constant feature whose entries are all equal to 5.0 is equal to 5.0.", False, "A constant feature has zero dispersion; its variance and standard deviation are exactly 0.0."),
        ("In pandas, df.sort_values(by=['pclass', 'age']) sorts by pclass descending and age descending by default.", False, "sort_values() defaults to ASCENDING=True for all specified sort columns unless ascending=False is passed."),
        ("A distribution with positive skewness has its longest tail extending toward negative infinity.", False, "Positive skewness means the long tail extends toward POSITIVE infinity (to the right)."),
        ("In Seaborn, sns.heatmap(df.corr()) fails if the DataFrame contains float values.", False, "sns.heatmap() requires numerical floats or integers to color-code matrix cells."),
        ("The range of a dataset is robust against extreme outliers.", False, "Range = Max - Min depends directly on the extreme boundary values, making it highly sensitive to outliers."),
        ("In pandas, df['sex'].unique() returns a DataFrame containing sorted unique frequency counts.", False, ".unique() returns a NumPy 1D array of unique values without frequency counts or DataFrame formatting."),
        ("Bimodal distributions can be accurately characterized by reporting only their sample mean and standard deviation.", False, "Reporting only mean and std hides the two-peak bimodal structure; graphical histograms or KDE plots are required.")
    ]

    for i, (q, a, exp) in enumerate(tricky_data, 91):
        questions.append({
            "id": f"TP2_{i:03d}",
            "tp": 2,
            "category": "tricky",
            "question": q,
            "answer": a,
            "explanation": exp
        })

    # ---------------------------------------------------------
    # 60 TRAP QUESTIONS (TP2_141 to TP2_200)
    # ---------------------------------------------------------
    trap_data = [
        ("Confusing correlation with causation during EDA leads to incorrectly assuming feature X directly drives target Y.", False, "Correlation establishes association strength but does not prove direct causal mechanisms."),
        ("Assuming that df.describe() displays statistics for text/string columns by default.", False, "By default, describe() processes only numerical columns, ignoring non-numeric string features."),
        ("Believing that a Pearson correlation of 0.0 proves two variables are completely independent.", False, "Pearson r = 0 checks for linear dependence only; strong non-linear relationships can exist with r = 0."),
        ("Confusing the median (50th percentile) with the arithmetic mean in right-skewed distributions.", False, "In right-skewed data, the mean is pulled right toward large tail values while the median stays at the 50th percentile."),
        ("Assuming that calling plt.savefig() after plt.show() saves the rendered visual plot correctly.", False, "plt.show() clears the visual canvas; calling savefig() afterward saves a blank image."),
        ("Believing that histograms and bar plots are identical tools for continuous numerical features.", False, "Histograms plot continuous numerical range bins; bar plots compare discrete categorical levels."),
        ("Confusing IQR (Q3 - Q1) with full range (Max - Min) when evaluating distribution spread.", False, "IQR measures middle 50% spread between quartiles, whereas Range measures total distance between extremes."),
        ("Assuming that sns.countplot() is suitable for visualizing continuous floating-point attributes with 5000 unique values.", False, "countplot renders distinct bars per unique value, producing an unreadable overcrowded plot for continuous floats."),
        ("Believing that df.shape[0] reports the number of columns in a pandas DataFrame.", False, "df.shape[0] gives the total ROW count; df.shape[1] gives the column count."),
        ("Confusing positive skewness (long right tail) with negative skewness (long left tail).", False, "Positive skew stretches toward high values (right); negative skew stretches toward low values (left)."),

        ("Assuming that adding a constant value to every observation increases feature variance.", False, "Adding a constant shifts the mean location without changing dispersion or variance."),
        ("Believing that df.groupby('sex').mean() includes non-numeric string columns in its output table.", False, "Pandas mean() automatically skips non-numeric string columns because text cannot be averaged."),
        ("Confusing Spearman rank correlation with Pearson linear correlation when analyzing non-linear monotonic trends.", False, "Spearman evaluates rank-order monotonicity; Pearson evaluates strict linear association."),
        ("Assuming that a box plot whisker always extends to the absolute maximum data value.", False, "Whiskers stop at 1.5*IQR from quartiles; points beyond are plotted individually as outliers."),
        ("Believing that high multicollinearity between predictor features improves linear model stability.", False, "High multicollinearity inflates coefficient variance and destabilizes linear model estimation."),
        ("Confusing df.isnull().sum() with total non-null row counts.", False, "df.isnull().sum() counts missing NaN entries; non-null entries are counted via df.notnull().sum()."),
        ("Assuming that a correlation matrix of 4 numerical features has dimensions 4 x 8.", False, "Pairwise correlation matrices are always square N x N matrices (4 x 4)."),
        ("Believing that log-transformation can be directly applied to columns containing negative numbers.", False, "Log transforms require strictly positive inputs (x > 0) and fail or yield NaNs on negative numbers."),
        ("Confusing Seaborn pairplot with single feature distribution histograms.", False, "Pairplot constructs an N x N matrix of scatter plots and marginal distributions across feature pairs."),
        ("Assuming that df.value_counts() returns results sorted alphabetically by category name by default.", False, "value_counts() sorts results by frequency counts in descending order by default."),

        ("Believing that high correlation between two input features guarantees both features are necessary for modeling.", False, "Highly correlated inputs provide redundant information; one feature can often be removed."),
        ("Confusing df.sort_values(ascending=False) with default ascending sort order.", False, "ascending=False sorts from highest to lowest; default ascending=True sorts from lowest to highest."),
        ("Assuming that plt.legend() defines numerical axis ranges on Matplotlib plots.", False, "plt.legend() annotates plot series keys; axis ranges are set via xlim/ylim or xticks/yticks."),
        ("Believing that mean imputation on a bimodal distribution preserves its original shape.", False, "Imputing the mean places values between the two peaks, distorting the original bimodal structure."),
        ("Confusing sample standard deviation with sample variance when interpreting feature units.", False, "Standard deviation shares the original feature units; variance is expressed in squared units."),
        ("Assuming that df.head() permanently modifies the DataFrame structure on disk.", False, "df.head() returns an in-memory preview slice without altering original stored files."),
        ("Believing that a correlation magnitude of -0.8 reflects a weaker relationship than +0.4.", False, "Correlation strength depends on absolute value: |-0.8| = 0.8 is stronger than |+0.4| = 0.4."),
        ("Confusing pd.crosstab() with pd.DataFrame.describe().", False, "crosstab computes joint frequency tables for categorical pairs; describe outputs univariate summary statistics."),
        ("Assuming that out-of-range outlier values in box plots are always data recording errors.", False, "Outliers beyond 1.5*IQR can represent legitimate extreme physical events in real distributions."),
        ("Believing that Seaborn heatmap requires categorical string text inside matrix cells.", False, "sns.heatmap requires a numerical matrix of floats or ints to map cell colors."),

        ("Confusing Q1 (25th percentile) with Q3 (75th percentile) when calculating IQR.", False, "Q1 is the lower 25th percentile boundary; Q3 is the upper 75th percentile boundary."),
        ("Assuming that df.sample(n=5) selects the first 5 rows of a DataFrame sequentially.", False, "df.sample(n=5) extracts 5 random rows; sequential extraction is done via df.head(5) or iloc[:5]."),
        ("Believing that alpha parameter in scatter plots changes marker font size.", False, "alpha controls marker transparency (0.0 transparent to 1.0 opaque), not font size."),
        ("Confusing row-level missingness heatmaps with feature correlation heatmaps.", False, "Missingness heatmaps visualize NaN locations across rows; correlation heatmaps show pairwise float correlations."),
        ("Assuming that df.corr() throws an error when missing NaN values are present.", False, "Pandas corr() computes correlations by automatically skipping NaN values pairwise."),
        ("Believing that a pie chart is superior to a bar chart for comparing 15 categorical levels.", False, "Pie charts become cluttered and unreadable with 15 slices; bar charts compare many levels far better."),
        ("Confusing right-skewed distributions with left-skewed distributions when choosing central metrics.", False, "Right-skewed data has a long positive tail (mean > median); left-skewed data has a long negative tail (mean < median)."),
        ("Assuming that setting hue in Seaborn scatter plots reduces dataset row count.", False, "hue adds a categorical or numeric color dimension to plot points without dropping rows."),
        ("Believing that variance of a constant feature equals 1.0.", False, "A constant feature has zero variation; its variance is strictly 0.0."),
        ("Confusing pd.read_excel() with pd.read_csv() when parsing comma-separated text files.", False, "read_csv() parses text CSVs; read_excel() parses binary spreadsheet formats like .xlsx."),

        {"id": "TP2_181", "tp": 2, "category": "trap", "question": "Assuming that calculating df.nunique() includes missing NaN values in the unique count.", "answer": False, "explanation": "nunique() excludes NaN values by default (dropna=True) when counting unique elements."},
        {"id": "TP2_182", "tp": 2, "category": "trap", "question": "Believing that plt.clf() exports the rendered figure to a PNG file.", "answer": False, "explanation": "plt.clf() clears the current figure canvas; exporting to file requires plt.savefig()."},
        {"id": "TP2_183", "tp": 2, "category": "trap", "question": "Confusing univariate EDA (single variable) with bivariate EDA (variable pairs).", "answer": False, "explanation": "Univariate EDA analyzes one feature alone; bivariate EDA examines relationships between feature pairs."},
        {"id": "TP2_184", "tp": 2, "category": "trap", "question": "Assuming that pd.crosstab normalize='index' computes column percentages that sum to 100% vertically.", "answer": False, "explanation": "normalize='index' computes ROW percentages summing to 1.0 horizontally; column percentages require normalize='columns'."},
        {"id": "TP2_185", "tp": 2, "category": "trap", "question": "Believing that standard deviation can be calculated for non-ordinal nominal text categories.", "answer": False, "explanation": "Standard deviation requires numerical values and cannot be computed for non-numeric nominal text."},
        {"id": "TP2_186", "tp": 2, "category": "trap", "question": "Confusing df.info() with df.describe().", "answer": False, "explanation": "df.info() summarizes data types and null counts; df.describe() outputs numerical summary statistics."},
        {"id": "TP2_187", "tp": 2, "category": "trap", "question": "Assuming that KDE density curves can only be plotted for discrete binary 0/1 features.", "answer": False, "explanation": "KDE estimates smooth probability density functions for continuous numerical variables."},
        {"id": "TP2_188", "tp": 2, "category": "trap", "question": "Believing that Pearson correlation matrix diagonal contains zeroes.", "answer": False, "explanation": "The main diagonal of a correlation matrix contains 1.0 because every variable has perfect correlation with itself."},
        {"id": "TP2_189", "tp": 2, "category": "trap", "question": "Confusing sample range (Max - Min) with standard deviation.", "answer": False, "explanation": "Range measures distance between extreme bounds; standard deviation measures average distance from the mean."},
        {"id": "TP2_190", "tp": 2, "category": "trap", "question": "Assuming that scatter plot markers must always be drawn as solid black dots.", "answer": False, "explanation": "Scatter plot markers can be customized with different shapes, sizes, colors (hue), and opacity (alpha)."},

        {"id": "TP2_191", "tp": 2, "category": "trap", "question": "Believing that filtering a DataFrame with boolean mask alters column names.", "answer": False, "explanation": "Boolean filtering selects matching rows while leaving DataFrame column names unchanged."},
        {"id": "TP2_192", "tp": 2, "category": "trap", "question": "Confusing exploratory data analysis with final production model deployment.", "answer": False, "explanation": "EDA explores dataset characteristics during initial analysis; deployment runs trained models in production."},
        {"id": "TP2_193", "tp": 2, "category": "trap", "question": "Assuming that pd.value_counts(dropna=False) ignores missing values.", "answer": False, "explanation": "dropna=False explicitly INCLUDES missing NaN values in the output frequency count table."},
        {"id": "TP2_194", "tp": 2, "category": "trap", "question": "Believing that a high correlation between feature X and target Y guarantees 100% classification accuracy.", "answer": False, "explanation": "Correlation indicates linear association strength but does not guarantee error-free classification performance."},
        {"id": "TP2_195", "tp": 2, "category": "trap", "question": "Confusing horizontal box plots with vertical bar charts.", "answer": False, "explanation": "Box plots display quartile distribution summaries; bar charts display discrete group value heights."},
        {"id": "TP2_196", "tp": 2, "category": "trap", "question": "Assuming that df.tail() returns the top rows of a DataFrame.", "answer": False, "explanation": "df.tail() returns the BOTTOM (last) rows; df.head() returns the top rows."},
        {"id": "TP2_197", "tp": 2, "category": "trap", "question": "Believing that Seaborn pairplot displays non-numeric text columns as scatter axes.", "answer": False, "explanation": "Seaborn pairplot selects only numerical columns for scatter plot grid axes."},
        {"id": "TP2_198", "tp": 2, "category": "trap", "question": "Confusing dataset mean with dataset mode.", "answer": False, "explanation": "Mean is the arithmetic average; mode is the most frequently occurring value."},
        {"id": "TP2_199", "tp": 2, "category": "trap", "question": "Assuming that Matplotlib plt.subplots() creates a single figure with no axes.", "answer": False, "explanation": "plt.subplots() creates a figure object AND one or more subplot axes objects."},
        {"id": "TP2_200", "tp": 2, "category": "trap", "question": "Believing that exploratory data analysis eliminates the need for data preprocessing.", "answer": False, "explanation": "EDA identifies data issues (missingness, scaling needs, outliers) that MUST then be handled during preprocessing."}
    ]

    # Convert tuple rows to dicts for 141..180
    for i, item in enumerate(trap_data[:40], 141):
        q, a, exp = item
        questions.append({
            "id": f"TP2_{i:03d}",
            "tp": 2,
            "category": "trap",
            "question": q,
            "answer": a,
            "explanation": exp
        })
    
    # Add remaining dict items 181..200
    for item in trap_data[40:]:
        questions.append(item)

    return questions

if __name__ == "__main__":
    qs = get_tp2_questions()
    print(f"TP2 Total: {len(qs)}")
    print("Normal:", sum(1 for q in qs if q["category"] == "normal"))
    print("Tricky:", sum(1 for q in qs if q["category"] == "tricky"))
    print("Trap:", sum(1 for q in qs if q["category"] == "trap"))
