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
def Blockchain_Security(id):
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
    Cold_Storage = 0
    Multi_Signature1 = 0
    Hierarchical_Deterministic_Wallets = 0
    Key_Management_Services = 0
    Hot_Wallets = 0
    Proof_of_Work = 0
    Proof_of_Stake = 0
    Byzantine_Fault_Tolerance = 0
    Delegated_Proof_of_Stake = 0
    Proof_of_Authority = 0
    Public_n_Private_Key_Encryption = 0
    Multi_Signature2 = 0
    Access_Control = 0
    Cryptography1 = 0
    for item in data:
        if item['name'] == 'Cold_Storage':
            Cold_Storage = item['description']
        if item['name'] == 'Multi_Signature1':
            Multi_Signature1 = item['description']
        if item['name'] == 'Hierarchical_Deterministic_Wallets':
            Hierarchical_Deterministic_Wallets = item['description']
        if item['name'] == 'Key_Management_Services':
            Key_Management_Services = item['description']
        if item['name'] == 'Hot_Wallets':
            Hot_Wallets = item['description']
        if item['name'] == 'Proof_of_Work':
            Proof_of_Work = item['description']
        if item['name'] == 'Proof_of_Stake':
            Proof_of_Stake = item['description']
        if item['name'] == 'Byzantine_Fault_Tolerance':
            Byzantine_Fault_Tolerance = item['description']
        if item['name'] == 'Delegated_Proof_of_Stake':
            Delegated_Proof_of_Stake = item['description']
        if item['name'] == 'Proof_of_Authority':
            Proof_of_Authority = item['description']
        if item['name'] == 'Public_n_Private_Key_Encryption':
            Public_n_Private_Key_Encryption = item['description']
        if item['name'] == 'Multi_Signature2':
            Multi_Signature2 = item['description']
        if item['name'] == 'Access_Control':
            Access_Control = item['description']
        if item['name'] == 'Cryptography1':
            Cryptography1 = item['description']


    Private_key_management1 = (Cold_Storage*0.27)+(Multi_Signature1*0.24)+(Hierarchical_Deterministic_Wallets*0.21)+(Key_Management_Services*.16)+(Hot_Wallets*.12)
    private_key_management= Private_key_management1 * 0.4
    consensus_mech= (Proof_of_Work * 0.27) + (Proof_of_Stake *0.24)+ (Byzantine_Fault_Tolerance *0.21) +(Delegated_Proof_of_Stake * 0.16) + (Proof_of_Authority * 0.12)
    Consensus_Mechanism= consensus_mech * 0.33
    wallet_prov= (Public_n_Private_Key_Encryption* 0.35) + (Multi_Signature2 * 0.3) +(Access_Control * 0.2)+(Cryptography1 * 0.15)
    Wallet_Provider= wallet_prov * 0.27
    BlockChain_Security= 0.22 * (private_key_management + Consensus_Mechanism + Wallet_Provider)

    BlockChain_Security_json={
            "parameter_name": "BlockChain_Security",
            "parameter_score": BlockChain_Security,
            "sub_parameters": [
                {
                    "sub_parameter_name": "Private_Key_Management",
                    "sub_parameter_score": private_key_management

                },
                {
                    "sub_parameter_name": "Consensus_Mechanism",
                    "sub_parameter_score": Consensus_Mechanism

                },
                {
                    "sub_parameter_name": "Wallet_Provider",
                    "sub_parameter_score": Wallet_Provider

                }
            ]
        }
    return BlockChain_Security_json
