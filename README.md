# EC601 project 1

## Problem statement:

In recent years, due to the popularity of graph structure data, graph-based deep learning has begun to attract attention in the field of artificial intelligence. However, most of the deep learning work on graphs focuses on supervised or semi-supervised learning scenarios. In this scenario, the model is trained for downstream tasks based on manual annotation information. Despite the success of supervised and semi-supervised graph learning, it relies heavily on label information. The cost of obtaining ground-truth tags is too high, over-fitting occurs, and robustness is poor. In other fields, such as the medical field, obtaining sufficient data is itself a challenge.

Self-supervised learning (SSL) is a promising method to solve the problems of supervised and semi-supervised learning, with important potential and research prospects. SSL optimizes well-designed auxiliary tasks through training models, which can help the model learn more generalized representations from unlabeled data, thereby achieving better performance and generalization in downstream tasks. The specific points are as follows: 

First, most of the work of graph learning relies too much on tags and less considers the underlying structure, so designing various SSL auxiliary tasks can help improve this situation and help understand the structure and attribute data of the graph data. Secondly, the cost of collecting image tag information is too high, and it is difficult to apply most of the existing methods to real-world data, but SSL reduces the dependence on artificial tags. Thirdly, graphics are universal and complex data structure This makes SSL pre-tasks work better in this situation, and is more suitable for constructing various SSL pre-tasks to obtain supervision signals than the CV/NLP field.

