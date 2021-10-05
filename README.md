# TP Cloud Computing #2

__Link of the API:__ https://project2-4dpwuprv7a-ew.a.run.app/

__Link of the Model:__ https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english

__Computation of the cost of the API for 10,000 instances with Docker Storage (except free tier):__ 12€ per month

## __Use of the API:__




### 1.  Files Cloning (2 Methods)
    
   Method 1: Clone the following link (Using GIT): https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english.

   Method 2: Install the following files available in the "files and versions" section of the Model link: 
        *    "config.json", 
        *    "tokenizer_config.json", 
        *    "vocab.txt", 
        *    "pytorch_model.bin".


### 2.  Requirement and Execution

* Make sure you have the model (name the folder "Distilbert" or you will have to modify the "model_path" in the python file) in the same folder as the python file.
* Ensure to have the "requirements.txt", "Dockerfile" and the folder "templates" with the file "index.html" (the CSS is not useful).

Once you have all the previous steps done, you can execute the python file "main.py". 



### 3.  Localhost

If the execution of the python file is successful, a link toward the localhost will be displayed (should be like this :http://localhost:8080/).



### 4.  Sentiment Analysis

In the localhost, you can see a "text area" to be filled with the desire sentence and a "submit button" to send the text to be analysed.
After pressing the submit button, the sentiment analysis results will be displayed and you should see:
    * The text you wrote
    * The result of the sentiment analysis (Positive/Negative).
    * The score of the sentiment analysis (Between 0 and 1, depending on the polarity and the previous result; being 0 the least and 1 the highest). 




### 5.  Graphical Interface

Finally, this method use the graphical interface, that allows you to interact continously. The API execute each time you press the submit button. 

The graphical interface allows to rewrite and reanalyse any text with a more user-friendly approach (faster and easier) and without requiring to reload the page or going back.




## __Infrastructure-as-a-Service (IaaS) VS Serverless (Function-as-a-Service, FaaS)__

IaaS is the closest service to on-premises. In IaaS, a cloud provider rents infrastructure such as servers, virtual machines, networks, and storage. However, customers are still responsible for managing provisioning and installing applications. 

FaaS is the closest to fully managed service. In FaaS, the provider is responsible for powering up and shutting down the server on which the applications run. In such service, the customers do not have to worry about managing or provisioning the server.

To compare with a real-life example, let us imagine the service being a cheeseburger fries. 
* In IaaS, the customer responsibility is to provide the ingredients and all necessities to make the cheeseburger such as the bread, the cheeses, the steaks,  the potatoes, the plates, the utensils, etc., while the “infrastructure” such as the gas/electricity, oven are provided.
* In FaaS, the customer does not have any responsibility except knowing what he wants to order. The infrastructure and the ingredients are provided. 

Finally, IaaS is better when you want the benefits of the cloud while maintaining a large degree of control, while the FaaS is better when you are running application on a high volume transactions or when you need your applications to run on a dynamic basis (or regular schedule) and with a fast scale due to some spike in the workload.

