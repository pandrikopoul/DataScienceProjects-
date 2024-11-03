"""
Data mining - assingment 1 - Classification Trees and Random Forest

Ziv Hochman, student number: 8454434
Stylianos Psara, student number: 2140527
Panagiotis Andrikopoulos, student number: 1780743

"""
import numpy as np
import random
from sklearn.metrics import confusion_matrix,accuracy_score,recall_score,precision_score
class Tree_node:
    def __init__(self,data,impurity,class_zero,class_one,split_point= None, left = None,right = None):
        """This is our tree class that will represent the decision tree.
            each node will contain:
            :param data: (2-dimensional array) : The data.
            :param impurity: (float) : The impurity of the current node according to the given data.
            :param class_zero: (int) : The count of the number "0" that accurs in the class lable.
            :param class_one: (int) : The count of the number "1" that accurs in the class lable.
            :param split_point: (index (int),( value (float), quality (float)):
                The best split point for the data:
                index - The index of the class (on which category to split).
                value - The value that we will split the data on.
                quality - The quality of the split.
            :param left: (Tree_node) : All the data that contains the values that below the split point value.
            :param right: (Tree_node) : All the data that contains the values that above the split point value.
           """
        self.data = data
        self.split_point = split_point
        self.impurity = impurity
        self.class_zero = class_zero
        self.class_one = class_one
        self.left = left
        self.right = right
def tree_grow(x, y, nmin, minleaf, nfeat):
    """
    Generating the best classification tree with the Gini-index impurity calculation.
    :param x: (2-dimensional array) : Data matrix.
    :param y: (1-dimensional binary array) : Class label.
    :param nmin: (int) : Number of observations that a node must contain at least in order to be splitted.
    :param minleaf: (int) : A split is not allowed if it creates a child node with less then minleaf cases.
    :param nfeat: (int) : Number of features that should be considered for each split.
    :return:
    (Tree_node type) :The generated tree according to the given data.
    """
    # Constrain the tree by nmin and minleaf before considering the splits.
    length_y = len(y)
    if length_y < nmin or length_y < 2 * minleaf:#Why this?
        return make_a_leaf(x,y)
    else:
        split_point = best_split_point(x, y, minleaf, nfeat)
        if split_point is None:
            return make_a_leaf(x,y)
        # Splitting the data according to the best split point.
        below_data_split_point = x[x[:, split_point[0]] < split_point[1][0]]
        below_split_point_labels =np.array( [y[i] for i in range(length_y) if x[i, split_point[0]] < split_point[1][0]])
        above_data_split_point = x[x[:, split_point[0]] > split_point[1][0]]
        above_split_point_labels = np.array([y[i] for i in range(length_y) if x[i, split_point[0]] > split_point[1][0]])
        left = tree_grow(below_data_split_point, below_split_point_labels, nmin, minleaf, nfeat)
        right = tree_grow(above_data_split_point, above_split_point_labels, nmin, minleaf, nfeat)
        ones_count = sum(y)
    return Tree_node(x, impurity(y), length_y - ones_count, ones_count, split_point, left, right)
def tree_pred(x, tr) -> []:
    """
    Generating the prediction class labels for the given data with the given tree.
    :param x: (2-dimensional array) : Data matrix.
    :param tr: (Tree_node object) : A classification tree.
    :return:
    (1-dimensional binary array) : The predicted class labels for the given data matrix.
    """
    predictions = []
    for record in x:
        cur_node = tr
        # Running through the given tree
        while cur_node.split_point is not None: # as long as the current node is not a leaf keep "going down the tree"
            if record[cur_node.split_point[0]] < cur_node.split_point[1][0]:
                cur_node = cur_node.left
            else:
                cur_node = cur_node.right
        # We are at a leaf node -> classify as the majority of the class
        if cur_node.class_zero > cur_node.class_one:
            predictions.append(0)
        else:
            predictions.append(1)
    return predictions
