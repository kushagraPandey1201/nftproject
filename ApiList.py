from flask import Flask,jsonify
from NFTCal import nftCalc
from test import Smart_Contract
from testrun2 import Blockchain_Security
from Wallet_Architecture import Wallet_Architecture
from marketplace import marketplace
from ipfs import ipfs
from USER import user
from nft_prop import nft_prop
from werkzeug.routing import BaseConverter
from apiname import apiname
import psycopg2

import json
app = Flask(__name__)
class ListConverter(BaseConverter):
    def to_python(self, value):
        return [int(x) for x in value.split(",")]

    def to_url(self, value):
        return ",".join(str(x) for x in value)

app.url_map.converters['list'] = ListConverter





@app.route("/nftList")
def apidropdown_list():
    #return "<p>Radhe Shyam!</p>"
    result= [{"NFT name":"CryptoPunks",
             "ID:":1},
    {"NFT name": "Pudgy Penguins",
     "ID:": 2},

             {"NFT name": "Bored Ape Yacht Club",
              "ID:": 3},
             {"NFT name": "Mutant Ape Yacht Club",
              "ID:": 4},
             {"NFT name": "Otherdeed for Otherside",
              "ID:": 5},
             {"NFT name": "Azuki",
              "ID:": 6},
             {"NFT name": "Clone X-X TAKASHI MURAKAMI",
              "ID:": 7},
             {"NFT name": "Bored Ape Kennel Club",
              "ID:": 8},
             {"NFT name": "Sewer Pass",
              "ID:": 9},
             {"NFT name": "Moonbirds",
              "ID:": 10},
             {"NFT name": "Checks - VV Edition",
              "ID:": 11},
             {"NFT name": "ANIPANG SUPPORTER CLUB",
              "ID:": 12},
             {"NFT name": "Mint Pass Tokyo AI Collection| Bright Moments| MPAI",
              "ID:": 13},
             {"NFT name": "Sappy Seals",
              "ID:": 14},
             {"NFT name": "MGland",
              "ID:": 15},
             ]

    return jsonify(result)

@app.route("/nftTest/<list:ids>")


def calculate(ids):
    final_results = []
    for id in ids:
        result1 = Smart_Contract(id)
        result2 = Blockchain_Security(id)
        result3 = Wallet_Architecture(id)
        result4 = marketplace(id)
        result5 = ipfs(id)
        result6 = user(id)
        result7 = nft_prop(id)
        nameapi= apiname(id)

        result1_value = result1["parameter_score"]
        result2_value = result2["parameter_score"]
        result3_value = result3["parameter_score"]
        result4_value = result4["parameter_score"]
        result5_value = result5["parameter_score"]
        result6_value = result6["parameter_score"]
        result7_value = result7["parameter_score"]

        final_result = result1_value + result2_value + result3_value + result4_value + result5_value + result6_value + result7_value
        final_json = {
            "NFT name": nameapi,
            "NFT score": final_result,
            "parameters": [result1, result2, result3, result4, result5, result6, result7]
        }
        final_results.append(final_json)
    return jsonify(final_results)

    #result1=testrun2(id)
#def  Wallet_Architecture(id):
    #result= testrun(id)
    #result1=testrun2(id)
#def  MarketPlace(id):
    #result= testrun(id)
    #result1=testrun2(id)

#def  IPFS(id):
    #result= testrun(id)
    #result1=testrun2(id)
#def  User(id):
    #result= testrun(id)
    #result1=testrun2(id)






if __name__ == "__main__":
    app.run(debug=True)