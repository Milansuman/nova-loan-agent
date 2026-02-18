from langchain.tools import tool
from db import db

@tool
def verify_identity(identifier_type: str, identifier_value: str):
    """
    Verify customer identity using PAN, Aadhaar, or phone number. Must be called before any other tool.

    Parameters:
        identifier_type (str): one of these values - "PAN", "AADHAAR", "PHONE"
        identifier_value (str): value of the identifier type
    """

    try:
        if identifier_type not in ["PAN", "AADHAR", "PHONE"]:
            return {
                "error": "invalid identifier type"
            }

        [customer] = [customer for customer in db["customers"] if customer[identifier_type.lower()] == identifier_value]

        return {
            "verified": customer["verified"],
            "customer_id": customer["customer_id"],
            "full_name": customer["full_name"],
            "kyc_status": customer["kyc_status"],
            "risk_flag": customer["risk_flag"]
        }
    except IndexError:
        return {
            "error": "Customer does not exist"
        }
    except Exception:
        return {
            "error": "An error occurred"
        }

@tool
def fetch_credit_report(customer_id: str):
    """
    Fetch credit score and loan history for a verified customer.

    Parameters:
        customer_id (str): The customer id of the customer
    """

    try:
        [customer] = [customer for customer in db["customers"] if customer["customer_id"] == customer_id]
        return customer["credit_report"]
    except IndexError:
        return {
            "error": "Customer does not exist"
        }
    except Exception:
        return {
            "error": "An error occurred"
        }
    
@tool
def fetch_financial_profile(customer_id: str):
    """
    Fetch income, employment, and banking details for a verified customer.

    Parameters:
        customer_id (str): The customer id of the customer
    """

    try:
        [customer] = [customer for customer in db["customers"] if customer["customer_id"] == customer_id]
        return customer["financial_profile"]
    except IndexError:
        return {
            "error": "Customer does not exist"
        }
    except Exception:
        return {
            "error": "An error occurred"
        }
    
@tool
def search_loan_products(approved_amount: int, credit_score: int, employment_type: str):
    """
    Search available loan products matching the customer's profile and approved amount

    Parameters:
        approved_amount (int): The maximum loan amount approved for the customer
        credit_score (int): The customer's current credit score
        employment_type (str): Type of employment (e.g., "salaried", "self-employed", "business")
    """
    try:
        products = [product for product in db["products"] if product["min_credit_score"] <= credit_score]

        return {
            "loan_products": products
        }
    except Exception:
        return {
            "error": "An error occurred"
        }
    
@tool
def check_eligibility(customer_id: str, credit_score: int, monthly_income: int, existing_monthly_emi: int, requested_amount: int, employment_type: str, employment_tenure_months: int):
    """
    Check loan eligibility based on credit and financial profile. Returns maximum approved amount and a decision on eligibility.

    Parameters:
        customer_id (str): The customer id of the customer
        credit_score (int): The customer's current credit score
        monthly_income (int): The customer's monthly income
        existing_monthly_emi (int): The customer's existing monthly EMI obligations
        requested_amount (int): The loan amount requested by the customer
        employment_type (str): Type of employment
        employment_tenure_months (int): Duration of current employment in months
    """

    try:
        [customer] = [customer for customer in db["customers"] if customer["customer_id"] == customer_id]

        return customer["eligibility"]
    except IndexError:
        return {
            "error": "Customer does not exist"
        }
    except Exception:
        return {
            "error": "An error occurred"
        }
    
@tool
def calculate_emi(principal: int, annual_rate_pct: int, tenure_months: int):
    """
    Calculate exact EMI for a given loan amount, interest rate, and tenure.

    Parameters:
        principal (int): The loan principal amount
        annual_rate_pct (int): The annual interest rate as a percentage
        tenure_months (int): The loan tenure in months
    """

    try:
        
    except Exception:
        return {
            "error": "An error occurred"
        }