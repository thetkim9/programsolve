from hashlib import sha256
import time

class Block:
    def __init__(self, data, previousHash = ""):
        self.timeStamp = time.time()
        self.data = data
        self.previousHash = previousHash
        self.hash = ""
        self.changeHash = 0

    def calculateHash(self):
        toHash = str(self.timeStamp) + str(self.data) + str(self.previousHash) + str(self.changeHash)
        return sha256(toHash.encode('utf-8')).hexdigest()

    def mineBlock(self, difficulty):
        condition = "0"*difficulty
        self.changeHash += 1
        self.hash = self.calculateHash()
        while self.hash[:difficulty]!=condition:
            self.changeHash += 1
            self.hash = self.calculateHash()

    def __str__(self):
        return '''
    time: {}
    data: {}
    previousHash: {}
    hash: {}
    changeHash: {}
    '''.format(self.timeStamp, self.data, self.previousHash, self.hash, self.changeHash)

class Blockchain:
    def __init__(self, difficulty):
        genesisBlock = Block("gensisData")
        genesisBlock.hash = genesisBlock.mineBlock(difficulty)
        self.chain = [genesisBlock]
        self.difficulty = difficulty

    def addBlock(self, newBlock):
        newBlock.previousHash = self.chain[len(self.chain)-1].hash
        newBlock.mineBlock(self.difficulty)
        self.chain.append(newBlock)

    def isValid(self):
        for i in range(1, len(self.chain)):
            currentBlock = self.chain[i]
            previousBlock = self.chain[i-1]

            if currentBlock.hash != currentBlock.calculateHash():
                return False

            if currentBlock.previousHash != previousBlock.hash:
                return False

        return True

    def tamperBlock(self, index):
        self.chain[index].data = "valid tamper..."
        self.chain[index].mineBlock(self.difficulty)
        previousHash = self.chain[index].hash
        for i in range(index+1, len(self.chain)):
            self.chain[i].previousHash = previousHash
            self.chain[i].mineBlock(self.difficulty)
            previousHash = self.chain[i].hash


    def __str__(self):
        String = "This chain...\n"
        for block in self.chain:
            String += str(block) + "\n"
        return String


if __name__=="__main__":
    difficulty = int(input("Enter difficulty: "))

    start = time.time()
    chain = Blockchain(difficulty)
    chain.addBlock(Block("secondData"))
    chain.addBlock(Block("thirdData"))
    chain.addBlock(Block("fourthData"))
    print("time taken to create the blockchain:", time.time() - start)

    print()
    print(chain)
    print("valid?", chain.isValid())
    print()

    start = time.time()
    chain.tamperBlock(2)
    print("time taken to tamper a block:", time.time() - start)
    print(chain)
    print("valid?", chain.isValid())
    print()

    chain.chain[1].data = "invalid tamper..."
    print(chain)
    print("valid?", chain.isValid())
