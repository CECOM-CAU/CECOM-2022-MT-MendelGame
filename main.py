from flask import Flask
import random

flaskApp = Flask(__name__)

@flaskApp.route("/")
def main():
    wordFile = open("wordlist.txt", "r")
    wordList = wordFile.readlines()
    
    wordData = random.sample(wordList, 3)
    wordData[0] = wordData[0].strip()
    wordData[1] = wordData[1].strip()
    wordData[2] = wordData[2].strip()

    return str(wordData)
 
if __name__ == "__main__":
    flaskApp.run(host="0.0.0.0", port=3000)