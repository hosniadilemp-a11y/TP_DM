# TP 3 — Data Preprocessing, Feature Engineering & Selection (200 Questions: 90 Normal, 50 Tricky, 60 Trap)

def get_tp3_questions():
    questions = []
    
    # ---------------------------------------------------------
    # 90 NORMAL QUESTIONS (TP3_001 to TP3_090)
    # ---------------------------------------------------------
    normal_data = [
        # Data Imputation Strategies (Easy/Medium)
        ("In scikit-learn, SimpleImputer provides strategies to replace missing values using mean, median, most_frequent, or constant.", True, "SimpleImputer supports four core univariate imputation strategies for handling missing data."),
        ("SimpleImputer(strategy='mean') replaces missing values in a column with the column average.", True, "The mean strategy computes column arithmetic averages for missing numerical entries."),
        ("SimpleImputer(strategy='median') replaces missing values with the 50th percentile median of available column entries.", True, "The median strategy uses central percentile values, robust against numerical outliers."),
        ("The 'most_frequent' strategy in SimpleImputer replaces missing values with the mode of the column.", True, "The most_frequent strategy calculates the most common value, suitable for categorical features."),
        ("SimpleImputer(strategy='constant', fill_value=99) substitutes all missing entries with the specified constant scalar value.", True, "The constant strategy replaces NaNs with a user-defined fixed fill value like 99 or 'Missing'."),
        ("Mean and median imputation strategies are suitable for continuous numerical distributions.", True, "Mean and median represent continuous central tendencies for numerical variables."),
        ("Mode ('most_frequent') imputation is appropriate for categorical attributes.", True, "Categorical attributes lack numerical order, making the mode the appropriate frequency-based fill statistic."),
        ("Applying fit_transform() on SimpleImputer calculates imputation statistics and replaces missing entries in one step.", True, "fit_transform() fits imputer statistics on the dataset and immediately applies the transformation."),
        ("SimpleImputer defaults missing_values to np.nan.", True, "By default, SimpleImputer identifies np.nan as the missing value target to replace."),
        ("Imputing missing values prevents errors when passing data to algorithms that cannot handle NaNs natively.", True, "Most scikit-learn estimators raise errors if input arrays contain NaN values."),

        # Categorical Encoding Methods (Medium)
        ("LabelEncoder transforms categorical string labels into unique discrete integer values.", True, "LabelEncoder maps distinct text categories to integer labels (e.g., 0, 1, 2)."),
        ("LabelEncoder is primarily intended for encoding target labels (y) rather than feature matrices (X).", True, "Scikit-learn documentation recommends LabelEncoder for 1D target vectors and OrdinalEncoder for 2D feature matrices."),
        ("OneHotEncoder converts categorical features into a binary matrix with distinct 0/1 indicator columns.", True, "OneHotEncoder creates separate dummy columns for each unique category level."),
        ("OneHotEncoder avoids introducing an artificial numerical ordering among nominal categories.", True, "Binarizing categories into separate dummy columns prevents algorithms from inferring false ordinal rank."),
        ("OrdinalEncoder maps ordered categorical variables to integers while preserving their relative rank.", True, "OrdinalEncoder assigns sequential integer values respecting intrinsic category ordering."),
        ("LabelBinarizer transforms binary or multi-class target labels into a binary indicator matrix.", True, "LabelBinarizer converts 1D categorical targets into 1-hot or binary matrices."),
        ("MultiLabelBinarizer is designed for multi-label data where an observation can belong to multiple categories simultaneously.", True, "MultiLabelBinarizer processes tuples/lists of tags per sample into multi-hot binary indicator vectors."),
        ("OneHotEncoder(sparse=False) returns a dense NumPy array instead of a scipy sparse matrix.", True, "sparse=False (or sparse_output=False in newer sklearn) forces dense array output."),
        ("Applying LabelEncoder on nominal features like animal species ('cat', 'dog', 'bird') imposes an arbitrary numerical ordering.", True, "Encoding nominal categories as 0, 1, 2 implies 'bird' > 'dog' > 'cat', which distorts non-ordered attributes."),
        ("Inverse transformation with encoder.inverse_transform() maps encoded integers back to original string labels.", True, "inverse_transform() reverses the encoding mapping to recover raw string labels."),

        # Feature Scaling & Normalization (Medium/Hard)
        ("MinMaxScaler rescales feature values to a fixed range, typically between 0 and 1.", True, "MinMaxScaler uses min and max bounds to compress values into [0, 1]."),
        ("The formula for Min-Max scaling is X_scaled = (X - X_min) / (X_max - X_min).", True, "MinMaxScaler subtracts the minimum and divides by the total feature range."),
        ("StandardScaler standardizes features by centering them around a mean of 0 with a standard deviation of 1.", True, "StandardScaler computes Z-scores: Z = (X - mean) / std_dev."),
        ("The formula for Standard scaling (Z-score) is X_scaled = (X - mean) / std_dev.", True, "StandardScaler centers by subtracting the sample mean and divides by standard deviation."),
        ("RobustScaler uses the median and Interquartile Range (IQR) for scaling, making it robust against outliers.", True, "RobustScaler subtracts Q2 (median) and divides by IQR (Q3 - Q1), resisting outlier distortion."),
        ("The formula for Robust scaling is X_scaled = (X - Q1) / (Q3 - Q1).", True, "RobustScaler scales features using interquartile spread around the median."),
        ("Distance-based algorithms like k-Nearest Neighbors (k-NN) are sensitive to feature scales.", True, "k-NN computes Euclidean distances; unscaled features with large ranges dominate distance metrics."),
        ("StandardScaler can be influenced by extreme outliers because outliers distort sample mean and standard deviation.", True, "Outliers pull the mean and inflate standard deviation, altering Z-score scaling results."),
        ("MinMaxScaler is sensitive to extreme outliers because outliers define the X_min or X_max bounds.", True, "An extreme outlier sets X_max, compressing non-outlier data into a tiny sub-range near 0."),
        ("Feature scaling ensures that continuous features with large numerical magnitudes do not dominate smaller-scale features.", True, "Scaling unifies feature ranges so all variables contribute proportionally to model training."),

        # Train-Test Splitting & Data Leakage (Medium/Hard)
        ("The train_test_split function in scikit-learn partitions a dataset into distinct training and testing subsets.", True, "train_test_split divides data arrays into train and test sets for model validation."),
        ("test_size=0.2 allocates 20% of the dataset to the test set and 80% to the training set.", True, "test_size specifies the proportion of sample data assigned to the evaluation test split."),
        ("Setting random_state in train_test_split ensures reproducible random data partitions across code runs.", True, "random_state seeds the pseudo-random generator for consistent data splitting."),
        ("shuffle=True shuffles the dataset before splitting to prevent ordered sample bias.", True, "Shuffling randomizes row ordering before splitting into training and testing sets."),
        ("Stratified splitting (stratify=y) maintains identical class label proportions in both train and test sets.", True, "stratify ensures class distribution ratios in train and test splits match the original dataset."),
        ("Data leakage occurs when information from the test set is inadvertently used during preprocessing or training.", True, "Data leakage corrupts validation integrity by giving the model access to test set information."),
        ("To avoid data leakage, scalers and imputers must be fitted strictly on the training set only.", True, "Fitting transformers on training data alone prevents leaking test set parameters into the model."),
        ("Applying transform() on the test set using train-fitted parameters applies learned training statistics safely.", True, "test_set.transform() uses parameters (means, mins, modes) learned exclusively from training data."),
        ("Evaluating a model on unseen test data provides an unbiased estimate of its generalization performance.", True, "Test set metrics reflect how well the trained model generalizes to new real-world data."),
        ("Stratified splitting is particularly crucial when dealing with imbalanced target classes.", True, "Stratification prevents rare minority classes from being underrepresented or absent in train or test splits."),

        # Pipelines & Column Transformers (Medium/Hard)
        ("make_column_transformer allows applying different preprocessing pipelines to specific column subsets.", True, "make_column_transformer maps distinct feature column lists to specialized transformers."),
        ("make_pipeline creates a sequential chain of transformers and a final estimator.", True, "make_pipeline chains preprocessing steps sequentially, ending with an estimator or transformer."),
        ("In scikit-learn, a Pipeline automatically executes fit_transform on transformers and fit on the final estimator.", True, "Calling pipeline.fit(X, y) sequentially fits and transforms data through all pipeline stages."),
        ("Using Pipelines prevents data leakage during cross-validation by refitting all transformers within each CV fold.", True, "Pipelines isolate fold-level transformer fitting inside cross-validation loops, preventing leakage."),
        ("ColumnTransformers can combine numerical pipelines (imputer + scaler) and categorical pipelines (imputer + encoder).", True, "ColumnTransformers apply custom sub-pipelines in parallel across different feature types."),
        ("The fit_transform method of a Pipeline returns the transformed dataset after executing all processing steps.", True, "fit_transform runs fit and transform sequentially across all pipeline steps."),
        ("Pipelines simplify production deployment by encapsulating all data transformation rules into a single object.", True, "A single pipeline object accepts raw input data and outputs model predictions end-to-end."),
        ("In a Pipeline ending with a classifier, calling model.score(X_test, y_test) automatically transforms X_test first.", True, "Pipeline predict() and score() pass raw test data through all fitted transformers before scoring."),
        ("Specifying feature column lists (numerical_features, categorical_features) guides ColumnTransformer operations.", True, "Passing explicit column names or indices directs appropriate transformers to target columns."),
        ("Combining SimpleImputer and StandardScaler in a numerical pipeline ensures clean scaled numerical inputs.", True, "Chaining imputation then scaling cleans missing entries first before standardizing feature scales."),

        # Preprocessing Impact & Feature Engineering (Medium/Hard)
        ("Feature engineering involves creating new features or transforming existing ones to improve model performance.", True, "Engineering domain-relevant features exposes underlying patterns more effectively to models."),
        ("Log transformation can stabilize variance and linearize exponential relationships in numerical features.", True, "Log transforms compress skewed ranges and linearize multiplicative relationships."),
        ("PolynomialFeatures generates interaction terms and polynomial powers of input numerical features.", True, "PolynomialFeatures creates degree powers (X^2) and pairwise interaction terms (X1 * X2)."),
        ("Binarization converts continuous numerical features into binary 0/1 flags based on a specified threshold.", True, "Binarizer thresholding maps values above a limit to 1 and values below to 0."),
        ("Feature selection reduces dimensionality by removing irrelevant or redundant features.", True, "Selecting top informative features reduces noise, speeds training, and mitigates overfitting."),
        ("One-Hot Encoding a categorical feature with K unique levels creates K binary dummy columns by default.", True, "By default, OneHotEncoder creates a separate binary column for every unique category level."),
        ("Dropping one dummy column (drop='first') in OneHotEncoder avoids multicollinearity in linear models.", True, "drop='first' creates K-1 dummy variables, preventing the dummy variable trap in linear models."),
        ("Preprocessing choices directly influence the prediction accuracy of k-NN classifiers.", True, "Imputation quality, scaling, and encoding directly dictate Euclidean distance calculations in k-NN."),
        ("RobustScaler uses median and IQR, making scaled values resistant to extreme outlier distortions.", True, "Centering on the median and dividing by IQR prevents extreme values from warping non-outlier scaling."),
        ("Applying StandardScaler before k-NN classification prevents features with large ranges from dominating predictions.", True, "Standardizing feature variances balances feature weights in Euclidean distance calculations."),

        # Operational Scikit-Learn Concepts (Medium)
        ("Scikit-learn transformers implement fit(), transform(), and fit_transform() methods.", True, "Transformers conform to the standard scikit-learn API layout with fit and transform methods."),
        ("The fit() method computes transformer parameters (e.g., mean and std) from training data without altering data.", True, "fit() calculates summary statistics needed for transformation without modifying input arrays."),
        ("The transform() method applies learned transformation parameters to convert input dataset arrays.", True, "transform() executes the mathematical scaling or encoding mapping using previously fitted parameters."),
        ("Scikit-learn estimators implement fit() and predict() (or score()) methods.", True, "Estimators learn model parameters during fit() and generate output predictions via predict()."),
        ("Categorical encoding must be performed before passing data to scikit-learn estimators.", True, "Scikit-learn classification models require numerical input arrays and fail on raw string data."),
        ("Passing sparse=False to OneHotEncoder produces dense NumPy array outputs.", True, "Setting sparse=False forces dense array format instead of scipy compressed sparse row matrices."),
        ("ColumnTransformers concatenate parallel transformation outputs into a single unified array.", True, "ColumnTransformer executes feature transformations in parallel and horizontally stacks results."),
        ("OrdinalEncoder requires defining explicit category order lists if natural rank ordering exists.", True, "Providing an explicit categories list ensures integers map to the correct rank hierarchy."),
        ("Numerical feature scaling does not alter the relative rank order of values within a single column.", True, "Monotonic scalers like MinMaxScaler and StandardScaler preserve rank order within individual features."),
        ("Imputing missing values after splitting prevents test set summary statistics from influencing training fills.", True, "Calculating fill statistics solely on training data maintains true out-of-sample evaluation."),

        # Practical Preprocessing Workflows (Medium/Hard)
        ("In scikit-learn, SimpleImputer(strategy='constant', fill_value=0) fills NaNs with zeros.", True, "Specifying strategy='constant' and fill_value=0 substitutes missing entries with numeric 0."),
        ("Target variable y should be separated from feature matrix X before applying feature scaling.", True, "Scaling applies to independent predictor features (X), not target classification labels (y)."),
        ("Evaluating preprocessing pipelines on test data confirms which scaling technique maximizes accuracy.", True, "Comparing pipeline test scores identifies optimal preprocessing configurations for specific models."),
        ("Using make_pipeline removes the need to manually name every processing step.", True, "make_pipeline automatically generates step names based on class names."),
        ("StandardScaler subtracts the feature mean and divides by the feature standard deviation.", True, "StandardScaler computes Z = (X - u) / s for each numerical column."),
        ("MinMaxScaler maps the minimum feature value to 0 and maximum feature value to 1.", True, "After Min-Max scaling, the column minimum becomes 0.0 and maximum becomes 1.0."),
        ("Handling missing values is required before applying StandardScaler in scikit-learn.", True, "StandardScaler cannot process NaN entries and raises a ValueError if missing values remain."),
        ("OneHotEncoder handles unknown categories during test transform when handle_unknown='ignore' is set.", True, "handle_unknown='ignore' encodes unseen test categories as all zeros without raising errors."),
        ("Preprocessing pipelines can be evaluated inside cross-validation loops seamlessly using cross_val_score.", True, "cross_val_score accepts Pipeline objects, fitting transformers on each fold automatically."),
        ("Feature scaling is unnecessary for Decision Tree classifiers because tree splits are invariant to monotonic scaling.", True, "Decision trees split features based on value order thresholds, making scaling unnecessary for tree logic."),

        # Additional 10 Normal Questions (TP3_081 to TP3_090)
        ("SimpleImputer can be initialized with strategy='most_frequent' to perform mode imputation.", True, "most_frequent calculates the modal value for missing entries."),
        ("OneHotEncoder creates separate dummy binary columns for each unique categorical value.", True, "One-hot encoding creates binary 0/1 indicator features per category level."),
        ("StandardScaler centers numerical features by subtracting the mean and dividing by the standard deviation.", True, "StandardScaler calculates Z-scores to transform variables to zero mean and unit variance."),
        ("MinMaxScaler rescales feature values to a bounded interval between 0 and 1 by default.", True, "MinMax scaling compresses data into the [0, 1] range using minimum and maximum bounds."),
        ("RobustScaler uses the median and Interquartile Range (IQR) for scaling, resisting extreme outliers.", True, "RobustScaler subtracts the median and divides by IQR, resisting outlier distortions."),
        ("scikit-learn ColumnTransformer applies different preprocessing pipelines to specified column lists.", True, "make_column_transformer maps separate transformer pipelines to distinct feature column subsets."),
        ("scikit-learn Pipeline chains preprocessing transformers and a final estimator sequentially.", True, "Pipelines execute sequential transformations before passing processed data to an estimator."),
        ("Fitting scalers only on training data prevents test set data leakage.", True, "Learning transformation parameters strictly from training data preserves test set validation integrity."),
        ("Stratified splitting with train_test_split preserves class label proportions in train and test sets.", True, "stratify=y ensures identical target class ratios in train and test splits."),
        ("LabelEncoder maps categorical text strings to unique discrete integer labels.", True, "LabelEncoder assigns discrete integer codes to distinct target class labels.")
    ]

    for i, (q, a, exp) in enumerate(normal_data, 1):
        questions.append({
            "id": f"TP3_{i:03d}",
            "tp": 3,
            "category": "normal",
            "question": q,
            "answer": a,
            "explanation": exp
        })

    # ---------------------------------------------------------
    # 50 TRICKY QUESTIONS (TP3_091 to TP3_140)
    # ---------------------------------------------------------
    tricky_data = [
        ("Fitting a StandardScaler on the entire dataset before train_test_split is valid and prevents data leakage.", False, "Fitting scalers on the entire dataset prior to splitting leaks test set statistics into training data."),
        ("LabelEncoder should be used to encode multi-column nominal feature matrices in scikit-learn.", False, "LabelEncoder is designed for 1D target labels; 2D nominal feature matrices should be encoded with OneHotEncoder or OrdinalEncoder."),
        ("MinMaxScaler transforms feature distributions so that their mean becomes exactly 0 and standard deviation becomes 1.", False, "StandardScaler sets mean to 0 and std to 1; MinMaxScaler rescales data between 0 and 1 without setting mean to 0."),
        ("Decision Tree classifiers require strict numerical feature scaling with StandardScaler to operate correctly.", False, "Decision trees evaluate threshold splits on individual features independently and are invariant to monotonic feature scaling."),
        ("Applying fit_transform() on the test set using a StandardScaler updates the training mean parameters.", False, "fit_transform() on the test set computes NEW test statistics, corrupting learned training parameters and leaking data."),
        ("SimpleImputer(strategy='mean') works directly on categorical string columns containing text.", False, "Mean imputation calculates arithmetic averages, which cannot be computed for non-numeric text columns."),
        ("RobustScaler scales data using the minimum and maximum values of the feature distribution.", False, "RobustScaler scales data using the median and Interquartile Range (IQR); MinMaxScaler uses min and max values."),
        ("OneHotEncoder with drop='first' creates K dummy columns for a categorical feature with K unique levels.", False, "drop='first' removes the baseline category, producing K-1 dummy columns instead of K."),
        ("In scikit-learn, fit() returns the fully transformed output array.", False, "fit() calculates parameter statistics and returns the fitted transformer object; transform() returns the transformed array."),
        ("OneHotEncoder automatically converts string target vectors y into 1D integer classification labels.", False, "OneHotEncoder produces 2D binary dummy matrices; target vector encoding uses LabelEncoder or LabelBinarizer."),

        ("StandardScaler guarantees that transformed feature values will strictly lie between -1 and +1.", False, "StandardScaler computes Z-scores, which have no bounded upper or lower limit; values can exceed +/-3."),
        ("Using SimpleImputer(strategy='median') on nominal categorical string features is standard practice.", False, "Median requires ordered numerical data; nominal categorical features require 'most_frequent' or 'constant' imputation."),
        ("Applying fit_transform() to test data within a cross-validation fold prevents data leakage.", False, "Transformers must be fit ONLY on training folds; fit_transforming test folds causes severe data leakage."),
        ("MultiLabelBinarizer produces a 1D vector containing categorical text strings for each row.", False, "MultiLabelBinarizer outputs a 2D binary matrix where columns represent distinct tag presence/absence."),
        ("In a scikit-learn Pipeline, transformers can be placed after the final classifier estimator.", False, "Pipelines require all intermediate steps to be transformers; only the FINAL step can be an estimator/classifier."),
        ("MinMaxScaler is robust against extreme outliers because it compresses data into [0, 1].", False, "Extreme outliers define X_max or X_min, compressing non-outlier values into a tiny dense sub-interval."),
        ("OrdinalEncoder introduces no implicit numerical ordering when applied to nominal categorical features.", False, "OrdinalEncoder maps categories to integers (0, 1, 2), which imposes an implicit numerical order that linear/distance models exploit."),
        ("SimpleImputer(strategy='constant', fill_value=0) preserves the original standard deviation of a feature.", False, "Imputing constant zeros alters sample variance and reduces standard deviation."),
        ("Stratified splitting with train_test_split shuffles data without preserving class label ratios.", False, "Stratified splitting explicitly preserves original class label ratios in both train and test splits."),
        ("Calling transform() on a scikit-learn scaler re-fits its internal mean and variance parameters.", False, "transform() applies previously fitted mean and variance parameters without recalculating them."),

        ("LabelBinarizer can be used inside a ColumnTransformer to process multi-column feature matrices.", False, "LabelBinarizer is designed for 1D target vectors y and raises errors if used in ColumnTransformer on 2D feature matrices."),
        ("Applying log transformation to negative numbers in a numerical column produces valid positive float outputs.", False, "Logarithms of negative numbers are undefined in real numbers and produce NaN values in NumPy."),
        ("make_column_transformer applies specified transformations sequentially to the same columns.", False, "ColumnTransformer applies specified transformations in PARALLEL to selected column subsets and concatenates results."),
        ("StandardScaler alters the shape of a feature distribution from skewed to perfectly Gaussian.", False, "StandardScaler shifts location and rescales spread without changing the underlying skewness or shape of the distribution."),
        ("SimpleImputer automatically encodes categorical text columns into numeric integers during imputation.", False, "SimpleImputer replaces missing entries with string mode/constant values without performing numeric encoding."),
        ("PolynomialFeatures with degree=2 reduces the total number of features in a dataset.", False, "PolynomialFeatures creates squared terms and pairwise interactions, increasing total feature count."),
        ("Passing random_state=None to train_test_split ensures identical reproducible data splits across executions.", False, "random_state=None uses random system noise, generating different splits on every code execution."),
        ("In scikit-learn, Pipeline.fit(X, y) calls fit_transform on every step including the final classifier.", False, "Pipeline calls fit_transform on intermediate transformers, but calls fit() on the final classifier step."),
        ("Dropping rows with missing values (dropna) inside a ColumnTransformer is standard scikit-learn practice.", False, "ColumnTransformers apply column-wise transformations and cannot drop rows; row dropping must occur prior to pipeline execution."),
        ("The 'most_frequent' strategy in SimpleImputer computes the arithmetic mean of discrete integer columns.", False, "The 'most_frequent' strategy finds the categorical mode (most frequent value), not the arithmetic mean."),

        ("MinMaxScaler preserves original zero values in sparse matrices when feature minimum is negative.", False, "If feature minimum is negative, subtracting X_min shifts zeroes to non-zero positive values, destroying sparsity."),
        ("Scikit-learn KNeighborsClassifier automatically scales unscaled input features before distance calculations.", False, "KNeighborsClassifier uses raw feature values directly; feature scaling must be applied explicitly in preprocessing."),
        ("Using OneHotEncoder with handle_unknown='ignore' throws an error whenever an unseen category appears in test data.", False, "handle_unknown='ignore' silently encodes unseen test categories as all-zero vectors without raising errors."),
        ("LabelEncoder fit_transform() accepts 2D DataFrames containing multiple feature columns.", False, "LabelEncoder expects a 1D vector (target label y) and raises a DataConversionWarning or ValueError on 2D inputs."),
        ("Scaling continuous features alters the decision boundaries of a Decision Tree classifier significantly.", False, "Decision trees evaluate axis-aligned threshold splits per feature independently, making them invariant to monotonic scaling."),
        ("SimpleImputer(strategy='mean') can impute missing values in boolean true/false columns without casting.", False, "Mean imputation converts boolean columns to floating-point averages, altering boolean data types."),
        ("Applying StandardScaler before OneHotEncoding categorical variables is recommended.", False, "Categorical text strings must be One-Hot encoded into numbers BEFORE numerical scaling can be applied."),
        ("The fit() method of a transformer modifies the input array X in place and returns the transformed array.", False, "fit() computes parameter statistics without modifying input array X and returns the transformer instance itself."),
        ("StratifiedKFold cross-validation should be used for regression targets with continuous floating-point values.", False, "StratifiedKFold requires discrete classification labels y; continuous regression targets use standard KFold."),
        ("Applying log1p transformation log(x + 1) fails on zero values.", False, "log1p(x) computes log(1 + x), which safely evaluates log(1) = 0 when x = 0.")
    ]

    for i, (q, a, exp) in enumerate(tricky_data, 91):
        questions.append({
            "id": f"TP3_{i:03d}",
            "tp": 3,
            "category": "tricky",
            "question": q,
            "answer": a,
            "explanation": exp
        })

    # Add 10 additional tricky questions to complete 50 (TP3_131 to TP3_140)
    extra_tricky = [
        ("ColumnTransformer automatically reorders output columns to match the original input DataFrame column order.", False, "ColumnTransformer concatenates transformed outputs in the order transformers were specified, not original column order."),
        ("SimpleImputer strategy='constant' without fill_value defaults to filling missing entries with 0 for text columns.", False, "SimpleImputer with strategy='constant' defaults fill_value to 0 for numbers and 'missing_value' for strings."),
        ("Over-sampling minority classes with SMOTE before splitting data into train and test sets prevents data leakage.", False, "Applying SMOTE before splitting creates synthetic test samples derived from training data, causing severe leakage."),
        ("StandardScaler divides feature values by the Interquartile Range (IQR).", False, "StandardScaler divides by the standard deviation; RobustScaler divides by the Interquartile Range."),
        ("OrdinalEncoder automatically detects ordinal rank from categorical string labels alphabetically.", False, "Alphabetical ordering rarely reflects true ordinal rank (e.g., 'low', 'medium', 'high'); explicit categories must be supplied."),
        ("Using test_size=0.0 in train_test_split allocates 100% of data to the test set.", False, "test_size=0.0 allocates 0% to the test set and 100% to the training set."),
        ("Feature binarization with Binarizer(threshold=0.5) transforms values above 0.5 into 2.", False, "Binarizer maps values above threshold to 1 and values below or equal to threshold to 0."),
        ("ColumnTransformer can execute fit_transform on a pandas DataFrame and return a pandas DataFrame with original headers.", False, "ColumnTransformer returns a raw 2D NumPy ndarray by default, stripping pandas column headers."),
        ("MinMaxScaler scales features so that sample variance is guaranteed to equal 1.0.", False, "MinMaxScaler bounds values between 0 and 1; StandardScaler sets sample variance to 1.0."),
        ("SimpleImputer(strategy='most_frequent') always returns a 1D vector regardless of input dimensions.", False, "SimpleImputer preserves 2D array shapes when transforming 2D feature matrices.")
    ]

    for i, (q, a, exp) in enumerate(extra_tricky, 131):
        questions.append({
            "id": f"TP3_{i:03d}",
            "tp": 3,
            "category": "tricky",
            "question": q,
            "answer": a,
            "explanation": exp
        })

    # ---------------------------------------------------------
    # 60 TRAP QUESTIONS (TP3_141 to TP3_200)
    # ---------------------------------------------------------
    trap_data = [
        ("Confusing data leakage with feature scaling when fitting transformers on the entire dataset prior to splitting.", False, "Fitting scalers on full datasets before splitting causes data leakage by exposing test distribution parameters to training."),
        ("Assuming that LabelEncoder is designed for multi-column categorical feature matrix X in scikit-learn.", False, "LabelEncoder is meant for 1D target vectors y; feature matrices require OneHotEncoder or OrdinalEncoder."),
        ("Believing that MinMaxScaler centers data around a mean of 0 with standard deviation of 1.", False, "StandardScaler centers around mean 0 with std 1; MinMaxScaler rescales data strictly into [0, 1]."),
        ("Confusing Ordinal Encoding with One-Hot Encoding when processing nominal categorical variables without intrinsic rank.", False, "Ordinal encoding imposes arbitrary integer ranks on nominal data, misleading linear and distance-based algorithms."),
        ("Assuming that fitting SimpleImputer on test data inside a cross-validation fold avoids data leakage.", False, "Imputers must be fit ONLY on training folds; fitting on test folds leaks test statistics into preprocessing."),
        ("Believing that Decision Tree classifiers require feature scaling with StandardScaler to build splits.", False, "Decision trees evaluate axis-aligned threshold splits per feature independently, making scaling unnecessary."),
        ("Confusing SimpleImputer strategy='mean' with strategy='most_frequent' when imputing categorical string columns.", False, "Mean imputation fails on string columns; categorical text requires 'most_frequent' (mode) or 'constant' imputation."),
        ("Assuming that RobustScaler uses feature min and max values to perform feature normalization.", False, "RobustScaler uses median and IQR; MinMaxScaler uses minimum and maximum values."),
        ("Believing that OneHotEncoder(drop='first') produces K dummy columns for K unique categories.", False, "drop='first' drops the reference category, creating K-1 dummy columns to prevent dummy variable trap multicollinearity."),
        ("Confusing transformer fit() method with transform() method during dataset preparation.", False, "fit() calculates transformation parameters from data; transform() applies learned parameters to scale or encode data."),

        ("Assuming that StandardScaler bounds scaled feature values strictly between -1 and +1.", False, "StandardScaler Z-scores have no fixed upper/lower bounds and can exceed +/-3 for extreme values."),
        ("Believing that MultiLabelBinarizer outputs a 1D vector of text strings per sample.", False, "MultiLabelBinarizer outputs a 2D binary indicator matrix where columns represent individual tag presence."),
        ("Confusing Pipeline intermediate steps with final estimator steps in scikit-learn.", False, "All intermediate pipeline steps must be transformers implementing fit_transform; only the final step can be an estimator."),
        ("Assuming that StratifiedKFold cross-validation works on continuous floating-point regression targets.", False, "StratifiedKFold requires discrete classification labels y; continuous regression targets require standard KFold."),
        ("Believing that SimpleImputer fit_transform preserves pandas DataFrame column headers.", False, "SimpleImputer fit_transform returns a raw NumPy ndarray, stripping DataFrame column names."),
        ("Confusing log transformation (log1p) requirements with scaling negative continuous values.", False, "Log transforms require non-negative inputs (x >= 0); applying log to negative numbers produces NaN values."),
        ("Assuming that make_column_transformer executes feature transformers sequentially in series.", False, "ColumnTransformer executes specified feature transformations in PARALLEL and stacks resulting columns."),
        ("Believing that MinMaxScaler is immune to extreme outlier distortions.", False, "Extreme outliers set X_max or X_min, compressing non-outlier data into a tiny sub-range."),
        ("Confusing train_test_split shuffle=False with stratified splitting (stratify=y).", False, "shuffle=False retains original dataset row ordering; stratify=y preserves class label ratios in splits."),
        ("Assuming that k-NN classifiers are unaffected by unscaled features with large numerical magnitudes.", False, "k-NN relies on Euclidean distances, allowing unscaled large-magnitude features to dominate distance calculations."),

        ("Believing that LabelBinarizer can be passed directly inside ColumnTransformer for feature matrices.", False, "LabelBinarizer is designed for 1D target labels y and raises errors when used in ColumnTransformer on 2D feature matrices."),
        ("Confusing fit_transform() on test set with transform() on test set.", False, "fit_transform() on test set calculates NEW test parameters causing leakage; transform() correctly applies learned training parameters."),
        ("Assuming that SimpleImputer strategy='median' can process nominal text columns.", False, "Median calculation requires ordered numerical data and fails on non-numeric text columns."),
        ("Believing that PolynomialFeatures degree=2 reduces total feature count.", False, "PolynomialFeatures creates interaction terms and squared terms, increasing total feature count."),
        ("Confusing random_state=None with random_state=42 in train_test_split.", False, "random_state=None generates different random splits on every execution; integer seeds like 42 ensure exact reproducibility."),
        ("Assuming that Pipeline.fit(X, y) calls fit_transform on the final estimator step.", False, "Pipeline calls fit_transform on intermediate transformers, but calls fit() on the final estimator step."),
        ("Believing that ColumnTransformer can drop rows containing missing values natively.", False, "ColumnTransformer operates column-wise and cannot drop rows; row dropping must be done before pipeline execution."),
        ("Confusing OneHotEncoder handle_unknown='ignore' with handle_unknown='error'.", False, "handle_unknown='ignore' encodes unseen test categories as all zeros; 'error' raises an exception on unseen categories."),
        ("Assuming that target variable y should be included in feature scaling pipelines.", False, "Feature scaling applies to independent predictors X, not target classification labels y."),
        ("Believing that StandardScaler changes feature distribution skewness.", False, "StandardScaler shifts location and rescales spread without altering the underlying distribution skewness."),

        ("Confusing Min-Max scaling with Robust scaling when handling datasets with extreme outliers.", False, "MinMax scaling is warped by extreme outliers; RobustScaler uses median and IQR to resist outlier distortion."),
        ("Assuming that OneHotEncoder requires categorical inputs to be pre-encoded as numerical integers.", False, "Scikit-learn OneHotEncoder processes raw string categorical columns directly without pre-encoding to integers."),
        ("Believing that SimpleImputer strategy='constant' fill_value defaults to 0 for text columns.", False, "SimpleImputer with strategy='constant' defaults fill_value to 'missing_value' for string columns."),
        ("Confusing test_size=0.2 with train_size=0.2 in train_test_split.", False, "test_size=0.2 allocates 20% to test and 80% to train; train_size=0.2 allocates 20% to train and 80% to test."),
        ("Assuming that Binarizer threshold=0.5 maps values above 0.5 to 2.", False, "Binarizer maps values above threshold to 1 and values below or equal to 0."),
        ("Believing that SMOTE oversampling applied before train_test_split is valid.", False, "Applying SMOTE before splitting creates synthetic test samples derived from training data, causing severe data leakage."),
        ("Confusing OrdinalEncoder with LabelEncoder in scikit-learn.", False, "OrdinalEncoder processes 2D feature matrices X; LabelEncoder processes 1D target vectors y."),
        ("Assuming that MinMaxScaler preserves sparse matrix structure when feature minimum is negative.", False, "If feature minimum is negative, subtracting X_min converts zeroes to non-zero values, destroying matrix sparsity."),
        ("Believing that Pipeline.predict() requires manual step-by-step feature transformation of raw test data.", False, "Pipeline.predict() automatically passes raw test inputs through all intermediate transformers before predicting."),
        ("Confusing StandardScaler formula (X - mean)/std with MinMax formula (X - min)/(max - min).", False, "StandardScaler divides by std_dev after subtracting mean; MinMaxScaler divides by range (max - min) after subtracting min."),

        {"id": "TP3_181", "tp": 3, "category": "trap", "question": "Assuming that SimpleImputer(strategy='most_frequent') computes the arithmetic mean of discrete columns.", "answer": False, "explanation": "The 'most_frequent' strategy computes the mode (most common value), not the arithmetic mean."},
        {"id": "TP3_182", "tp": 3, "category": "trap", "question": "Believing that StandardScaler converts negative numbers into positive numbers exclusively.", "answer": False, "explanation": "StandardScaler centers data around 0, producing negative Z-scores for values below the mean."},
        {"id": "TP3_183", "tp": 3, "category": "trap", "question": "Confusing fit() with fit_transform() when initializing a scikit-learn scaler object.", "answer": False, "explanation": "fit() calculates parameters without returning transformed data; fit_transform() calculates parameters and returns transformed data."},
        {"id": "TP3_184", "tp": 3, "category": "trap", "question": "Assuming that OneHotEncoder dense output is forced by sparse=True.", "answer": False, "explanation": "Dense output is produced when sparse=False (or sparse_output=False); sparse=True outputs scipy sparse matrices."},
        {"id": "TP3_185", "tp": 3, "category": "trap", "question": "Believing that feature selection must be performed AFTER training the final classifier.", "answer": False, "explanation": "Feature selection must be performed BEFORE or DURING pipeline training to reduce input dimension for the classifier."},
        {"id": "TP3_186", "tp": 3, "category": "trap", "question": "Confusing train set metrics with generalization metrics evaluated on unseen test data.", "answer": False, "explanation": "Train metrics measure fitting on known data; test metrics measure generalization to unseen data."},
        {"id": "TP3_187", "tp": 3, "category": "trap", "question": "Assuming that log1p(x) transformation can be applied to negative numbers smaller than -1.", "answer": False, "explanation": "log1p(x) computes log(1 + x), which fails for x < -1 because log of negative numbers is undefined in real arithmetic."},
        {"id": "TP3_188", "tp": 3, "category": "trap", "question": "Believing that ColumnTransformer output column names match input DataFrame column names by default.", "answer": False, "explanation": "ColumnTransformer outputs a raw NumPy array without column names unless verbose_feature_names_out or get_feature_names_out is used."},
        {"id": "TP3_189", "tp": 3, "category": "trap", "question": "Confusing scikit-learn Pipeline with pandas DataFrame chaining.", "answer": False, "explanation": "Scikit-learn Pipeline encapsulates ML transformers/estimators; pandas chaining sequences DataFrame method calls."},
        {"id": "TP3_190", "tp": 3, "category": "trap", "question": "Assuming that StratifiedKFold maintains equal fold sizes when dataset class distribution is imbalanced.", "answer": False, "explanation": "StratifiedKFold maintains class PROPORTIONS within folds; fold sample sizes remain equal while class counts reflect ratios."},

        {"id": "TP3_191", "tp": 3, "category": "trap", "question": "Believing that SimpleImputer handles missing values represented as '?' without configuring missing_values parameter.", "answer": False, "explanation": "SimpleImputer defaults missing_values to np.nan; custom text representations like '?' must be passed explicitly to missing_values."},
        {"id": "TP3_192", "tp": 3, "category": "trap", "question": "Confusing LabelEncoder inverse_transform with OneHotEncoder fit_transform.", "answer": False, "explanation": "inverse_transform reverses encoded integers to original text labels; fit_transform computes and applies initial encoding."},
        {"id": "TP3_193", "tp": 3, "category": "trap", "question": "Assuming that feature scaling changes the number of rows in a dataset matrix.", "answer": False, "explanation": "Feature scaling transforms numerical values within columns without adding or dropping rows."},
        {"id": "TP3_194", "tp": 3, "category": "trap", "question": "Believing that MinMaxScaler scales features based on sample variance.", "answer": False, "explanation": "MinMaxScaler scales features based on min and max range bounds; StandardScaler scales based on variance/std_dev."},
        {"id": "TP3_195", "tp": 3, "category": "trap", "question": "Confusing data preprocessing pipelines with raw dataset exploratory visualization.", "answer": False, "explanation": "Preprocessing pipelines transform data for modeling; exploratory visualization inspects data distributions graphics."},
        {"id": "TP3_196", "tp": 3, "category": "trap", "question": "Assuming that fit_transform should be called on test data when deploying a production pipeline.", "answer": False, "explanation": "Production pipelines must call transform() on new data using fitted training parameters, NEVER fit_transform()."},
        {"id": "TP3_197", "tp": 3, "category": "trap", "question": "Believing that OneHotEncoder creates 10 dummy columns for a binary feature with 2 categories.", "answer": False, "explanation": "OneHotEncoder creates exactly 2 dummy columns for a binary feature (or 1 column if drop='first')."},
        {"id": "TP3_198", "tp": 3, "category": "trap", "question": "Confusing RobustScaler median centering with StandardScaler mean centering.", "answer": False, "explanation": "RobustScaler centers data by subtracting the median (Q2); StandardScaler centers data by subtracting the mean."},
        {"id": "TP3_199", "tp": 3, "category": "trap", "question": "Assuming that scikit-learn transformers modify Python list objects directly.", "answer": False, "explanation": "Scikit-learn transformers operate on NumPy arrays, pandas DataFrames, or scipy sparse matrices, returning array structures."},
        {"id": "TP3_200", "tp": 3, "category": "trap", "question": "Believing that feature engineering guarantees 100% elimination of all classification errors.", "answer": False, "explanation": "Feature engineering improves model representation signal but cannot guarantee zero classification error on complex noisy data."}
    ]

    # Convert tuple rows to dicts for 141..180
    for i, item in enumerate(trap_data[:40], 141):
        q, a, exp = item
        questions.append({
            "id": f"TP3_{i:03d}",
            "tp": 3,
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
    qs = get_tp3_questions()
    print(f"TP3 Total: {len(qs)}")
    print("Normal:", sum(1 for q in qs if q["category"] == "normal"))
    print("Tricky:", sum(1 for q in qs if q["category"] == "tricky"))
    print("Trap:", sum(1 for q in qs if q["category"] == "trap"))
