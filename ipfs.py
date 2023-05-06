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
def ipfs(id):
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
    Cryptographic_verification = 0
    Content_addressing1 = 0
    Distributed_storage = 0
    Data_replication = 0
    Access_control = 0
    Encryption3 = 0
    Content_addressing2 = 0
    Distributed_storage1 = 0
    Digital_signatures = 0
    Firewalls_network_security = 0
    Decentralized_identity = 0
    Content_addressing3 = 0
    Distributed_storage2 = 0
    Redundancy_replication = 0
    Pinning = 0

    for item in data:
        if item['name'] == 'Cryptographic_verification':
            Cryptographic_verification = item['description']
        if item['name'] == 'Content_addressing1':
            Content_addressing1 = item['description']
        if item['name'] == 'Distributed_storage':
            Distributed_storage = item['description']
        if item['name'] == 'Data_replication':
            Data_replication = item['description']
        if item['name'] == 'Access_control':
            Access_control = item['description']
        if item['name'] == 'Encryption3':
            Encryption3 = item['description']
        if item['name'] == 'Content_addressing2':
            Content_addressing2 = item['description']
        if item['name'] == 'Distributed_storage1':
            Distributed_storage1 = item['description']
        if item['name'] == 'Digital_signatures':
            Digital_signatures = item['description']
        if item['name'] == 'Firewalls_network_security':
            Firewalls_network_security = item['description']
        if item['name'] == 'Decentralized_identity':
            Decentralized_identity = item['description']
        if item['name'] == 'Content_addressing3':
            Content_addressing3 = item['description']
        if item['name'] == 'Distributed_storage2':
            Distributed_storage2 = item['description']
        if item['name'] == 'Redundancy_replication':
            Redundancy_replication = item['description']
        if item['name'] == 'Pinning':
            Pinning = item['description']

    data_integrity1=(Cryptographic_verification*0.35)+(Content_addressing1*0.3)+(Distributed_storage*0.2)+(Data_replication*0.15)
    data_integrity=data_integrity1*0.4
    security1=(Access_control*0.35)+(Encryption3*0.2)+(Content_addressing2*0.15)+(Distributed_storage1*0.09)+(Digital_signatures*0.09)+(Firewalls_network_security*0.07)+(Decentralized_identity*0.05)
    security=security1*0.33
    data_availability1=(Content_addressing3*0.35)+(Distributed_storage2*0.3)+(Redundancy_replication*0.2)+(Pinning*0.15)
    data_availability=data_availability1*0.27
    ipfs1=data_integrity+security+data_availability
    ipfs=ipfs1*0.12



    ipfs_json={
            "parameter_name": "IPFS",
            "parameter_score":ipfs ,
            "sub_parameters": [
                {
                    "sub_parameter_name": "Data Integrity",
                    "sub_parameter_score": data_integrity

                },
                {
                    "sub_parameter_name": "Security",
                    "sub_parameter_score": security

                },
                {
                    "sub_parameter_name": "Data Availability",
                    "sub_parameter_score": data_availability

                }
            ]
        }

    return ipfs_json