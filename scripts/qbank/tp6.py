# TP 6 — Unsupervised Learning, Clustering & Association Rules (200 Questions: 90 Normal, 50 Tricky, 60 Trap)
# ABSOLUTE PROHIBITION: ZERO DBSCAN, ZERO K-MEANS++

def get_tp6_questions():
    questions = []
    
    # ---------------------------------------------------------
    # 90 NORMAL QUESTIONS (TP6_001 to TP6_090)
    # ---------------------------------------------------------
    normal_data = [
        # Unsupervised Learning & Clustering Overview (Easy/Medium)
        ("Unsupervised learning algorithms discover underlying structures, patterns, or groupings in unlabeled datasets without explicit target labels.", True, "Unsupervised learning operates on unlabeled feature matrix X to discover intrinsic data geometry and clusters."),
        ("Clustering is an unsupervised learning technique that partitions data observations into distinct groups based on feature similarity.", True, "Clustering groups similar samples together while ensuring samples in different clusters are distinct."),
        ("In clustering, data points within the same cluster should exhibit high intra-cluster similarity.", True, "Effective clustering maximizes similarity between points assigned to the same cluster group."),
        ("Data points assigned to different clusters should exhibit high inter-cluster dissimilarity.", True, "Effective clustering maximizes dissimilarity between distinct cluster groups."),
        ("Unlike supervised classification, clustering operates without pre-existing target outcome labels y.", True, "Clustering algorithms learn structural patterns directly from feature matrix X without target label guidance."),
        ("Feature scaling with StandardScaler is important before clustering when features possess disparate numerical units.", True, "Distance-based clustering algorithms are sensitive to feature scales; standardizing ensures equal feature weighting."),
        ("In scikit-learn, clustering models implement fit() to learn cluster assignments and labels_ to store cluster IDs.", True, "Clustering estimators learn partition structures during fit() and store sample cluster assignments in labels_."),
        ("Clustering is widely applied in business for customer segmentation based on purchasing behavior.", True, "Grouping customers with similar purchasing habits enables targeted marketing campaigns."),
        ("Evaluation of clustering algorithms often relies on intrinsic metrics because ground truth labels are absent.", True, "Without target labels, metrics like Silhouette score evaluate cluster compactness and separation intrinsically."),
        ("Discarding target labels from labeled datasets allows evaluating how well unsupervised clustering recovers true groups.", True, "Testing clustering algorithms on unlabeled datasets like Iris measures cluster alignment with physical domain groups."),

        # K-Means Clustering (Medium)
        ("K-Means is a partition-based algorithm that divides N observations into K disjoint clusters.", True, "K-Means partitions data into K specified clusters by assigning samples to the nearest cluster centroid."),
        ("In scikit-learn, the n_clusters hyperparameter specifies the target number of clusters K for KMeans.", True, "n_clusters sets the exact number of cluster centroids K to construct."),
        ("K-Means iteratively updates cluster centroids to minimize the within-cluster sum-of-squares (inertia).", True, "K-Means alternates between assigning samples to nearest centroids and recalculating centroid means to minimize inertia."),
        ("Inertia in KMeans represents the sum of squared Euclidean distances from samples to their assigned cluster centroid.", True, "Inertia quantifies internal cluster compactness as the sum of squared distances to cluster centers."),
        ("The kmeans.cluster_centers_ attribute stores the final coordinate positions of all K cluster centroids.", True, "cluster_centers_ holds the fitted mean coordinates of cluster centers in feature space."),
        ("The Elbow Method helps identify an optimal K by plotting inertia against K and searching for a sharp bend point.", True, "The Elbow plot highlights where adding more clusters yields diminishing reductions in within-cluster inertia."),
        ("Inertia monotonically decreases as the number of clusters K increases toward sample size N.", True, "As K increases, cluster boundaries shrink, reaching 0 inertia when K equals total sample count N."),
        ("K-Means assumes that clusters are spherical and isotropic in feature space.", True, "K-Means distance calculations assume convex, spherical cluster geometries of equal variance."),
        ("Standardizing features before running K-Means prevents features with large ranges from dominating centroid calculations.", True, "Unscaled features warp Euclidean centroid distance calculations in K-Means."),
        ("In scikit-learn, kmeans.fit_transform(X) returns the Euclidean distance from each sample to every cluster centroid.", True, "fit_transform() in KMeans outputs an N x K matrix of sample-to-centroid spatial distances."),

        # Silhouette Analysis & Clustering Metrics (Medium/Hard)
        ("Silhouette Analysis measures how well-separated and compact individual clusters are.", True, "Silhouette analysis quantifies how close each point is to its own cluster compared to neighboring clusters."),
        ("The Silhouette Coefficient for a sample ranges from -1.0 to +1.0.", True, "Silhouette scores range from -1.0 (incorrect cluster assignment) to +1.0 (highly dense, well-separated cluster)."),
        ("A Silhouette score close to +1.0 indicates that a sample is well-matched to its own cluster and far from neighboring clusters.", True, "High positive Silhouette scores signify dense, well-separated cluster partitioning."),
        ("A Silhouette score close to 0.0 indicates that a sample lies near the decision boundary between two clusters.", True, "Silhouette scores near zero indicate samples sitting on overlapping cluster boundaries."),
        ("A negative Silhouette score indicates that a sample may have been assigned to the wrong cluster.", True, "Negative scores mean a sample is closer on average to a neighboring cluster than to its assigned cluster."),
        ("In scikit-learn, silhouette_score(X, labels) calculates the mean Silhouette Coefficient across all samples.", True, "silhouette_score computes the overall average Silhouette value for a dataset and label assignment."),
        ("The silhouette_samples(X, labels) function calculates the individual Silhouette score for each sample row.", True, "silhouette_samples outputs an array of per-sample Silhouette coefficients for detailed plotting."),
        ("Higher overall mean Silhouette scores generally indicate better clustering quality.", True, "Maximizing mean Silhouette score serves as a key criterion for selecting optimal cluster count K."),
        ("Silhouette Analysis can be used alongside the Elbow Method to validate the optimal number of clusters K.", True, "Combining Silhouette scores and Elbow plots provides strong intrinsic evidence for cluster count selection."),
        ("Calculating Silhouette scores requires computing pairwise distances between all dataset samples.", True, "Silhouette formulas evaluate average intra-cluster distance a(i) and nearest-cluster distance b(i) for every point."),

        # Hierarchical Agglomerative Clustering (Medium/Hard)
        ("Hierarchical clustering builds a nested tree-like hierarchy of clusters.", True, "Hierarchical algorithms create tree structures representing sequential cluster mergers or splits."),
        ("Agglomerative clustering is a bottom-up approach where each sample starts in its own cluster and pairs merge successively.", True, "Agglomerative clustering begins with N single-element clusters and iteratively merges the closest cluster pairs."),
        ("In scikit-learn, AgglomerativeClustering implements bottom-up hierarchical clustering.", True, "AgglomerativeClustering performs iterative bottom-up cluster merging based on specified linkage criteria."),
        ("The linkage hyperparameter defines the distance metric used to determine which cluster pairs should merge.", True, "Linkage criteria (e.g., ward, complete, average, single) define how distance between cluster sets is computed."),
        ("Ward linkage minimizes the within-cluster variance when merging two candidate clusters.", True, "Ward's method merges cluster pairs that yield the smallest increase in total within-cluster variance."),
        ("Ward linkage is generally preferred for standard continuous numerical datasets.", True, "Ward's variance-minimizing criterion produces compact, balanced clusters on continuous numerical features."),
        ("Complete linkage measures the distance between cluster pairs as the MAXIMUM distance between any single sample pair.", True, "Complete linkage considers the farthest distance between elements of two clusters."),
        ("Single linkage measures the distance between cluster pairs as the MINIMUM distance between any single sample pair.", True, "Single linkage considers the closest distance between elements of two clusters, capable of following non-spherical chains."),
        ("Average linkage measures the distance between cluster pairs as the average distance between all sample pairs.", True, "Average linkage averages pairwise distances between all observations in the two candidate clusters."),
        ("A dendrogram is a tree diagram that visualizes the sequential merges and distance thresholds of hierarchical clustering.", True, "Dendrograms plot hierarchical tree branches where height represents the distance at which clusters merged."),

        # Dendrograms & Scipy Linkage (Medium/Hard)
        ("In Python, scipy.cluster.hierarchy.linkage calculates the hierarchical linkage matrix used to plot dendrograms.", True, "scipy linkage() generates the merge history matrix required by dendrogram()."),
        ("In SciPy, dendrogram(Z) renders a visual tree diagram from a computed linkage matrix Z.", True, "dendrogram() draws the hierarchical tree layout displaying cluster merge distances."),
        ("Cutting a dendrogram with a horizontal line at a specified height determines the number of final clusters.", True, "Intersecting dendrogram branches with a horizontal distance line cuts the tree into K discrete clusters."),
        ("Dendrogram tree branch height represents the dissimilarity distance at which two sub-clusters were merged.", True, "Higher vertical branches indicate that merged clusters were farther apart in distance space."),
        ("Ward linkage in SciPy requires input features to be numerical continuous variables.", True, "Ward's variance calculation assumes Euclidean distance metrics on continuous numerical features."),
        ("Hierarchical clustering does not require specifying cluster count K prior to computing the full tree hierarchy.", True, "Agglomerative clustering builds the complete merge tree from 1 to N clusters; K is selected by cutting the tree."),
        ("Truncating a complex dendrogram (truncate_mode='lastp') simplifies visualization for large datasets.", True, "Truncation condenses deep dendrogram trees to display only the top p merged cluster nodes."),
        ("The cophenetic correlation coefficient measures how faithfully a dendrogram preserves pairwise sample distances.", True, "Cophenetic correlation quantifies the alignment between dendrogram merge heights and original pairwise distances."),
        ("AgglomerativeClustering(n_clusters=3, linkage='ward') segments data into exactly 3 hierarchical clusters.", True, "Setting n_clusters=3 cuts the hierarchical tree to return 3 discrete cluster label assignments."),
        ("Agglomerative clustering requires storing or computing pairwise distance matrices, making it memory-intensive for huge N.", True, "Bottom-up hierarchical merging evaluates N x N distance matrices, scaling quadratically O(N^2) in memory."),

        # Association Rules & Market Basket Analysis (Medium)
        ("Association rule mining uncovers interesting relationships and co-occurrence patterns in transactional datasets.", True, "Association rules discover items that frequently occur together in large transaction databases."),
        ("An association rule is typically written in the antecedent-consequent form X => Y.", True, "Rules express conditional co-occurrence: if antecedent itemset X is present, consequent itemset Y is likely present."),
        ("Support measures the proportion of total transactions that contain a given itemset.", True, "Support(X) = (Transactions containing X) / (Total Transactions) measures itemset frequency."),
        ("Confidence measures the conditional probability that a transaction contains Y given that it contains X.", True, "Confidence(X => Y) = Support(X U Y) / Support(X) measures rule reliability."),
        ("Lift measures how much more frequently X and Y occur together than would be expected if they were statistically independent.", True, "Lift(X => Y) = Support(X U Y) / (Support(X) * Support(Y)) measures association strength."),
        ("A Lift score greater than 1.0 indicates a positive association between itemset X and itemset Y.", True, "Lift > 1.0 signifies that item X and item Y co-occur more frequently than random chance."),
        ("A Lift score equal to 1.0 indicates that itemset X and itemset Y are statistically independent.", True, "Lift = 1.0 means occurrence of X provides no information about occurrence of Y."),
        ("A Lift score less than 1.0 indicates a negative association (substitution effect) between itemsets.", True, "Lift < 1.0 signifies that presence of X makes occurrence of Y less likely than random chance."),
        ("Market Basket Analysis is a classic application of association rules to identify products purchased together.", True, "Retailers analyze checkout transactions to identify item combinations for product placement and cross-selling."),
        ("TransactionEncoder in mlxtend converts a list of transactional item lists into a boolean One-Hot DataFrame.", True, "TransactionEncoder transforms raw item lists (e.g., [['bread', 'milk']]) into a boolean item matrix."),

        # Frequent Itemset Algorithms: Apriori & FP-Growth (Medium/Hard)
        ("The Apriori algorithm mines frequent itemsets by enforcing the downward closure property of support.", True, "Apriori principle states that all subsets of a frequent itemset must also be frequent."),
        ("According to the Apriori principle, if an itemset is infrequent, all of its supersets must also be infrequent.", True, "If itemset {A, B} is infrequent, any larger set containing {A, B} cannot satisfy minimum support."),
        ("The downward closure property allows Apriori to prune candidate itemsets efficiently without counting all permutations.", True, "Pruning infrequent itemset supersets dramatically shrinks the search space of candidate itemsets."),
        ("In mlxtend, apriori(df, min_support=0.4, use_colnames=True) generates itemsets satisfying at least 40% support.", True, "apriori() extracts itemsets whose support meets or exceeds the specified min_support threshold."),
        ("FP-Growth (Frequent Pattern Growth) mines frequent itemsets without candidate generation by constructing an FP-Tree.", True, "FP-Growth compresses transactions into an FP-Tree structure, avoiding costly Apriori candidate generation passes."),
        ("FP-Growth is generally faster than Apriori on dense datasets with low minimum support thresholds.", True, "FP-Tree compression allows FP-Growth to scale much better than Apriori on large, dense transaction sets."),
        ("In mlxtend, association_rules(frequent_itemsets, metric='confidence', min_threshold=0.6) extracts rules.", True, "association_rules() filters rule combinations generated from frequent itemsets using metric thresholds."),
        ("The antecedents column in an association rules DataFrame lists the IF itemset conditions.", True, "Antecedents represent the left-hand itemset X in rule X => Y."),
        ("The consequents column in an association rules DataFrame lists the THEN itemset outcomes.", True, "Consequents represent the right-hand itemset Y in rule X => Y."),
        ("Mining association rules requires setting both a minimum support threshold and a minimum confidence threshold.", True, "Min support isolates frequent itemsets first; min confidence filters strong reliable rules second.")
    ]

    for i, (q, a, exp) in enumerate(normal_data, 1):
        questions.append({
            "id": f"TP6_{i:03d}",
            "tp": 6,
            "category": "normal",
            "question": q,
            "answer": a,
            "explanation": exp
        })

    # Add 20 additional normal questions to reach 90 (TP6_071 to TP6_090)
    extra_normal = [
        ("K-Means requires specifying the number of clusters K before running the algorithm.", True, "K-Means is a parametric partitioning algorithm requiring explicit pre-specification of K."),
        ("Inertia is zero when K equals the total number of data samples N in K-Means.", True, "When K = N, every sample becomes its own centroid, resulting in zero distance inertia."),
        ("Silhouette score can be computed for any clustering assignment regardless of the underlying algorithm.", True, "Silhouette score evaluates sample distances to assigned clusters, making it model-agnostic."),
        ("Ward linkage minimizes the total within-cluster variance when building agglomerative hierarchies.", True, "Ward's criterion merges cluster pairs that yield the minimum increase in within-cluster variance."),
        ("Dendrogram horizontal line cuts determine cluster assignments in agglomerative clustering.", True, "Intersecting dendrogram branches with a horizontal distance threshold defines discrete clusters."),
        ("Confidence in association rules measures the conditional probability P(Y|X).", True, "Confidence(X => Y) = P(Y|X) measures how often Y appears in transactions containing X."),
        ("Support for a rule X => Y is equal to the support of the combined itemset X U Y.", True, "Support(X => Y) = P(X U Y) represents the transaction fraction containing both itemsets."),
        ("Lift values above 1.0 signify that items in the rule appear together more often than expected by chance.", True, "Lift > 1.0 indicates a positive co-occurrence relationship beyond independent random chance."),
        ("TransactionEncoder converts list-of-lists dataset formats into boolean DataFrames.", True, "TransactionEncoder transforms raw purchase lists into boolean dummy indicator matrices."),
        ("The Apriori algorithm iteratively generates candidate itemsets of size k from frequent itemsets of size k-1.", True, "Apriori builds candidate k-itemsets by joining frequent (k-1)-itemsets."),

        ("FP-Growth avoids candidate itemset generation by compressing data into a compact FP-Tree.", True, "FP-Growth mines frequent patterns directly from the FP-Tree without generating candidate itemsets."),
        ("Inertia decreases monotonically as K increases in K-Means.", True, "Adding more cluster centroids strictly reduces or maintains within-cluster distance sums."),
        ("Hierarchical clustering dendrograms visualize sample distance merges as tree branches.", True, "Dendrogram branch heights correspond to the dissimilarity distance at which sub-clusters merged."),
        ("K-Means cluster centroids represent the mean coordinate vector of all samples assigned to that cluster.", True, "Centroid coordinates are calculated as the component-wise average of all cluster members."),
        ("In scikit-learn, silhouette_score requires both the feature matrix X and cluster labels.", True, "silhouette_score computes sample-to-cluster spatial distances using feature matrix X and labels."),
        ("Single linkage hierarchical clustering merges clusters based on the minimum distance between any two points.", True, "Single linkage evaluates the shortest pairwise distance between elements of two candidate clusters."),
        ("Association rule mining can be applied to web clickstream analysis and medical co-occurrence diagnosis.", True, "Co-occurrence pattern mining extends to website page views, medical symptoms, and bio-sequences."),
        ("If Lift = 1.0, knowing that a customer bought item X provides no information about whether they will buy item Y.", True, "Lift = 1.0 means X and Y are statistically independent; purchasing X does not alter odds of purchasing Y."),
        ("K-Means performs well on compact, well-separated, spherical clusters of similar size.", True, "K-Means Euclidean distance optimization is ideal for convex, spherical, equal-variance clusters."),
        ("In agglomerative clustering, every observation begins in its own isolated cluster.", True, "Agglomerative hierarchical clustering initializes with N single-observation clusters.")
    ]

    for i, (q, a, exp) in enumerate(extra_normal, 71):
        questions.append({
            "id": f"TP6_{i:03d}",
            "tp": 6,
            "category": "normal",
            "question": q,
            "answer": a,
            "explanation": exp
        })

    # ---------------------------------------------------------
    # 50 TRICKY QUESTIONS (TP6_091 to TP6_140)
    # ---------------------------------------------------------
    tricky_data = [
        ("K-Means clustering guarantees finding the global optimal centroid positioning on every execution.", False, "K-Means converges to local optima depending on initial centroid placement; multiple random restarts (n_init) are used."),
        ("The Elbow Method provides an exact, mathematically definitive automated threshold for setting K without human judgment.", False, "The Elbow Method relies on visual inspection of the inertia curve elbow, which can be ambiguous or gradual."),
        ("A Silhouette score of -0.8 indicates an optimal, highly compact cluster assignment.", False, "Negative Silhouette scores indicate bad cluster assignments where samples are closer to neighboring clusters."),
        ("Hierarchical AgglomerativeClustering automatically deletes outlier rows during tree construction.", False, "Agglomerative clustering merges every single sample into the hierarchy without dropping outliers."),
        ("Single linkage hierarchical clustering is completely immune to the chaining effect.", False, "Single linkage is famously vulnerable to the chaining effect, forming long string-like clusters connected by single intermediate points."),
        ("Ward linkage in hierarchical clustering can be used directly with Manhattan (L1) distance metrics.", False, "Ward's method strictly requires Euclidean distance (L2 norm) because it minimizes within-cluster variance."),
        ("Confidence in association rules is a symmetric metric where Confidence(X => Y) always equals Confidence(Y => X).", False, "Confidence(X => Y) = Support(X U Y)/Support(X), whereas Confidence(Y => X) = Support(X U Y)/Support(Y); they differ unless Support(X) == Support(Y)."),
        ("A Lift score of 0.0 indicates a strong positive co-occurrence relationship between items.", False, "Lift = 0.0 means items NEVER co-occur (Support(X U Y) = 0); strong positive association requires Lift > 1.0."),
        ("The Apriori principle states that if an itemset is frequent, all of its subsets must be infrequent.", False, "The Apriori principle states that if an itemset is frequent, all of its subsets MUST ALSO BE FREQUENT."),
        ("K-Means clustering performs exceptionally well on complex non-spherical crescent moon shapes.", False, "K-Means assumes spherical isotropic clusters and fails to segment non-spherical crescent moon geometries correctly."),

        ("Increasing K in K-Means always increases the within-cluster sum of squares (inertia).", False, "Increasing K strictly DECREASES (or maintains) within-cluster inertia as cluster centroids get closer to samples."),
        ("In scikit-learn, silhouette_score can be calculated without providing cluster label assignments.", False, "silhouette_score strictly requires cluster label assignments to evaluate intra-cluster vs inter-cluster distances."),
        ("Agglomerative clustering requires specifying cluster count K prior to generating the dendrogram linkage matrix.", False, "The dendrogram linkage matrix is computed across all N-1 merges from 1 to N clusters BEFORE choosing K."),
        ("Support for an association rule X => Y is calculated as Support(X) divided by Support(Y).", False, "Support(X => Y) is the proportion of total transactions containing BOTH X and Y: Support(X U Y)."),
        ("In FP-Growth, candidate itemsets are generated and tested iteratively in multiple passes over disk data.", False, "FP-Growth eliminates candidate generation by compressing transaction data into a memory FP-Tree structure."),
        ("A Silhouette score of +1.0 indicates that all clusters overlap completely with each other.", False, "Silhouette score of +1.0 indicates perfectly dense, non-overlapping, well-separated clusters."),
        ("Complete linkage merges clusters based on the shortest distance between any single sample pair.", False, "Complete linkage merges based on the FARTHEST (maximum) distance between sample pairs; Single linkage uses shortest distance."),
        ("In K-Means, cluster centroids must correspond to actual real sample points present in the dataset.", False, "K-Means centroids represent arithmetic mean coordinate vectors and rarely coincide with actual sample data points."),
        ("TransactionEncoder in mlxtend accepts standard 2D NumPy arrays of continuous float values.", False, "TransactionEncoder expects a list of item lists (e.g., [['bread', 'milk']]) representing transaction item sets."),
        ("Lift measures rule confidence divided by total dataset row count.", False, "Lift(X => Y) = Confidence(X => Y) / Support(Y) = Support(X U Y) / (Support(X) * Support(Y))."),

        ("In scikit-learn KMeans, fit_transform(X) returns predicted integer cluster labels for each sample.", False, "fit_transform(X) in KMeans returns an N x K matrix of spatial DISTANCES to centroids; integer labels are stored in labels_."),
        ("Dendrogram vertical branch height in SciPy represents the number of samples inside the merged cluster.", False, "Vertical branch height represents the DISSIMILARITY DISTANCE at which two sub-clusters merged, not sample count."),
        ("An itemset with 10% support is guaranteed to generate association rules with 100% confidence.", False, "Support and confidence are separate metrics; a frequent itemset can produce rules with low confidence if antecedents occur without consequents."),
        ("K-Means is completely immune to initial centroid seed positions when n_init=1.", False, "With n_init=1, K-Means is highly sensitive to initial random centroid placement and can converge to poor local optima."),
        ("In agglomerative clustering, setting distance_threshold=0 merges all samples into a single global cluster.", False, "Setting distance_threshold=0 stops merging immediately, leaving every sample in its own isolated cluster."),
        ("Apriori algorithm efficiency improves as the minimum support threshold (min_support) approaches zero.", False, "As min_support approaches 0, candidate itemsets explode exponentially, drastically slowing down Apriori."),
        ("Confidence equal to 0.8 means that 80% of all dataset transactions contain both itemset X and itemset Y.", False, "80% of transactions containing X U Y describes SUPPORT = 0.8; Confidence = 0.8 means 80% of transactions THAT CONTAIN X also contain Y."),
        ("Average linkage measures the minimum distance between cluster centroids exclusively.", False, "Average linkage computes the average of ALL pairwise sample distances between two clusters, not just centroid distance."),
        ("Inertia in K-Means can take negative values if dataset features contain negative numbers.", False, "Inertia is a sum of SQUARED Euclidean distances and is strictly non-negative (>= 0)."),
        ("FP-Growth produces completely different frequent itemsets compared to Apriori on the same dataset and support threshold.", False, "FP-Growth and Apriori are mathematically guaranteed to mine the EXACT SAME frequent itemsets for identical support thresholds.")
    ]

    for i, (q, a, exp) in enumerate(tricky_data, 91):
        questions.append({
            "id": f"TP6_{i:03d}",
            "tp": 6,
            "category": "tricky",
            "question": q,
            "answer": a,
            "explanation": exp
        })

    # Add 20 additional tricky questions to complete 50 (TP6_121 to TP6_140)
    extra_tricky = [
        ("The Silhouette Coefficient of a dataset with only K=1 cluster assigned to all samples is equal to +1.0.", False, "Silhouette score requires at least K=2 clusters to evaluate neighbor cluster distance b(i); for K=1 it is undefined or 0."),
        ("Ward linkage in AgglomerativeClustering minimizes the maximum pairwise distance between points.", False, "Ward linkage minimizes within-cluster variance; Complete linkage minimizes maximum pairwise distance."),
        ("If Lift(X => Y) = 2.5, then Lift(Y => X) must equal 0.4.", False, "Lift is symmetric: Lift(X => Y) = Support(X U Y)/(Support(X)*Support(Y)) = Lift(Y => X) = 2.5."),
        ("K-Means requires target labels y during fit(X, y) to position cluster centroids accurately.", False, "K-Means is an unsupervised algorithm that ignores target y during fit(X), partitioning data based solely on feature matrix X."),
        ("In SciPy dendrogram(Z), setting color_threshold=0 colors all tree branches with different distinct rainbow colors.", False, "color_threshold=0 colors all tree branches below the cut threshold with a single default color."),
        ("A transaction dataset with 5 unique items can generate at most 5 total association rules.", False, "5 items generate 2^5 - 1 = 31 candidate itemsets and dozens of candidate association rules."),
        ("In scikit-learn, KMeans(n_clusters=3).fit(X) modifies original feature matrix X in place.", False, "fit() computes internal centroids and label attributes without modifying input feature matrix X."),
        ("Higher values of min_support in Apriori increase the total number of mined frequent itemsets.", False, "Higher min_support enforces a stricter frequency threshold, REDUCING the number of qualified frequent itemsets."),
        ("Cophenetic correlation coefficient of 0.0 indicates a dendrogram that perfectly preserves original sample distances.", False, "Cophenetic correlation near 1.0 indicates perfect distance preservation; 0.0 indicates no correlation."),
        ("K-Means inertia increases as dataset features are standardized with StandardScaler.", False, "Standardizing rescales feature variances to 1.0, which typically REDUCES numeric distance magnitudes and inertia."),

        ("Association rule Lift metric depends strictly on the total order in which transactions were recorded.", False, "Lift evaluates aggregate transaction frequency counts, making it completely invariant to transaction record order."),
        ("AgglomerativeClustering linkage='single' is robust against noisy points bridging separate clusters.", False, "Single linkage suffers from chaining, where single noisy points bridge distinct clusters into one."),
        ("Inertia can be used to compare clustering quality across datasets with different numbers of features.", False, "Inertia depends on feature dimensions and scale, making raw inertia unsuited for comparing different datasets."),
        ("The Apriori algorithm requires transaction data to be formatted as a scipy sparse matrix of floats.", False, "Apriori in mlxtend requires a boolean pandas DataFrame of item occurrence flags."),
        ("In K-Means, setting n_init=10 runs 10 parallel iterations on 10 different dataset feature subsets.", False, "n_init=10 runs K-Means 10 times with different random CENTROID SEEDS on the full dataset, returning the best fit."),
        ("Confidence metric in association rules accounts for the baseline occurrence probability of consequent Y.", False, "Confidence ignores baseline P(Y); Lift scales confidence by P(Y) to account for baseline consequent frequency."),
        ("Dendrogram tree branches extend horizontally to represent cluster dissimilarity in standard SciPy plots.", False, "In standard vertical SciPy dendrograms, VERTICAL branch height represents dissimilarity distance."),
        ("K-Means clustering automatically determines the optimal number of clusters K without user input.", False, "K-Means requires the user to explicitly specify n_clusters hyperparameter K."),
        ("Support for itemset {bread, milk} is always greater than Support for itemset {bread}.", False, "By downward closure, adding items can only decrease or maintain support: Support({bread, milk}) <= Support({bread})."),
        ("Silhouette analysis cannot be computed for hierarchical clustering output labels.", False, "Silhouette score evaluates any valid cluster label array against feature matrix X, regardless of clustering algorithm.")
    ]

    for i, (q, a, exp) in enumerate(extra_tricky, 121):
        questions.append({
            "id": f"TP6_{i:03d}",
            "tp": 6,
            "category": "tricky",
            "question": q,
            "answer": a,
            "explanation": exp
        })

    # ---------------------------------------------------------
    # 60 TRAP QUESTIONS (TP6_141 to TP6_200)
    # ---------------------------------------------------------
    trap_data = [
        ("Confusing K-Means inertia minimization with supervised classification loss minimization.", False, "Inertia minimizes unsupervised within-cluster spatial distances to centroids, not supervised prediction label errors."),
        ("Assuming that the Elbow Method automatically sets optimal K in K-Means without manual visual inspection.", False, "The Elbow Method requires visual inspection of the inertia curve elbow to select candidate K values."),
        ("Believing that negative Silhouette scores indicate high-quality dense cluster assignments.", False, "Negative Silhouette scores signify misallocated samples that are closer to neighboring clusters than their assigned cluster."),
        ("Confusing Ward linkage (minimizing within-cluster variance) with Single linkage (minimizing minimum pairwise distance).", False, "Ward linkage minimizes variance increases; Single linkage uses shortest pairwise sample distances."),
        ("Assuming that confidence in association rule X => Y equals confidence in rule Y => X.", False, "Confidence is directional: P(Y|X) does not equal P(X|Y) unless Support(X) equals Support(Y)."),
        ("Believing that Lift = 1.0 indicates a strong positive co-occurrence relationship between items.", False, "Lift = 1.0 indicates statistical independence; positive association requires Lift > 1.0."),
        ("Confusing the Apriori downward closure principle (subsets of frequent itemsets are frequent).", False, "The Apriori principle states that all subsets of a frequent itemset must be frequent (and supersets of infrequent are infrequent)."),
        ("Assuming that FP-Growth generates millions of candidate itemsets in disk memory like basic Apriori.", False, "FP-Growth compresses transactions into an in-memory FP-Tree, avoiding candidate itemset generation entirely."),
        ("Believing that K-Means cluster centroids must correspond to actual physical data points in the dataset.", False, "K-Means centroids are calculated arithmetic means of feature coordinates and rarely match actual data points."),
        ("Confusing Agglomerative hierarchical clustering (bottom-up merging) with Divisive hierarchical clustering (top-down splitting).", False, "Agglomerative clustering merges small clusters bottom-up; Divisive clustering splits large clusters top-down."),

        ("Assuming that K-Means works flawlessly on non-spherical complex geometries like concentric rings.", False, "K-Means assumes spherical isotropic clusters and fails to properly partition non-spherical concentric or crescent shapes."),
        ("Believing that increasing K in K-Means increases total within-cluster inertia.", False, "Increasing K strictly decreases or maintains within-cluster inertia by placing centroids closer to sample subsets."),
        ("Confusing Support(X => Y) with Confidence(X => Y) in market basket analysis.", False, "Support measures overall transaction fraction containing X U Y; Confidence measures P(Y|X) within transactions containing X."),
        ("Assuming that TransactionEncoder in mlxtend processes continuous float matrices directly.", False, "TransactionEncoder transforms categorical item lists (e.g., [['bread', 'milk']]) into boolean dummy indicator DataFrames."),
        ("Believing that dendrogram vertical branch height represents sample count inside the merged cluster.", False, "Dendrogram branch height represents the dissimilarity distance threshold at which sub-clusters were merged."),
        ("Confusing Complete linkage (maximum pairwise distance) with Average linkage (mean pairwise distance).", False, "Complete linkage evaluates farthest pairwise sample distance; Average linkage averages all pairwise sample distances."),
        ("Assuming that Lift can never exceed 1.0 in association rule mining.", False, "Lift ranges from 0 to infinity; values above 1.0 indicate strong positive co-occurrence associations."),
        ("Believing that Silhouette score can be evaluated when all samples are assigned to a single cluster K=1.", False, "Silhouette score evaluates intra-cluster vs nearest neighbor cluster distances and requires at least K >= 2 clusters."),
        ("Confusing Apriori min_support with min_confidence thresholds.", False, "min_support filters frequent itemsets based on transaction prevalence; min_confidence filters strong association rules."),
        ("Assuming that K-Means output is deterministic and completely independent of random initial centroid seeds.", False, "K-Means convergence depends on initial random centroid seeds; running multiple restarts (n_init) finds better local optima."),

        ("Believing that Ward linkage in AgglomerativeClustering supports Manhattan (L1) distance metrics.", False, "Ward linkage strictly requires Euclidean distance (L2 norm) to calculate within-cluster variance."),
        ("Confusing single linkage chaining susceptibility with Ward linkage variance optimization.", False, "Single linkage suffers from chaining noisy points into long clusters; Ward linkage forms compact spherical clusters."),
        ("Assuming that high Lift automatically guarantees high rule Support in transaction data.", False, "A rule can have very high Lift (e.g., 10.0) while having very low overall Support (e.g., 0.01) if itemsets are rare."),
        ("Believing that K-Means fit_transform() outputs integer cluster label assignments.", False, "KMeans fit_transform() outputs an N x K matrix of sample-to-centroid spatial distances; labels are stored in labels_."),
        ("Confusing FP-Tree structural compression with raw CSV file disk storage.", False, "FP-Tree is a compact in-memory graph structure used by FP-Growth to mine itemsets rapidly."),
        ("Assuming that hierarchical clustering requires specifying K before building the linkage matrix.", False, "Hierarchical clustering computes the complete dendrogram merge tree across all N samples before cutting at candidate K."),
        ("Believing that an itemset subset can have higher support than the parent itemset itself.", True, "By downward closure, smaller subsets can have EQUAL OR HIGHER support than larger supersets containing them."),
        ("Confusing intra-cluster distance a(i) with inter-cluster distance b(i) in Silhouette calculations.", False, "a(i) measures mean distance to points in the SAME cluster; b(i) measures mean distance to points in the NEAREST neighbor cluster."),
        ("Assuming that K-Means requires supervised class labels y to calculate cluster centroids.", False, "K-Means is an unsupervised algorithm that calculates centroids from feature matrix X without target y."),
        ("Believing that apriori() in mlxtend returns association rules directly without calling association_rules().", False, "apriori() outputs frequent itemsets; generating association rules requires calling association_rules() on frequent itemsets."),

        ("Confusing cluster centroid coordinates with sample feature values in raw DataFrame rows.", False, "Centroids represent calculated average coordinate centers of assigned cluster samples in feature space."),
        ("Assuming that dendrogram horizontal cuts must always produce 2 clusters.", False, "Horizontal cuts can be made at any distance height to produce any desired number of clusters K."),
        ("Believing that Lift values below 1.0 indicate strong positive co-occurrence.", False, "Lift values below 1.0 indicate negative association or substitution (items co-occur less often than random chance)."),
        ("Confusing scikit-learn KMeans n_init parameter with max_iter parameter.", False, "n_init sets the number of random centroid seed restarts; max_iter sets maximum coordinate update iterations per run."),
        ("Assuming that Silhouette Coefficient of 0.0 means perfect cluster separation.", False, "Silhouette of 0.0 means samples sit on overlapping cluster decision boundaries; perfect separation yields +1.0."),
        ("Believing that FP-Growth mines association rules without calculating itemset support.", False, "FP-Growth evaluates itemset support directly from the FP-Tree to identify frequent itemsets before rule generation."),
        ("Confusing AgglomerativeClustering labels_ array with dataset row index values.", False, "labels_ contains assigned integer cluster IDs (0, 1, 2) for each sample row in order."),
        ("Assuming that itemset {A, B} can be frequent if itemset {A} is infrequent under the Apriori principle.", False, "If itemset {A} is infrequent, all supersets containing {A} (including {A, B}) MUST be infrequent."),
        ("Believing that K-Means inertia can be compared directly between 2D and 100D datasets without dimensional scaling.", False, "Inertia sums squared distances across all feature dimensions, scaling with dimension count and feature scale."),
        ("Confusing market basket transaction item lists with continuous numerical feature matrices.", False, "Market basket transactions consist of variable-length item sets, converted to boolean matrices via TransactionEncoder."),

        {"id": "TP6_181", "tp": 6, "category": "trap", "question": "Assuming that Ward linkage minimizes maximum pairwise sample distance in hierarchical clustering.", "answer": False, "explanation": "Ward linkage minimizes total within-cluster variance; Complete linkage minimizes maximum pairwise distance."},
        {"id": "TP6_182", "tp": 6, "category": "trap", "question": "Believing that confidence in an association rule can exceed 1.0 (100%).", "answer": False, "explanation": "Confidence represents conditional probability P(Y|X) and is bounded strictly between 0.0 and 1.0 (0% to 100%)."},
        {"id": "TP6_183", "tp": 6, "category": "trap", "question": "Confusing K-Means inertia with overall classification accuracy.", "answer": False, "explanation": "Inertia measures within-cluster spatial distance sums in unsupervised clustering, not classification prediction accuracy."},
        {"id": "TP6_184", "tp": 6, "category": "trap", "question": "Assuming that silhouette_samples() returns a single overall dataset average float.", "answer": False, "explanation": "silhouette_samples() returns an array of per-sample Silhouette scores; silhouette_score() returns the overall average float."},
        {"id": "TP6_185", "tp": 6, "category": "trap", "question": "Believing that single linkage hierarchical clustering forms spherical compact clusters.", "answer": False, "explanation": "Single linkage follows minimum pairwise distances, forming elongated chaining clusters rather than compact spherical shapes."},
        {"id": "TP6_186", "tp": 6, "category": "trap", "question": "Confusing antecedent itemsets X with consequent itemsets Y in rule X => Y.", "answer": False, "explanation": "Antecedent X is the IF condition itemset; Consequent Y is the THEN outcome itemset."},
        {"id": "TP6_187", "tp": 6, "category": "trap", "question": "Assuming that K-Means requires features to be unscaled to preserve original physical magnitudes.", "answer": False, "explanation": "Unscaled features warp Euclidean distance metrics in K-Means; feature scaling with StandardScaler is recommended."},
        {"id": "TP6_188", "tp": 6, "category": "trap", "question": "Believing that FP-Growth requires running candidate itemset join passes on disk.", "answer": False, "explanation": "FP-Growth mines patterns from an in-memory FP-Tree structure, avoiding candidate join passes on disk."},
        {"id": "TP6_189", "tp": 6, "category": "trap", "question": "Confusing Cophenetic correlation with Pearson correlation in hierarchical clustering validation.", "answer": False, "explanation": "Cophenetic correlation measures how faithfully a dendrogram tree preserves original pairwise sample distances."},
        {"id": "TP6_190", "tp": 6, "category": "trap", "question": "Assuming that setting min_support=1.0 in Apriori mines all possible item combinations.", "answer": False, "explanation": "min_support=1.0 requires itemsets to appear in 100% of all transactions, returning only universally present items."},

        {"id": "TP6_191", "tp": 6, "category": "trap", "question": "Believing that K-Means cluster assignment changes if feature order in DataFrame X is shuffled.", "answer": False, "explanation": "Euclidean distance sums squared differences across features independently of column order in matrix X."},
        {"id": "TP6_192", "tp": 6, "category": "trap", "question": "Confusing mlxtend association_rules metric parameter with mlxtend apriori min_support.", "answer": False, "explanation": "apriori uses min_support to mine frequent itemsets; association_rules uses metric (e.g., confidence, lift) to filter rules."},
        {"id": "TP6_193", "tp": 6, "category": "trap", "question": "Assuming that AgglomerativeClustering supports predict() on new unseen data rows directly.", "answer": False, "explanation": "Standard AgglomerativeClustering in scikit-learn fits historical data hierarchies and does not support predict() on new points."},
        {"id": "TP6_194", "tp": 6, "category": "trap", "question": "Believing that a Lift score of 0.5 indicates items are frequently bought together as a pair.", "answer": False, "explanation": "Lift = 0.5 indicates a negative association (items co-occur less often than random chance)."},
        {"id": "TP6_195", "tp": 6, "category": "trap", "question": "Confusing cluster inertia reduction with gradient descent loss optimization.", "answer": False, "explanation": "Inertia reduction in K-Means optimizes sample-to-centroid distances via Lloyd's algorithm, not gradient descent loss."},
        {"id": "TP6_196", "tp": 6, "category": "trap", "question": "Assuming that dendrogram visual plots can only be rendered for datasets with exactly 2 features.", "answer": False, "explanation": "Dendrograms plot hierarchical cluster distance merges regardless of input feature matrix dimensionality."},
        {"id": "TP6_197", "tp": 6, "category": "trap", "question": "Believing that support of itemset {bread} can be lower than support of rule {bread} => {butter}.", "answer": False, "explanation": "Rule support = Support({bread, butter}) <= Support({bread}); an itemset subset support is always >= rule support."},
        {"id": "TP6_198", "tp": 6, "category": "trap", "question": "Confusing silhouette_score output range (-1 to +1) with inertia output range (0 to infinity).", "answer": False, "explanation": "Silhouette score is normalized between -1.0 and +1.0; inertia is an unbounded sum of squared Euclidean distances (>= 0)."},
        {"id": "TP6_199", "tp": 6, "category": "trap", "question": "Assuming that market basket analysis requires labeled target outcomes y during transaction encoding.", "answer": False, "explanation": "Market basket analysis is an unsupervised technique that mines transaction itemsets without target labels y."},
        {"id": "TP6_200", "tp": 6, "category": "trap", "question": "Believing that unsupervised clustering guarantees discovering true physical causality between features.", "answer": False, "explanation": "Clustering discovers mathematical spatial groupings in feature space, which require domain validation to confirm physical meaning."}
    ]

    # Convert tuple rows to dicts for 141..180
    for i, item in enumerate(trap_data[:40], 141):
        q, a, exp = item
        questions.append({
            "id": f"TP6_{i:03d}",
            "tp": 6,
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
    qs = get_tp6_questions()
    print(f"TP6 Total: {len(qs)}")
    print("Normal:", sum(1 for q in qs if q["category"] == "normal"))
    print("Tricky:", sum(1 for q in qs if q["category"] == "tricky"))
    print("Trap:", sum(1 for q in qs if q["category"] == "trap"))
