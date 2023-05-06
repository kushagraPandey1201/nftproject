from flask import Flask,jsonify
import psycopg2
# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(
        host="containers-us-west-174.railway.app",
        database="railway",
        user="postgres",
        password="mR3d5KcnjNwN31BuPKi6",
        port=8037
    )
def marketplace(id):
    # Retrieve the NFTName corresponding to the given ID from the nftnames table
    cur = conn.cursor()
    cur.execute("SELECT nftname FROM nftlist WHERE ID = %s", (id,))
    row = cur.fetchone()
    cur.close()

    if row is None:
        # Return an error response if the given ID is not found in the nftnames table
        return jsonify(error='ID not found'), 404

    nft_name = row[0]

    # Retrieve all the data from the table with the same name as the NFTName
    cur = conn.cursor()
    cur.execute("SELECT * FROM {} ORDER BY id".format(nft_name))
    rows = cur.fetchall()
    cur.close()

    # Construct a list of dictionaries representing the data rows
    data = []
    for row in rows:
        data.append({
            'id': row[0],
            'name': row[1],
            'description': row[2],
            # Add more fields here as needed
        })
    Smart_Contract_Security = 0
    Escrow_Services1 = 0
    KYC_AML_Compliance = 0
    Two_Factor_Authentication2 = 0
    Encryption2 = 0
    Two_Factor_Authentication3 = 0
    Secure_Socket_Layer_Certificate = 0
    Data_Protection_Policies = 0
    Privacy_Notices = 0
    Custodial_Insurance = 0
    Cyber_Liability_Insurance = 0
    Theft_Fraud_Insurance = 0
    Physical_Damage_Loss_Insurance = 0
    Errors_Omissions_Insurance = 0
    KYC_AML = 0
    Securities_Exchange_Commission_Compliance = 0
    IP_Compliance = 0
    Consumer_Protection_Compliance = 0
    Tax_Compliance = 0
    Transaction_Fees = 0
    Withdrawal_Fees = 0
    Listing_Fees = 0
    Minting_Fees = 0
    Subscription_Fees = 0

    for item in data:
        if item['name'] == 'Smart_Contract_Security':
            Smart_Contract_Security = item['description']
        if item['name'] == 'Escrow_Services1':
            Escrow_Services1 = item['description']
        if item['name'] == 'KYC_AML_Compliance':
            KYC_AML_Compliance = item['description']
        if item['name'] == 'Two_Factor_Authentication2':
            Two_Factor_Authentication2 = item['description']
        if item['name'] == 'Encryption2':
            Encryption2 = item['description']
        if item['name'] == 'Two_Factor_Authentication3':
            Two_Factor_Authentication3 = item['description']
        if item['name'] == 'Secure_Socket_Layer_Certificate':
            Secure_Socket_Layer_Certificate = item['description']
        if item['name'] == 'Data_Protection_Policies':
            Data_Protection_Policies = item['description']
        if item['name'] == 'Privacy_Notices':
            Privacy_Notices = item['description']
        if item['name'] == 'Custodial_Insurance':
            Custodial_Insurance = item['description']
        if item['name'] == 'Cyber_Liability_Insurance':
            Cyber_Liability_Insurance = item['description']
        if item['name'] == 'Theft_Fraud_Insurance':
            Theft_Fraud_Insurance = item['description']
        if item['name'] == 'Physical_Damage_Loss_Insurance':
            Physical_Damage_Loss_Insurance = item['description']
        if item['name'] == 'Errors_Omissions_Insurance':
            Errors_Omissions_Insurance = item['description']
        if item['name'] == 'KYC_AML':
            KYC_AML = item['description']
        if item['name'] == 'Securities_Exchange_Commission_Compliance':
            Securities_Exchange_Commission_Compliance = item['description']
        if item['name'] == 'IP_Compliance':
            IP_Compliance = item['description']
        if item['name'] == 'Consumer_Protection_Compliance':
            Consumer_Protection_Compliance = item['description']
        if item['name'] == 'Tax_Compliance':
            Tax_Compliance = item['description']
        if item['name'] == 'Transaction_Fees':
            Transaction_Fees = item['description']
        if item['name'] == 'Withdrawal_Fees':
            Withdrawal_Fees = item['description']
        if item['name'] == 'Listing_Fees':
            Listing_Fees = item['description']
        if item['name'] == 'Minting_Fees':
            Minting_Fees = item['description']
        if item['name'] == 'Subscription_Fees':
            Subscription_Fees = item['description']

    market_transac_sec1=(Smart_Contract_Security*0.35)+(Escrow_Services1*0.3)+(KYC_AML_Compliance*0.2)+(Two_Factor_Authentication2*0.15)
    market_transac_sec=(market_transac_sec1*0.27)
    data_privacy1=(Encryption2*0.27)+(Two_Factor_Authentication3*0.24)+(Secure_Socket_Layer_Certificate*0.21)+(Data_Protection_Policies*0.16)+(Privacy_Notices*0.12)
    data_privacy=(data_privacy1*0.24)
    insurance_coverage1=(Custodial_Insurance*0.27)+(Cyber_Liability_Insurance*0.24)+(Theft_Fraud_Insurance*0.21)+(Physical_Damage_Loss_Insurance*0.16)+(Errors_Omissions_Insurance*0.12)
    insurance_coverage=(insurance_coverage1*0.21)
    regulatory_compliance1=(KYC_AML*0.27)+(Securities_Exchange_Commission_Compliance*0.24)+(IP_Compliance*0.21)+(Consumer_Protection_Compliance*0.16)+(Tax_Compliance*0.12)
    regulatory_compliance=(regulatory_compliance1*0.16)
    fees_charged1=(Transaction_Fees*0.27)+(Withdrawal_Fees*0.24)+(Listing_Fees*0.21)+(Minting_Fees*0.16)+(Subscription_Fees*0.12)
    fees_charged=(fees_charged1*0.12)
    marketplace1=(market_transac_sec+data_privacy+insurance_coverage+regulatory_compliance+fees_charged)
    marketplace=marketplace1*0.14






    marketplace_json={
            "parameter_name": "Marketplace",
            "parameter_score":marketplace ,
            "sub_parameters": [
                {
                    "sub_parameter_name": "Marketplace Transaction Security",
                    "sub_parameter_score": market_transac_sec

                },
                {
                    "sub_parameter_name": "Data Privacy",
                    "sub_parameter_score": data_privacy

                },
                {
                    "sub_parameter_name": "Insurance Coverage",
                    "sub_parameter_score": insurance_coverage

                },
                {
                    "sub_parameter_name": "Regulatory Compliance",
                    "sub_parameter_score": regulatory_compliance

                },
                {
                    "sub_parameter_name": "Fees Charged",
                    "sub_parameter_score": fees_charged

                }
            ]
        }

    return marketplace_json