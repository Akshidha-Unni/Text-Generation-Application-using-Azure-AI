from openai import AzureOpenAI
import openai
import dotenv
import os

# In this code snippet, we create a text generation app using OpenAI and Azure OpenAI.


# load environment variables from .env file
dotenv.load_dotenv()

### Using Azure OpenAI

# Configure a Azure OpenAI service client , we can also use openai library to create a client.
# Why we define a client?
# Because in openai everything is hosted on fixed server, but in azure we use our own deployment (model) hosted on our own Azure resource.
# Azure needs the endpoint, model version, deployment name, api key. Instead of repeating all these in the code.
#  We can just create a client with these parameters.

client = AzureOpenAI(
  azure_endpoint = os.environ['API_BASE'], 
  api_key = os.environ['OPENAI_API_KEY'],  
  api_version = "2024-12-01-preview"
  )

deployment=os.environ['AZURE_OPENAI_DEPLOYMENT']

# add your completion code
prompt = "Complete the following: Once upon a time there was a"

# defining the role of the user is mandatory, defining the role of the system and assistant is optional.
messages = [{"role": "user", "content": prompt}]  
# make completion
completion = client.chat.completions.create(model=deployment, messages=messages)

## print response
print(completion.choices[0].message.content)
## why we print completion.choices[0].message.content, because the openai returns a structured json , 
# choices is a list of possible completions, and we want to print the first choice.
# message containes role( "role":"assistant") and content , and we print this content.


### Using OpenAI

# #API key
openai.api_key = os.getenv("OPENAI_API_KEY")
#endpoint of the API
openai.api_base = os.getenv("API_BASE")
# Set the Azure endpoint environment variable that the library expects
os.environ['AZURE_OPENAI_ENDPOINT'] = os.getenv("API_BASE")
#tells the library to use Azure OpenAI and not OpenAI
openai.api_type = "azure"
#version of the API we want to use.
openai.api_version = "2024-12-01-preview"


deployment_name = os.environ['AZURE_OPENAI_DEPLOYMENT']

# add your completion code
prompt = "Complete the following: Once upon a time there was a"
messages = [{"role": "user", "content": prompt}]

# make completion
completion = openai.chat.completions.create(model=deployment_name, messages=messages)

# print response
print(completion.choices[0].message.content)



