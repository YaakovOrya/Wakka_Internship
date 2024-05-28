# Intro to Deep Learning Course

In this course, we will learn about the basics of deep learning. We will cover the following topics:
* Understanding Data
* What is Machine Learning
* Linear Regression
* Logistic Regression
* Intro to Deep Learning


### Understanding Data
**What is data? How is it used in everyday life?** Think of data as the basic building blocks of information that we collect and use every day to make sense of the world. This information comes in various forms like text, numbers, images, and more. It's everywhere and affects almost every aspect of our lives.

In practical terms, data is essential for:
* Making informed decisions in business
* Tailoring marketing to individual preferences
* Managing patient health records
* Improving educational methods
* Enhancing the functionality of devices like smartphones and smartwatches

Its widespread use across different fields highlights its importance in our society, helping us make better decisions, enjoy personalized services, and leverage technology for convenience and efficiency.


### What is Machine Learning:

**Machine Learning (ML)** is a subset of artificial intelligence (AI) that involves the development of algorithms and models that enable computers to learn from and make predictions or decisions based on data without being explicitly programmed for each task. In essence, ML algorithms identify patterns in data and use them to make predictions or decisions. ML can be categorized into several types, including supervised learning, unsupervised learning, and reinforcement learning. It finds applications in various fields such as image recognition, natural language processing, recommendation systems, predictive analytics, and autonomous vehicles. The goal of ML is to create systems that can learn from data and improve their performance over time without human intervention.

### Supervised Learning:

**Supervised learning** is a type of machine learning algorithm where the model learns from labeled data, meaning the input data is paired with the correct output. The goal of supervised learning is to learn a mapping from input variables to output variables. In supervised learning, the algorithm is provided with a dataset consisting of input-output pairs. It then learns the relationship between the input and output by finding patterns and correlations within the data. Once the model is trained on the labeled dataset, it can make predictions on new, unseen data.

### Linear Regression:

**Linear regression** is a statistical method used to model the relationship between a dependent variable (often denoted as 'Y') and one or more independent variables (often denoted as 'X'). The basic idea behind linear regression is to fit a straight line to the data points in such a way that the distance between the line and the data points (residuals) is minimized. This line can then be used to make predictions about the dependent variable based on the values of the independent variables. In its simplest form, linear regression involves fitting a line to the data using the equation:

Y = a * X + b

- **Y:** dependent variable (the variable we want to predict).
- **X:** independent variable (the variable used to make predictions).
- **a:** slope of the line, representing the change in Y for a one-unit change in X.
- **b:** intercept, representing the value of Y when X is zero.

Linear regression is related to machine learning because it is often used as a foundational technique in predictive modeling. In the context of machine learning, linear regression is typically used for regression tasks, where the goal is to predict a continuous value. Machine learning algorithms can automatically learn the coefficients m and b that best fit the data by minimizing a cost function, such as the mean squared error, using optimization techniques like gradient descent. Moreover, linear regression serves as a simple and interpretable model, making it a valuable tool in the machine learning toolkit. It forms the basis for more complex regression algorithms and is often used as a benchmark for comparing the performance of other machine learning models.

### Logistic Regression:

**Logistic regression** is a statistical method used for binary classification tasks, where the goal is to predict the probability of an outcome belonging to one of two categories. Unlike linear regression, which predicts a continuous value, logistic regression predicts the probability of a binary outcome based on one or more predictor variables. The logistic regression model uses the logistic function (also known as the sigmoid function) to map the output to a probability value between 0 and 1. The equation for logistic regression can be represented as:

P(Y=1|X) = 1 / (1 + e^-(aX + b))

- **P(Y=1|X):** probability of the outcome being in class 1 given the predictor variables X.
- **X:** input (predictor variables).
- **a:** coefficient vector.
- **b:** intercept.

Logistic regression is related to machine learning as it is commonly used as a binary classification algorithm in supervised learning tasks. Machine learning algorithms can automatically learn the coefficients a and b that best fit the data by optimizing a cost function, such as the logistic loss function, using techniques like gradient descent. Moreover, logistic regression serves as a fundamental and interpretable model in machine learning, providing insights into the relationship between predictor variables and the probability of a binary outcome. It is often used as a benchmark for comparing the performance of more complex classification algorithms.
