import openai
from openai import AzureOpenAI
import dotenv
import os

'''In this code snippet, we create a recipe generation app using OpenAI.
  - We get the number of recipes, ingredients, and filter from the user as input.
  - We combine the old prompt and the new prompt to create a new prompt.
  - We set the max tokens to 100 since tokens cost money we need to limit the number of tokens.
  - We can set the temperature to 0.7 to make the output more creative. (The higher the temperature the more creative the output will be.)
  - we are using o3-mini model,which does not support temperature also max_completion_tokens is specified instead of max_tokens.
'''
# load environment variables from .env file
dotenv.load_dotenv()

# Can also create a client using openai library
client = AzureOpenAI(
  azure_endpoint = os.environ['API_BASE'], 
  api_key = os.environ['OPENAI_API_KEY'],  
  api_version = "2024-12-01-preview"
  )


deployment_name = os.environ['AZURE_OPENAI_DEPLOYMENT']

#get the number of recipes from the user as input
no_recipes = input("No of recipes(1-10):")

#get the ingredients from the user as input
ingredients = input("List of ingredients( for example: chicken, rice, tomato):")

#specify a filter out ingredients
filter = input("Filter( for example: vegan, vegetarian, gluten-free):")


#Write a prompt to generate the recipes, use {} to include the variables,
old_prompt = f"Show me {no_recipes} recipes using these ingredients: {ingredients}. For each recipe, list all ingredients needed and provide cooking instructions."
prompt = "Also create a shopping list of additional ingredients needed beyond what I already have."

# We can combine two prompts together to create a new prompt
new_prompt =f"{old_prompt} {prompt}"

messages = [{"role": "user", "content": new_prompt}]

print(f"Prompt: {new_prompt}")
print(f"Deployment: {deployment_name}")
print("Making API call...")

#make completion
completion = client.chat.completions.create(model=deployment_name, messages=messages, max_completion_tokens=1000)

print("API call completed!")

#print response
print(f"Response type: {type(completion)}")
print(f"Number of choices: {len(completion.choices)}")
if len(completion.choices) > 0:
    content = completion.choices[0].message.content
    print(f"Content: {content}")
    print(f"Content length: {len(content)}")
else:
    print("No choices in response")