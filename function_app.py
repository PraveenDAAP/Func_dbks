import logging
import os
import subprocess
import json
 
import azure.functions as func
 
def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
 
    # Example Databricks CLI command
    command = "databricks clusters list"
 
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        output = result.stdout
        logging.info(f"Command output: {output}")
 
        return func.HttpResponse(output, status_code=200)
    except Exception as e:
        logging.error(f"Error: {str(e)}")
        return func.HttpResponse(str(e), status_code=500)