from openai import OpenAI
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
model = "gpt-4"

def load_file(file_path):
    try:
        with open(file_path, "r") as file:
            return file.read()
    except IOError as e:
        print(f"Error reading the file: {e}")
        return None
    
def write_file(file_path, content):
    try:
        with open(file_path, "w") as file:
            file.write(content)
    except IOError as e:
        print(f"Error writing the file: {e}")
        return None
    
def transaction_analyzer(transaction_list):
    print("Starting transaction analysis")
    prompt_system = """
        Analyze the following financial transactions and determine whether each should be classified as "Potential Fraud" or "Approved."
        Add a "Status" attribute with one of the following values: "Potential Fraud" or "Approved."

        Each new transaction should be added to the JSON list.

        # Potential Fraud Indicators
        - Transactions with significantly discrepant amounts
        - Transactions that occur in locations far from one another

        Use the output format below to structure your response.
            
        # Output Format
        {
            "transactions": [
                {
                "id": "id",
                "type": "credit or debit",
                "merchant": "merchant name",
                "time": "transaction time",
                "amount": "$XX.XX",
                "product_name": "product name",
                "location": "city - state (Country)"
                "status": ""
                },
            ]
        } 
    """

    messages_list = [
        {
            "role": "system", 
            "content": prompt_system
        },
        {
            "role": "user", 
            "content": f"consider the following CSV file, where each row represents a transaction: {transaction_list}. Your response should be only a JSON object with the 'status' attribute filled for each transaction, whithout any extra text."
        },
    ]

    response = client.chat.completions.create(
        messages=messages_list,
        model=model,
        temperature=0
    )

    content = response.choices[0].message.content
    response_json = json.loads(content)
    write_file("output/transactions_analysis.json", content)
    print("Transaction analysis completed")
    return response_json

def create_fraud_alert(transaction):
    print(f"Creating fraud alert for transaction")
    prompt_system = f"""
        For the following transaction, provide an assessment only if its status is "Potential Fraud." In the assessment, include a justification for identifying it as fraud.
        Transaction: {transaction}

        Response Format should be exactly as follows:
        [
            "id": "id",
            "type": "credit or debit",
            "merchant": "merchant name",
            "time": "transaction time",
            "amount": "$XX.XX",
            "product_name": "product name",
            "location": "city - state (Country)"
            "status": "",
            "assessment": "Use Not Applicable if the status is Approved"
        ]
    """

    messages_list = [
        {
            "role": "system", 
            "content": prompt_system
        },
        {
            "role": "user", 
            "content": json.dumps(transaction)
        },
    ]

    response = client.chat.completions.create(
        messages=messages_list,
        model=model,
        temperature=0
    )

    content = response.choices[0].message.content
    print(f"Fraud alert for transaction")
    return content

def generate_recomendation(fraud_alert):
    print(f"Generating recommendation for transaction")
    prompt_system = f""" 
        To the following transaction, provide an appropriate recommendation based on the transaction's status and details for Transaction: {fraud_alert}
        Recommendations may include "Notify Client," "Trigger Anti-Fraud Department," or "Perform Manual Verification." They should be formatted technically. 
        Also, include a classification of the type of fraud if applicable.

        Response Format should be:
        Recommendation: "Notify Client/Trigger Anti-Fraud Department/Perform Manual Verification"
        
        Type of Fraud: "Type of Fraud"

        Description: "Description text of the fraud and why the recommendation was made."
    """

    messages_list = [
        {
            "role": "system", 
            "content": prompt_system
        }
    ]

    response = client.chat.completions.create(
        messages=messages_list,
        model=model,
    )

    content = response.choices[0].message.content
    print(f"Recommendation for transaction")
    return content

transaction_list = load_file("data/transactions.csv")
analyzed_transactions = transaction_analyzer(transaction_list)

for transaction in analyzed_transactions["transactions"]:
    if transaction["status"] == "Potential Fraud":
        print(f"Transaction {transaction['id']} was classified as Potential Fraud")
        fraud_alert = create_fraud_alert(transaction)
        recomendation = generate_recomendation(fraud_alert)
        transaction_id = transaction["id"]
        transaction_product_name = transaction["product_name"]
        transaction_status = transaction["status"]
        write_file(f"output/fraud_alert_{transaction_id}_{transaction_product_name}_{transaction_status}.txt", recomendation)