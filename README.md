# Text_Generation_Application_Using_Azure_AI

A sample application showcasing how to generate text using Azure OpenAI Service. It includes two code files, each demonstrating a different integration method.

## 📚 Overview
This repository contains :
- a code snippet to develop a simple text generation application, which explores the basics of text generation using both AzureOpenAI and OpenAI.
- a simple recipe generation application which gets the ingredients, no of recipes and filters from the user to generate recipes.

## 🚀 Azure Resource Setup
Note: Active Azure subscription is required.
1. Create a Azure OpenAI Resource
- Go to Azure Portal : https://portal.azure.com
- Search **Azure OpenAI** in search bar.
- Click **Create**.
- Choose the **Subscription**
- Create or Select an existing **Resource Group**.
- Choose one of the supported **Regions** (e.g. East US)
- Give a Unique name for the resource.
- Review the details and Create the resource.

2. Deploy a Model
Once the resource is created:
- Open the created the resource.
- Click on **Explore and Deploy**.
- Create a new deployment and choose either base model or fine-tuned model.
- Select a model:
        - Model : Choose o3-mini or gpt-4 (choose model according to your application)
        - Deployment name : e.g., text-gen-model.
        - Version : Choose default or latest.

3. Get Endpoints and Keys
- In the resource’s left menu, click Keys and Endpoint.
- Copy the following:
   - Endpoint (e.g., https://your-resource-name.openai.azure.com/)
   - API Key 1 or API Key 2.


## 🛠 Installation & Setup
1. Clone the repository
<pre>```bash 
   git clone https://github.com/Your-Profile/Your-Repository-Name.git
   cd Your-Repository-Name```</pre>

2. Install dependencies
<pre>```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt```</pre>


3. Set Up Environment Variables (Refer .env_example)
- Create a .env file 
<pre>```bash
    OPENAI_API_KEY='Your-api-key'
    OPENAI_API_TYPE='azure'
    OPENAI_API_VERSION='2023-05-15'
    API_BASE='Your-base-url'
    AZURE_OPENAI_DEPLOYMENT='o3-mini'```</pre>




    