def tree_grow_b(x, y, nmin, minleaf, nfeat, m):
    """
     This function creates m classification trees with nmin and minleaf constraints,
     using either bagging or random forest based on the nfeat variable.
     It returns the trees as an array.
    :param x: (2-dimensional array) : Data matrix.
    :param y: (1-dimensional binary array) : Class label.
    :param nmin: (int) : Number of observations that a node must contain at least in order to be splitted.
    :param minleaf: (int) : A split is not allowed if it creates a child node with less then minleaf cases.
    :param nfeat: (int) : Number of features that should be considered for each split.
    :param m: (int) : The number of bootstrap samples to be drawn.
    :return:
    (1-dimensional Tree_node array) : An array of Tree_node objects that represent m trees.
    """

    tree_arr = []
    for i in range(m):
        #Generating a new dataset with randomly sampled observations (with potential repetitions).
        temp = np.random.choice(x.shape[0],x.shape[0],replace=True)
        current_data = x[temp]
        current_data_labels = y[temp]
        #Constructing a tree accordingly
        tree_arr.append(tree_grow(current_data,current_data_labels,nmin,minleaf,nfeat))
    return tree_arr
def tree_pred_b(tree_arr,x) -> []:
    """
       Generating the prediction by choosing the majority of the predicted class in all of the trees
       for the given data.
       :param tree_arr: (1-dimensional Tree_node array) : An array of classification trees.
       :param x: (2-dimensional array) : Data matrix.
       :return:
       (1-dimensional binary array) : The predicted class labels for the given data matrix.
       """

    final_prediction =[]
    prediction_arr = []
    for tree in tree_arr:
        prediction_arr.append(tree_pred(x,tree))
    ones_per_record_arr = np.count_nonzero(prediction_arr,axis=0)
    zeros_per_record_arr = len(tree_arr) - np.count_nonzero(prediction_arr,axis=0)
    for i in range(ones_per_record_arr.shape[0]):
        if zeros_per_record_arr[i] > ones_per_record_arr[i]:
            final_prediction.append(0)
        else:
            final_prediction.append(1)
    return final_prediction
def make_a_leaf(x,y) -> Tree_node:
    """This function return a node of the Tree_node object that represent a leaf node
    :param x: (2-dimensional array) : Data matrix
    :param y: (1-dimensional binary array) : Class label
    :return:
    (Tree_node type) : A leaf node that represent the given data
    """
    return Tree_node(x,impurity(y),np.count_nonzero(y == 0), sum(y),None, None, None)
def impurity(curr_class) -> float:
    """
    Computing the impurity of the current feature using the Gini index.
    :param curr_class: (1-dimensional float array) : The classification's array
    :return:
    (float) : Returning the impurity of the given array
    """

    if len(curr_class) == 0:
        return 0
    one_count  = sum(curr_class)
    one_proportion = one_count / len(curr_class)
    current_impurity = one_proportion * (1 - one_proportion)
    return current_impurity
