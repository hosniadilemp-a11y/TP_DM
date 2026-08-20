# TP 5 — Supervised Classification Algorithms & Training (200 Questions: 90 Normal, 50 Tricky, 60 Trap)

def get_tp5_questions():
    questions = []
    
    # ---------------------------------------------------------
    # 90 NORMAL QUESTIONS (TP5_001 to TP5_090)
    # ---------------------------------------------------------
    normal_data = [
        # Scikit-Learn Standard Workflow (Easy/Medium)
        ("Supervised classification trains algorithms on labeled data (X, y) to predict class labels for new unseen observations.", True, "Supervised classification uses feature matrix X and known target vector y to learn a predictive mapping."),
        ("In scikit-learn, model.fit(X_train, y_train) trains the classification model on training features and target labels.", True, "fit() executes the training procedure, optimizing internal model parameters using training data."),
        ("In scikit-learn, model.predict(X_test) returns predicted class labels for new input instances.", True, "predict() applies the trained model parameters to infer target class labels for input feature rows."),
        ("In scikit-learn, model.score(X_test, y_test) calculates the mean classification accuracy on test data.", True, "For classification estimators, score() computes the fraction of correct target predictions on test inputs."),
        ("In scikit-learn, model.predict_proba(X_test) returns predicted class probability distributions for input samples.", True, "predict_proba() computes continuous class membership probabilities for each sample row."),
        ("Supervised classification algorithms require feature matrix X to be numerically encoded before training.", True, "Scikit-learn estimators require numerical inputs and raise errors if raw categorical strings are passed directly."),
        ("Hyperparameters are model configuration settings specified prior to training that are not learned directly from data.", True, "Hyperparameters (e.g., n_neighbors, max_depth) are specified during model initialization before fit() is called."),
        ("Parameters like linear regression coefficients or decision tree splits are learned automatically during model fitting.", True, "Internal parameters (e.g., coef_, intercept_) are computed automatically by fit() from training data."),
        ("The target vector y in binary classification contains two distinct class labels (e.g., 0 and 1).", True, "Binary classification targets discrete outcomes into one of two mutually exclusive classes."),
        ("Multi-class classification involves predicting a target variable that takes three or more distinct class labels.", True, "Multi-class classification targets discrete categorical outcomes spanning three or more unique classes."),

        # k-Nearest Neighbors (k-NN) Algorithm (Medium)
        ("KNeighborsClassifier classifies a sample based on the majority class vote among its k nearest neighbors in feature space.", True, "k-NN identifies the k closest training instances in distance space and assigns the most common class label."),
        ("The n_neighbors hyperparameter in KNeighborsClassifier specifies the number of nearest neighbors to evaluate.", True, "n_neighbors dictates how many nearby data points contribute to the classification decision vote."),
        ("k-NN is a non-parametric, instance-based lazy learning algorithm that stores training instances rather than building an explicit model.", True, "k-NN stores training instances in memory and performs distance computations on-the-fly during prediction."),
        ("Euclidean distance is a standard distance metric used by KNeighborsClassifier to calculate neighbor proximity.", True, "Euclidean distance (L2 norm) measures straight-line spatial distance between feature vectors."),
        ("Manhattan distance (L1 norm) computes neighbor proximity by summing absolute differences across feature coordinates.", True, "Manhattan distance measures grid-like distance along feature coordinate axes."),
        ("A small value of k (e.g., k=1) makes k-NN sensitive to noise, increasing the risk of overfitting.", True, "k=1 creates complex localized decision boundaries around individual outliers, causing high variance."),
        ("A large value of k (e.g., k=50) smooths decision boundaries, potentially causing underfitting.", True, "Very large k averages over broad regions, oversmoothing boundaries and ignoring local class signals."),
        ("Feature scaling with StandardScaler is critical for k-NN because unscaled large-magnitude features distort distance metrics.", True, "Distance metrics weigh raw magnitudes equally; unscaled large features dominate neighbor distance calculations."),
        ("In scikit-learn, metric='minkowski' with p=2 corresponds to standard Euclidean distance in KNeighborsClassifier.", True, "Minkowski distance with p=2 equals Euclidean distance; p=1 equals Manhattan distance."),
        ("k-NN prediction speed slows down on large training datasets because distance must be computed against stored training samples.", True, "Lazy learning requires calculating distances to stored training points during prediction execution."),

        # Decision Tree Classifier (Medium)
        ("DecisionTreeClassifier builds a hierarchical tree structure by partitioning feature space using axis-aligned split thresholds.", True, "Decision trees recursively split features at threshold values to maximize class purity in leaf nodes."),
        ("Decision trees are highly interpretable models because their decision rules can be visualized and understood by humans.", True, "Tree decision rules can be rendered as clear conditional logic flowcharts."),
        ("The max_depth hyperparameter constrains the maximum vertical depth of a DecisionTreeClassifier.", True, "max_depth limits maximum tree splitting depth to prevent over-complex deep trees."),
        ("Limiting max_depth in DecisionTreeClassifier helps prevent overfitting on noisy training data.", True, "Restricting tree depth stops the tree from growing leaves around single isolated outliers."),
        ("Gini Impurity and Entropy are standard criteria used to measure node impurity in DecisionTreeClassifier.", True, "Gini impurity and Entropy quantify class mixing in tree nodes to select optimal feature splits."),
        ("A decision tree leaf node with Gini impurity equal to 0.0 contains samples belonging to a single pure class.", True, "Gini = 0.0 indicates a perfectly pure node where 100% of samples belong to one target class."),
        ("DecisionTreeClassifier computes feature_importances_ indicating the relative contribution of each feature to node purity gains.", True, "feature_importances_ quantifies total normalized Gini/Entropy impurity reduction achieved by each feature."),
        ("Decision trees are invariant to monotonic numerical feature scaling like StandardScaler.", True, "Trees evaluate threshold inequalities (X >= threshold) per feature, making feature scaling unnecessary."),
        ("An unconstrained DecisionTreeClassifier (max_depth=None) can grow until all leaves are pure, leading to severe overfitting.", True, "Deep unconstrained trees memorize training instances, achieving 100% train accuracy but poor generalization."),
        ("The min_samples_split hyperparameter sets the minimum number of samples required in a node to attempt a split.", True, "min_samples_split prevents nodes with very few samples from splitting further."),

        # Random Forest & Ensemble Learning (Medium/Hard)
        ("RandomForestClassifier is an ensemble learning method that constructs a collection of decision trees and combines their predictions.", True, "Random Forest trains multiple decision trees and aggregates their votes to improve accuracy and stability."),
        ("Random Forest uses Bootstrap Aggregating (Bagging) to train each tree on a random sample of dataset rows drawn with replacement.", True, "Bagging samples training rows randomly with replacement, creating diverse datasets for individual trees."),
        ("Random Forest selects a random subset of features at each candidate split to decorrelate individual decision trees.", True, "Random feature subsampling decorrelates individual trees, reducing ensemble variance."),
        ("Random Forest determines classification outcomes using majority voting across all individual decision trees.", True, "The ensemble predicts the target class that receives the most votes from constituent decision trees."),
        ("The n_estimators hyperparameter specifies the total number of decision trees in a RandomForestClassifier.", True, "n_estimators sets the number of individual trees constructed inside the ensemble."),
        ("Random Forest is generally less prone to overfitting than a single unconstrained Decision Tree.", True, "Averaging predictions over multiple diverse trees cancels out individual tree variance."),
        ("Random Forest computes feature_importances_ by averaging impurity reductions across all trees in the forest.", True, "Ensemble feature importance averages individual tree impurity contributions for each feature."),
        ("Increasing n_estimators in RandomForestClassifier generally improves ensemble stability without causing overfitting.", True, "Adding more trees smooths ensemble voting without increasing model variance or overfitting."),
        ("Out-Of-Bag (OOB) error estimates model generalization performance using bootstrap samples omitted during tree training.", True, "OOB scoring evaluates each tree on training rows left out of its bootstrap sample, providing built-in validation."),
        ("Random Forest can process both numerical and categorical features once categorical variables are properly encoded.", True, "Once text features are numerically encoded, Random Forest processes high-dimensional mixed inputs effectively."),

        # Naive Bayes Classifiers (Medium)
        ("Naive Bayes classifiers apply Bayes' Theorem with the strong assumption of conditional independence between features.", True, "Naive Bayes assumes that all predictor features are conditionally independent given the target class label."),
        ("GaussianNB assumes that continuous feature values within each target class follow a normal (Gaussian) distribution.", True, "GaussianNB models continuous features using Gaussian normal distribution parameters (mean and variance)."),
        ("BernoulliNB is designed for classification tasks where features are binary (0/1) indicator variables.", True, "BernoulliNB models binary occurrence features, evaluating presence/absence of attributes."),
        ("Naive Bayes classifiers are fast to train because feature distribution parameters are calculated independently per feature.", True, "Independent feature estimation allows Naive Bayes to train in a single fast pass over data."),
        ("Despite the unrealistic independence assumption, Naive Bayes often performs surprisingly well on text classification and real-world tasks.", True, "Even when feature independence is violated, Naive Bayes yields accurate classification decision boundaries."),
        ("In scikit-learn, GaussianNB.fit(X, y) calculates class prior probabilities and feature means/variances per class.", True, "fit() estimates class priors P(y) and feature Gaussian parameters P(X_i|y) from training data."),
        ("Naive Bayes outputs predicted class probabilities via predict_proba() using Bayes' rule posterior calculations.", True, "predict_proba() normalizes posterior class likelihoods P(y|X) into valid class probabilities."),
        ("Zero-frequency problem occurs in Naive Bayes when a feature value never appears in a class during training.", True, "Zero counts yield 0 probability multipliers; Laplace smoothing adds pseudo-counts to resolve zero frequency."),
        ("BernoulliNB is suitable for binary document classification where features flag word presence (1) or absence (0).", True, "BernoulliNB models binary word occurrence matrices for text document classification."),
        ("GaussianNB does not require tuning complex structural hyperparameters during standard initialization.", True, "GaussianNB has virtually no structural hyperparameters to tune, relying directly on feature statistics."),

        # Support Vector Machine (SVM) Classifier (Medium/Hard)
        ("SVC (Support Vector Classifier) finds an optimal decision hyperplane that maximizes the margin between target classes.", True, "SVM constructs a hyper-plane maximizing spatial margin distance to the nearest training support vectors."),
        ("Support vectors are the training data points located closest to the decision hyperplane that define the margin bounds.", True, "Support vectors lie on margin boundaries and strictly determine hyperplane orientation."),
        ("The C hyperparameter in SVC controls the trade-off between maximizing margin width and minimizing training classification errors.", True, "A small C allows misclassifications for a wider margin; a large C penalizes errors heavily for a narrower margin."),
        ("A large value of C in SVC creates a narrow margin and penalizes misclassifications strictly, risking overfitting.", True, "High C forces strict training sample separation, creating complex margins prone to overfitting."),
        ("A small value of C in SVC creates a wider margin, allowing some training misclassifications to improve generalization.", True, "Low C tolerates minor training errors to achieve a smoother, wider decision boundary."),
        ("SVC uses kernel functions (e.g., 'linear', 'rbf', 'poly') to map non-linearly separable data into higher dimensions.", True, "Kernel functions compute inner products in implicit high-dimensional spaces to separate non-linear data."),
        ("The 'rbf' (Radial Basis Function) kernel is a popular default kernel for SVC that models non-linear decision boundaries.", True, "RBF kernel uses Gaussian distance functions to map complex non-linear decision boundaries."),
        ("The gamma hyperparameter in SVC with RBF kernel controls the radius of influence of individual support vectors.", True, "High gamma limits support vector influence to immediate neighbors; low gamma spreads influence broadly."),
        ("Feature scaling with StandardScaler is essential for SVC because distance-based margin calculations depend on feature scales.", True, "Unscaled features warp spatial margin distances, causing SVC optimization to fail."),
        ("SVC training time scales quadratically to cubically with sample size, making it slow on very large datasets.", True, "SVM quadratic programming solver complexity makes SVC slow for datasets with tens of thousands of samples."),

        # Logistic Regression & SGD Classifier (Medium)
        ("LogisticRegression models the log-odds of a binary target outcome as a linear combination of input features.", True, "Logistic Regression applies the sigmoid (logistic) function to linear inputs to predict class probabilities."),
        ("The sigmoid activation function S(z) = 1 / (1 + e^-z) maps linear outputs z to continuous probabilities between 0 and 1.", True, "The sigmoid function squashes any real value into a continuous probability interval [0, 1]."),
        ("In scikit-learn, LogisticRegression calculates model.coef_ representing feature weights and model.intercept_ representing bias.", True, "coef_ stores learned feature weights and intercept_ stores the baseline bias term."),
        ("The C hyperparameter in scikit-learn LogisticRegression controls inverse regularization strength.", True, "C = 1/lambda; smaller C values specify stronger regularization, while larger C values weaken regularization."),
        ("L2 regularization (Ridge) adds a penalty proportional to the sum of squared coefficient weights to prevent overfitting.", True, "L2 penalty shrinks feature weights toward zero without forcing them exactly to zero."),
        ("L1 regularization (Lasso) adds a penalty proportional to absolute coefficient weights, promoting feature sparsity.", True, "L1 penalty forces uninformative feature coefficients exactly to zero, performing automatic feature selection."),
        ("SGDClassifier implements linear models (e.g., SVM or Logistic Regression) using Stochastic Gradient Descent optimization.", True, "SGDClassifier optimizes linear loss functions (hinge, log_loss) using efficient mini-batch/sample gradient descent."),
        ("SGDClassifier with loss='log_loss' fits a logistic regression model using stochastic gradient descent.", True, "Setting loss='log_loss' configures SGDClassifier to optimize logistic loss."),
        ("SGDClassifier with loss='hinge' fits a linear Support Vector Machine classifier.", True, "Setting loss='hinge' configures SGDClassifier to optimize linear SVM margin loss."),
        ("SGDClassifier is highly efficient for large-scale and online/streaming datasets because it updates weights per sample/batch.", True, "Stochastic gradient updates process massive datasets iteratively without loading all data into memory at once."),

        # Boosting Algorithms: AdaBoost, Gradient Boosting, XGBoost (Hard)
        ("Boosting ensembles construct weak learners sequentially, where each new model focuses on correcting errors made by previous models.", True, "Boosting builds sequential chains of weak trees, reweighting misclassified instances at each step."),
        ("AdaBoostClassifier iteratively adjusts sample weights to increase the influence of misclassified instances in subsequent iterations.", True, "AdaBoost increases weights of incorrectly predicted samples so the next weak learner focuses on hard cases."),
        ("GradientBoostingClassifier builds sequential decision trees where each new tree fits the residual errors (pseudo-residuals) of the ensemble.", True, "Gradient Boosting optimizes loss functions by fitting new trees to the negative gradient residuals of prior trees."),
        ("XGBClassifier (Extreme Gradient Boosting) is an optimized, scalable implementation of gradient boosted decision trees.", True, "XGBoost provides high-performance parallelized gradient boosting with built-in regularization and fast tree building."),
        ("The learning_rate hyperparameter in Gradient Boosting scales the contribution of each individual tree added to the ensemble.", True, "learning_rate shrinks tree contributions, requiring more trees (n_estimators) to prevent overfitting."),
        ("Lower learning_rate values in Gradient Boosting require more trees (n_estimators) to achieve optimal performance.", True, "Smaller shrinkage steps require adding more sequential trees to fit dataset patterns completely."),
        ("XGBoost includes built-in L1 and L2 regularization to prevent individual trees from overfitting.", True, "XGBoost incorporates tree complexity penalties directly into its objective optimization loss."),
        ("Boosting algorithms generally achieve state-of-the-art accuracy on structured tabular datasets.", True, "Gradient boosted decision trees routinely dominate tabular machine learning benchmarks and competitions."),
        ("Unlike Random Forest which builds trees in parallel independently, Gradient Boosting builds trees sequentially in series.", True, "Random Forest parallelizes independent trees; Gradient Boosting relies on sequential residual error dependencies."),
        ("AdaBoost commonly uses shallow decision trees (decision stumps with max_depth=1) as base estimators.", True, "AdaBoost historically chains single-split decision stumps as simple weak base learners."),

        # Additional 10 Normal Questions (TP5_081 to TP5_090)
        ("KNeighborsClassifier classifies test samples based on the majority class vote of their k nearest spatial neighbors.", True, "k-NN identifies the k nearest training samples in distance space to cast class prediction votes."),
        ("DecisionTreeClassifier constructs a hierarchical rule tree by making optimal feature threshold splits.", True, "Decision trees recursively partition feature space at thresholds that maximize node purity."),
        ("RandomForestClassifier combines predictions from multiple decision trees trained on bootstrap samples.", True, "Random Forest builds parallel trees via bagging to reduce variance and improve accuracy."),
        ("GaussianNB calculates class priors and feature Gaussian normal distributions for continuous variables.", True, "GaussianNB assumes normal feature distributions within target classes."),
        ("BernoulliNB is tailored for classification problems where features are binary 0/1 indicators.", True, "BernoulliNB models binary feature occurrence probabilities."),
        ("Support Vector Classifier (SVC) finds an optimal hyperplane that maximizes spatial margin separation between classes.", True, "SVC maximizes spatial margin width to the nearest support vector data points."),
        ("LogisticRegression uses the sigmoid function to map linear combination outputs to continuous class probabilities.", True, "The sigmoid function squashes real linear outputs into valid continuous probabilities between 0 and 1."),
        ("SGDClassifier uses stochastic gradient updates to train linear classifiers efficiently on large datasets.", True, "Stochastic gradient descent updates parameters per sample/batch, scaling efficiently to large data."),
        ("AdaBoostClassifier iteratively increases weights of misclassified instances to train sequential weak learners.", True, "AdaBoost reweights hard misclassified samples so subsequent weak trees focus on correcting errors."),
        ("GradientBoostingClassifier builds sequential decision trees that fit residual errors of previous ensemble stages.", True, "Gradient Boosting fits sequential decision trees to negative gradient pseudo-residuals.")
    ]

    for i, (q, a, exp) in enumerate(normal_data, 1):
        questions.append({
            "id": f"TP5_{i:03d}",
            "tp": 5,
            "category": "normal",
            "question": q,
            "answer": a,
            "explanation": exp
        })

    # ---------------------------------------------------------
    # 50 TRICKY QUESTIONS (TP5_091 to TP5_140)
    # ---------------------------------------------------------
    tricky_data = [
        ("In scikit-learn, LogisticRegression handles non-linear decision boundaries natively without feature transformations.", False, "LogisticRegression constructs linear decision boundaries in raw feature space; non-linear boundaries require feature engineering or kernels."),
        ("DecisionTreeClassifier requires feature scaling with StandardScaler to build accurate decision splits.", False, "Decision trees evaluate axis-aligned threshold splits per feature independently, making them completely invariant to monotonic feature scaling."),
        ("RandomForestClassifier fits every constituent tree on the exact same full training dataset without row sampling.", False, "Random Forest uses bootstrap sampling (bagging) to train each tree on a different random sample of rows drawn with replacement."),
        ("GaussianNB requires features to be One-Hot encoded before model fitting.", False, "GaussianNB is designed for continuous features assuming normal distributions; binary categorical features are better modeled with BernoulliNB."),
        ("SVC with a linear kernel generates non-linear circular decision boundaries in raw 2D feature space.", False, "A linear kernel constructs straight hyperplanes (linear decision boundaries) in feature space."),
        ("In scikit-learn LogisticRegression, setting C=1000 applies extremely strong weight regularization.", False, "C is INVERSE regularization strength; large C values (C=1000) specify very WEAK regularization, while small C values (C=0.01) enforce strong regularization."),
        ("Increasing n_neighbors in KNeighborsClassifier from 3 to 50 increases model complexity and causes overfitting.", False, "Increasing n_neighbors smooths decision boundaries, REDUCING model complexity and variance (moving toward underfitting)."),
        ("GradientBoostingClassifier builds individual decision trees independently in parallel.", False, "Gradient Boosting builds trees SEQUENTIALLY, where each tree fits the residual errors of the prior ensemble; Random Forest builds trees in parallel."),
        ("KNeighborsClassifier computes feature_importances_ attributes after fitting.", False, "k-NN is an instance-based lazy learner that stores samples; it does not compute decision trees or feature_importances_."),
        ("An unconstrained DecisionTreeClassifier with max_depth=None is guaranteed to generalize well to unseen test data.", False, "Unconstrained trees memorize training noise, achieving 100% train accuracy but severe overfitting and poor test generalization."),

        ("SVC with an RBF kernel requires setting n_estimators to control the number of support vector trees.", False, "SVC is a support vector machine, not a tree ensemble; n_estimators is used in Random Forest or Boosting models."),
        ("BernoulliNB models continuous floating-point variables using Gaussian distribution means.", False, "BernoulliNB models binary 0/1 indicator features; continuous floating-point variables are modeled by GaussianNB."),
        ("Random Forest uses boosting to build sequential trees that correct prior tree classification errors.", False, "Random Forest uses BAGGING (bootstrap aggregating) of independent parallel trees; sequential error correction is used by BOOSTING (AdaBoost/GBDT)."),
        ("In LogisticRegression, L1 regularization shrinks feature weights without forcing any weight exactly to zero.", False, "L1 regularization (Lasso) forces uninformative feature weights EXACTLY to zero; L2 regularization shrinks weights without zeroing them."),
        ("AdaBoostClassifier assigns equal voting weight to every constituent weak learner tree regardless of its accuracy.", False, "AdaBoost weights tree voting power based on individual tree accuracy; Random Forest weights all tree votes equally."),
        ("In scikit-learn, calling model.predict_proba() on a trained DecisionTreeClassifier raises an error.", False, "DecisionTreeClassifier supports predict_proba(), returning class sample proportions in the matching leaf node."),
        ("Stochastic Gradient Descent (SGDClassifier) updates model weights only once after processing the complete dataset.", False, "SGD updates model weights iteratively per sample or mini-batch, unlike Batch Gradient Descent which processes all data before updating."),
        ("XGBClassifier requires all input numerical features to be normalized between 0 and 1 using MinMaxScaler.", False, "XGBoost builds decision trees that split on feature thresholds independently, making tree logic invariant to monotonic feature scaling."),
        ("Support vectors in SVC represent the training samples located farthest from the decision boundary.", False, "Support vectors are the training points located CLOSEST to the decision boundary that define margin bounds."),
        ("Increasing the gamma hyperparameter in SVC with RBF kernel creates a smoother, less complex decision boundary.", False, "High gamma restricts support vector influence to small local radii, creating highly complex, wiggly decision boundaries prone to overfitting."),

        ("KNeighborsClassifier requires training target labels y to be continuous floating-point values.", False, "KNeighborsClassifier is a classification model requiring discrete target labels; continuous targets use KNeighborsRegressor."),
        ("In scikit-learn, RandomForestClassifier automatically performs feature selection by deleting features with low importance during fit().", False, "RandomForestClassifier computes feature_importances_ for inspection but does NOT delete columns from X during fit()."),
        ("GaussianNB computes covariance matrices between all pairs of features during model fitting.", False, "GaussianNB assumes naive conditional independence between features, calculating univariate variance per feature rather than full covariance matrices."),
        ("SVC with penalty C=0.0001 forces the decision boundary to fit every training point with zero error.", False, "Very small C enforces massive regularization, allowing many training errors to achieve a wide, simple margin."),
        ("LogisticRegression outputs raw unbounded real values from -infinity to +infinity as class probabilities.", False, "LogisticRegression passes linear outputs through the sigmoid function, constraining predictions strictly to probabilities between 0 and 1."),
        ("Setting max_depth=1 in RandomForestClassifier produces a highly complex, overfitted model.", False, "max_depth=1 restricts trees to single-split decision stumps, producing an underfitted ensemble with low complexity."),
        ("SGDClassifier loss='hinge' optimizes logistic loss to output class probabilities via predict_proba().", False, "loss='hinge' optimizes SVM margin loss and does NOT support predict_proba(); probability estimates require loss='log_loss'."),
        ("AdaBoostClassifier increases the weights of correctly classified samples after each boosting iteration.", False, "AdaBoost INCREASES weights of MISCLASSIFIED samples (and decreases weights of correctly classified samples) to focus on hard cases."),
        ("A Gini Impurity score of 0.5 in a binary decision tree node represents a completely pure node.", False, "In binary classification, Gini = 0.5 represents maximum IMPURITY (50% Class 0, 50% Class 1); Gini = 0.0 represents a pure node."),
        ("Random Forest performs poorly when dataset rows contain unencoded string values.", False, "ALL scikit-learn models (including Random Forest) require categorical strings to be numerically encoded before fitting."),

        ("k-NN classifier prediction time is fastest when the training dataset contains 1,000,000 samples.", False, "k-NN lazy learning computes distances against stored training samples during prediction, making prediction very SLOW on large datasets."),
        ("SVC(kernel='rbf') computes an explicit finite 100-dimensional matrix for feature inputs.", False, "The RBF kernel computes inner products in an IMPLICIT infinite-dimensional Hilbert space using the kernel trick."),
        ("GradientBoostingClassifier learning_rate=1.0 heavily regularizes the model to prevent overfitting.", False, "learning_rate=1.0 applies NO shrinkage to tree contributions, increasing the risk of overfitting compared to smaller learning rates like 0.1."),
        ("In scikit-learn, model.fit(X_train, y_train) returns a new array containing predicted y labels.", False, "model.fit() trains internal parameters and returns the fitted ESTIMATOR object itself, NOT predicted labels; predictions require predict()."),
        ("DecisionTreeClassifier splits nodes by calculating the Euclidean distance between sample vectors.", False, "Decision trees split nodes by evaluating axis-aligned feature inequalities that minimize Gini/Entropy impurity, NOT Euclidean distance."),
        ("BernoulliNB models continuous features by calculating sample means and standard deviations.", False, "BernoulliNB evaluates binary feature presence (0/1); continuous features are modeled by GaussianNB."),
        ("In LogisticRegression, feature coefficients stored in model.coef_ are always non-negative numbers.", False, "Logistic regression coefficients can be positive (increasing odds) or negative (decreasing odds)."),
        ("Out-Of-Bag (OOB) scoring in RandomForestClassifier requires evaluating models on a separate test set.", False, "OOB scoring uses training samples left out of bootstrap samples during forest construction, requiring NO separate test set."),
        ("XGBClassifier cannot handle missing NaN values natively in input datasets.", False, "XGBoost includes native missing value handling, automatically learning default split directions for missing NaN entries."),
        ("Increasing n_estimators in AdaBoostClassifier from 10 to 1000 never leads to overfitting.", False, "Unlike Random Forest, boosting algorithms sequentially fit residual noise and CAN overfit if n_estimators is set excessively high without regularization.")
    ]

    for i, (q, a, exp) in enumerate(tricky_data, 91):
        questions.append({
            "id": f"TP5_{i:03d}",
            "tp": 5,
            "category": "tricky",
            "question": q,
            "answer": a,
            "explanation": exp
        })

    # Add 10 additional tricky questions to complete 50 (TP5_131 to TP5_140)
    extra_tricky = [
        ("Setting p=1 in KNeighborsClassifier Minkowski metric evaluates standard Euclidean distance.", False, "p=1 evaluates Manhattan distance (L1 norm); p=2 evaluates Euclidean distance (L2 norm)."),
        ("In scikit-learn, DecisionTreeClassifier compute feature importances that sum to 1.0.", True, "Decision tree feature_importances_ are normalized so that total feature contributions sum to 1.0."),
        ("Linear SVC decision boundaries are curved non-linear parabolas in 2D space.", False, "Linear SVC constructs straight linear hyperplanes in feature space."),
        ("Logistic regression assumes that predictor features are non-linearly combined to predict log-odds.", False, "Logistic regression assumes a LINEAR combination of features to model log-odds: z = w1*x1 + w2*x2 + b."),
        ("GaussianNB performs poorly when continuous features follow normal distributions within each class.", False, "GaussianNB explicitly assumes normal distributions per class and performs optimally when features are normally distributed."),
        ("In RandomForestClassifier, max_features='sqrt' selects a random sample of rows for each tree.", False, "max_features='sqrt' selects a random subset of FEATURES at each split; row sampling is controlled by bootstrap."),
        ("SGDClassifier requires feature scaling with StandardScaler prior to model training for gradient stability.", True, "Gradient descent optimization in SGD is sensitive to feature scales and requires standardized features to converge efficiently."),
        ("AdaBoost base estimators must be deep, complex decision trees with max_depth=20.", False, "AdaBoost works best with simple weak learners, typically shallow decision stumps with max_depth=1."),
        ("SVC predict_proba() is enabled by default without configuring probability=True during initialization.", False, "SVC requires setting probability=True during initialization to enable predict_proba() using Platt scaling."),
        ("GradientBoostingClassifier fits each new decision tree on the raw original target labels y.", False, "Gradient Boosting fits new trees to the RESIDUAL ERRORS (pseudo-residuals) of the preceding ensemble, not raw target y.")
    ]

    for i, (q, a, exp) in enumerate(extra_tricky, 131):
        questions.append({
            "id": f"TP5_{i:03d}",
            "tp": 5,
            "category": "tricky",
            "question": q,
            "answer": a,
            "explanation": exp
        })

    # ---------------------------------------------------------
    # 60 TRAP QUESTIONS (TP5_141 to TP5_200)
    # ---------------------------------------------------------
    trap_data = [
        ("Confusing Random Forest parallel bagging with Gradient Boosting sequential boosting.", False, "Random Forest builds independent trees in parallel via bagging; Gradient Boosting builds dependent trees sequentially to fit residuals."),
        ("Assuming that DecisionTreeClassifier requires feature scaling with StandardScaler prior to training.", False, "Decision trees evaluate threshold splits per feature independently, making tree split decisions invariant to feature scaling."),
        ("Believing that k-NN classifiers construct explicit decision tree flowcharts during fit().", False, "k-NN is an instance-based lazy learner that stores training points in memory without building explicit parametric trees."),
        ("Confusing GaussianNB (continuous normal features) with BernoulliNB (binary 0/1 features).", False, "GaussianNB models continuous features via normal distributions; BernoulliNB models binary occurrence features."),
        ("Assuming that SVC C parameter is direct regularization strength where large C increases regularization.", False, "C is INVERSE regularization strength: small C enforces strong regularization; large C weakens regularization."),
        ("Believing that LogisticRegression outputs unbounded continuous numbers from -infinity to +infinity as probabilities.", False, "LogisticRegression applies the sigmoid function, constraining class probability outputs strictly to [0, 1]."),
        ("Confusing small k (k=1, high variance overfitting) with large k (k=50, low variance underfitting) in k-NN.", False, "k=1 creates complex boundaries sensitive to noise (overfitting); large k smooths boundaries excessively (underfitting)."),
        ("Assuming that scikit-learn estimators can fit raw unencoded string columns directly.", False, "All scikit-learn classification estimators require numerical feature matrices X and fail on raw string columns."),
        ("Believing that LogisticRegression can only perform binary classification and cannot handle multi-class targets.", False, "LogisticRegression handles multi-class targets natively using One-vs-Rest (OvR) or Multinomial (Cross-Entropy) strategies."),
        ("Confusing SGDClassifier loss='hinge' (linear SVM) with loss='log_loss' (logistic regression).", False, "loss='hinge' fits a linear SVM; loss='log_loss' fits a logistic regression model."),

        ("Assuming that increasing n_estimators in RandomForestClassifier causes severe overfitting.", False, "Adding more trees in Random Forest averages ensemble voting, improving stability without increasing overfitting risk."),
        ("Believing that AdaBoost weights all weak learner trees equally during final prediction voting.", False, "AdaBoost weights tree voting power based on individual tree accuracy; Random Forest weights all trees equally."),
        ("Confusing decision tree Gini Impurity 0.0 (pure node) with maximum impurity 0.5.", False, "Gini = 0.0 indicates a perfectly pure single-class node; Gini = 0.5 represents maximum binary class mixing."),
        ("Assuming that SVC with RBF kernel gamma=1000 creates a smooth, flat decision boundary.", False, "High gamma restricts support vector influence to tiny local radii, creating highly wiggly decision boundaries prone to severe overfitting."),
        ("Believing that model.fit(X, y) returns predicted target labels y_pred.", False, "model.fit() trains internal model parameters and returns the fitted estimator object; target predictions require model.predict(X)."),
        ("Confusing L1 regularization (Lasso, zeroing weights) with L2 regularization (Ridge, shrinking weights).", False, "L1 regularization forces uninformative weights exactly to 0; L2 regularization shrinks weights toward 0 without zeroing them."),
        ("Assuming that k-NN classifier prediction is fast on massive 1,000,000 sample datasets.", False, "k-NN must compute spatial distances against stored training samples for every query, making prediction very slow on large datasets."),
        ("Believing that XGBClassifier requires feature scaling with MinMaxScaler prior to training.", False, "XGBoost builds decision trees that evaluate threshold splits per feature independently, making tree logic invariant to scaling."),
        ("Confusing support vectors in SVC (closest points defining margin) with dataset outliers.", False, "Support vectors are critical boundary samples defining the margin; they are not corrupt data outliers."),
        ("Assuming that Naive Bayes conditional independence assumption must strictly hold for the model to work.", False, "Naive Bayes often yields highly accurate classification decision boundaries even when the independence assumption is violated."),

        ("Believing that DecisionTreeClassifier feature_importances_ can take negative values.", False, "Decision tree feature_importances_ measure normalized impurity reductions and are strictly non-negative (>= 0)."),
        ("Confusing Gradient Boosting learning_rate shrinkage with optimizer gradient descent steps.", False, "learning_rate in boosting shrinks individual tree contributions to the ensemble, requiring more trees to fit data."),
        ("Assuming that BernoulliNB models multi-class continuous features using Gaussian distributions.", False, "BernoulliNB models binary 0/1 indicator features; continuous features require GaussianNB."),
        ("Believing that Out-Of-Bag (OOB) scoring in Random Forest requires a dedicated held-out test set.", False, "OOB scoring evaluates trees on training samples omitted from bootstrap samples, requiring no separate test set."),
        ("Confusing Linear SVC decision boundaries with non-linear kernel boundaries.", False, "Linear SVC constructs straight linear hyperplanes; RBF/Polynomial kernels construct non-linear boundaries."),
        ("Assuming that AdaBoost base estimators should be deep decision trees with max_depth=20.", False, "AdaBoost works best with shallow weak base learners, typically decision stumps with max_depth=1."),
        ("Believing that SVC predict_proba() is enabled by default without configuring probability=True.", False, "SVC requires setting probability=True during initialization to enable predict_proba() via Platt scaling."),
        ("Confusing LogisticRegression coef_ (learned feature weights) with hyperparameters (e.g., C, penalty).", False, "coef_ represents learned internal weights fit from data; C and penalty are hyperparameters specified before training."),
        ("Assuming that Random Forest max_features='sqrt' restricts row sampling.", False, "max_features='sqrt' restricts feature selection at each node split; row sampling is controlled by bootstrap."),
        ("Believing that Gradient Boosting fits each sequential tree directly on the raw original target labels y.", False, "Gradient Boosting fits sequential trees to residual errors (pseudo-residuals) of prior trees, not raw target y."),

        ("Confusing k-NN Minkowski metric p=1 (Manhattan distance) with p=2 (Euclidean distance).", False, "Minkowski p=1 computes Manhattan distance (L1); p=2 computes Euclidean distance (L2)."),
        ("Assuming that GaussianNB calculates full feature covariance matrices for multi-dimensional data.", False, "GaussianNB assumes naive conditional independence, calculating univariate feature variances independently per class."),
        ("Believing that unconstrained DecisionTreeClassifier (max_depth=None) prevents overfitting.", False, "Unconstrained trees grow until all leaves are pure, memorizing training noise and causing severe overfitting."),
        ("Confusing SGDClassifier (online stochastic gradient optimization) with batch gradient descent.", False, "SGDClassifier updates model weights per sample/batch iteratively, enabling fast online streaming learning."),
        ("Assuming that LogisticRegression sigmoid function outputs values from -1 to +1.", False, "The sigmoid function squashes inputs strictly into continuous probabilities between 0 and 1."),
        ("Believing that Random Forest feature_importances_ sum to 100.0 instead of 1.0.", False, "Feature importances in scikit-learn tree ensembles are normalized to sum to 1.0."),
        ("Confusing SVM margin maximization with decision tree Gini impurity minimization.", False, "SVM maximizes spatial distance (margin) between support vectors; decision trees minimize node impurity (Gini/Entropy)."),
        ("Assuming that AdaBoost increases weights of correctly classified samples after each fold.", False, "AdaBoost increases weights of MISCLASSIFIED samples to force subsequent weak learners to focus on hard cases."),
        ("Believing that XGBClassifier does not support native missing value handling.", False, "XGBoost automatically learns optimal split directions for missing NaN values during tree construction."),
        ("Confusing n_neighbors parameter in k-NN with n_estimators parameter in Random Forest.", False, "n_neighbors specifies nearby data points in k-NN; n_estimators specifies tree counts in ensemble models."),

        {"id": "TP5_181", "tp": 5, "category": "trap", "question": "Assuming that LogisticRegression calculates predictions using Euclidean distance to class centroids.", "answer": False, "explanation": "LogisticRegression computes linear dot products of features and weights passed through a sigmoid function, not centroid distances."},
        {"id": "TP5_182", "tp": 5, "category": "trap", "question": "Believing that Naive Bayes classifiers are slow to train on high-dimensional text data.", "answer": False, "explanation": "Naive Bayes computes independent univariate probability distributions, making training extremely fast on high-dimensional text data."},
        {"id": "TP5_183", "tp": 5, "category": "trap", "question": "Confusing Decision Tree max_depth with min_samples_split.", "answer": False, "explanation": "max_depth limits vertical tree height; min_samples_split sets the minimum node sample count required to split."},
        {"id": "TP5_184", "tp": 5, "category": "trap", "question": "Assuming that SVC rbf kernel gamma=0.0001 creates highly localized decision boundaries.", "answer": False, "explanation": "Small gamma expands support vector influence broadly, creating smooth linear-like decision boundaries."},
        {"id": "TP5_185", "tp": 5, "category": "trap", "question": "Believing that RandomForestClassifier predictions change on every execution when random_state is set.", "answer": False, "explanation": "Setting random_state ensures reproducible random bootstrap sampling and feature selection across executions."},
        {"id": "TP5_186", "tp": 5, "category": "trap", "question": "Confusing boosting (sequential error reduction) with bagging (parallel variance reduction).", "answer": False, "explanation": "Boosting builds sequential models to reduce bias/error; bagging builds parallel independent models to reduce variance."},
        {"id": "TP5_187", "tp": 5, "category": "trap", "question": "Assuming that SGDClassifier loss='log_loss' fits a Support Vector Machine.", "answer": False, "explanation": "loss='log_loss' fits a logistic regression model; loss='hinge' fits a linear SVM."},
        {"id": "TP5_188", "tp": 5, "category": "trap", "question": "Believing that DecisionTreeClassifier requires categorical target labels y to be string text.", "answer": False, "explanation": "Target labels y can be integers (0, 1, 2) or encoded strings; scikit-learn handles integer class labels natively."},
        {"id": "TP5_189", "tp": 5, "category": "trap", "question": "Confusing k-NN lazy evaluation with eager model training in decision trees.", "answer": False, "explanation": "k-NN delays computation until prediction (lazy); decision trees build explicit tree structures during fit() (eager)."},
        {"id": "TP5_190", "tp": 5, "category": "trap", "question": "Assuming that AdaBoost handles continuous targets natively in classification mode.", "answer": False, "explanation": "AdaBoostClassifier requires discrete classification target labels y; continuous targets require AdaBoostRegressor."},

        {"id": "TP5_191", "tp": 5, "category": "trap", "question": "Believing that LogisticRegression with L2 penalty sets uninformative feature weights strictly to zero.", "answer": False, "explanation": "L2 regularization shrinks weights toward zero without forcing them to exact zero; L1 regularization forces weights to 0."},
        {"id": "TP5_192", "tp": 5, "category": "trap", "question": "Confusing GaussianNB with KNeighborsClassifier in scikit-learn.", "answer": False, "explanation": "GaussianNB is a probabilistic Bayes model; KNeighborsClassifier is a distance-based instance model."},
        {"id": "TP5_193", "tp": 5, "category": "trap", "question": "Assuming that RandomForestClassifier requires training data to be sorted prior to fitting.", "answer": False, "explanation": "Random Forest evaluates sample rows independently; row sorting order does not affect tree splits or predictions."},
        {"id": "TP5_194", "tp": 5, "category": "trap", "question": "Believing that GradientBoostingClassifier builds deep trees with max_depth=50 by default.", "answer": False, "explanation": "Gradient Boosting builds shallow weak trees (typically max_depth=3 to 5) to prevent sequential ensemble overfitting."},
        {"id": "TP5_195", "tp": 5, "category": "trap", "question": "Confusing SVC support vectors with hyperplane normal vectors.", "answer": False, "explanation": "Support vectors are actual data sample points on margin boundaries; normal vectors specify hyperplane orientation math."},
        {"id": "TP5_196", "tp": 5, "category": "trap", "question": "Assuming that XGBClassifier executes single-threaded iterations exclusively.", "answer": False, "explanation": "XGBoost is highly parallelized, utilizing multi-threading CPU/GPU acceleration for fast tree construction."},
        {"id": "TP5_197", "tp": 5, "category": "trap", "question": "Believing that model.score() on a trained classifier evaluates mean squared error (MSE).", "answer": False, "explanation": "model.score() on classification estimators evaluates mean classification ACCURACY, not mean squared error."},
        {"id": "TP5_198", "tp": 5, "category": "trap", "question": "Confusing k-NN distance weights (weights='distance') with uniform voting (weights='uniform').", "answer": False, "explanation": "weights='distance' weighs closer neighbors more heavily; weights='uniform' treats all k neighbors equally in voting."},
        {"id": "TP5_199", "tp": 5, "category": "trap", "question": "Assuming that DecisionTreeClassifier Gini impurity calculation requires log transformations.", "answer": False, "explanation": "Gini impurity uses squared class probabilities (1 - sum(p_i^2)); Entropy uses log probability terms."},
        {"id": "TP5_200", "tp": 5, "category": "trap", "question": "Believing that supervised classification algorithms can learn patterns without ground truth target labels y.", "answer": False, "explanation": "Supervised classification strictly requires ground truth target labels y during training to learn predictive mappings."}
    ]

    # Convert tuple rows to dicts for 141..180
    for i, item in enumerate(trap_data[:40], 141):
        q, a, exp = item
        questions.append({
            "id": f"TP5_{i:03d}",
            "tp": 5,
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
    qs = get_tp5_questions()
    print(f"TP5 Total: {len(qs)}")
    print("Normal:", sum(1 for q in qs if q["category"] == "normal"))
    print("Tricky:", sum(1 for q in qs if q["category"] == "tricky"))
    print("Trap:", sum(1 for q in qs if q["category"] == "trap"))
