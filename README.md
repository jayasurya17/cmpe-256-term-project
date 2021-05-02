**Installing requirements** 
Install requirements from requirements.txt using the following command

> pip install -r requirements.txt

**Executing the project**

 - Install requirements
 - Find source code in code folder
 - Open with jupyter notebook
 - Run preprocessing 

**Abstract** 
Rent the runway (RTR), a clothing-based business model, was co-founded in 2009 where women can rent designer outfits, accessories for every day or special occasion. It is an online service which has about 6 million customers as of October 2016 (as mentioned on wiki). Basically, it gives a solution to wearing everything a woman wants without purchasing it, a customer can save time and money (as low as 10% of the retail price throw their traditional platform). The dataset we selected is posted by one of the UCSD’ professor. It has about ~105K unique users and 5850 unique items. Considering different features for various algorithms we developed a recommendation engine.
In this project our goal is to develop a recommendation system to recommend items to users based on the prior knowledge/ history, meta-data. We used techniques such as TF-IDF content based filtering, collaborative user based filtering (Jaccard and cosine similarity, K-means clustering) to design our recommendation engine.  Additionally, we used neural network-based CF in order to predict the rating a user might provide and compared the results by taking results of SVD as our baseline.