def best_split(attribute, cur_class, minleaf):
    """
    Calculating the best possible split point for the current attribute with the given class with the constrain minleaf.
    :param attribute: (1-dimensional float array) : The candidate attribute.
    :param cur_class: (1-dimensional float array) : The class distribution.
    :param minleaf: (int) : the minimum number of observations required for each node in order to be splitted.
    :return:
    (float) : The best split point for the candidate attribute.
    (float) : The quality value of this point.
    """
    sorted_attribute = np.sort(np.unique(attribute))
    #skip this attribue because all the values are the same (cannot be splitted)
    if sorted_attribute.shape[0] < 2:
        return -1,0

    possible_split_points = (sorted_attribute[0:sorted_attribute.shape[0] - 1] + sorted_attribute[
                                                                            1:sorted_attribute.shape[0]]) / 2
    total_impurity = impurity(cur_class)
    dtype = np.dtype([('split_point', float), ('split_quality', float)])
    split_quality_array = np.array([], dtype=dtype)
    # Using the calculation for the current quality:
    # TQ = TI - ( (IBS) * (PBS) + (IAS) * (PAS) )
    #
    # TQ = total quality
    # TI = total impurity
    # IBS = impurity of before the split
    # PBS = proportion of the data before the split
    # IAS = impurity of after the split
    # PAS = proportion of the data after the split
    #
    # Searching for the best quality for the selection of the best split point.
    for i in possible_split_points:
        impurity_arr_below_split_point = cur_class[attribute < i]
        impurity_arr_above_split_point = cur_class[attribute > i]

        #if the split point violate the minleaf constrain, continue to the next possible split.
        if (impurity_arr_below_split_point.shape[0] < minleaf or impurity_arr_above_split_point.shape[0] < minleaf):
            continue
        proportion_below_split_point = impurity_arr_below_split_point.shape[0] / cur_class.shape[0]
        proportion_above_split_point = 1 - proportion_below_split_point
        impurity_below_split_point = impurity(impurity_arr_below_split_point) * proportion_below_split_point
        impurity_above_split_point = impurity(impurity_arr_above_split_point) * proportion_above_split_point
        cur_quality = total_impurity - (impurity_below_split_point + impurity_above_split_point)
        cur_split_quality = (i, cur_quality)
        split_quality_array = np.append(split_quality_array, np.array([cur_split_quality], dtype=dtype))
    # if there is no valid split return -1,0
    if split_quality_array.shape[0] == 0:
        return -1,0
    best_quality = np.max(split_quality_array["split_quality"])
    best_split_point = 0
    # finding the corresponding split point to the best quality
    for i in range(0, split_quality_array.shape[0]):
        if split_quality_array["split_quality"][i] == best_quality:
            best_split_point = split_quality_array["split_point"][i]
    return best_split_point, best_quality
def best_split_point(x, y, minleaf,nfeat):
    """
    This function calculate the best split point between all of the "nfeat" randomized features
    and return the best split that doesn't violate the minleaf constrain.
    :param x: (2-dimensional array) : Data matrix.
    :param minleaf: (int) : A split is not allowed if it creates a child node with less then minleaf cases.
    :param nfeat: (int) : Number of features that should be considered for each split.
    :return:
    The best split point :
        (index ,( value , quality ):
        index (int)- The index of the class (on which category to split).
        value (float)- The value that we will split the data on.
        quality (float)- The quality of the split.
    """

    random_features = random.sample(range(0,x.shape[1]),nfeat)
    # finding the best split point that has the best quality value (that doesn't violate the minleaf constrain)
    best_split_fit = (random_features[0], best_split(x[:, random_features[0]], y, minleaf))
    for i in range(0, nfeat):
        cur_fit = (i, best_split(x[:, random_features[i]], y, minleaf))
        if cur_fit[1][1] > best_split_fit[1][1]:
            best_split_fit = cur_fit
    # if all of the splits are violating the minleaf constrain or there isn't any possible split
    if best_split_fit[1][0] == -1:
        return None
    return best_split_fit
def data_preprossesing(data_url):
    """
    In order to work with eclipse-metrics-packages we will have to preprosses it as following:
    1.  Remove all the unnesseary column (the first 2 that have the package and plugin names
        and all the columns after VG_sum) according to the assignment.
    2. Move the 'post' column to the end as classification column.
    3. Change all the valuse of the 'post' column from numeric to binary.
    :param data_url (string): the url of the data
    :return:
    (2-dimensional array) : The prossessed data.
    """
    candidate_data = np.genfromtxt(data_url, delimiter=';', skip_header=True)
    candidate_data = candidate_data[:,2:44]
    candidate_data = candidate_data[:,[col for col in range(candidate_data.shape[1]) if col != 1] + [1]]
    candidate_data[:,-1] = np.where(candidate_data[:,-1]>0,1,0)
    return candidate_data
