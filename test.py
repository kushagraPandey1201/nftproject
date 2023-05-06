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


def Smart_Contract(id):
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

    # Retrieve values for different parameters
    Authentication_n_Access_Control = 0
    GasLimits_n_Optimization = 0
    Reentrancy_Attacks = 0
    Malicious_External_Calls = 0
    Integer_Over_Underflow = 0
    Malicious_Input_Data = 0
    Time_Manipulation = 0

    for item in data:
        if item['name'] == 'Authentication_n_Access_Control':
            Authentication_n_Access_Control = item['description']
        if item['name'] == 'GasLimits_n_Optimization':
            GasLimits_n_Optimization = item['description']
        if item['name'] == 'Reentrancy_Attacks':
            Reentrancy_Attacks = item['description']
        if item['name'] == 'Malicious_External_Calls':
            Malicious_External_Calls = item['description']
        if item['name'] == 'Integer_Over_Underflow':
            Integer_Over_Underflow = item['description']
        if item['name'] == 'Malicious_Input_Data':
            Malicious_Input_Data = item['description']
        if item['name'] == 'Time_Manipulation':
            Time_Manipulation = item['description']

    Smart_Contracts_Vulnerability = (Authentication_n_Access_Control * 0.35) + (GasLimits_n_Optimization * 0.2) + (
                Reentrancy_Attacks * 0.15) + (Malicious_External_Calls * 0.09) + (Integer_Over_Underflow * 0.09) + (
                                                Malicious_Input_Data * 0.07) + (Time_Manipulation * 0.05)
    smart_contract = Smart_Contracts_Vulnerability * 0.25

    res_json = {
        "parameter_name": "Smart_Contract",
        "parameter_score": smart_contract,
        "sub_parameters": [
            {
                "sub_parameter_name": "Smart_Contracts_Vulnerability",
                "sub_parameter_score": Smart_Contracts_Vulnerability
            }
        ]
    }

    return res_json

