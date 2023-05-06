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
def Wallet_Architecture(id):
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
    Private_Keys = 0
    Multi_Signature3 = 0
    Encryption1 = 0
    Two_Factor_Authentication1 = 0
    Public_Keys = 0
    Smart_Contracts1 = 0
    Audit_Trails = 0
    Asymmetric_Encryption = 0
    Hashing = 0
    Symmetric_Encryption = 0
    Elliptic_Curve_Cryptography = 0
    Homomorphic_Encryption = 0
    Seed_Phrase_Backup = 0
    Multi_Signature_Wallets = 0
    Cold_Storage_Backup = 0
    Decentralized_Backup = 0
    Cloud_Backup = 0
    On_Chain_Transfers = 0
    Decentralized_Exchanges = 0
    Off_Chain_Transfers = 0
    Peer_to_Peer_Trading = 0
    Centralized_Exchanges = 0
    Hardware_Wallets = 0
    Paper_Wallets1 = 0
    Software_Wallets = 0
    Web_Wallets = 0
    Brain_Wallets = 0
    Ledger = 0
    Trezor = 0
    MetaMask = 0
    Trust_Wallet = 0
    Coinbase_Wallet = 0
    Atomic_Wallet = 0
    My_Ether_Wallet = 0
    Paper_Wallet2 = 0

    for item in data:
        if item['name'] == 'Private_Keys':
            Private_Keys = item['description']
        if item['name'] == 'Multi_Signature3':
            Multi_Signature3 = item['description']
        if item['name'] == 'Encryption1':
            Encryption1 = item['description']
        if item['name'] == 'Two_Factor_Authentication1':
            Two_Factor_Authentication1 = item['description']
        if item['name'] == 'Public_Keys':
            Public_Keys = item['description']
        if item['name'] == 'Smart_Contracts1':
            Smart_Contracts1 = item['description']
        if item['name'] == 'Audit_Trails':
            Audit_Trails = item['description']
        if item['name'] == 'Asymmetric_Encryption':
            Asymmetric_Encryption = item['description']
        if item['name'] == 'Hashing':
            Hashing = item['description']
        if item['name'] == 'Symmetric_Encryption':
            Symmetric_Encryption = item['description']
        if item['name'] == 'Elliptic_Curve_Cryptography':
            Elliptic_Curve_Cryptography = item['description']
        if item['name'] == 'Homomorphic_Encryption':
            Homomorphic_Encryption = item['description']
        if item['name'] == 'Seed_Phrase_Backup':
            Seed_Phrase_Backup = item['description']
        if item['name'] == 'Multi_Signature_Wallets':
            Multi_Signature_Wallets = item['description']
        if item['name'] == 'Cold_Storage_Backup':
            Cold_Storage_Backup = item['description']
        if item['name'] == 'Decentralized_Backup':
            Decentralized_Backup = item['description']
        if item['name'] == 'Cloud_Backup':
            Cloud_Backup = item['description']
        if item['name'] == 'On_Chain_Transfers':
            On_Chain_Transfers = item['description']
        if item['name'] == 'Decentralized_Exchanges':
            Decentralized_Exchanges = item['description']
        if item['name'] == 'Off_Chain_Transfers':
            Off_Chain_Transfers = item['description']
        if item['name'] == 'Peer_to_Peer_Trading':
            Peer_to_Peer_Trading = item['description']
        if item['name'] == 'Centralized_Exchanges':
            Centralized_Exchanges = item['description']
        if item['name'] == 'Hardware_Wallets':
            Hardware_Wallets = item['description']
        if item['name'] == 'Paper_Wallets1':
            Paper_Wallets1 = item['description']
        if item['name'] == 'Software_Wallets':
            Software_Wallets = item['description']
        if item['name'] == 'Web_Wallets':
            Web_Wallets = item['description']
        if item['name'] == 'Brain_Wallets':
            Brain_Wallets = item['description']
        if item['name'] == 'Ledger':
            Ledger = item['description']
        if item['name'] == 'Trezor':
            Trezor = item['description']
        if item['name'] == 'MetaMask':
            MetaMask = item['description']
        if item['name'] == 'Trust_Wallet':
            Trust_Wallet = item['description']
        if item['name'] == 'Coinbase_Wallet':
            Coinbase_Wallet = item['description']
        if item['name'] == 'Atomic_Wallet':
            Atomic_Wallet = item['description']
        if item['name'] == 'My_Ether_Wallet':
            My_Ether_Wallet = item['description']
        if item['name'] == 'Paper_Wallet2':
            Paper_Wallet2 = item['description']


    security_feature1=(Private_Keys * 0.35)+(Multi_Signature3 * 0.2)+(Encryption1 *0.15)+(Two_Factor_Authentication1 * 0.09)+(Public_Keys * 0.09)+(Smart_Contracts1*0.07)+(Audit_Trails*0.05)
    security_feature= (security_feature1 *0.25)
    encryp1=(Asymmetric_Encryption*0.27)+(Hashing*0.24)+(Symmetric_Encryption*0.21)+(Elliptic_Curve_Cryptography*0.16)+(Homomorphic_Encryption*0.12)
    encryp= (encryp1 * 0.22)
    back_n_rec1=(Seed_Phrase_Backup*0.27)+(Multi_Signature_Wallets*0.24)+(Cold_Storage_Backup*0.21)+(Decentralized_Backup*0.16)+(Cloud_Backup*0.12)
    back_n_rec= (back_n_rec1 * 0.19)
    trans_exchange1=(On_Chain_Transfers * 0.27)+(Decentralized_Exchanges*0.24)+(Off_Chain_Transfers * 0.21)+(Peer_to_Peer_Trading * 0.16)+(Centralized_Exchanges * 0.12)
    trans_exchange= (trans_exchange1 * 0.15)
    wallet_type1=(Hardware_Wallets * 0.27)+(Paper_Wallets1 * 0.24)+(Software_Wallets * 0.21)+(Web_Wallets*0.16)+(Brain_Wallets * 0.12)
    wallet_type=(wallet_type1 * 0.12)
    wallet_provider1=(Ledger*0.32)+(Trezor*0.2)+(MetaMask*0.15)+(Trust_Wallet*0.09)+(Coinbase_Wallet*0.09)+(Atomic_Wallet*0.07)+(My_Ether_Wallet*0.05)+(Paper_Wallet2*0.03)
    wallet_provider=(wallet_provider1 *0.07)
    Wallet_Architecture_score=(security_feature+encryp+back_n_rec+trans_exchange+wallet_type+wallet_provider) * 0.18


    wallet_architecture_json={
            "parameter_name": "Wallet_Architecture",
            "parameter_score":Wallet_Architecture_score ,
            "sub_parameters": [
                {
                    "sub_parameter_name": "Security_Features",
                    "sub_parameter_score": security_feature

                },
                {
                    "sub_parameter_name": "Encryption",
                    "sub_parameter_score": encryp

                },
                {
                    "sub_parameter_name": "Backup_Recovery",
                    "sub_parameter_score": back_n_rec

                },
                {
                    "sub_parameter_name": "Transfer_Exchange",
                    "sub_parameter_score": trans_exchange

                },
                {
                    "sub_parameter_name": "Wallet_Type",
                    "sub_parameter_score": wallet_type

                },
                {
                    "sub_parameter_name": "Wallet_Provider",
                    "sub_parameter_score": wallet_provider

                }
            ]
        }

    return wallet_architecture_json