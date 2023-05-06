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
def nft_prop(id):
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

    Rarity=0
    Scarcity=0
    Demand=0
    Popularity=0
    Utility=0
    Creator=0
    Historic_Significance=0


    for item in data:
        if item['name'] == 'Rarity':
            Rarity = item['description']
        if item['name'] == 'Scarcity':
            Scarcity= item['description']
        if item['name'] == 'Demand':
            Demand = item['description']
        if item['name'] == 'Popularity':
            Popularity = item['description']
        if item['name'] == 'Utility':
            Utility = item['description']
        if item['name'] == 'Creator':
            Creator = item['description']
        if item['name'] == 'Historic_Significance':
            Historic_Significance= item['description']

    properties=(Rarity*0.18)+(Scarcity*0.18)+(Demand*0.16)+(Popularity*0.16)+(Utility*0.15)+(Creator*0.1)+(Historic_Significance*0.07)











    nft_prop_json={
            "parameter_name": "NFT Properties",
            "parameter_score":properties ,
            "sub_parameters": [
                {
                    "sub_parameter_name": "Properties",
                    "sub_parameter_score": properties

                }
            ]
        }

    return nft_prop_json