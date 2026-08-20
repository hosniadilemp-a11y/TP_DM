# TP 4 — Model Evaluation Metrics & Validation (200 Questions: 90 Normal, 50 Tricky, 60 Trap)

def get_tp4_questions():
    questions = []
    
    # ---------------------------------------------------------
    # 90 NORMAL QUESTIONS (TP4_001 to TP4_090)
    # ---------------------------------------------------------
    normal_data = [
        # Confusion Matrix & Basic Classification Metrics (Easy/Medium)
        ("A confusion matrix is a tabular layout displaying true positive, true negative, false positive, and false negative prediction counts.", True, "The confusion matrix summarizes classification predictions against actual ground truth labels."),
        ("True Positives (TP) represent actual positive instances that were correctly predicted as positive by the model.", True, "TP counts positive cases where model prediction matches actual positive ground truth."),
        ("True Negatives (TN) represent actual negative instances that were correctly predicted as negative by the model.", True, "TN counts negative cases where model prediction matches actual negative ground truth."),
        ("False Positives (FP) represent actual negative instances that were incorrectly predicted as positive by the model.", True, "FP (Type I error) occurs when a negative instance is falsely classified as positive."),
        ("False Negatives (FN) represent actual positive instances that were incorrectly predicted as negative by the model.", True, "FN (Type II error) occurs when a positive instance is falsely classified as negative."),
        ("Accuracy is calculated as the ratio of correct predictions (TP + TN) to total predictions (TP + TN + FP + FN).", True, "Accuracy measures the overall proportion of correctly classified instances."),
        ("Precision is calculated as TP / (TP + FP), measuring the proportion of true positives among all positive predictions.", True, "Precision evaluates prediction accuracy within the positive predicted class."),
        ("Recall (Sensitivity) is calculated as TP / (TP + FN), measuring the proportion of actual positive instances correctly identified.", True, "Recall measures the model's ability to catch all true positive instances."),
        ("F1-score is the harmonic mean of precision and recall.", True, "F1-score balances precision and recall into a single metric using their harmonic mean."),
        ("The formula for F1-score is 2 * (Precision * Recall) / (Precision + Recall).", True, "The harmonic mean formula balances precision and recall, penalizing extreme trade-off imbalances."),

        # Trade-offs & Specialized Metrics (Medium)
        ("Precision is particularly critical when False Positives carry high cost or penalty.", True, "High precision minimizes false alarms in scenarios where false positive predictions are costly."),
        ("Recall is particularly critical when False Negatives carry high cost or danger, such as medical disease detection.", True, "High recall ensures missing a true positive case (e.g., undiagnosed illness) is minimized."),
        ("Accuracy can be misleading when evaluating models on heavily imbalanced datasets.", True, "In imbalanced data (e.g., 99% negative), a naive model predicting all negatives achieves 99% accuracy while failing completely."),
        ("The ROC curve plots the True Positive Rate (Recall) against the False Positive Rate (FPR) across various classification thresholds.", True, "ROC curves map TPR (y-axis) vs FPR (x-axis) across varying probability decision thresholds."),
        ("False Positive Rate (FPR) is calculated as FP / (FP + TN).", True, "FPR measures the proportion of actual negatives incorrectly flagged as positive."),
        ("The Area Under the ROC Curve (AUC-ROC) score ranges from 0.0 to 1.0.", True, "AUC-ROC measures discrimination capability: 1.0 represents perfect separation, 0.5 represents random guessing."),
        ("An AUC-ROC score of 0.5 indicates a classifier with performance equivalent to random guessing.", True, "An AUC of 0.5 corresponds to the diagonal baseline of no class discrimination capability."),
        ("An AUC-ROC score of 1.0 represents a perfect classification model with zero prediction error.", True, "AUC = 1.0 means the model separates positive and negative classes perfectly across thresholds."),
        ("In scikit-learn, classification_report generates precision, recall, f1-score, and support metrics for each class.", True, "classification_report summarizes comprehensive per-class classification metrics in a clean text layout."),
        ("The predict_proba() method returns predicted class probabilities for input instances.", True, "predict_proba() outputs continuous probability estimates used to construct ROC curves and threshold metrics."),

        # Cross-Validation Techniques (Medium/Hard)
        ("Cross-validation provides a robust estimate of model generalization performance by partitioning data into multiple folds.", True, "Cross-validation evaluates models across iterative train/validation splits, reducing single-split sampling variance."),
        ("In K-Fold cross-validation, the dataset is divided into K equal partitions (folds).", True, "K-Fold splits data into K subsets, training K times on K-1 folds and validating on the remaining fold."),
        ("In 5-Fold cross-validation, the model is trained 5 separate times, each time using 4 folds for training and 1 for validation.", True, "Each iteration uses 80% data for training and 20% for validation across 5 total iterations."),
        ("The final cross-validation score is typically reported as the mean of the validation scores across all K folds.", True, "Averaging fold scores yields a stable summary metric of generalization performance."),
        ("StratifiedKFold ensures that each fold maintains approximately the same class label proportions as the full dataset.", True, "Stratification preserves target class distributions across every cross-validation partition fold."),
        ("StratifiedKFold is recommended over standard KFold when evaluating models on imbalanced classification datasets.", True, "Preserving class ratios prevents folds from lacking minority class samples entirely."),
        ("ShuffleSplit cross-validation randomly shuffles and splits data into training and validation sets for a specified number of iterations.", True, "ShuffleSplit allows independent random splits with custom train/validation sizing per iteration."),
        ("LeaveOneOut (LOO) cross-validation is equivalent to K-Fold cross-validation where K equals the total sample size N.", True, "LOO uses N-1 samples for training and 1 sample for validation across N iterations."),
        ("In scikit-learn, cross_val_score(model, X, y, cv=5) returns an array of 5 validation scores.", True, "cross_val_score evaluates estimator performance over cross-validation folds and returns fold score arrays."),
        ("LeaveOneOut cross-validation can be computationally expensive on large datasets because it fits the model N times.", True, "Fitting N separate models when N is large requires extensive computational processing time."),

        # Hyperparameter Tuning with GridSearchCV (Medium/Hard)
        ("GridSearchCV systematically evaluates a specified grid of hyperparameter combinations using cross-validation.", True, "GridSearchCV performs exhaustive search over a parameter grid to find optimal model settings."),
        ("In scikit-learn, param_grid is defined as a dictionary mapping hyperparameter names to lists of values to test.", True, "param_grid dict specifies candidate parameter arrays (e.g., {'n_neighbors': [3, 5, 7], 'metric': ['euclidean', 'manhattan']})."),
        ("GridSearchCV identifies the hyperparameter combination that achieves the highest mean cross-validation score.", True, "GridSearchCV ranks parameter configurations by their mean validation performance."),
        ("After fitting, grid.best_params_ returns a dictionary of the top-performing hyperparameter settings.", True, "best_params_ stores the parameter dictionary yielding the highest cross-validation score."),
        ("After fitting, grid.best_score_ returns the mean cross-validation score achieved by the best hyperparameter configuration.", True, "best_score_ reports the peak mean validation score observed during grid search."),
        ("After fitting, grid.best_estimator_ returns the trained model instance configured with the best hyperparameters.", True, "best_estimator_ holds the optimized model fitted on the complete training set."),
        ("GridSearchCV automatically refits the best model on the entire training dataset after completing grid search by default.", True, "refit=True (default) fits the optimal parameter model on the full training dataset after search completion."),
        ("Evaluating grid.best_estimator_.score(X_test, y_test) measures generalization performance on unseen test data.", True, "Scoring the best estimator on held-out test data verifies out-of-sample prediction capability."),
        ("Grid Search helps optimize non-learnable hyperparameters like the number of neighbors k in k-NN.", True, "Hyperparameters cannot be learned directly via gradient descent and require tuning routines like Grid Search."),
        ("Exhaustive grid search on large parameter grids can require significant computation time.", True, "Testing all parameter combinations across K folds multiplies training iterations rapidly."),

        # Diagnostic Curves: Learning & Validation Curves (Medium/Hard)
        ("A validation curve displays model training and validation scores as a function of varying hyperparameter values.", True, "validation_curve plots performance against hyperparameter values to diagnose underfitting and overfitting ranges."),
        ("A learning curve displays training and validation scores as a function of increasing training dataset size.", True, "learning_curve plots performance against training sample size N to evaluate data volume impact."),
        ("Overfitting occurs when a model performs exceptionally well on training data but poorly on validation/test data.", True, "Overfitting means the model memorizes training noise, failing to generalize to unseen samples."),
        ("Underfitting occurs when a model performs poorly on both training data and validation/test data.", True, "Underfitting indicates insufficient model complexity or poor feature representation to capture signal."),
        ("On a validation curve, a large gap between high training score and low validation score indicates overfitting.", True, "A wide performance gap signifies high variance (overfitting) on training data."),
        ("On a validation curve, low training score and low validation score together indicate underfitting.", True, "Simultaneously poor training and validation scores signify high bias (underfitting)."),
        ("A learning curve can indicate whether collecting additional training samples is likely to improve model performance.", True, "If validation score is still rising as training size increases, adding data can improve performance."),
        ("In scikit-learn, validation_curve returns arrays of training and validation scores for specified hyperparameter values.", True, "validation_curve outputs train_scores and test_scores matrices across parameter values and folds."),
        ("In scikit-learn, learning_curve returns training set sizes N along with train and validation score arrays.", True, "learning_curve outputs sample sizes N, train_scores, and test_scores across specified sample fractions."),
        ("Plotting mean train vs mean validation scores on diagnostic curves helps select optimal parameter ranges visually.", True, "Visualizing curve means clarifies where validation performance peaks relative to training fit."),

        # Metric Definitions & Interpretation (Medium/Hard)
        ("In binary classification, Macro Average calculates metrics independently for each class and averages them equally.", True, "Macro average treats all classes equally, averaging per-class metrics without weighting by class support."),
        ("Weighted Average calculates per-class metrics weighted by the number of actual instances (support) in each class.", True, "Weighted average scales per-class metrics by class instance frequency, accounting for class imbalance."),
        ("Support in a classification report represents the actual count of ground truth instances in each class.", True, "Support lists the total number of true samples belonging to each target category in the test set."),
        ("Evaluating accuracy alone on a dataset with 95% Class 0 and 5% Class 1 can mask a model that predicts only Class 0.", True, "A trivial model predicting only majority class achieves 95% accuracy while failing 100% of minority class 1 cases."),
        ("The Receiver Operating Characteristic (ROC) curve x-axis represents the False Positive Rate (FPR).", True, "ROC curve plots FPR on the horizontal x-axis and TPR (Recall) on the vertical y-axis."),
        ("The ROC curve y-axis represents the True Positive Rate (TPR / Recall).", True, "TPR (Sensitivity/Recall) is plotted on the vertical y-axis of the ROC curve."),
        ("Increasing the classification decision threshold increases precision while generally decreasing recall.", True, "A higher decision threshold requires higher probability confidence for positive predictions, raising precision but missing positive cases."),
        ("Decreasing the classification decision threshold increases recall while generally decreasing precision.", True, "A lower decision threshold flags more positive predictions, catching more true positives (higher recall) with more false alarms (lower precision)."),
        ("A random classifier yields a diagonal line from (0,0) to (1,1) on an ROC plot.", True, "Uninformative random guessing produces a straight diagonal line with AUC = 0.5."),
        ("Precision-Recall (PR) curves are often preferred over ROC curves for evaluating models on highly imbalanced datasets.", True, "PR curves focus exclusively on the minority positive class without being dampened by large true negative counts."),

        # Operational Scikit-Learn Metric Functions (Medium)
        ("In scikit-learn, accuracy_score(y_true, y_pred) calculates classification accuracy.", True, "accuracy_score computes the fraction of correct prediction matches between y_true and y_pred."),
        ("In scikit-learn, precision_score(y_true, y_pred) computes precision for positive class predictions.", True, "precision_score calculates TP / (TP + FP) for binary target classification."),
        ("In scikit-learn, recall_score(y_true, y_pred) computes recall for true positive instances.", True, "recall_score calculates TP / (TP + FN) for binary target classification."),
        ("In scikit-learn, f1_score(y_true, y_pred) computes the harmonic mean F1-score.", True, "f1_score evaluates the balanced harmonic metric between precision and recall."),
        ("In scikit-learn, roc_auc_score(y_true, y_score) computes the area under the ROC curve.", True, "roc_auc_score calculates the numerical AUC score given true labels and predicted positive probabilities."),
        ("In scikit-learn, confusion_matrix(y_true, y_pred) returns a 2x2 matrix for binary classification.", True, "confusion_matrix outputs array([[TN, FP], [FN, TP]]) for binary targets."),
        ("Seaborn heatmap (sns.heatmap) can visually display a confusion matrix with numerical annotations.", True, "sns.heatmap(cm, annot=True, fmt='d') renders a clear annotated visual matrix layout."),
        ("Evaluating cross_val_score with scoring='f1' computes F1-scores across cross-validation folds.", True, "Passing scoring='f1' directs cross_val_score to evaluate F1 performance instead of default accuracy."),
        ("GridSearchCV can optimize models based on custom scoring metrics such as scoring='roc_auc'.", True, "GridSearchCV accepts custom scoring targets (e.g., roc_auc, f1, precision) to guide hyperparameter selection."),
        ("Holding out a dedicated test set guarantees unbiased validation of final model performance after hyperparameter tuning.", True, "Evaluating on held-out test data ensures hyperparameter search choices did not overfit validation folds."),

        # Practical Evaluation Workflows & Best Practices (Medium/Hard)
        ("Cross-validation prevents reporting overly optimistic performance metrics caused by a single lucky train/test split.", True, "Averaging across multiple fold partitions smooths out random split variations."),
        ("When tuning hyperparameters, the test set must remain untouched until final model validation.", True, "Tuning parameters directly on test data corrupts test set independence and leads to biased evaluation."),
        ("A model with 99% training accuracy and 50% test accuracy suffers from severe overfitting.", True, "A huge performance drop between train and test performance is a textbook indicator of high variance overfitting."),
        ("Underfitting can be mitigated by increasing model complexity or engineering more informative features.", True, "Adding model capacity or richer feature signals helps underfitting models capture complex data patterns."),
        ("Overfitting can be mitigated by regularization, reducing feature count, or collecting more training samples.", True, "Constraining model complexity or expanding sample size prevents models from memorizing sample noise."),
        ("In scikit-learn, cross_val_score uses StratifiedKFold by default when passed a classification estimator and discrete y.", True, "Scikit-learn cross_val_score automatically applies stratified splitting for classification tasks by default."),
        ("In K-Fold cross-validation, increasing K increases training set size per fold while increasing computational load.", True, "Larger K provides more training data per fold (N*(K-1)/K) but requires training K separate model iterations."),
        ("In scikit-learn, roc_curve returns false positive rates, true positive rates, and decision thresholds.", True, "roc_curve outputs (fpr, tpr, thresholds) arrays used for ROC plotting and threshold selection."),
        ("Comparing multiple algorithms using identical cross-validation folds ensures fair model comparison.", True, "Evaluating candidate algorithms on identical data partitions isolates algorithm quality from split noise."),
        ("Model evaluation strategy should align directly with domain business goals and error costs.", True, "Metric selection must reflect domain consequences, prioritizing recall for critical safety/medical tasks or precision for low-false-alarm requirements."),

        # Additional 10 Normal Questions (TP4_081 to TP4_090)
        ("In binary classification, accuracy is defined as (TP + TN) / (TP + TN + FP + FN).", True, "Accuracy computes the total proportion of correct predictions across all instances."),
        ("Precision measures the proportion of positive predictions that are true positive cases.", True, "Precision evaluates TP / (TP + FP) to measure prediction reliability."),
        ("Recall measures the proportion of actual positive instances correctly flagged by the model.", True, "Recall evaluates TP / (TP + FN) to measure true positive coverage."),
        ("F1-score combines precision and recall into a single metric using their harmonic mean.", True, "F1-score balances precision and recall into a single harmonic mean metric."),
        ("AUC-ROC score measures the ability of a classification model to rank positive samples higher than negative samples.", True, "AUC-ROC quantifies overall class ranking discrimination across thresholds."),
        ("Confusion matrix summarizes true positive, true negative, false positive, and false negative predictions.", True, "The confusion matrix organizes prediction results into a 2x2 contingency table."),
        ("K-Fold cross-validation splits data into K equal folds, training K times on K-1 folds and validating on 1 fold.", True, "K-Fold evaluates model stability across K iterative partitions."),
        ("StratifiedKFold maintains identical target class proportions in every fold partition.", True, "Stratification preserves target class distributions across cross-validation splits."),
        ("GridSearchCV exhaustively tests hyperparameter combinations on cross-validation folds.", True, "GridSearchCV searches parameter grids to find configurations yielding peak cross-validation scores."),
        ("Learning curves plot training and validation performance against increasing sample size N.", True, "Learning curves diagnose underfitting or overfitting as dataset size increases.")
    ]

    for i, (q, a, exp) in enumerate(normal_data, 1):
        questions.append({
            "id": f"TP4_{i:03d}",
            "tp": 4,
            "category": "normal",
            "question": q,
            "answer": a,
            "explanation": exp
        })

    # ---------------------------------------------------------
    # 50 TRICKY QUESTIONS (TP4_091 to TP4_140)
    # ---------------------------------------------------------
    tricky_data = [
        ("Accuracy is always the best metric for evaluating classification models regardless of class balance.", False, "Accuracy is misleading on imbalanced datasets; a model predicting only the majority class achieves high accuracy while failing completely on minority cases."),
        ("In a binary confusion matrix formatted as [[TN, FP], [FN, TP]], the top-left cell represents True Positives.", False, "In standard scikit-learn confusion matrix layout [[TN, FP], [FN, TP]], the top-left cell represents True Negatives (TN)."),
        ("Recall measures the proportion of positive predictions that are actually correct.", False, "Precision measures correct positive PREDICTIONS (TP / (TP+FP)); Recall measures identified actual POSITIVE INSTANCES (TP / (TP+FN))."),
        ("F1-score is calculated as the standard arithmetic mean of precision and recall.", False, "F1-score is the HARMONIC mean of precision and recall: 2*(P*R)/(P+R), not the arithmetic mean."),
        ("An AUC-ROC score of 0.0 indicates a model whose predictions are equivalent to random guessing.", False, "AUC of 0.5 represents random guessing; AUC of 0.0 represents a perfectly inverted model whose predictions can be flipped to achieve AUC 1.0."),
        ("Cross-validation fit statistics computed across all folds simultaneously should be used to scale pre-split data.", False, "Computing scaling statistics across all data/folds prior to splitting leaks validation statistics into training, causing data leakage."),
        ("In scikit-learn, cross_val_score modifies the input model object in place and saves the best fold model.", False, "cross_val_score clones the estimator for each fold and discards fold models, returning only score arrays without modifying the input estimator."),
        ("GridSearchCV evaluates hyperparameter combinations directly on the held-out test set.", False, "GridSearchCV evaluates parameter combinations using cross-validation on the TRAINING set, reserving the test set for final evaluation."),
        ("A model with low training accuracy and high validation accuracy suffers from severe overfitting.", False, "Overfitting is characterized by HIGH training accuracy and LOW validation accuracy."),
        ("Increasing the decision probability threshold from 0.5 to 0.8 always increases recall.", False, "Raising the probability threshold makes positive predictions stricter, which DECREASES (or maintains) recall while increasing precision."),

        ("LeaveOneOut cross-validation is fast and computationally cheap for a dataset with 1,000,000 samples.", False, "LeaveOneOut fits N separate models (1,000,000 model fits here), making it extremely slow and computationally expensive."),
        ("StratifiedKFold partitions data such that each fold contains equal numbers of samples from every class, even on imbalanced data.", False, "StratifiedKFold preserves the ORIGINAL class proportion ratio in each fold, not equal numbers across classes."),
        ("On a validation curve, an underfitting model exhibits a very high training score and a very low validation score.", False, "Underfitting is characterized by LOW training score and LOW validation score; high train and low validation indicate overfitting."),
        ("A learning curve that shows training score and validation score converging at a high performance level indicates severe underfitting.", False, "Convergence at a HIGH performance level indicates a well-fitted model that generalizes well with sufficient data."),
        ("In scikit-learn, precision_score(y_true, y_pred) requires y_pred to contain continuous probability floats.", False, "precision_score requires discrete binary/class predictions (0/1), whereas roc_auc_score requires continuous probabilities."),
        ("The ROC curve is plotted with Precision on the y-axis and Recall on the x-axis.", False, "ROC curve plots True Positive Rate (Recall) on the y-axis and False Positive Rate (FPR) on the x-axis; PR curves plot Precision vs Recall."),
        ("Using grid.best_estimator_ automatically fits a new model using default hyperparameters.", False, "best_estimator_ returns the model configured with OPTIMAL hyperparameters tuned during grid search."),
        ("Macro average in classification_report weights each class metric by its sample size support.", False, "Macro average computes an UNWEIGHTED arithmetic mean across classes; Weighted average weights metrics by class support."),
        ("A model with 100% precision is guaranteed to catch all actual positive cases in the dataset.", False, "100% precision means every positive prediction was correct, but it may miss many positive cases (yielding low recall)."),
        ("ShuffleSplit cross-validation guarantees that every sample is used in the validation set exactly once.", False, "ShuffleSplit samples partitions randomly with replacement across iterations; some samples may appear in validation multiple times or never."),

        ("Applying cross_val_score on a dataset with missing NaN values automatically imputes missing entries.", False, "cross_val_score does not impute NaNs automatically; missing entries must be handled in a Pipeline or prior to scoring."),
        ("The False Positive Rate (FPR) is calculated as FP / (TP + FP).", False, "FPR is calculated as FP / (FP + TN); FP / (TP + FP) equals 1 - Precision."),
        ("A high F1-score guarantees that both precision and recall are equal to 1.0.", False, "High F1-score indicates a strong balance between precision and recall, but they need not be exactly 1.0 nor equal."),
        ("GridSearchCV parameter param_grid accepts a list of trained classifier instances.", False, "param_grid accepts a dictionary mapping hyperparameter string names to lists of candidate parameter values."),
        ("An AUC-ROC score of 0.85 means the model correctly classifies 85% of all test instances.", False, "AUC-ROC measures class ranking discrimination probability (85% chance a random positive ranks higher than a random negative), not raw accuracy."),
        ("KFold with shuffle=False generates identical random splits regardless of initial dataset order.", False, "shuffle=False takes consecutive sample slices based strictly on initial dataset order; changing dataset order changes fold contents."),
        ("Evaluating a classifier using model.score(X_test, y_test) calculates the F1-score by default.", False, "In scikit-learn classifiers, model.score() calculates mean ACCURACY by default, not F1-score."),
        ("On a learning curve, if training score remains much higher than validation score as N grows, adding data will never help.", False, "A persistent gap between train and validation scores indicates high variance (overfitting); adding more training data often helps close the gap."),
        ("Precision-Recall curves are uninformative when evaluating datasets with severe class imbalance.", False, "Precision-Recall curves are specifically RECOMMENDED for severely imbalanced datasets because they ignore True Negatives."),
        ("In scikit-learn confusion_matrix(y_true, y_pred), the rows represent predicted labels and columns represent true labels.", False, "In scikit-learn confusion_matrix, ROWS represent TRUE labels and COLUMNS represent PREDICTED labels."),

        ("A model that predicts the positive class for every single instance achieves 100% precision.", False, "Predicting positive for every instance catches all positive cases (100% recall) but generates many false positives, lowering precision."),
        ("Setting cv=1 in cross_val_score executes standard single-fold validation.", False, "Cross-validation requires at least 2 folds (cv >= 2); passing cv=1 raises a ValueError in scikit-learn."),
        ("The harmonic mean used in F1-score gives equal weight to extreme values compared to the arithmetic mean.", False, "The harmonic mean heavily penalizes low values, ensuring F1-score stays low if EITHER precision or recall is low."),
        ("GridSearchCV refit=False returns a fully trained best_estimator_ model fitted on all training data.", False, "refit=False skips final model fitting on the full dataset; best_estimator_ is NOT available when refit=False."),
        ("In ROC analysis, a lower threshold always produces a lower True Positive Rate.", False, "Lowering the decision threshold makes positive predictions easier, which INCREASES (or maintains) the True Positive Rate (Recall)."),
        ("Validation curves plot training size N on the horizontal x-axis.", False, "Validation curves plot HYPERPARAMETER values on the x-axis; Learning curves plot training size N on the x-axis."),
        ("A classification model with high variance is characterized by underfitting both train and test data.", False, "High variance corresponds to OVERFITTING (memorizing training data); high bias corresponds to underfitting."),
        ("LeaveOneOut cross-validation uses 50% of data for training and 50% for validation in each iteration.", False, "LeaveOneOut uses N-1 samples (almost 100%) for training and exactly 1 sample for validation in each iteration."),
        ("Evaluating accuracy on balanced binary data yields misleading results compared to imbalanced data.", False, "Accuracy is a valid and reliable metric on BALANCED data; it becomes misleading on IMBALANCED data."),
        ("Scikit-learn roc_curve function accepts discrete binary predictions (0/1) to draw smooth ROC curves.", False, "roc_curve requires continuous probability estimates or decision scores (from predict_proba or decision_function) to evaluate thresholds.")
    ]

    for i, (q, a, exp) in enumerate(tricky_data, 91):
        questions.append({
            "id": f"TP4_{i:03d}",
            "tp": 4,
            "category": "tricky",
            "question": q,
            "answer": a,
            "explanation": exp
        })

    # Add 10 additional tricky questions to complete 50 (TP4_131 to TP4_140)
    extra_tricky = [
        ("StratifiedKFold splits continuous target values y into equal-width histogram bins for regression scoring.", False, "StratifiedKFold is strictly for discrete classification labels; continuous regression targets use standard KFold."),
        ("In scikit-learn, precision_score with pos_label=0 computes precision targeting class 1.", False, "pos_label specifies which class is treated as positive; pos_label=0 computes precision targeting class 0."),
        ("A model with 0% false positives achieves 100% recall unconditionally.", False, "0% false positives means FP = 0 (100% precision), but recall depends on TP / (TP + FN) and can still be low if FN > 0."),
        ("GridSearchCV evaluate step executes fit_transform on test set folds to optimize scaling.", False, "GridSearchCV fits transformers ONLY on training folds to prevent data leakage into validation folds."),
        ("Specificty is mathematically identical to Recall in binary classification.", False, "Recall is Sensitivity (TP / (TP+FN)); Specificity is True Negative Rate (TN / (TN+FP))."),
        ("Overfitting models exhibit low training error and low cross-validation error.", False, "Overfitting models exhibit low training error but HIGH cross-validation error."),
        ("In scikit-learn classification_report, support indicates the accuracy score achieved for that class.", False, "Support indicates the total number of actual ground truth samples present in that class."),
        ("AUC-ROC score is heavily distorted by changing the classification decision threshold.", False, "AUC-ROC evaluates performance ACROSS ALL decision thresholds, making it invariant to single threshold choices."),
        ("K-Fold cross-validation with K=10 trains a total of 100 model instances.", False, "K-Fold cross-validation with K=10 trains exactly 10 model instances (one per fold)."),
        ("Setting scoring='accuracy' in GridSearchCV optimizes for F1-score.", False, "scoring='accuracy' optimizes for classification accuracy; optimizing for F1 requires scoring='f1'.")
    ]

    for i, (q, a, exp) in enumerate(extra_tricky, 131):
        questions.append({
            "id": f"TP4_{i:03d}",
            "tp": 4,
            "category": "tricky",
            "question": q,
            "answer": a,
            "explanation": exp
        })

    # ---------------------------------------------------------
    # 60 TRAP QUESTIONS (TP4_141 to TP4_200)
    # ---------------------------------------------------------
    trap_data = [
        ("Confusing Precision with Recall when evaluating medical diagnosis models where missing a disease case is fatal.", False, "Medical diagnosis prioritizes RECALL (catching all true positive cases) to minimize dangerous false negatives."),
        ("Assuming that Accuracy is a reliable performance metric for severely imbalanced datasets (e.g., 99% negative).", False, "Accuracy is misleading on imbalanced data because a dummy model predicting 100% negative achieves 99% accuracy while failing completely."),
        ("Believing that scikit-learn confusion_matrix places True Positives in the top-left cell.", False, "Scikit-learn confusion_matrix format [[TN, FP], [FN, TP]] places True Negatives (TN) top-left and True Positives (TP) bottom-right."),
        ("Confusing the arithmetic mean with the harmonic mean when calculating F1-score.", False, "F1-score uses the HARMONIC mean 2*(P*R)/(P+R), which heavily penalizes imbalances between precision and recall."),
        ("Assuming that an AUC-ROC score of 0.5 represents a perfect classification model.", False, "AUC of 0.5 represents uninformative random guessing; AUC of 1.0 represents a perfect classifier."),
        ("Believing that fitting transformers on the full dataset before cross_val_score is valid preprocessing.", False, "Fitting transformers on full datasets before cross-validation leaks validation fold statistics into training folds."),
        ("Confusing False Positives (Type I error) with False Negatives (Type II error).", False, "False Positive (Type I) is incorrectly flagging a negative as positive; False Negative (Type II) is failing to flag a true positive."),
        ("Assuming that GridSearchCV best_estimator_ evaluates parameter combinations directly on the test set.", False, "GridSearchCV tunes parameters using training set cross-validation, reserving the test set for final evaluation."),
        ("Believing that high training accuracy combined with low test accuracy indicates an underfitting model.", False, "High training accuracy with low test accuracy indicates OVERFITTING (high variance), not underfitting."),
        ("Confusing ROC curves (TPR vs FPR) with Precision-Recall curves (Precision vs Recall).", False, "ROC curves plot TPR against FPR across thresholds; PR curves plot Precision against Recall."),

        ("Assuming that raising the classification decision threshold from 0.5 to 0.8 always increases recall.", False, "Raising the probability threshold requires stronger confidence for positive calls, which DECREASES recall."),
        ("Believing that StratifiedKFold alters class proportions in each fold to make classes 50/50 balanced.", False, "StratifiedKFold preserves the ORIGINAL dataset class proportions in each fold, not a 50/50 balance."),
        ("Confusing validation curves (score vs hyperparameter) with learning curves (score vs sample size N).", False, "Validation curves evaluate hyperparameter impact; learning curves evaluate training sample size N impact."),
        ("Assuming that cross_val_score modifies the input classifier object and saves fold model weights.", False, "cross_val_score evaluates temporary clones of the estimator across folds without modifying the original input estimator."),
        ("Believing that Macro Average in classification_report weights class metrics by sample support.", False, "Macro average computes an unweighted mean across classes; Weighted average weights class metrics by support."),
        ("Confusing Sensitivity (Recall) with Specificity (True Negative Rate).", False, "Sensitivity/Recall is TP / (TP+FN); Specificity is TN / (TN+FP)."),
        ("Assuming that a model with 100% precision catches every actual positive instance in the dataset.", False, "100% precision means zero false positives, but the model may miss many positive instances (yielding low recall)."),
        ("Believing that LeaveOneOut cross-validation is computationally fast for 500,000 samples.", False, "LeaveOneOut fits N separate models (500,000 model fits here), making it extremely slow for large datasets."),
        ("Confusing FPR formula FP/(FP+TN) with Precision formula TP/(TP+FP).", False, "FPR measures false alarms among actual negatives; Precision measures accuracy among positive predictions."),
        ("Assuming that GridSearchCV parameter grid param_grid accepts a list of fitted model instances.", False, "param_grid accepts a dictionary mapping hyperparameter string names to lists of candidate parameter values."),

        ("Believing that PR curves are inferior to ROC curves for evaluating severely imbalanced datasets.", False, "PR curves are specifically RECOMMENDED for imbalanced data because they focus on the minority positive class without TN dampening."),
        ("Confusing scikit-learn predict() discrete labels with predict_proba() continuous probabilities.", False, "predict() outputs discrete class labels (0/1); predict_proba() outputs continuous class probability estimates."),
        ("Assuming that K-Fold cross-validation with K=5 trains a total of 1 model.", False, "K-Fold with K=5 trains exactly 5 separate model instances (one per fold iteration)."),
        ("Believing that a learning curve showing high train score and low validation score needs higher model complexity.", False, "A persistent gap between high train and low validation score indicates OVERFITTING, which requires regularization or simpler models."),
        ("Confusing scikit-learn accuracy_score(y_true, y_pred) argument order.", False, "accuracy_score expects ground truth y_true as first argument and predictions y_pred as second argument."),
        ("Assuming that setting refit=False in GridSearchCV still exposes grid.best_estimator_.", False, "When refit=False, GridSearchCV skips final model fitting and best_estimator_ is NOT generated."),
        ("Believing that increasing training sample size N always worsens model validation performance.", False, "Increasing training sample size N generally improves generalization and raises validation scores."),
        ("Confusing high bias (underfitting) with high variance (overfitting) in error diagnosis.", False, "High bias causes underfitting (poor train and test scores); high variance causes overfitting (high train, poor test scores)."),
        ("Assuming that roc_auc_score function can accept raw text labels without binary/probability conversion.", False, "roc_auc_score requires numerical binary target labels and continuous probability estimates."),
        ("Believing that model evaluation can be skipped if training score reaches 100%.", False, "100% training score often indicates severe memorization/overfitting, making rigorous test set evaluation essential."),

        ("Confusing support in classification_report with classification accuracy percentage.", False, "Support represents the actual COUNT of ground truth instances in a class, not an accuracy percentage."),
        ("Assuming that StratifiedKFold can be used on continuous numerical target variables in regression.", False, "StratifiedKFold requires discrete classification labels y; continuous regression targets use standard KFold."),
        ("Believing that an AUC-ROC score of 1.0 means the model makes 50% prediction errors.", False, "AUC-ROC of 1.0 represents a perfect classification model with ZERO prediction errors."),
        ("Confusing F1-score with Accuracy on balanced classification datasets.", False, "Accuracy measures overall correct fraction (TP+TN)/Total; F1-score measures harmonic balance 2*P*R/(P+R)."),
        ("Assuming that cross_val_score scoring='roc_auc' accepts discrete binary predictions y_pred.", False, "scoring='roc_auc' requires estimators that implement predict_proba or decision_function to generate continuous probabilities."),
        ("Believing that lowering the classification decision threshold always decreases recall.", False, "Lowering the decision threshold makes positive calls easier, which INCREASES (or maintains) recall."),
        ("Confusing scikit-learn f1_score average='macro' with average='weighted'.", False, "average='macro' averages class F1-scores equally; average='weighted' weights class F1-scores by class support."),
        ("Assuming that random guessing yields an AUC-ROC curve hugging the top-left corner.", False, "Random guessing yields a straight diagonal line from (0,0) to (1,1) with AUC = 0.5."),
        ("Believing that model.score() on a scikit-learn classifier computes F1-score by default.", False, "Scikit-learn classifier model.score() computes mean ACCURACY by default."),
        ("Confusing test set evaluation with cross-validation fold evaluation during hyperparameter tuning.", False, "Cross-validation tunes parameters on training folds; test set provides final independent validation."),

        {"id": "TP4_181", "tp": 4, "category": "trap", "question": "Assuming that precision_score equals recall_score when False Positives equal False Negatives.", "answer": True, "explanation": "If FP == FN, then TP / (TP + FP) equals TP / (TP + FN), making precision equal to recall."},
        {"id": "TP4_182", "tp": 4, "category": "trap", "question": "Believing that GridSearchCV cannot optimize multiple hyperparameters simultaneously.", "answer": False, "explanation": "GridSearchCV evaluates all combinations of multiple specified hyperparameters simultaneously across a grid matrix."},
        {"id": "TP4_183", "tp": 4, "category": "trap", "question": "Confusing Type I error (False Positive) with Type II error (False Negative).", "answer": False, "explanation": "Type I error is a False Positive (incorrectly flagging negative as positive); Type II error is a False Negative (missing a true positive)."},
        {"id": "TP4_184", "tp": 4, "category": "trap", "question": "Assuming that LeaveOneOut cross-validation uses test_size=0.5 in each fold.", "answer": False, "explanation": "LeaveOneOut uses exactly 1 sample for validation (test_size = 1/N) and N-1 samples for training in each fold."},
        {"id": "TP4_185", "tp": 4, "category": "trap", "question": "Believing that a confusion matrix can only be constructed for binary classification problems.", "answer": False, "explanation": "Confusion matrices extend naturally to multi-class problems as N x N matrices comparing actual vs predicted classes."},
        {"id": "TP4_186", "tp": 4, "category": "trap", "question": "Confusing training score curves with test score curves on a learning curve plot.", "answer": False, "explanation": "Training score curves measure performance on training subsets; test/validation curves measure generalization on validation folds."},
        {"id": "TP4_187", "tp": 4, "category": "trap", "question": "Assuming that zero false negatives results in a Recall score of 1.0 (100%).", "answer": True, "explanation": "Recall = TP / (TP + FN); if FN = 0, Recall = TP / TP = 1.0 (100%)."},
        {"id": "TP4_188", "tp": 4, "category": "trap", "question": "Believing that cross-validation eliminates the need for an independent test set completely.", "answer": False, "explanation": "An independent test set is still required to provide unbiased final validation after using cross-validation for parameter tuning."},
        {"id": "TP4_189", "tp": 4, "category": "trap", "question": "Confusing ROC AUC score calculation with raw confusion matrix accuracy.", "answer": False, "explanation": "ROC AUC calculates area under probability threshold curves; accuracy calculates discrete prediction matches."},
        {"id": "TP4_190", "tp": 4, "category": "trap", "question": "Assuming that raising the probability threshold to 1.0 guarantees catching all true positive cases.", "answer": False, "explanation": "Threshold of 1.0 requires 100% confidence for positive calls, missing most positive cases and driving recall toward 0."},

        {"id": "TP4_191", "tp": 4, "category": "trap", "question": "Believing that scikit-learn f1_score returns a 2x2 matrix object.", "answer": False, "explanation": "f1_score returns a single scalar float value (or array of per-class floats), not a 2x2 matrix."},
        {"id": "TP4_192", "tp": 4, "category": "trap", "question": "Confusing KFold n_splits parameter with total dataset sample count N.", "answer": False, "explanation": "n_splits specifies the number of partition folds K (e.g., 5 or 10), not the total dataset sample count N."},
        {"id": "TP4_193", "tp": 4, "category": "trap", "question": "Assuming that high bias in a model is resolved by dropping training data.", "answer": False, "explanation": "High bias (underfitting) requires increasing model complexity or feature richness, not dropping training data."},
        {"id": "TP4_194", "tp": 4, "category": "trap", "question": "Believing that GridSearchCV param_grid values must be numerical floats exclusively.", "answer": False, "explanation": "param_grid supports any hyperparameter types, including strings (e.g., metrics, kernels) and booleans."},
        {"id": "TP4_195", "tp": 4, "category": "trap", "question": "Confusing precision_score with recall_score when false alarms must be minimized.", "answer": False, "explanation": "Minimizing false alarms (False Positives) prioritizes Precision; catching all true cases (minimizing FN) prioritizes Recall."},
        {"id": "TP4_196", "tp": 4, "category": "trap", "question": "Assuming that a model with high variance performs poorly on training data.", "answer": False, "explanation": "High variance (overfitting) models perform EXCELLENTLY on training data but poorly on test data."},
        {"id": "TP4_197", "tp": 4, "category": "trap", "question": "Believing that ROC curves can be computed without probability predictions or decision scores.", "answer": False, "explanation": "ROC curves evaluate performance across varying threshold cutoffs, requiring continuous probability or decision scores."},
        {"id": "TP4_198", "tp": 4, "category": "trap", "question": "Confusing StratifiedKFold with ShuffleSplit in scikit-learn.", "answer": False, "explanation": "StratifiedKFold splits data into K non-overlapping folds preserving class ratios; ShuffleSplit generates independent random train/test iterations."},
        {"id": "TP4_199", "tp": 4, "category": "trap", "question": "Assuming that F1-score is always greater than both Precision and Recall.", "answer": False, "explanation": "F1-score is the harmonic mean of Precision and Recall and lies BETWEEN them (or equals them if P == R)."},
        {"id": "TP4_200", "tp": 4, "category": "trap", "question": "Believing that model evaluation metrics guarantee an algorithm will perform flawlessly on future out-of-distribution data.", "answer": False, "explanation": "Evaluation metrics measure performance on sampled test data; future out-of-distribution data shifts can still degrade performance."}
    ]

    # Convert tuple rows to dicts for 141..180
    for i, item in enumerate(trap_data[:40], 141):
        q, a, exp = item
        questions.append({
            "id": f"TP4_{i:03d}",
            "tp": 4,
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
    qs = get_tp4_questions()
    print(f"TP4 Total: {len(qs)}")
    print("Normal:", sum(1 for q in qs if q["category"] == "normal"))
    print("Tricky:", sum(1 for q in qs if q["category"] == "tricky"))
    print("Trap:", sum(1 for q in qs if q["category"] == "trap"))
