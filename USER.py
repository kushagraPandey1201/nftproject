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
def user(id):
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

    Chainalysis_KYT = 0
    IdentityMind = 0
    Sumsub = 0
    Shufti_Pro = 0
    Smart_contract_protocols = 0
    Escrow_services2 = 0
    Insurance_providers = 0
    Arbitration_services = 0


    for item in data:
        if item['name'] == 'Chainalysis_KYT':
            Chainalysis_KYT = item['description']
        if item['name'] == 'IdentityMind':
            IdentityMind = item['description']
        if item['name'] == 'Sumsub':
            Sumsub = item['description']
        if item['name'] == 'Shufti_Pro':
            Shufti_Pro = item['description']
        if item['name'] == 'Smart_contract_protocols':
            Smart_contract_protocols = item['description']
        if item['name'] == 'Escrow_services2':
            Escrow_services2 = item['description']
        if item['name'] == ' Insurance_providers':
            Insurance_providers= item['description']
        if item['name'] == 'Arbitration_services':
            Arbitration_services = item['description']

    kyc_compliance1=(Chainalysis_KYT*0.35)+(IdentityMind*0.3)+(Sumsub*0.2)+(Shufti_Pro*0.15)
    kyc_compliance=kyc_compliance1*0.6
    claim_management1=(Smart_contract_protocols*0.35)+(Escrow_services2*0.3)+(Insurance_providers*0.2)+(Arbitration_services*0.15)
    claim_management=claim_management1*0.4
    user_val1=kyc_compliance+claim_management
    user_val=user_val1*0.09







    user_json={
            "parameter_name": "User",
            "parameter_score":user_val ,
            "sub_parameters": [
                {
                    "sub_parameter_name": "KYC/AML Compliance",
                    "sub_parameter_score": kyc_compliance

                },
                {
                    "sub_parameter_name": "Claim Management",
                    "sub_parameter_score": claim_management

                }
            ]
        }

    return user_json